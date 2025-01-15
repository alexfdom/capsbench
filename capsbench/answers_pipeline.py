import os
import json
import requests
from abc import ABC, abstractmethod
from typing import Tuple, List, Any
from pydantic import BaseModel, ValidationError
from openai import OpenAI
import logging
import yaml

with open("config/answered_by_config.yaml", "r") as f:
    answered_by_config = yaml.safe_load(f)


class Config:
    def __init__(self):
        self.answered_by_config = answered_by_config
        self.logger_config = logging.getLogger(__name__)
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self._validate_configs()

    def _validate_configs(self):
        assert (
            self.answered_by_config["models"]["openai"]["types"]["gpt-4o-2024-08-06"][
                "name"
            ]
            == "gpt-4o-2024-08-06"
        )

    @property
    def OPENAI_MODEL_TYPE(self):
        return self.answered_by_config["models"]["openai"]["types"][
            "gpt-4o-2024-08-06"
        ]["name"]

    @property
    def OPENAI_TEMPERATURE(self):
        return self.answered_by_config["models"]["openai"]["types"][
            "gpt-4o-2024-08-06"
        ]["temperature"]

    @property
    def OPENAI_MAX_TOKENS(self):
        return self.answered_by_config["models"]["openai"]["types"][
            "gpt-4o-2024-08-06"
        ]["token_limit"]

    @property
    def OPENAI_PROMPT_ACCURACY_TEMPLATE(self):
        return self.answered_by_config["prompt_accuracy_template"]

    @property
    def OPENAI_PROMPT_EVALUATION_TEMPLATE(self):
        return self.answered_by_config["prompt_evaluation_template"]["openai"]


class Utilities:
    @staticmethod
    def prompt_handler(
        prompt_template: str, candidate_caption: str, ground_truth: str
    ) -> str:
        return prompt_template.format(
            candidate_caption=candidate_caption, ground_truth=ground_truth
        )

    @staticmethod
    def prompt_evaluation_gpt(
        prompt_template: str, candidate_caption: str, openai_answers: str
    ) -> str:
        return prompt_template.format(
            candidate_caption=candidate_caption, openai_answers=openai_answers
        )


class ModelClient(ABC):
    def __init__(self, config: Config, logger: Any):
        self.config = config
        self.logger = logger

    @abstractmethod
    def answers(self, img_base64: str, prompt: str) -> str:
        pass

    @abstractmethod
    def structured_outputs(self, img_base64: str, prompt: str) -> Tuple[float, str]:
        pass


class KeyDetails(BaseModel):
    score: float
    reason: str


class OpenAIClient(ModelClient):
    def __init__(self, config: Config, logger: Any):
        super().__init__(config, logger)
        self.api_key = config.OPENAI_API_KEY
        self.model = config.OPENAI_MODEL_TYPE
        self.temperature = config.OPENAI_TEMPERATURE
        self.max_tokens = config.OPENAI_MAX_TOKENS
        self.endpoint = "https://api.openai.com/v1/chat/completions"
        self.openai_client = OpenAI(api_key=self.api_key)

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            }
        )

    def answers(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
            "temperature": self.temperature,
        }

        try:
            response = self.session.post(self.endpoint, json=payload)
            response.raise_for_status()
            response_data = response.json()
            reference = response_data["choices"][0]["message"]["content"]

            forbidden_phrases = ["I can’t", "I'm unable to", "I won't", "I'm sorry"]
            if reference is None or any(
                phrase in reference for phrase in forbidden_phrases
            ):
                self.logger.error(f"Invalid output received: '{reference}'.")
                return "Error generating."
            return reference

        except requests.exceptions.RequestException as e:
            self.logger.error(f"OpenAI request failed: {e}")
            return "Error generating."
        except KeyError as e:
            self.logger.error(f"Unexpected response structure: {e}")
            return "Error generating."

    def structured_outputs(self, prompt: str) -> Tuple[float, str]:
        score: List[int] = []
        reasons: List[str] = []

        try:
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }
            ]

            response = self.openai_client.beta.chat.completions.parse(
                model=self.model,
                messages=messages,
                response_format=KeyDetails,
                temperature=self.temperature,
            )

            try:
                structured_output = response.choices[0].message.parsed
                score.append(structured_output.score)
                reasons.append(structured_output.reason)
                self.logger.info(
                    f"Successful evaluation with score {structured_output.score}"
                )
                return structured_output.score, structured_output.reason

            except ValidationError as ve:
                self.logger.warning(f"Validation error when parsing KeyDetails: {ve}")
                return 0.0, "Validation error."
            except json.JSONDecodeError:
                self.logger.warning("JSON decode error.")
                return 0.0, "JSON decode error."
        except Exception as e:
            self.logger.warning(f"Unexpected error: {e}")
            return 0.0, f"Unexpected error: {e}"


class AnswersPipelineApp:
    def __init__(self):
        self.config = Config()
        self.logger = self.config.logger_config
        self.openai_client = OpenAIClient(self.config, self.logger)

    def generate_answers(
        self,
        client_type: str,
        candidate_caption: str,
        ground_truth: str,
    ) -> str:
        prompt = Utilities.prompt_handler(
            self.config.OPENAI_PROMPT_ACCURACY_TEMPLATE,
            candidate_caption,
            ground_truth,
        )
        if client_type.lower() == "openai":
            return self.openai_client.answers(prompt)
        else:
            self.logger.error(f"Unsupported client type: {client_type}")
            return "Error generating."

    def generate_structured_outputs(
        self, client_type: str, candidate_caption: str, answers: str
    ) -> Tuple[float, str]:
        if client_type.lower() == "openai":
            prompt = Utilities.prompt_evaluation_gpt(
                self.config.OPENAI_PROMPT_EVALUATION_TEMPLATE,
                candidate_caption,
                answers,
            )
            return self.openai_client.structured_outputs(prompt)
        else:
            self.logger.error(f"Unsupported client type: {client_type}")
            return 0.0, "Evaluation failed."


# --- Example of usage --- #

if __name__ == "__main__":
    app = AnswersPipelineApp()
    img_to_describe = (
        "https://en.wikipedia.org/wiki/Google_logo#/media/File:Google_2015_logo.svg"
    )
    candidate_caption = "A logo of Bing."
    validation_questions = "Is there a logo? Yes,\n Is it of Bing? No."

    openai_answers = app.generate_answers(
        "openai", candidate_caption, validation_questions
    )
    app.logger.info(f"Answers from OpenAI: {openai_answers}")

    openai_score, openai_reason = app.generate_structured_outputs(
        "openai", candidate_caption, openai_answers
    )
    app.logger.info(
        f"OpenAI Evaluation - Score: {openai_score}, Reason: {openai_reason}"
    )
