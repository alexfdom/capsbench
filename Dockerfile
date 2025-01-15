FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "streamlit-app/capsbench_app.py", "--server.maxUploadSize=500"]

# cd streamlit-app
# docker build -t capsbench_streamlit_app:latest .
# docker run -d -p 8501:8501 -e OPENAI_API_KEY=<____> capsbench_streamlit_app:latest
# docker save -o capsbench_streamlit_app.tar capsbench_streamlit_app:latest
# docker load -i capsbench_streamlit_app.tar

# To visualize the app, go to http://localhost:8501