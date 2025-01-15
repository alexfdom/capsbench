# CapsBench Analysis

## Data Source

The data used in this analysis is from the PG-CAPTIONER column of the [CapsBench](https://huggingface.co/datasets/playgroundai/CapsBench?row=13) dataset.

> Data from: [huggingface.co/playgroundai/CapsBench](https://huggingface.co/datasets/playgroundai/CapsBench?row=13) 

> Paper: [Playground v3: Improving Text-to-Image Alignment with Deep-Fusion Large Language Models](https://arxiv.org/abs/2409.10695)
## Score Definition

Each candidate caption is evaluated based on how effectively it answers the questions related to the image it aims to describe. A Large Language Model (LLM) is employed to perform this evaluation. The model's responses are compared to `the meticulously crafted answers in the dataset`, which `serve as the ground truth`.
A higher score indicates that the candidate caption more accurately and effectively addresses the posed questions.

> Note: To ensure reliable results, we recommend performing the evaluation three times and then averaging the outcomes, as the [paper](https://arxiv.org/abs/2409.10695) recommends.
## Score Calculation Methodology

The score is calculated based on the following tasks to be accomplished for `gpt-4o-2024-08-06`:

1. **Answer Each Question:**

For each question, respond with one of the following options based solely on the information present in the candidate caption:

- **"yes"** if the answer is affirmative.
- **"no"** if the answer is negative.
- **"n/a"** (not applicable) if the information required to answer the question is not available in the caption.

**Note:** No explanations or additional information are provided—only the specified answer.

2. **Calculate Score:**

- Compare the provided answers to the **reference answers**.
- Calculate the score using the formula:


$$
Score = \frac{\text{Number of Correct Answers}}{\text{Total Number of Questions}}*100
$$
- The resulting score reflects the percentage of questions accurately addressed in the candidate captions.

## Data Description

Upon performing the CapsBench evaluation framework, the resulting DataFrame contains the following columns:

- candidate_caption
- captioned_by
- ground_truth
- openai_answers
- score
- reasons
- token_count
- caption_vocabulary_size
- score_bin
- evaluated_by
## Caption Analysis

- **Average Caption Length:** 357.04 tokens
- **Vocabulary Size:** 6456.0 unique tokens
## Data Sample

```python
                                   candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
0  A surreal 3D digital illustration features a w...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     233      60-70  gpt-4o-2024-08-06
1  A vintage-style coffee label features an ornat...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     232     90-100  gpt-4o-2024-08-06
2  A surreal digital illustration features a cent...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     281      70-80  gpt-4o-2024-08-06
3  Three men are seated at a black table covered ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     217      60-70  gpt-4o-2024-08-06
4  A close-up photograph captures an intimate mom...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     252      70-80  gpt-4o-2024-08-06

[5 rows x 10 columns]
```

## Score Distribution

![img](./images/pg-captioner_capsbench_gpt-4o-2024-08-06.png)

### Score Bins

```python
score_bin
0-10       0
10-20      0
20-30      0
30-40      2
40-50      2
50-60     14
60-70     39
70-80     57
80-90     48
90-100    21
Name: count, dtype: int64
```

### Detailed Analysis

```python
            score  token_count  caption_vocabulary_size
count  200.000000   200.000000                200.00000
mean    76.586200   357.040000                232.37500
std     13.671797    69.300731                 39.69715
min     30.000000   183.000000                126.00000
25%     68.967500   308.750000                206.00000
50%     76.920000   357.000000                235.50000
75%     85.710000   397.500000                259.00000
max    100.000000   549.000000                352.00000
```

### Scores in 30-40 Bin

```python
                                    candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
52  This establishing shot captures an expansive v...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     277      30-40  gpt-4o-2024-08-06
54  The scene depicts a serene, nature-inspired ba...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     222      30-40  gpt-4o-2024-08-06

[2 rows x 10 columns]
```

#### Sample 52

candidate_caption: This establishing shot captures an expansive view of New York City's urban landscape, likely from a high-rise window, showcasing a diverse mix of architectural styles and heights. The foreground features several rooftops with varying materials such as white tarps, brick facades, and concrete surfaces, adorned with various objects including satellite dishes, HVAC units, chimneys, ventilation pipes, air conditioning units, and small statues or decorative items. Some roofs have balconies equipped with metal railings, while others display potted plants adding touches of greenery to the concrete expanse. On the left side, a rooftop terrace is visible with large umbrellas, patio furniture, and lush trees in vibrant foliage framing its edges. The midground includes more buildings, predominantly gray and beige structures with numerous rectangular windows arranged in grid patterns on some facades, balconies, and flat roofs with visible fire escape staircases. A prominent light gray building dominates this section, featuring large glass panels that reflect surrounding elements and a white balcony area on top. Scattered among these are patches of greenery from nearby trees, providing subtle contrast against the urban setting. In the background, the city skyline extends towards the horizon, displaying numerous skyscrapers of different heights and designs, including one tall construction site with visible scaffolding and orange safety netting near its peak. This structure stands out due to its skeletal frame and missing sections revealing internal framework. Another notable feature is a dome-shaped structure, possibly part of a church or cathedral, peeking above other silhouettes. An elevated road or highway curves through the scene, connecting different parts of the city and allowing vehicles to move between buildings. The sky above is partly cloudy with soft, diffused daylight creating gentle shadows across the landscape, enhancing the overall depth and realism of the scene. The color palette consists of muted tones like grays, whites, browns, and greens, contributing to the neutral and calm mood of the image. The composition is balanced, capturing both the bustling urban environment and the serene atmosphere of the cityscape under natural lighting conditions typical of early morning or late afternoon.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the tallest building near the center of the image?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have lens flare?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the building in the foreground small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the shape of the grey building rectangular?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the small brown building closer to the camera than the grey building?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low contrast?'}]

openai_answers: 1. Is the sky white?  
   - n/a

2. Is the tallest building near the center of the image?  
   - n/a

3. Does the image have lens flare?  
   - n/a

4. Is the building in the foreground small?  
   - n/a

5. Is the shape of the grey building rectangular?  
   - yes

6. Is there a tree in the image?  
   - yes

7. Is the small brown building closer to the camera than the grey building?  
   - n/a

8. Does the image show daylight?  
   - yes

9. Is the image a photograph?  
   - n/a

10. Does the image have low contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 3  
Total Number of Questions: 10  

Score = (3/10) × 100 = 30

score: 30.0

reasons: The score is calculated based on the number of questions answered correctly out of the total number of questions. In this case, 3 questions were answered correctly out of 10, resulting in a score of 30%.

token_count: 419

caption_vocabulary_size: 277

score_bin: 30-40

evaluated_by: gpt-4o-2024-08-06

#### Sample 54

candidate_caption: The scene depicts a serene, nature-inspired bathroom with a harmonious blend of natural materials and modern fixtures. The central focus is an oval-shaped stone bathtub with a smooth, metallic gray interior and rough-textured edges in varying shades of brown and earthy tones. The tub features subtle variations in color and texture, creating an organic appearance that complements its surroundings. A polished chrome faucet with a temperature control lever and hose extends from above, positioned centrally within the tub. In front of the bathtub, there's a tall plant with thin green stems and white flowers, adding to the room's tranquil atmosphere. The floor consists of light-colored stone tiles arranged in a herringbone pattern, enhancing the rustic aesthetic. Behind the tub, vertical wooden slats in rich reddish-brown hues with visible grain patterns serve as a privacy screen, allowing glimpses of lush tropical foliage through their gaps. This backdrop includes various types of plants with broad leaves, ferns, and dense greenery in different shades, creating a vibrant contrast between indoor comfort and outdoor beauty. On either side of the wooden slats are sheer white curtains tied back, draping vertically and giving soft shadows. These curtains frame glass doors or windows on both sides, revealing more views of the garden outside. Above the slats, stone walls add texture and continuity to the design. Dark wooden beams across the ceiling contribute to the warm ambiance, while additional wooden elements support the structure. The overall mood is calm and inviting, achieved through natural lighting filtered through the curtains and openings, casting gentle shadows and highlights throughout the space. The composition balances industrial elements like the metal fixtures against the organic textures of wood and stone, resulting in a sophisticated yet cozy atmosphere perfect for relaxation.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the bathtub metal?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the curtains white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bathtub in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a plant on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the plant to the right of the bathtub?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the side table to the left of the bathtub?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bathtub large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the side table cylindrical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one bathtub in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the bathtub positioned in front of vertical wooden slats?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a natural color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the bathtub metal?  
   - n/a

2. Are the curtains white?  
   - yes

3. Is the bathtub in the center of the image?  
   - n/a

4. Is there a plant on the right side of the image?  
   - n/a

5. Is the plant to the right of the bathtub?  
   - n/a

6. Is the side table to the left of the bathtub?  
   - n/a

7. Is the bathtub large?  
   - n/a

8. Is the side table cylindrical?  
   - n/a

9. Is there one bathtub in the image?  
   - yes

10. Is the bathtub positioned in front of vertical wooden slats?  
    - yes

11. Does the image have a natural color palette?  
    - yes

12. Is the image a photograph?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 4  
Total Number of Questions: 12  

Score = (4/12) × 100 = 33.33

score: 33.33

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, divided by the total number of questions. In this case, there are 4 'yes' answers out of 12 questions, resulting in a score of 33.33%.

token_count: 344

caption_vocabulary_size: 222

score_bin: 30-40

evaluated_by: gpt-4o-2024-08-06

### Scores in 40-50 Bin

```python
                                     candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
59   A surrealistic photograph features three human...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     183      40-50  gpt-4o-2024-08-06
169  The scene depicts an indoor workspace with a w...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     235      40-50  gpt-4o-2024-08-06

[2 rows x 10 columns]
```

#### Sample 59

candidate_caption: A surrealistic photograph features three humanoid figures with their faces obscured by white, textured clay-like material on their skin, creating a smooth yet cracked appearance reminiscent of plaster or concrete. The figures are positioned closely together against a solid black background, with the central figure slightly ahead of the others. Each figure has one hand gesturing in different ways: the leftmost figure touches its temple, while the middle and right figures have both hands resting near their chests. Their bodies exhibit visible cracks across the surface, adding to the unsettling texture. Four photographs depicting human faces are pinned to their torsos using wooden clothespins attached to thin red strings horizontally across their upper chests. These images show intricate details such as closed eyes, open mouths revealing lips, and prominent eyelashes, all rendered in monochromatic tones with exaggerated features like large dark eyes with bloodshot irises. The central figure displays two fragments of eyes - one wide open showing a red eye surrounded by intricate detail including iris, pupil, and eyelashes; another partially open revealing cracked lips. The lighting is dramatic and low-key, emphasizing the high contrast between the white-painted figures and the deep black background, enhancing the eerie atmosphere. This artistic composition creates a haunting and thought-provoking visual narrative that delves into themes of identity, fragmentation, and the juxtaposition of reality and representation.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the predominant color in the image white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the left figure holding their head with the right hand?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the middle figure in front of the other two figures?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Are the figures in the image life-sized?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three photos on the middle figure?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Are the images hanging from the right figure's chest close-ups of eyes?"}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the predominant color in the image white?  
     - yes

   - Is the left figure holding their head with the right hand?  
     - n/a

   - Is the middle figure in front of the other two figures?  
     - yes

   - Are the figures in the image life-sized?  
     - n/a

   - Are there three photos on the middle figure?  
     - n/a

   - Are the images hanging from the right figure's chest close-ups of eyes?  
     - n/a

   - Does the image have high contrast?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 3
   - Total Number of Questions: 7

   Score = (3/7) × 100 = 42.86

score: 42.86

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 3 out of 7 questions were answered correctly, resulting in a score of 42.86.

token_count: 268

caption_vocabulary_size: 183

score_bin: 40-50

evaluated_by: gpt-4o-2024-08-06

#### Sample 169

candidate_caption: The scene depicts an indoor workspace with a warm, cozy atmosphere created by natural sunlight streaming through a window on the left side of the frame, casting a striking triangular shadow across a wall of light brown wooden panels (#b59472). The desk is positioned centrally against this backdrop, supported by a dark metal stand with visible crossbars underneath. Various items are neatly arranged on its surface, including a black adjustable desk lamp angled towards the center-left, creating focused illumination; colorful pencils in a blue cylindrical holder; a white mug labeled 'Café' with pencil-like objects inside it; a small black speaker or clock; and a light blue baseball cap with the number '501' displayed prominently in bold white text. A set of three wooden step stools with curved legs and simple designs sits at the front of the desk, adding to the rustic charm. Behind these elements, the empty space above features thin vertical planks painted in a lighter shade (#9c7d5a), adding texture and warmth to the room. To the right of the desk, there's a partially visible wooden chair with a cream-colored cushioned seat. Above the desk, mounted high up on the wall, is a modern off-white air conditioning unit that casts a sharp triangle of bright light onto the adjacent paneling, emphasizing the room's architectural details and the interplay between man-made structures and nature. On the floor near the desk, several power strips with various cables extend from unseen sources, suggesting multiple electronic devices in use. Through the window, lush greenery is visible, providing a serene outdoor view and contrasting beautifully with the warm tones of the interior. The overall composition creates a harmonious blend of functionality and aesthetic appeal, highlighting both the minimalist design and the inviting ambiance of this contemporary wooden-paneled room.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text '501'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the desk light brown?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the air conditioner white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the air conditioner on the top center of the image?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the lamp small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the desk rectangular?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there a lamp on the desk?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the step stool in front of the chair?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an indoor setting?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the image contain the text '501'?  
   - yes

2. Is the desk light brown?  
   - n/a

3. Is the air conditioner white?  
   - yes

4. Is the air conditioner on the top center of the image?  
   - n/a

5. Is the lamp small?  
   - n/a

6. Is the desk rectangular?  
   - n/a

7. Is there a lamp on the desk?  
   - yes

8. Is the step stool in front of the chair?  
   - n/a

9. Does the image show an indoor setting?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a photograph?  
    - n/a

12. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 5  
Total Number of Questions: 12  

Score = (5/12) × 100 = 41.67

score: 41.67

reasons: The score is calculated based on the number of 'yes' answers provided in the text. Out of 12 questions, 5 were answered with 'yes', resulting in a score of 41.67%.

token_count: 357

caption_vocabulary_size: 235

score_bin: 40-50

evaluated_by: gpt-4o-2024-08-06

### Scores in 50-60 Bin

```python
                                     candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
23   The scene is set in a cluttered 1960s-style ki...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     226      50-60  gpt-4o-2024-08-06
28   A dynamic, high-speed photograph capturing a t...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     247      50-60  gpt-4o-2024-08-06
46   An animated scene from 'The Lion Guard: Return...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     192      50-60  gpt-4o-2024-08-06
48   The scene features an animated character, spec...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     180      50-60  gpt-4o-2024-08-06
51   The scene depicts an intimate moment set in a ...  pg-captioner  [{'answer': 'Yes', 'category': 'text', 'questi...  ...                     268      50-60  gpt-4o-2024-08-06
100  A photograph taken at sunset captures a young ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     298      50-60  gpt-4o-2024-08-06
108  A scene from 'My Hero Academia' features All M...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     219      50-60  gpt-4o-2024-08-06
131  A photograph taken during sunset captures an u...  pg-captioner  [{'answer': 'yes', 'category': 'blur', 'questi...  ...                     214      50-60  gpt-4o-2024-08-06
132  A photograph capturing a serene Mediterranean ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     194      50-60  gpt-4o-2024-08-06
159  A minimalist still life photograph features fi...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     215      50-60  gpt-4o-2024-08-06
179  A woman is seated in an off-white upholstered ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     146      50-60  gpt-4o-2024-08-06
184  A young woman with long, straight golden blond...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     269      50-60  gpt-4o-2024-08-06
189  The scene captures an intense night-time chase...  pg-captioner  [{'answer': 'yes', 'category': 'position', 'qu...  ...                     240      50-60  gpt-4o-2024-08-06
199  A centered photograph shows a person holding a...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     218      50-60  gpt-4o-2024-08-06

[14 rows x 10 columns]
```

#### Sample 23

candidate_caption: The scene is set in a cluttered 1960s-style kitchen with vintage yellow cabinetry, chrome handles, and a white refrigerator featuring a small magnet on its door. The floor is covered with light brown tiles arranged in a herringbone pattern. In the foreground, a woman stands under a table wearing a beige knee-length skirt that flares slightly at the bottom and distinctive platform wooden sandals with spiral patterns and dark straps around her ankles. Her legs are slightly bent, revealing smooth skin tones. The table is adorned with an off-white cloth featuring large floral patterns in shades of golden yellow, burnt orange, rust red, and white, creating a lively contrast against the light background. On the table are various items including a clear glass bowl containing lemons or other fruits, a silver teapot with a black handle, and a white plate with a fork lying next to it. Two people are crouching beneath the table; one person wears blue pajamas with a yellow leaf or feather design and has short dark hair, while the other has vibrant red hair and appears to be kissing the first individual on the cheek. Various kitchen appliances such as stovetop burners and cabinets are visible behind them. To the left, there's a clothes dryer with clothes hanging on it, adding to the disorganized ambiance. A wooden broom with a natural fiber bristle head rests against the baseboard near the refrigerator, which shows signs of wear, with some papers taped to its surface. The lighting is soft daylight coming from the right side, casting gentle shadows throughout the room and highlighting the textures and colors of the objects. The overall mood is intimate yet chaotic, capturing a moment of interaction between the two individuals under the table amidst the everyday hustle of the kitchen setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the tablecloth white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the dress of person standing in the foreground beige?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person wearing the dress standing on the right side of the image?'}
 {'answer': 'no', 'category': 'relative position', 'question': 'Is the person with patterned pajamas closer to the camera than the person wearing a dress?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have slight film grain?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the table large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a broom in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person with patterned pajamas sitting on the floor?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a vintage color grading?'}]

openai_answers: 1. Is the tablecloth white?  
   - Answer: no

2. Is the color of the dress of person standing in the foreground beige?  
   - Answer: yes

3. Is the person wearing the dress standing on the right side of the image?  
   - Answer: n/a

4. Is the person with patterned pajamas closer to the camera than the person wearing a dress?  
   - Answer: no

5. Does the image have slight film grain?  
   - Answer: n/a

6. Is the table large?  
   - Answer: n/a

7. Are there three people in the image?  
   - Answer: yes

8. Is there a broom in the image?  
   - Answer: yes

9. Is the person with patterned pajamas sitting on the floor?  
   - Answer: yes

10. Does the image show indoors?  
    - Answer: yes

11. Does the image have a warm color palette?  
    - Answer: yes

12. Is the image a shot from a film?  
    - Answer: n/a

13. Does the image have a vintage color grading?  
    - Answer: n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 13  

Score = (7/13) × 100 = 53.85

score: 53.85

reasons: The score is calculated based on the number of questions with definitive answers ('yes' or 'no') compared to the total number of questions. Out of 13 questions, 7 have definitive answers, resulting in a score of 53.85%.

token_count: 354

caption_vocabulary_size: 226

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 28

candidate_caption: A dynamic, high-speed photograph capturing a thrilling moment in a horse race, employing an extreme panning technique that creates horizontal streaks of motion blur throughout the frame. The foreground features eleven chestnut horses with dark manes racing closely together, their muscular forms leaning into the curve of the track as they gallop past the camera at extremely high speed. Each horse wears unique saddles adorned with bright yellow numbers ranging from '15' to '22', indicating different competitors. Jockeys are dressed in vibrant, contrasting outfits including neon yellow (#ebdc80), royal blue, forest green, white, orange, red, black, and pink helmets and jerseys, creating a kaleidoscope-like array of colors against the brown coats of the horses. Some jockeys wear helmets while others have headgear, adding variety to the scene. Notably, one rider leans forward over his saddle, wearing a navy blue jersey with white pants and a white helmet, leaning slightly to the left as he focuses intently on the race ahead. The midground consists of more blurred elements of the racetrack, featuring white railings running horizontally across the bottom and top of the image. Behind them, hints of brownish-red dirt or grassy areas are visible, representing the infield area. The background is intentionally blurred, consisting of horizontal bands of light beige, soft peach, and muted gray tones that represent the motion trails created by the rapid movement of the horses. These color bands create a sense of depth and emphasize the speed of the race. Natural daylight illuminates the scene evenly, highlighting the vivid hues of the jockeys' attire without casting harsh shadows. This lighting accentuates the energetic atmosphere and captures the essence of this competitive event. The overall composition emphasizes the intense competition and dynamic nature of horse racing, conveying the excitement and energy of the moment through its use of color contrast, motion blur, and shallow depth of field.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the text '13' appear in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Are there jockeys wearing colorful outfits?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color green and brown?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the horses at the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the jockeys bent forward on the horses?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have artifacts?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Are the horses large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Are the numbers on the horses' attire rectangular?"}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the jockeys riding the horses?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an outdoor scene?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have bright colors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the text '13' appear in the image?  
   - no

2. Are there jockeys wearing colorful outfits?  
   - yes

3. Is the background color green and brown?  
   - no

4. Are the horses at the center of the image?  
   - n/a

5. Are the jockeys bent forward on the horses?  
   - yes

6. Does the image have artifacts?  
   - n/a

7. Are the horses large?  
   - n/a

8. Are the numbers on the horses' attire rectangular?  
   - n/a

9. Are the jockeys riding the horses?  
   - yes

10. Does the image show an outdoor scene?  
    - yes

11. Does the image have bright colors?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 13  

Score = (7/13) × 100 ≈ 53.85

score: 53.85

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. In this case, 7 out of 13 questions were answered with 'yes', resulting in a score of approximately 53.85%.

token_count: 388

caption_vocabulary_size: 247

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 46

candidate_caption: An animated scene from 'The Lion Guard: Return of the Roar' featuring two lion cubs in an intense interaction. The character on the right has golden yellow fur (#f8b040), distinctive dark brown ears, large expressive amber-yellow eyes with black pupils, thick black eyebrows, and a small triangular nose. A striking red mohawk-style hairstyle adds vibrancy to his appearance. His mouth is open, revealing clenched teeth, suggesting shock or concern as he faces leftward towards another partially visible lion cub on the left side of the frame. This second cub's deep reddish-brown mane dominates the foreground, creating depth through partial blur due to shallow focus. Both characters are set against a blurred sandy-colored background resembling rocky terrain, likely representing Pride Rock. The lighting appears soft and diffused, typical of daylight, providing even illumination across both subjects without harsh shadows. The color palette includes warm hues like golden yellow, amber orange, light brown, and deep reds (#a83c30, #d87b2e), contributing to the vibrant yet balanced visual effect. The overall mood is tense and dramatic, emphasized by the characters' facial expressions and body language while maintaining a playful tone characteristic of 3D animation styles.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the lion cub's mane red?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the large lion with the red mane on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the lion cub with the red mane facing the camera?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the lion cub with the red mane looking worried?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the lion cub with the red mane small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the lion's head round?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two lions in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the character's name Kion?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a lion in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the lion cub looking at something?'}
 {'answer': 'no', 'category': 'relation', 'question': 'Is the lion standing on grass?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a frame from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the lion cub's mane red?  
   - yes

2. Is the large lion with the red mane on the left side of the image?  
   - n/a

3. Is the lion cub with the red mane facing the camera?  
   - n/a

4. Is the lion cub with the red mane looking worried?  
   - n/a

5. Is the lion cub with the red mane small?  
   - n/a

6. Is the lion's head round?  
   - n/a

7. Are there two lions in the image?  
   - yes

8. Does the image show outdoors?  
   - n/a

9. Is the character's name Kion?  
   - n/a

10. Is there a lion in the image?  
    - yes

11. Is the lion cub looking at something?  
    - yes

12. Is the lion standing on grass?  
    - no

13. Does the image have a warm color palette?  
    - yes

14. Is the image a frame from a cartoon?  
    - yes

15. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 15  

Score = (8/15) × 100 = 53.33

score: 53.33

reasons: The score is calculated based on the number of 'yes' or 'no' answers provided, which are considered correct, divided by the total number of questions. In this case, there are 8 'yes' or 'no' answers out of 15 questions, resulting in a score of 53.33%.

token_count: 250

caption_vocabulary_size: 192

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 48

candidate_caption: The scene features an animated character, specifically from the show 'South Park', sitting on a wooden stool with thick legs. The character has a large, round beige head with two small black eyes featuring white sclera and black pupils, giving them a wide-eyed expression of surprise or shock. Their mouth is slightly open, revealing two visible front teeth, indicating they might be speaking or reacting to something while holding a black rotary phone to their ear with their left hand. The character wears a vibrant turquoise blue hat with a bright yellow band around its rim and a yellow yarn-like tuft on top. They are dressed in a crisp red button-up shirt with three black buttons visible down the center, partially unbuttoned at the collar. Brown pants complete their outfit, and black shoes are visible at the bottom of the frame. To the left of the character, there's a dark brown dresser with two drawers featuring rectangular handles, topped by a black rotary phone with a circular gray central dial and thin wire connecting to it. The background is a solid lavender purple color (#937bae), providing high contrast to the foreground elements and creating a flat, two-dimensional effect typical of the show's animation style. In the bottom-left corner, there's a white '©' symbol in bold sans-serif font. The lighting is even and flat, typical of 2D animation styles, ensuring all details are clearly visible without shadows or highlights.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the background color purple?'}
 {'answer': 'Yes', 'category': 'color', 'question': "Is the person's hat light teal?"}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the black telephone on the left side of the image?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the character standing on a chair?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Is the character's right hand holding a phone?"}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the telephone to the left of the character?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the character talking on the phone?'}
 {'answer': 'Yes', 'category': 'proper noun', 'question': "Is the character's name Eric Cartman?"}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the character large compared to the telephone?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there one telephone in the image?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the background color purple?  
   - yes

2. Is the person's hat light teal?  
   - no

3. Is the black telephone on the left side of the image?  
   - no

4. Is the character standing on a chair?  
   - no

5. Is the character's right hand holding a phone?  
   - no

6. Is the telephone to the left of the character?  
   - yes

7. Is the character talking on the phone?  
   - yes

8. Is the character's name Eric Cartman?  
   - n/a

9. Is the character large compared to the telephone?  
   - n/a

10. Is there one telephone in the image?  
    - yes

11. Does the image show indoors?  
    - n/a

12. Is the image from a cartoon?  
    - yes

13. Does the image have high contrast?  
    - yes

14. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 14  

Score = (7/14) × 100 = 50

score: 50.0

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 7 out of 14 questions were answered correctly, resulting in a score of 50%.

token_count: 284

caption_vocabulary_size: 180

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 51

candidate_caption: The scene depicts an intimate moment set in a New York City apartment bedroom during sunrise, likely in the 1950s or 1960s. The lighting is hard daylight with high contrast, creating strong shadows and highlights through backlighting from two large windows covered with vibrant red blinds. This backlighting casts a warm amber glow throughout the room, producing a dramatic silhouette effect that emphasizes the contemplative mood. In the center foreground, a person sits on an elevated bed frame with a metal structure, wearing a white jersey bearing the number '33' in dark brown text. Their back faces the camera as they face slightly to the right, holding an indistinct object in their hand, possibly a glass or cup. The bed has a greenish-beige sheet and a partially unmade light-colored blanket draped over it. To the left of the bed, there's a woven chair with a circular patterned seat and a fan visible near the window. On the right side stands a tall floor lamp with a triangular-shaped shade made of translucent material, casting shadows onto nearby furniture. The background features two large windows with red-tinted blinds, one fully open allowing bright sunlight to stream into the room, illuminating the space with an orange-yellow hue. Through these windows, parts of neighboring brick buildings are faintly visible, adding depth to the composition. A small balcony railing can be seen below the lower window. Various objects such as clothing items hanging on hooks, a round mirror or decorative piece, plants, and other personal belongings contribute to the lived-in feel of the space. The color palette consists of rich earth tones like deep browns (#221003), burnt oranges (#e74d25), golden yellows (#c29f6f), and muted greens (#5b3a1d, #72653d, #7f6058), enhancing the nostalgic atmosphere. The overall composition centers on the solitary figure against the striking backdrop, capturing a quiet moment of reflection in this urban setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'text', 'question': "Is the number '23' visible?"}
 {'answer': 'Yes', 'category': 'color', 'question': 'Are the window shades red?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is there a person in the center of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the lamp to the right of the person?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the person facing the window?'}
 {'answer': 'Yes', 'category': 'blur', 'question': 'Is the background in focus?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have light film grain?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the bed large?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two windows in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a fan in the window?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the person sitting on the bed?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the number '23' visible?  
   - no

2. Are the window shades red?  
   - yes

3. Is there a person in the center of the image?  
   - yes

4. Is the lamp to the right of the person?  
   - yes

5. Is the person facing the window?  
   - no

6. Is the background in focus?  
   - n/a

7. Does the image have light film grain?  
   - n/a

8. Is the bed large?  
   - n/a

9. Are there two windows in the image?  
   - yes

10. Is there a fan in the window?  
    - no

11. Is the person sitting on the bed?  
    - yes

12. Does the image show indoors?  
    - yes

13. Does the image have a warm color palette?  
    - yes

14. Is the image a shot from a film?  
    - n/a

15. Does the image have low brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 15  

Score = (8/15) × 100 = 53.33

score: 53.33

reasons: The score is calculated based on the number of 'yes' or 'no' answers provided that are relevant to the questions. Out of 15 questions, 8 were answered with a definitive 'yes' or 'no', resulting in a score of 53.33%.

token_count: 400

caption_vocabulary_size: 268

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 100

candidate_caption: A photograph taken at sunset captures a young woman standing on a beach, facing left in profile view. She is positioned slightly off-center to the right of the frame, with her body angled towards the left side of the image. The woman has long, wavy dark brown hair styled in a high ponytail that cascades down her back, transitioning from dark roots to lighter blonde tips with subtle highlights near the ends. Loose strands fall naturally around her face and ears, framing it beautifully. Her expression appears neutral as she gazes into the distance. She wears a white lace crop top with intricate floral patterns, short cap sleeves, and a fitted silhouette that accentuates her figure. The top features scalloped edges along its neckline and shoulders, revealing delicate lacework underneath. High-waisted light blue denim jeans cinched at the waist by a snake-patterned belt complete her outfit. A delicate gold necklace adorns her neck, adding a touch of elegance. The foreground consists of patches of tall grasses interspersed with sandy soil, creating a natural texture leading up to the water's edge. In the midground, there are more dense vegetation areas surrounding the shoreline. The background showcases a calm body of water reflecting the soft hues of the setting sun, extending horizontally across the scene. A distant landmass covered with trees can be seen on the far left, while a faint horizon line separates the sky from the water. Above, the sky displays a beautiful gradient transition from pale pink near the horizon to slate gray higher up, suggesting the time is either sunrise or sunset. Soft clouds are scattered throughout, appearing almost invisible due to their diffuse nature and blending seamlessly with the colors above. The lighting is natural and diffused, typical of golden hour, providing even illumination without harsh shadows and enhancing the serene mood of the scene. The overall color palette includes cool tones such as slate gray (#70808e), peach (#d8b9c1), lavender-gray (#afb2bf), steel blue (#5f89aa), and charcoal (#4f5c6e). The composition follows the rule of thirds, with the subject occupying one third of the frame while maintaining balance within the larger landscape, creating an inviting and tranquil atmosphere reminiscent of a quiet coastal moment during twilight hours.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky pink and white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the shorts blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person closer to the camera than the water?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person large relative to the image?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's necklace silver?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there water in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person standing on land?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sky pink and white?  
   - yes

2. Are the shorts blue?  
   - no

3. Is the person in the center of the image?  
   - no

4. Is the person closer to the camera than the water?  
   - yes

5. Is the background blurred?  
   - n/a

6. Is the person large relative to the image?  
   - n/a

7. Is the person's necklace silver?  
   - no

8. Is there one person in the image?  
   - yes

9. Is there water in the image?  
   - yes

10. Is the person standing on land?  
    - yes

11. Does the image show outdoors?  
    - yes

12. Does the image have a cool color palette?  
    - yes

13. Is the image a photograph?  
    - yes

14. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 14  

Score = (8/14) × 100 = 57.14

score: 57.14

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. In this case, there are 8 'yes' answers out of 14 questions, resulting in a score of 57.14%.

token_count: 456

caption_vocabulary_size: 298

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 108

candidate_caption: A scene from 'My Hero Academia' features All Might lying on a red circular platform in the midground, bound by blue tape-like bands with golden horns on his head. His costume includes blue, yellow, and white colors with red accents. The character is positioned horizontally across the circle, facing left. In the foreground, a male character with spiky, vibrant forest green hair stands on an elevated platform, viewed from behind. He wears a maroon pinstriped suit with a cream-colored collar and inner sleeve visible at the wrists. His right hand is raised to his ear in a listening or thinking pose. A curved metallic railing runs along the bottom edge of the frame, separating him from the lower floor area. The checkered floor pattern consists alternating light peach and dark brown squares, creating a large chessboard effect. A large pale yellow tablecloth covers tables scattered around the room, including one prominently centered near the top left corner. Several individuals are seated or kneeling on the ground around these tables, appearing distressed or taking cover. One person holds a gun, adding tension to the scene. Soft, diffused lighting creates gentle shadows throughout the setting, contributing to a dramatic atmosphere. The overall color palette includes warm tones like peach (#b8967c), burgundy (#3e2d24), taupe (#9a6f5f), sage green (#84958c), and slate gray (#5f6960). This composition emphasizes the contrast between the lone figure observing the situation and the group below, suggesting a moment of reflection or anticipation amidst unfolding events.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the floor color a checkered pattern?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the person lying down tied with aquamarine rope?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person with green hair on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in the red striped suit closer to the camera than the person lying on the ground?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the table round?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than five people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person with green hair in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person with green hair looking at the person lying down?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is this an indoor scene?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the character in the image Deku?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is this image a scene from an animated movie?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have muted colors?'}]

openai_answers: 1. Is the floor color a checkered pattern?  
   - yes

2. Is the person lying down tied with aquamarine rope?  
   - no

3. Is the person with green hair on the right side of the image?  
   - n/a

4. Is the person in the red striped suit closer to the camera than the person lying on the ground?  
   - yes

5. Is the background blurred?  
   - n/a

6. Is the table round?  
   - n/a

7. Are there more than five people in the image?  
   - yes

8. Is there a person with green hair in the image?  
   - yes

9. Is the person with green hair looking at the person lying down?  
   - n/a

10. Is this an indoor scene?  
    - yes

11. Is the character in the image Deku?  
    - n/a

12. Is this image a scene from an animated movie?  
    - yes

13. Does the image have muted colors?  
    - yes

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 13  

Score = (7/13) × 100 ≈ 53.85

score: 53.85

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 7 correct answers out of 13 questions result in a score of approximately 53.85%.

token_count: 318

caption_vocabulary_size: 219

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 131

candidate_caption: A photograph taken during sunset captures an urban landscape with a strong bokeh effect, creating a serene and contemplative mood. The foreground is filled with numerous circular light spots in various colors including warm yellows (RGB(184, 155, 95)), soft whites, golden hues (RGB(216, 187, 161)), vibrant greens (RGB(100, 164, 96)), crimson reds (RGB(140, 47, 55)), and subtle blues (RGB(123, 136, 150)), spread across the entire frame. These lights form a dense pattern that transitions from dark navy blue (RGB(30, 27, 23)) at the bottom to lighter shades higher up, suggesting depth and distance. In the midground, the city lights continue but become slightly more defined, forming a blurred strip of lights stretching horizontally across the image. The background features a gradient sky transitioning from pale pink near the horizon to deeper shades of mauve (RGB(156, 128, 132)) and slate gray (RGB(83, 84, 87)) as it ascends, with scattered wispy clouds adding texture. Distant silhouettes of mountains or hills can be seen along the horizon line, enhancing the sense of scale and vastness. The overall composition follows the rule of thirds, with the colorful lights balancing against the softer tones of the setting sun and darker landscape below. The shallow depth of field creates a dreamy quality to the scene, emphasizing the interplay between the artificial lights and the natural elements of the twilight sky. The lighting is low-key with high contrast between the brightly lit areas and the surrounding darkness, resulting in a visually striking and emotionally evocative image that captures the tranquil beauty of dusk over a bustling city.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'blur', 'question': 'Is the image blurry?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show night?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have warm color tones?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky white and orange?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the image blurry?  
     - yes

   - Does the image show night?  
     - no

   - Does the image have warm color tones?  
     - yes

   - Is the sky white and orange?  
     - no

2. **Calculate Score:**

   - Number of Correct Answers: 2
   - Total Number of Questions: 4

   Score = (2/4) × 100 = 50

score: 50.0

reasons: The score is calculated based on the number of correct answers out of the total questions. In this case, 2 out of 4 questions were answered correctly, resulting in a score of 50%.

token_count: 360

caption_vocabulary_size: 214

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 132

candidate_caption: A photograph capturing a serene Mediterranean coastal scene, featuring crisp white bell towers of a traditional Greek church set against the expansive azure blue sea. The foreground showcases two prominent white bell towers with intricate architectural details. Each tower has multiple arches, including a large central arch flanked by smaller side arches, creating a stepped effect. Two green bells hang from within these arched openings, suspended by chains. The surfaces of the towers are smooth and well-maintained, reflecting sunlight and casting subtle shadows that accentuate their contours. A small white cross is visible on one of the towers' edges, adding to the religious aesthetic. The midground continues to display more sections of white architecture, including smooth walls and flat roofs characteristic of Cycladic design. In the background, the vast, calm sea occupies the entire frame, its vibrant azure color (#5abef0) extending beyond the horizon, dominated by gentle ripples created by sunlight. The sky above is not visible, emphasizing the striking contrast between the pristine white structures and the deep blue waters. Natural daylight bathes the scene in bright light, enhancing the vivid colors and creating high contrast between the bright whites and rich blues. The composition follows the rule of thirds, with the bell tower positioned off-center to the right, drawing attention while maintaining balance with the expanse of water. This balanced arrangement creates a visually appealing and tranquil atmosphere, showcasing the harmonious blend of man-made beauty and natural splendor in this iconic Mediterranean setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the water blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the dome blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the blue dome on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bell tower to the right of the blue dome?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a bell in the image?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the dome on the left side spherical?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the arch on the bell tower semi-circular?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the dome larger than the bells?'}]

openai_answers: 1. Is the color of the water blue?  
   - yes

2. Is the dome blue?  
   - n/a

3. Is the blue dome on the left side of the image?  
   - n/a

4. Is the bell tower to the right of the blue dome?  
   - n/a

5. Is there a bell in the image?  
   - yes

6. Does the image have a cool color palette?  
   - yes

7. Does the image show outdoors?  
   - yes

8. Is the dome on the left side spherical?  
   - n/a

9. Is the arch on the bell tower semi-circular?  
   - yes

10. Is the dome larger than the bells?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 5  
Total Number of Questions: 10  

Score = (5/10) × 100 = 50

score: 50.0

reasons: The score is calculated based on the number of questions answered with 'yes' or 'no' (5) out of the total number of questions (10). The 'n/a' responses are not considered in the calculation.

token_count: 296

caption_vocabulary_size: 194

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 159

candidate_caption: A minimalist still life photograph features five glass jars neatly arranged on a light beige fabric-covered table, set against an off-white textured wall. From left to right, the first jar is tall and cylindrical with a clear glass body and a metal clasp lid, filled completely with perfectly aligned spaghetti strands of golden yellow color. The second jar is shorter and wider, also made of clear glass with a metal clasp lid, containing rolled oats or similar grainy cereal. In front of this jar stands a smaller Ball Mason jar labeled 'Ball' in white cursive font, holding pale yellow parmesan cheese crumbles. To its right are two stacked jars; the top one contains fine brown buckwheat kernels, while the bottom jar holds small round brown lentils. All jars have metallic silver lids that reflect soft natural lighting from the left side, casting subtle shadows to the right. The scene is illuminated by diffused daylight, creating gentle highlights on the contents within the jars without harsh contrasts. This results in a calm and orderly mood, emphasizing simplicity and cleanliness through its neutral color palette dominated by shades of cream (#e4dcd3), warm gray (#847c7a), tan (#b79f85), olive green (#5f5742), sage green (#9aa49d), and taupe (#887a73). The composition follows the rule of thirds, with each jar occupying equal space horizontally, enhancing visual harmony and balance. The shallow depth of field keeps the focus entirely on the jars and their contents, further accentuating the clean aesthetic of the scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the tablecloth beige?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the tallest jar on the left side of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a jar of pasta in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there six jars in the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the shortest jar to the right of the second tallest jar?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background white?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a neutral color palette?'}]

openai_answers: 1. Is the tablecloth beige?  
   - yes

2. Is the tallest jar on the left side of the image?  
   - yes

3. Is there a jar of pasta in the image?  
   - yes

4. Are there six jars in the image?  
   - no

5. Is the shortest jar to the right of the second tallest jar?  
   - n/a

6. Is the background white?  
   - no

7. Does the image have a neutral color palette?  
   - yes

**Calculate Score:**

Number of Correct Answers: 4  
Total Number of Questions: 7  

Score = (4/7) × 100 = 57.14

score: 57.14

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 4 correct answers out of 7 questions, resulting in a score of 57.14%.

token_count: 315

caption_vocabulary_size: 215

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 179

candidate_caption: A woman is seated in an off-white upholstered chair with light wood armrests and a curved wooden frame, positioned slightly to the left of center against a textured beige wall with a subtle marbled pattern. She wears a long-sleeved button-down dress in a light beige color, featuring a collar, gathered elastic waistline, and elasticated cuffs on the sleeves. Her hair is styled in a neat low bun. The woman's left hand rests on her lap while she holds a black book with a white cover in her right hand. She is barefoot, with one leg crossed over the other, and a pair of beige high heels lies nearby on the geometric-patterned parquet floor composed of interlocking diamonds in shades of reddish-brown, brown, and tan. To the left edge of the image, there is a wooden wardrobe with four drawers visible, each equipped with a silver D-shaped handle. The lighting is soft and natural, coming from the right side of the frame, creating gentle shadows and highlighting the calm and contemplative mood of the scene. The overall composition is balanced, with muted colors and low contrast contributing to a serene atmosphere.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is the person holding a book?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the dominant color of the person's clothing beige?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the chair green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person sitting in a chair?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a pair of shoes on the floor?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person to the right of the wardrobe?'}
 {'answer': 'no', 'category': 'relative position', 'question': 'Are the shoes on the floor?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking relaxed?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the chair large?'}
 {'answer': 'no', 'category': 'entity shape', 'question': 'Is the pair of shoes angular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a wardrobe in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the person's dress touching the floor?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the person holding a book?  
   - yes

2. Is the dominant color of the person's clothing beige?  
   - yes

3. Is the color of the chair green?  
   - no

4. Is the person sitting in a chair?  
   - yes

5. Is there a pair of shoes on the floor?  
   - yes

6. Is the person to the right of the wardrobe?  
   - yes

7. Are the shoes on the floor?  
   - yes

8. Is the person looking relaxed?  
   - yes

9. Is the image sharp?  
   - n/a

10. Is the chair large?  
    - n/a

11. Is the pair of shoes angular?  
    - n/a

12. Is there one person in the image?  
    - yes

13. Is there a wardrobe in the image?  
    - yes

14. Is the person's dress touching the floor?  
    - n/a

15. Does the image show indoors?  
    - n/a

16. Is the image a photograph?  
    - n/a

17. Does the image have low brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 17  

Score = (9/17) × 100 ≈ 52.94

score: 52.94

reasons: The score is calculated based on the number of 'yes' answers provided for the questions. Out of 17 questions, 9 were answered with 'yes', resulting in a score of approximately 52.94%.

token_count: 233

caption_vocabulary_size: 146

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 184

candidate_caption: A young woman with long, straight golden blonde hair tied back in a high ponytail is crouching down in a parking garage. She is centered in the frame, wearing an all-black athletic outfit consisting of a form-fitting long-sleeve crop top with a scoop neckline that reveals a small portion of her midriff, paired with matching black leggings. On her feet are black Nike high-top sneakers with white soles and distinctive orange accents near the ankle area, featuring a subtle red swoosh logo on the side. A delicate silver necklace adorns her neck, with a small heart-shaped pendant visible at the center. Her hands rest on her knees as she looks directly at the camera with a neutral expression, slightly parted lips revealing a hint of teeth, and a slight smile. The background features a concrete ceiling structure with evenly spaced circular patterns created by alternating rows of large holes, alternating between dark gray (#333333) and light beige (#e5e3d1), forming geometric designs against the off-white interior walls. Circular lights or vents are arranged in two horizontal lines along the underside of the overpass beams. Below, there are wide horizontal windows allowing diffused daylight to filter through, creating a bright and airy atmosphere. The ground surface consists of textured concrete with faint white markings resembling parking lines extending towards the foreground, adding depth to the scene. The lighting is soft and natural, coming from above and behind, illuminating the subject while casting gentle shadows. This creates a balanced exposure with moderate contrast and saturation, emphasizing the textures of both the subject's attire and the surrounding environment. The overall color palette includes shades of black (#050404), gray (#808080), beige (#e5e3d1), brown (#6c4f33), and warm tones like #7b573b and #ab847a. The composition follows the rule of thirds, focusing attention on the subject while maintaining a sense of place within the urban setting, resulting in a striking portrait that captures a moment of quiet confidence in a bustling city context.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the color of the person's outfit black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person closer to the camera than the background?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Are the shoes Nike?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person large in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the person's hair straight?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the color of the person's outfit black?  
   - yes

2. Is the person in the center of the image?  
   - yes

3. Is the person closer to the camera than the background?  
   - yes

4. Does the person look serious?  
   - no

5. Is the background blurred?  
   - no

6. Are the shoes Nike?  
   - yes

7. Is the person large in the image?  
   - n/a

8. Is the person's hair straight?  
   - yes

9. Is there only one person in the image?  
   - yes

10. Does the image show indoors?  
    - yes

11. Is the image a photograph?  
    - n/a

12. Does the image have high contrast?  
    - no

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 12  

Score = (7/12) × 100 = 58.33

score: 58.33

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. In this case, there are 7 'yes' answers out of 12 questions, resulting in a score of 58.33%.

token_count: 411

caption_vocabulary_size: 269

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 189

candidate_caption: The scene captures an intense night-time chase on a city street in Detroit, Michigan, during the 2020s. The composition is right-heavy with a close-up shot of a classic muscle car's rear wheel prominently featured in the foreground on the right side of the frame. The tire has a chrome rim with multiple spokes, reflecting the surrounding lights, creating a dynamic contrast against its dark body painted in deep midnight blue (RGB(17, 28, 52)) with subtle hints of burnt sienna red along the edge. The glossy wet asphalt road surface dominates the midground, mirroring the vibrant police vehicle lights and street lamps, adding depth and movement to the image. Bright white light sources from the police vehicle's headlights create lens flares and colorful reflections (RGB(218, 216, 226), RGB(188, 148, 160), RGB(147, 156, 169)), including cobalt blue (RGB(108, 140, 172)) streaks across the wet pavement. In the background, additional cars' headlights can be seen, contributing to the sense of urgency and speed. Streetlights line both sides of the street, casting warm amber-yellow hues that enhance the moody atmosphere. Buildings flank either side of the street, their windows illuminated by interior lights. A blurred 'NO PARKING ANY TIME' sign is visible among other urban elements. The color palette includes cool tones like navy blue and midnight blue, complemented by warm accents such as amber yellow and burnt orange, enhancing the dramatic mood. The lighting is hard and high-contrast, dominated by artificial sources and practical lights from vehicles and street fixtures. This creates a striking visual effect with low luminance and high saturation, emphasizing the action-packed nature of the scene. The overall atmosphere conveys a sense of suspense and intensity typical of a high-speed pursuit at night, capturing the raw energy of this iconic moment in American law enforcement history.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'position', 'question': 'Is the closest car on the right side of the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is there blur in the background?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a police car in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a traffic light in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the police car behind the car on the right?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show nighttime?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the closest car on the right side of the image?  
   - yes

2. Is there blur in the background?  
   - n/a

3. Is there a police car in the image?  
   - yes

4. Is there a traffic light in the image?  
   - n/a

5. Is the police car behind the car on the right?  
   - n/a

6. Does the image show nighttime?  
   - yes

7. Is the image a shot from a film?  
   - n/a

8. Does the image have low brightness?  
   - yes

**Calculate Score:**

Number of Correct Answers: 4  
Total Number of Questions: 8  

Score = (4/8) × 100 = 50

score: 50.0

reasons: The score is calculated based on the number of questions answered with 'yes' or 'no', which are considered correct answers. Out of 8 questions, 4 were answered with 'yes', resulting in a score of 50%.

token_count: 390

caption_vocabulary_size: 240

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

#### Sample 199

candidate_caption: A centered photograph shows a person holding a whimsical, modern minimalist illustration print against a plain light beige background (RGB(245, 227, 214)). The hands gripping the sides of the print are visible, with short hair partially covering their face. The print features abstract floral elements in vibrant colors, creating a cheerful mood. At the center is a large pink flower with five rounded petals transitioning from soft peach at the base to bright orange towards the tips, supported by a forest green stem divided into two main sections. To its left, there's a smaller yellow-orange flower with similar petal shape and structure, featuring a blue stem and darker brown tip. On the right side, a blue flowering bud or budgie with thin branches supporting five small round yellow dots at its tip adds depth to the composition. Two olive green leaves with dark brown central vertical lines extend outward symmetrically. A caterpillar-like orange creature composed of seven oval segments with black legs and antennae is crawling along the left green leaf. Near the bottom right leaf rests a small beetle-like insect with a black body adorned with red spots on its head and legs, positioned centrally. Above this larger flower, a stylized bee with white wings outstretched, black body, yellow accents, and segmented body flies near the top right corner. The entire scene is set within a subtle pale pink border around the edges of the paper, enhancing the overall visual appeal. The lighting is soft, natural, and even, coming from the front-left, highlighting the vivid hues without casting harsh shadows. This creates a playful atmosphere that emphasizes the flat, graphic nature of the design while maintaining a balanced exposure throughout the image.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background color of the painting pink?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the large pink flower in the top half of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the orange caterpillar on the green stem?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the pink flower larger than the orange flower?'}
 {'answer': 'no', 'category': 'count', 'question': 'Are there three insects in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a bug in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the bee flying above the pink flower?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show child showing a painting?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the background color of the painting pink?  
   - no

2. Is the large pink flower in the top half of the image?  
   - n/a

3. Is the orange caterpillar on the green stem?  
   - no

4. Is the pink flower larger than the orange flower?  
   - yes

5. Are there three insects in the image?  
   - no

6. Is there a bug in the image?  
   - yes

7. Is the bee flying above the pink flower?  
   - yes

8. Does the image show child showing a painting?  
   - n/a

9. Is the image a photograph?  
   - yes

**Calculate Score:**

Number of Correct Answers: 5  
Total Number of Questions: 9  

Score = (5/9) × 100 = 55.56

score: 55.56

reasons: The score is calculated based on the number of correct answers out of the total number of questions. There are 5 correct answers out of 9 questions, resulting in a score of 55.56%.

token_count: 335

caption_vocabulary_size: 218

score_bin: 50-60

evaluated_by: gpt-4o-2024-08-06

### Scores in 60-70 Bin

```python
                                     candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
0    A surreal 3D digital illustration features a w...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     233      60-70  gpt-4o-2024-08-06
3    Three men are seated at a black table covered ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     217      60-70  gpt-4o-2024-08-06
13   A group of three anime characters is seated on...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     175      60-70  gpt-4o-2024-08-06
25   A scene from a period drama set in the 1800s, ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     231      60-70  gpt-4o-2024-08-06
29   A vibrant urban street scene in London capture...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     264      60-70  gpt-4o-2024-08-06
34   A serene landscape photograph captures a beaut...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     157      60-70  gpt-4o-2024-08-06
36   The photograph captures a modern, cozy indoor-...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     271      60-70  gpt-4o-2024-08-06
39   A close-up digital painting from the movie 'Sp...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     200      60-70  gpt-4o-2024-08-06
50   A modern, minimalist job advertisement flyer w...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     276      60-70  gpt-4o-2024-08-06
55   Theresa May, the Prime Minister of the United ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     218      60-70  gpt-4o-2024-08-06
63   A dynamic action shot captures an extreme spor...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     183      60-70  gpt-4o-2024-08-06
64   An anime-style illustration depicts a calm sce...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     260      60-70  gpt-4o-2024-08-06
73   A dynamic action shot captures eight rowers in...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     222      60-70  gpt-4o-2024-08-06
78   A cinematic photograph captures an intimate sc...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     281      60-70  gpt-4o-2024-08-06
83   A promotional photograph featuring Hector Jimé...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     180      60-70  gpt-4o-2024-08-06
87   A landscape photograph captures a historic ste...  pg-captioner  [{'answer': 'Yes', 'category': 'position', 'qu...  ...                     265      60-70  gpt-4o-2024-08-06
89   A close-up photograph captures a person's hand...  pg-captioner  [{'answer': 'yes', 'category': 'position', 'qu...  ...                     254      60-70  gpt-4o-2024-08-06
90   The interior showcases a stylish entryway lead...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     237      60-70  gpt-4o-2024-08-06
93   A dynamic action shot captures an athlete perf...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     252      60-70  gpt-4o-2024-08-06
102  A movie poster for 'Snatch' featuring six men ...  pg-captioner  [{'answer': 'Yes', 'category': 'text', 'questi...  ...                     229      60-70  gpt-4o-2024-08-06
107  A 3D rendering of a playful and colorful still...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     277      60-70  gpt-4o-2024-08-06
109  A cozy indoor scene featuring a polished woode...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     254      60-70  gpt-4o-2024-08-06
114  A close-up 3D animated scene depicts an emotio...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     240      60-70  gpt-4o-2024-08-06
117  A still life photograph features a cluttered w...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     159      60-70  gpt-4o-2024-08-06
121  A majestic, historical building is covered in ...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     202      60-70  gpt-4o-2024-08-06
126  A modern office workspace designed with a focu...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     195      60-70  gpt-4o-2024-08-06
134  A captivating food photograph showcases three ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     200      60-70  gpt-4o-2024-08-06
137  The scene from the movie 'Scarface', directed ...  pg-captioner  [{'answer': 'no', 'category': 'color', 'questi...  ...                     243      60-70  gpt-4o-2024-08-06
138  A close-up wildlife photograph captures a peac...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     286      60-70  gpt-4o-2024-08-06
139  A photograph captures a vintage gold Mercedes-...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     239      60-70  gpt-4o-2024-08-06
151  A photograph of the iconic Disney castle taken...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     231      60-70  gpt-4o-2024-08-06
170  A dynamic action shot captures two male triath...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     300      60-70  gpt-4o-2024-08-06
172  A candid street photograph taken from an eye-l...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     311      60-70  gpt-4o-2024-08-06
177  A vibrant nighttime urban scene featuring mult...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     231      60-70  gpt-4o-2024-08-06
182  A whimsical digital illustration of a cat in a...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     190      60-70  gpt-4o-2024-08-06
183  The scene captures an urban setting in Missour...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     244      60-70  gpt-4o-2024-08-06
186  A dramatic scene from a period piece set in th...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     284      60-70  gpt-4o-2024-08-06
196  A cinematic still from a 1980s-inspired film c...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     282      60-70  gpt-4o-2024-08-06
197  A movie poster featuring two characters, Hermi...  pg-captioner  [{'answer': 'Yes', 'category': 'text', 'questi...  ...                     235      60-70  gpt-4o-2024-08-06

[39 rows x 10 columns]
```

#### Sample 0

candidate_caption: A surreal 3D digital illustration features a woman's face in an avant-garde composition, divided into two parts. The left side shows her entire head with straight black hair parted at the middle, adorned with multiple gold stud earrings on both ears, including three small stones near the top of her right ear. Inside her head, which has been hollowed out like a mask, four vibrant sky blue butterflies (#4bc6f0) with dark brown edges and intricate vein patterns are visible, creating a whimsical scene reminiscent of morpho butterfly wings. A third butterfly rests on her shoulder, while another flies above to the left. Her eyes are closed, and she has a serene expression with a single teardrop-shaped gem embedded below her left eye, suggesting tears or emotion. Her lips are slightly parted, revealing teeth, and her skin texture is smooth with subtle pores and fine lines around the mouth area. A portion of her nose remains attached to the right side of the face, appearing detached from the rest. Her eyebrow is thick and well-defined. She holds the detached facial mask on a thin metallic rod, which extends diagonally from bottom right to upper left. The woman wears a dark gray kimono-style robe with white floral patterns and thin red branches. The background consists of soft white and light gray hues (#e2e8ef), featuring abstract shapes resembling blurred leaves or petals, enhancing the dreamlike quality. A large circular window adds depth to the scene. Additional elements include a small metallic object resembling a tear drop near her cheekbone and a ring with a greenish-blue stone and silver band on her index finger. The overall mood is contemplative yet enigmatic, with balanced lighting and moderate contrast, emphasizing the interplay between human form and nature-inspired elements.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the butterflies primarily blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the face mask on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there a butterfly on the left side above the head?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the face expression content?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there five butterflies?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a butterfly in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is there a butterfly sitting on the hand?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a digital artwork?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a high level of brightness?'}]

openai_answers: 1. Is the color of the butterflies primarily blue?  
   - yes

2. Is the face mask on the right side of the image?  
   - no

3. Is there a butterfly on the left side above the head?  
   - yes

4. Is the face expression content?  
   - yes

5. Is the background blurred?  
   - yes

6. Are there five butterflies?  
   - no

7. Is there a butterfly in the image?  
   - yes

8. Is there a butterfly sitting on the hand?  
   - n/a

9. Does the image have a cool color palette?  
   - yes

10. Is the image a digital artwork?  
    - yes

11. Is the image color graded with high contrast?  
    - n/a

12. Does the image have a high level of brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 12  

Score = (8/12) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 12 questions were answered correctly, resulting in a score of 66.67%.

token_count: 357

caption_vocabulary_size: 233

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 3

candidate_caption: Three men are seated at a black table covered with a dark blue cloth, engaged in what appears to be a live broadcast or podcast discussion. The man on the left is wearing glasses and a white Callaway cap with 'GOLF' written in black text, paired with a light gray short-sleeved button-up shirt featuring thin vertical stripes and subtle diagonal patterns. He has a silver laptop open in front of him with a sticker reading 'CBS SPORTS NETWORK', accompanied by a white paper cup. The center man is using a black laptop with his arms crossed, dressed in a plain black t-shirt. The rightmost man is gesturing actively while speaking, wearing a white short-sleeved button-up shirt with a delicate floral pattern in shades of beige and gray. All three men wear black headsets with microphones. Various items including another coffee cup, colorful snack pack, papers, and recording equipment are scattered across the table. Behind them is a metal railing separating the broadcasting area from an outdoor practice range where several people can be seen warming up under red umbrellas against a backdrop of dense green trees under a clear sky. To the right, there's a large white tent structure with a visible logo that reads 'PGA TOUR' along with other graphics. The scene is well-lit by natural daylight, providing even illumination across the entire setting. At the bottom of the image, there is text that reads 'BEST OF BOOMER & GIO' in white letters on a black background, followed by 'AKSHAY "SLIM REAPER" BHATIA' in bold white letters on a yellow background. Additionally, two logos with 'BOOMER AND GIO' in orange and red text on a black background flank the central name. The network logo 'CBS SPORTS NETWORK' appears in white at the bottom right corner.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': 'Does the image contain the text \'AKSHAY "SLIM REAPER" BHATIA\'?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the largest text white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center wearing a black t-shirt?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person on the left side wearing a cap?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person on the right side showing something with their hands?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the middle person focused on the laptop?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person on the left look attentive?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image slightly blurry?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the building in the background large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the cup on the table cylindrical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three people in the foreground?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person on the left wearing headphones?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the backdrop of the image outdoors?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken during the day?'}
 {'answer': 'yes', 'category': 'text', 'question': "Is 'BEST OF BOOMER & GIO' a part of the displayed text?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there laptops in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there microphones in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a coffee cup in the image?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a neutral color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a talk show?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high brightness?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'AKSHAY "SLIM REAPER" BHATIA'?  
   - yes

3. Is the color of the largest text white?  
   - n/a

4. Is the person in the center wearing a black t-shirt?  
   - yes

5. Is there a person on the left side wearing a cap?  
   - yes

6. Is the person on the right side showing something with their hands?  
   - yes

7. Is the middle person focused on the laptop?  
   - n/a

8. Does the person on the left look attentive?  
   - n/a

9. Is the image slightly blurry?  
   - n/a

10. Is the building in the background large?  
    - n/a

11. Is the cup on the table cylindrical?  
    - yes

12. Are there three people in the foreground?  
    - yes

13. Is the person on the left wearing headphones?  
    - yes

14. Is the backdrop of the image outdoors?  
    - yes

15. Is the image taken during the day?  
    - yes

16. Is 'BEST OF BOOMER & GIO' a part of the displayed text?  
    - yes

17. Are there laptops in the image?  
    - yes

18. Are there microphones in the image?  
    - yes

19. Is there a coffee cup in the image?  
    - yes

20. Does the image have a neutral color palette?  
    - n/a

21. Is the image a shot from a talk show?  
    - yes

22. Does the image have high brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 15  
Total Number of Questions: 22  

Score = (15/22) × 100 = 68.18

score: 68.18

reasons: The score is calculated based on the number of correct answers out of the total questions. Out of 22 questions, 15 were answered correctly, resulting in a score of 68.18%.

token_count: 370

caption_vocabulary_size: 217

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 13

candidate_caption: A group of three anime characters is seated on an ornate forest green couch with tufted buttons, buttonholes, and intricate wooden carvings in the background. The character on the left is a man with short pink hair and light blue eyes, wearing a brown suit with black accents over a white shirt. He has a calm expression and his hands rest on his lap. To his right sits a young girl with wavy pink hair adorned with a large coral-colored bow headband and a matching dress featuring a green scarf tied into a bow at the collar. She wears puffy sleeves and a white lace apron or skirt underneath. Her face shows a curious or anxious expression as she looks upwards, her large expressive blue eyes framed by long eyelashes and rosy cheeks. On the far right is a blonde woman with long hair styled in an updo with loose strands framing her face, wearing a sky-blue dress with puffy sleeves and a square neckline. The dress features a white underlayer with gold trim around the shoulders and waist, and a small bow detail at the waistline. She also wears light blue earrings and has a gentle smile while looking slightly to the side. The background consists of a muted teal chandelier-style wallpaper below a dark gray upper section, with part of a beige wall visible to the left. The lighting is soft and even, creating a warm and inviting atmosphere typical of 2D animation style.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the sofa green?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is one of the characters wearing a blue dress?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the small child in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the woman with blonde hair to the right of the child?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the child looking surprised?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the sofa large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the buttons on the sofa round?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a little girl in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the man on the left side of the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette have pastel tones?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the color of the sofa green?  
   - yes

2. Is one of the characters wearing a blue dress?  
   - yes

3. Is the small child in the center of the image?  
   - yes

4. Is the woman with blonde hair to the right of the child?  
   - yes

5. Is the child looking surprised?  
   - no

6. Is the sofa large?  
   - n/a

7. Are the buttons on the sofa round?  
   - n/a

8. Are there three people in the image?  
   - yes

9. Is there a little girl in the image?  
   - yes

10. Is the man on the left side of the image?  
    - yes

11. Does the image show indoors?  
    - yes

12. Does the image's color palette have pastel tones?  
    - n/a

13. Is the image from a cartoon?  
    - yes

14. Does the image have high contrast?  
    - n/a

15. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 15  

Score = (9/15) × 100 = 60

score: 60.0

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. In this case, 9 out of 15 questions were answered with 'yes', resulting in a score of 60%.

token_count: 287

caption_vocabulary_size: 175

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 25

candidate_caption: A scene from a period drama set in the 1800s, featuring Amanda Seyfried as the main subject standing near a pond in a lush park-like setting. She is positioned slightly left of center, facing the camera with her body turned slightly to her right. Her long, wavy strawberry blonde hair cascades over her shoulders, styled in loose curls with some strands falling freely around her face. She wears an off-white blouse adorned with intricate embroidery patterns, small bow ties at the neckline, and lace details along the edges. A sheer white shawl or scarf drapes elegantly over her shoulders and arms, its fabric softly flowing with subtle fringes visible on the sleeves. The garment features delicate floral patterns in soft pink and green, adding a touch of color to the ensemble. A light green corset cinches her waist before flowing into a pastel yellow skirt made of lightweight material with vertical stripes and subtle floral accents. A simple pendant necklace adorns her neck. In the midground, there's a serene pond covered with patches of water lilies and algae, surrounded by tall grasses and reeds. Another figure dressed in period-appropriate attire can be seen walking away across the grassy area towards the trees in the distance. The background showcases dense foliage of various shades of green trees under an overcast sky, creating a calm and contemplative atmosphere. On the far right edge of the frame, part of a white wooden bridge structure is faintly visible. The overall mood is serene and introspective, enhanced by natural daylight illuminating the scene evenly and casting gentle shadows. The color palette includes muted tones such as forest greens, pale yellows, whites, and touches of peach, contributing to the vintage feel of the image.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the woman's dress white?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the woman on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the woman in the foreground?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the woman smiling?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the woman large relative to the surroundings?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one woman in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the woman standing near the water?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a natural color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}]

openai_answers: 1. Is the woman's dress white? - no
2. Is the woman on the left side of the image? - yes
3. Is the woman in the foreground? - yes
4. Is the woman smiling? - n/a
5. Is the background blurred? - n/a
6. Is the woman large relative to the surroundings? - n/a
7. Is there one woman in the image? - yes
8. Is the woman standing near the water? - yes
9. Does the image show outdoors? - yes
10. Does the image have a natural color palette? - yes
11. Is the image a shot from a film? - yes

Score: (7/11) × 100 = 63.64

score: 63.64

reasons: The score is calculated based on the number of 'yes' responses out of the total questions. There are 7 'yes' responses out of 11 questions, resulting in a score of 63.64.

token_count: 349

caption_vocabulary_size: 231

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 29

candidate_caption: A vibrant urban street scene in London captures a rainy autumn day, with wet cobblestone pavement reflecting the surroundings and scattered golden-brown leaves indicating fall foliage. On the left side of the image, a modern red double-decker bus numbered 38 travels along the road, its headlights on and 'Hickory Central' displayed on an electronic signboard. The bus's sleek design features black windows and distinctive yellow wheel hubs. In the center-right foreground, near a curved building corner, stands a classic British red telephone booth with glass panels and a crown-topped roof, illuminated from within. A person dressed in dark clothing is using or approaching the phone booth, holding onto it while looking up at something above. To their right, a circular speed limit sign reading '20' is visible, indicating a limit of 20 miles per hour. Adjacent to this is the entrance of the shop named 'ANTONI ALIS', featuring a large black awning with white decorative lettering that includes a star symbol between 'ANTONI' and 'ALIS'. The storefront showcases warm interior lighting through its large windows, creating a cozy atmosphere. The buildings surrounding these elements are tall Victorian-style structures made of rich reddish-brown brick with ornate stone moldings around the windows and arches. Large trees with thick trunks and branches extending outward line both sides of the street, their leaves displaying a mix of amber yellows, burnt oranges, and greens, adding warmth to the cool, overcast ambiance. The overall color palette includes deep maroon (#2a1c1b), pale beige (#d6c8ac), warm brown (#856050), muted sage green (#9aa79e), steel blue (#7f94a0), and russet (#7c5f45), contributing to a nostalgic yet lively mood typical of autumn in London. The wet surfaces create glossy reflections of the surroundings, enhancing the atmospheric quality of the photograph.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'ANTONI'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the bus red?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the tree's foliage yellow and orange?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bus on the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the telephone booth on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bus to the left of the central tree?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person on the left of the phone booth?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the bus blurry?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bus larger than the telephone booth?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the telephone booth rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one bus in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the bus driving on a wet street?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a rainy day?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have warm color tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'ANTONI'?  
   - yes

3. Is the color of the bus red?  
   - yes

4. Is the tree's foliage yellow and orange?  
   - yes

5. Is the bus on the left side of the image?  
   - yes

6. Is the telephone booth on the right side of the image?  
   - no

7. Is the bus to the left of the central tree?  
   - n/a

8. Is the person on the left of the phone booth?  
   - no

9. Is the bus blurry?  
   - n/a

10. Is the bus larger than the telephone booth?  
    - n/a

11. Is the telephone booth rectangular?  
    - yes

12. Is there only one bus in the image?  
    - yes

13. Is there a tree in the image?  
    - yes

14. Is the bus driving on a wet street?  
    - yes

15. Does the image show a rainy day?  
    - yes

16. Does the image have warm color tones?  
    - yes

17. Is the image a photograph?  
    - n/a

18. Does the image have high contrast?  
    - n/a

19. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 19  

Score = (12/19) × 100 = 63.16

score: 63.16

reasons: The score is calculated based on the number of 'yes' answers that match the expected conditions. Out of 19 questions, 12 were answered 'yes', resulting in a score of 63.16%.

token_count: 394

caption_vocabulary_size: 264

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 34

candidate_caption: A serene landscape photograph captures a beautifully lit Christmas tree floating on a dark wooden platform in calm blue water during twilight. The tree, adorned with colorful multicolored LED lights and topped with a large glowing amber star, stands out against the surrounding darkness. Its reflection shimmers on the surface of the water, creating a striking contrast between warm yellow, red, green, blue, purple, and white hues and cool blues of the night sky and lake. The platform is positioned slightly off-center to the left, with a small wooden chair visible next to the tree's base. Surrounding the water body are rocky shorelines and dense evergreen forests forming silhouettes that create a stark contrast against the gradient sky transitioning from deep navy blue at the top through vibrant orange near the horizon to light blue higher up. Rolling hills or distant mountains form a natural boundary, their peaks fading into shadows. The foreground features gently rippling water reflecting the tree's illumination, while the background showcases a breathtaking view of mountains, enhancing the tranquil atmosphere of this festive scene. The overall composition follows the rule of thirds, with the brightly lit tree as the focal point, set against the majestic backdrop of nature's twilight beauty.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the lake color blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the Christmas tree multicolored?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the Christmas tree in the left part of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the mountains behind the Christmas tree?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the Christmas tree small within the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the Christmas tree triangular?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the Christmas tree floating on water?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the Christmas tree in front of the forest?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the lake color blue?  
   - yes

2. Is the Christmas tree multicolored?  
   - yes

3. Is the Christmas tree in the left part of the image?  
   - yes

4. Are the mountains behind the Christmas tree?  
   - yes

5. Is the image sharp?  
   - n/a

6. Is the Christmas tree small within the image?  
   - n/a

7. Is the Christmas tree triangular?  
   - yes

8. Is the Christmas tree floating on water?  
   - yes

9. Is the Christmas tree in front of the forest?  
   - yes

10. Does the image show outdoors?  
    - yes

11. Is the image a photograph?  
    - yes

12. Is the image color graded with high saturation?  
    - n/a

13. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 13  

Score = (9/13) × 100 = 69.23

score: 69.23

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. Out of 13 questions, 9 were answered 'yes', resulting in a score of 69.23%.

token_count: 239

caption_vocabulary_size: 157

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 36

candidate_caption: The photograph captures a modern, cozy indoor-outdoor living space with a blend of contemporary design elements and natural greenery. The foreground features lush green plants with broad leaves and white flowers, creating a vibrant contrast against the marble-like flooring composed of alternating slate gray stone slabs and patches of ground cover vegetation. A rectangular glass door frame on the left side reflects parts of the room while revealing glimpses of the adjacent garden area beyond. In the midground, there's a light gray upholstered sofa positioned on the right side of the scene, featuring a textured fabric with rounded arms and a distinctive shape. A brown checkered pillow adds an earthy touch to this L-shaped sofa. To its left sits a single-seater brown leather armchair facing slightly away from the camera. Between them stands a low, rectangular coffee table made of white marble with angled edges, adorned with three books stacked vertically (one titled 'THE NEW MODERNIST' in white text, another labeled 'ART AND ARCHITECTURE', and one titled 'DESIGN') and a small red lampshade. Above the sofa hangs a modern floor lamp with a large white shade featuring a downward-angled neck, adding to the ambient lighting. The background showcases large sliding glass doors framed by pinkish-beige metal, opening up to an outdoor patio area. These doors are partially open, allowing ample natural light to flood the space and offering views of vertical wooden planks forming a fence. Above these doors, decorative brickwork with intricate geometric patterns creates a visually striking effect, transitioning into larger windows that allow additional light. The walls inside the room combine smooth surfaces painted in light gray tones and exposed concrete textures. Outside the glass doors, various potted plants add layers of texture and color to the setting. Green foliage extends from above, enhancing the connection between indoor comfort and outdoor serenity. The overall composition is balanced, inviting, and harmoniously blends indoor luxury with nature outside, emphasizing both comfort and style through soft colors, moderate contrast, and well-balanced exposure levels.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the sofa gray?'}
 {'answer': 'Yes', 'category': 'color', 'question': 'Are the frames pink?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the sofa on the right side of the image?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is there a plant in the bottom left corner of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the table to the left of the sofa?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the armchair to the left of the sofa?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the coffee table small?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the coffee table square?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one lamp on the table?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the sofa next to the window?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sofa gray?  
   - yes

2. Are the frames pink?  
   - yes

3. Is the sofa on the right side of the image?  
   - yes

4. Is there a plant in the bottom left corner of the image?  
   - n/a

5. Is the table to the left of the sofa?  
   - no

6. Is the armchair to the left of the sofa?  
   - yes

7. Is the coffee table small?  
   - yes

8. Is the coffee table square?  
   - no

9. Is there one lamp on the table?  
   - no

10. Is the sofa next to the window?  
    - yes

11. Does the image show daylight?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have high contrast?  
    - no

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 13  

Score = (8/13) × 100 ≈ 61.54

score: 61.54

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 13 questions were answered correctly, resulting in a score of approximately 61.54%.

token_count: 408

caption_vocabulary_size: 271

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 39

candidate_caption: A close-up digital painting from the movie 'Spider-Man: Across the Spider-Verse' features an intense, futuristic character's face. The character has wide-open green eyes with intricate reflections, surrounded by vibrant magenta shadows extending towards the temples, conveying urgency or surprise. Their skin tone transitions between yellow-green and red hues, blending into neon colors across their face, creating a dynamic visual effect. The hair is styled in a messy manner, partially covering the right side of the face, displaying striking gradients from turquoise to forest green with blue highlights, flowing diagonally from the upper left to lower right. A prominent pinkish-purple streak runs vertically down the right cheek, adding complexity to the color scheme. The background consists of geometric shapes in warm shades of amber yellow and goldenrod, intersected by sky blue triangles outlined in white lines against a textured surface resembling brushed metal. These shapes create depth and contrast, enhancing the cyberpunk aesthetic. Pixelated effects and glitch-like distortions are scattered throughout the artwork, contributing to its modern, digital feel. The lighting is bright and even, highlighting facial features without casting harsh shadows. High saturation and contrast emphasize the vividness of the colors, while the composition centers the face slightly off-center to the left. Stray strands of light brown hair are visible near the top center, framing the forehead. The overall style blends surrealism with digital art techniques, resulting in a highly saturated, energetic mood with high luminance and balanced exposure.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is there a lot of yellow present in the background?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the character in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the character's hair covering part of their face?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the character look serious?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Are there any artifacts in the image?'}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the character's face large in the image?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one character in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the character facing the front?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a vibrant color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there a lot of yellow present in the background?  
   - yes

2. Is the character in the center of the image?  
   - no

3. Is the character's hair covering part of their face?  
   - yes

4. Does the character look serious?  
   - n/a

5. Are there any artifacts in the image?  
   - yes

6. Is the character's face large in the image?  
   - yes

7. Is there only one character in the image?  
   - yes

8. Is the character facing the front?  
   - n/a

9. Does the image have a vibrant color palette?  
   - yes

10. Is the image from a cartoon?  
    - n/a

11. Is the image color graded with high saturation?  
    - yes

12. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 12  

Score = (8/12) × 100 = 66.67

score: 66.67

reasons: The score was calculated based on the number of 'yes' answers provided in the text. Out of 12 questions, 8 were answered with 'yes', resulting in a score of 66.67%.

token_count: 294

caption_vocabulary_size: 200

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 50

candidate_caption: A modern, minimalist job advertisement flyer with a clean and professional design set against an off-white (#e9ebe6) background. The composition is divided into three main sections using dark slate gray vertical bars on both sides. At the top left, there's a large rectangular section in dark charcoal gray (#4c4b52). Centered at the top, bold black text reads 'Job Vacancies' followed by 'We are looking for applicants' in regular sans-serif font. Below this, two identical columns detail the requirements for each Marketing Manager position, aligned centrally within their respective columns. Each column contains four lines of text describing specific qualifications: age requirement (must be at least 22 years old and able to work from London), degree requirement (must have a Bachelor's degree in marketing or a related business track or equivalent), and social media skills required (must be adept in handling specific social media platforms or skills, specified as needed). These descriptions are presented in smaller black sans-serif font. The left column lists these criteria twice, while the right column mirrors them but only once. Dark charcoal gray vertical bars separate each job description from the next. At the bottom center, there's a note for interested applicants: 'Interested applicants should send their curriculum vitae and cover letter to humanresource@mail.com by December 31.' On the right side, near the top, there's a company logo featuring an abstract floral-like design composed of human figures forming a circle, represented by small silhouettes connected by lines resembling petals or rays. Below the logo, 'COMPANY LOGO' is written in uppercase letters. Two thin dark gray vertical bars frame the top and bottom edges of the page. Contact information is provided at the bottom right corner, including phone number '012 345 6789', email address 'humanresource@mail.com', and website URL 'www.company.com'. The overall color palette consists primarily of shades of gray (#a8abb1, #c5cac2, #c7cbce, #a3adac) and black, creating high contrast against the lighter background. The typography used throughout the document combines Arial, Helvetica, and Futura Condensed Medium styles, giving it a professional appearance suitable for formal communication.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the text 'Marketing Manager' appear twice?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color light grey?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the text black and dark grey?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the company logo in the top right corner?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the contact email at the bottom of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the job title 'Marketing Manager' positioned under 'Job Vacancies'?"}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the contact phone number above the contact email?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the company logo circular?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an job advertisement?'}]

openai_answers: 1. **Answer Each Question:**

   - Does the text 'Marketing Manager' appear twice?  
     - yes

   - Is the background color light grey?  
     - no

   - Is the color of the text black and dark grey?  
     - yes

   - Is the company logo in the top right corner?  
     - no

   - Is the contact email at the bottom of the image?  
     - yes

   - Is the job title 'Marketing Manager' positioned under 'Job Vacancies'?  
     - n/a

   - Is the contact phone number above the contact email?  
     - yes

   - Is the company logo circular?  
     - yes

   - Is the image an job advertisement?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 6
   - Total Number of Questions: 9

   Score = (6/9) × 100 = 66.67

score: 66.67

reasons: The score was calculated based on the number of correct answers provided out of the total number of questions. The user answered 6 questions correctly out of 9, resulting in a score of 66.67%.

token_count: 450

caption_vocabulary_size: 276

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 55

candidate_caption: Theresa May, the Prime Minister of the United Kingdom, stands behind an oak-colored podium adorned with the UK's coat of arms in a formal outdoor setting. The coat of arms features a black background with intricate white details, including two lions standing on their hind legs facing left (one wearing a crown) and a unicorn standing on its hind legs facing right (also wearing a crown), flanking a central shield divided into four quarters containing various symbols. Above the shield sits a crown with three crowns visible - one larger at the top center, smaller ones above each side wing. Below the shield, the Latin phrase 'EDEI ET MON' is written in white block letters. May is positioned slightly to the right of center, facing the camera with a serious expression and lips parted as if speaking. She has short, light gray hair styled in a neat, classic manner with slight volume at the roots and subtle waves framing her face. Her attire consists of a navy blue blazer over a darker V-neck top, revealing a hint of skin underneath. A prominent chunky silver chain necklace adorns her neck, complementing her look. The lighting is natural daylight, providing even illumination across the scene without harsh shadows. Behind her, the dark charcoal-gray exterior wall of 10 Downing Street is visible, featuring vertical black iron bars forming a fence-like pattern. A partially visible window with white I-bears, a small stone base, and part of a door are also noticeable. The ground appears paved with smooth gray stones arranged in a grid pattern. The overall mood of the photograph is formal and official, capturing a moment of public address by the Prime Minister in a dignified and composed atmosphere.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background wall black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the podium in front of the person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking serious?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is Theresa May in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the logo on the podium circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the background wall black?  
   - Answer: no

2. Is the person in the center of the image?  
   - Answer: no

3. Is the podium in front of the person?  
   - Answer: yes

4. Is the person looking serious?  
   - Answer: yes

5. Is Theresa May in the image?  
   - Answer: yes

6. Is the logo on the podium circular?  
   - Answer: no

7. Is there one person in the image?  
   - Answer: yes

8. Does the image show outdoors?  
   - Answer: yes

9. Is the image a photograph?  
   - Answer: yes

**Calculate Score:**

Number of Correct Answers: 6  
Total Number of Questions: 9  

Score = (6/9) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 6 out of 9 answers were correct, resulting in a score of 66.67%.

token_count: 339

caption_vocabulary_size: 218

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 63

candidate_caption: A dynamic action shot captures an extreme sports athlete performing an aerial maneuver mid-jump during nighttime, likely at an Olympic event in Sochi 2014. The athlete is positioned slightly right of center, facing left in profile view with their body curved downward, showcasing the skillful execution of the trick. They are dressed in a white jacket with black sleeves over a colorful patterned bib displaying 'Sochi 2014' on the chest, paired with black pants featuring neon green accents along the seams. A small red circular Japanese flag patch adorns the left sleeve of the jacket. The rider wears a black helmet with ventilation holes and a green visor, along with gloves that have neon green accents on the fingers. Their snowboard, with its distinctive red, blue, and white design, is angled diagonally beneath them, partially visible against the dark background. Intense artificial floodlights from the left side create a dramatic effect, casting bright light onto the scene and causing lens flares. This lighting emphasizes the movement and energy of the jump, contrasting sharply with the completely dark night sky filled with faint outlines of tree branches. Small particles or droplets are suspended in the air around the athlete, adding to the sense of motion. The overall mood is intense and focused, highlighting the athleticism and precision required in this high-stakes sport under controlled conditions typical of competitive events.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background dark?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the light to the left of the person?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have lens flare?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a snowboard in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person holding the snowboard?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show night?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the background dark?  
   - yes

2. Is the person in the right side of the image?  
   - yes

3. Is the light to the left of the person?  
   - yes

4. Is the background blurred?  
   - n/a

5. Does the image have lens flare?  
   - yes

6. Is there one person?  
   - yes

7. Is there a snowboard in the image?  
   - yes

8. Is the person holding the snowboard?  
   - n/a

9. Does the image show night?  
   - yes

10. Is the image a photograph?  
    - n/a

11. Does the image have high contrast?  
    - n/a

**Score Calculation:**

Number of Correct Answers: 7  
Total Number of Questions: 11  

Score = (7/11) × 100 = 63.64

score: 63.64

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. In this case, 7 out of 11 questions were answered with 'yes', resulting in a score of 63.64%.

token_count: 274

caption_vocabulary_size: 183

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 64

candidate_caption: An anime-style illustration depicts a calm scene set in a brightly lit hospital or clinic hallway. The foreground features two female characters sitting side by side on pastel pink benches with white seats arranged diagonally from bottom left to top right of the frame, their legs crossed and hands resting gently on their laps. The character on the left has long straight brown hair adorned with a pink headband, wearing a cream-colored blouse with long sleeves under a navy blue vest featuring a red tie, paired with a knee-length maroon skirt. She's barefooted but appears to be wearing sheer black stockings. Next to her sits another character with short light blue hair styled in bangs, dressed similarly in a dark outfit with a red necktie. Both characters are positioned facing slightly right, looking towards an unseen point off-camera. The midground includes more pink benches, reflective flooring, and beige walls with soft peach trim. Two potted plants with lush green foliage add touches of nature to the space - one large leafy plant near the left wall and another smaller one near the center-right. In the background, there's a reception desk on the left side with three figures behind it, likely staff members engaged in conversation. A large framed display showing an indistinct scene with people holding flowers is mounted on the right wall above a sink area. The hallway extends into the distance, revealing several closed doors painted in soft pastel shades of pink, yellow, and beige. The ceiling features recessed lighting fixtures arranged in a geometric pattern, emitting a cool white glow that illuminates the entire area evenly. The overall color palette consists of warm hues like beige (#e9d8ca), chestnut (#5c3a1f), and taupe (#947b6f), complemented by cooler tones such as powder blue (#9cb0ba) and slate gray (#64747e). The bright, diffused lighting creates a serene atmosphere while emphasizing the clean, modern aesthetic of the setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the hair of the person in the foreground brown?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person sitting in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there a large plant on the left side of the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the plant on the left side of the image small within the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the benches in the image rectangular?'}
 {'answer': 'no', 'category': 'count', 'question': 'Are there two people in the foreground?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an indoor scene?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look calm?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from an animated movie?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high brightness?'}]

openai_answers: 1. Is the hair of the person in the foreground brown?  
   - yes

2. Is the person sitting in the center of the image?  
   - n/a

3. Is there a large plant on the left side of the image?  
   - yes

4. Is the background blurred?  
   - no

5. Is the plant on the left side of the image small within the image?  
   - no

6. Are the benches in the image rectangular?  
   - yes

7. Are there two people in the foreground?  
   - yes

8. Does the image show an indoor scene?  
   - yes

9. Does the person look calm?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image from an animated movie?  
    - n/a

12. Does the image have high brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 12  

Score = (8/12) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 12 questions were answered correctly, resulting in a score of 66.67%.

token_count: 397

caption_vocabulary_size: 260

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 73

candidate_caption: A dynamic action shot captures eight rowers in mid-motion during a competitive boat race, creating an intense scene of synchronized teamwork. The photograph is taken from a slightly elevated angle, focusing on the energetic movement of the team as they row with black paddles through golden-hued water. Each rower wears vibrant orange sleeveless shirts and dark shorts or pants, their faces mostly obscured by splashes and motion blur. The rows are arranged diagonally across the frame, forming a powerful diagonal line that adds to the sense of motion. Water droplets are frozen in time around them, forming a dramatic mist-like effect that enhances the sense of speed and energy. The lighting is warm and natural, provided by sunlight, casting a bright glow over the entire scene and highlighting the fine details of the droplets' sparkle. This backlighting creates high contrast between illuminated areas and darker shadows, adding depth and texture to the image. The color palette includes rich earthy tones like deep umber (#261a0f), light beige (#d3c49e), warm brown (#7b5c33), muted taupe (#8c8066), soft gray (#9e9894), and sandy yellow (#ae9862), contributing to the overall warm and inviting atmosphere. In the foreground, the rippling surface of the water reflects the overhead sun, creating a shimmering effect with scattered highlights. The background remains blurred due to shallow depth of field, emphasizing the rapid movement of the rowers while maintaining focus on the main subjects. The composition's horizontal orientation further accentuates the width and flow of the water, effectively conveying the intensity, coordination, and raw power of this competitive aquatic sport.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the outfits red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the people in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the water below the people?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image blurry?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the paddles straight?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there six people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there water in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the people sitting in a boat?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the color of the outfits red? - no
2. Are the people in the center of the image? - n/a
3. Is the water below the people? - yes
4. Is the image blurry? - yes
5. Are the paddles straight? - n/a
6. Are there six people in the image? - no
7. Is there water in the image? - yes
8. Are the people sitting in a boat? - yes
9. Does the image show daylight? - yes
10. Does the image have a warm color palette? - yes
11. Is the image a photograph? - yes
12. Does the image have high contrast? - yes

Score = (8/12) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of 'yes' responses out of the total questions. There are 8 'yes' responses out of 12 questions, resulting in a score of 66.67.

token_count: 336

caption_vocabulary_size: 222

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 78

candidate_caption: A cinematic photograph captures an intimate scene in a dimly lit bedroom at night, featuring a person standing near the center-right of the frame. The individual, dressed in a loose-fitting short-sleeved shirt with rolled-up sleeves and dark pants or skirt, is seen in silhouette against a striking beam of warm amber-orange light emanating from an open doorway to their right. This artificial light source creates a high-contrast effect, casting diagonal beams across the room and bathing the subject in a reddish glow that illuminates the surrounding area, adding depth and dimension to the composition. The person's head is slightly tilted downward, with their left hand extended forward as if reaching towards something out of view. Their right arm rests by their side. In the foreground, there is a partially visible bed with an ornate metal frame featuring curved top rails, decorative horizontal bars, and rounded finials at each post. The bedding appears floral-patterned with intricate designs in muted tones of beige and white, though its details are largely obscured due to low lighting conditions. A framed botanical print hangs on the wall above the bed, depicting a plant illustration within a simple gold-framed rectangular shape. To the far left, heavy curtains with subtle vertical stripes can be seen covering windows, contributing to the overall moody atmosphere. The background reveals part of another room through the open door, where more curtains are visible. The walls have horizontal paneling, creating texture and depth throughout the space. The color palette includes deep forest greens (#191e15), rich mahogany browns (#3a2d1c), vibrant coral pinks (#f17b6a), warm peach hues (#eb7055), soft rose tones (#ca7e8c), and muted sage greens (#8aa59b). The low-key lighting technique enhances the mysterious mood, emphasizing shadows and highlights while maintaining a balanced exposure despite the high contrast between illuminated areas and darker surroundings. This atmospheric shot evokes feelings of intrigue, suspense, and introspection, blending elements of vintage realism with contemporary cinematic techniques.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the dominant color of the light red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person standing in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person near the door?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look calm?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have film grain?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bed large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a framed picture in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person illuminated by the light?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the dominant color of the light red?  
   - yes

2. Is the person standing in the center of the image?  
   - no

3. Is the person near the door?  
   - yes

4. Does the person look calm?  
   - n/a

5. Does the image have film grain?  
   - n/a

6. Is the bed large?  
   - n/a

7. Is there only one person in the image?  
   - yes

8. Is there a framed picture in the image?  
   - yes

9. Is the person illuminated by the light?  
   - yes

10. Does the image show indoors?  
    - yes

11. Does the image have a warm color palette?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have low brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 13  

Score = (9/13) × 100 = 69.23

score: 69.23

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. There are 9 'yes' answers out of 13 questions, resulting in a score of 69.23%.

token_count: 412

caption_vocabulary_size: 281

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 83

candidate_caption: A promotional photograph featuring Hector Jiménez, a defender for Austin FC, positioned in the center of the frame. He is wearing an official green and black vertically striped soccer jersey with white stripes on the shoulders and sleeves. The Adidas logo is visible on the right chest area. On the left side of the jersey is the team's emblem, which includes a tree symbol inside a circular badge, along with the word 'AUINN' above it. Additional sponsor logos are present on both sides of the jersey, including one that reads 'SPEND' near the sleeve. His short brown hair is neatly styled, and he has a light beard and mustache. Hector is smiling warmly while looking directly at the camera, with his face illuminated by natural daylight coming from the front-left side, creating soft shadows on his features. The background showcases an empty stadium with rows of green seats extending into the distance, creating depth in the composition. Modern architectural elements such as glass windows, metal railings, and concrete structures are visible, along with large glass panels lining the interior spaces. A curved roof structure is partially visible, adding to the stadium's contemporary design. Text in bold white sans-serif font at the bottom left corner identifies Hector Jiménez as '#16 • Defender • Austin FC'. The overall mood is professional yet approachable, captured in bright, balanced lighting typical of a sports documentary style.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'HECTOR JIMENEZ'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is there number '16' in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's jersey green and black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the text to the left of the person?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the text at the bottom left corner?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person smiling?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person in the image fairly large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person wearing a sports jersey?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the player wearing a striped jersey?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Does the image contain the text 'HECTOR JIMENEZ'?  
   - n/a

2. Is there number '16' in the image?  
   - yes

3. Is the person's jersey green and black?  
   - yes

4. Is the person in the center of the image?  
   - yes

5. Is the text to the left of the person?  
   - yes

6. Is the text at the bottom left corner?  
   - yes

7. Is the person smiling?  
   - yes

8. Is the background blurred?  
   - no

9. Is the person in the image fairly large?  
   - n/a

10. Is there only one person in the image?  
    - yes

11. Is the person wearing a sports jersey?  
    - yes

12. Is the player wearing a striped jersey?  
    - yes

13. Does the image have high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 13  

Score = (9/13) × 100 = 69.23

score: 69.23

reasons: The score is calculated based on the number of 'yes' answers that match the criteria provided. Out of 13 questions, 9 were answered 'yes', resulting in a score of 69.23%.

token_count: 278

caption_vocabulary_size: 180

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 87

candidate_caption: A landscape photograph captures a historic steam train crossing an impressive stone viaduct, known as Glenfinnan Viaduct, in Scotland's Highland region. The scene is set during daylight hours with natural lighting enhancing the colors of early autumn. A black steam locomotive leads a series of seven burgundy passenger carriages labeled 'The Jacobite Express,' each featuring large windows and red trimmings. The train travels along the curved track of the viaduct, which consists of multiple light gray stone arches supported by thick columns. Each arch spans the entire width of the railway, creating a striking architectural feature against the vibrant backdrop. The tracks are covered with brown wooden sleepers and rust-colored rails, curving smoothly through the landscape. A prominent plume of white steam billows from the locomotive's chimney, adding dynamism to the otherwise serene setting. The viaduct curves slightly to the right, allowing viewers to see more of the stunning landscape beyond. Surrounding the viaduct are rolling hills blanketed in lush vegetation displaying a rich palette of autumn hues - golden yellows, burnt oranges, forest greens, and rusty browns. Trees with varying shades of green, yellow, and orange leaves dot the landscape, indicating the season. Some trees show signs of early fall, while others retain their summer greenery. The foreground features several leafy trees with bright lime-green foliage partially obscuring parts of the structure, adding depth and complexity to the composition. In the background, additional hills with sparse trees and shrubs can be seen under a slightly overcast sky, contributing to the tranquil atmosphere. The color grading includes shades of taupe (#3a321c), pale gold (#c9b16d), warm beige (#8e7f64), muted sage (#6d7451), soft terracotta (#c97d5b), and deep charcoal (#2e262b). The overall mood is peaceful yet nostalgic, capturing the essence of travel and exploration in this picturesque Scottish setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'position', 'question': 'Is the train in the center of the image?'}
 {'answer': 'No', 'category': 'relative position', 'question': 'Is the steam above the train?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the bridge large?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Are the arches of the bridge curved?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there seven train cars visible?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a train in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the train moving on the bridge?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have warm color tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the train in the center of the image?  
   - Answer: n/a

2. Is the steam above the train?  
   - Answer: yes

3. Is the bridge large?  
   - Answer: yes

4. Are the arches of the bridge curved?  
   - Answer: yes

5. Are there seven train cars visible?  
   - Answer: yes

6. Is there a train in the image?  
   - Answer: yes

7. Is the train moving on the bridge?  
   - Answer: yes

8. Does the image show outdoors?  
   - Answer: yes

9. Does the image have warm color tones?  
   - Answer: yes

10. Is the image a photograph?  
    - Answer: yes

11. Does the image have high contrast?  
    - Answer: n/a

12. Is the image color graded with high saturation?  
    - Answer: n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 12  

Score = (8/12) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of questions with definitive 'yes' or 'no' answers. Out of 12 questions, 8 were answered with 'yes', resulting in a score of 66.67%.

token_count: 404

caption_vocabulary_size: 265

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 89

candidate_caption: A close-up photograph captures a person's hands meticulously chopping green onions on a light brown wooden cutting board with visible grain patterns, scratches, and signs of frequent use. The individual is wearing clear plastic gloves, revealing slightly tanned skin beneath. They are dressed in a gray hoodie featuring a subtle horizontal stripe pattern near the hem and a blue-and-white vertically striped apron tied around their waist with a white ribbon bow. The knife being used has a red handle with black text 'KITCHEN' printed along its length. Freshly cut green onion pieces are piled neatly on the board, showcasing various stages from whole to diced. Some green onions remain whole while others are halved or chopped into small cubes. In the foreground, three empty light brown wooden bowls are partially visible, one filled with bright yellow diced mangoes and vibrant orange-red bell pepper chunks, adding pops of color to the scene. To the right, two metallic spray bottles—one cobalt blue with a black pump dispenser, another silver—stand upright on the table. The background features a vibrant azure blue (#1e5b9c) and white checkered tablecloth that extends across the entire frame, creating a dynamic backdrop. Blurred objects include wooden crates containing assorted colorful produce such as lemons and tomatoes, suggesting an outdoor market setting. Two stainless steel mixing bowls sit nearby, one holding more chopped green onions. The lighting appears natural and diffused, illuminating the scene evenly and highlighting the textures and colors of the ingredients and utensils without casting harsh shadows. This creates a warm and inviting atmosphere, emphasizing the freshness and variety of the food preparation process. The overall composition follows the rule of thirds, focusing on the hands and the cutting action while maintaining context through the surrounding elements, resulting in a balanced and visually appealing image that evokes a sense of busy kitchen activity.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'position', 'question': 'Is the chopping board in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person cutting vegetables behind the chopping board?'}
 {'answer': 'no', 'category': 'entity', 'question': "Is the person's face visible?"}
 {'answer': 'no', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the chopping board large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the chopping board rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two metal bottles in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a wooden bowl in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person holding a knife?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a kitchen?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the chopping board in the center of the image?  
   - yes

2. Is the person cutting vegetables behind the chopping board?  
   - yes

3. Is the person's face visible?  
   - no

4. Is the background blurred?  
   - yes

5. Is the chopping board large?  
   - n/a

6. Is the chopping board rectangular?  
   - n/a

7. Are there two metal bottles in the image?  
   - yes

8. Is there a wooden bowl in the image?  
   - yes

9. Is the person holding a knife?  
   - yes

10. Does the image show a kitchen?  
    - n/a

11. Does the image have a cool color palette?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have high contrast?  
    - n/a

14. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 14  

Score = (9/14) × 100 = 64.29

score: 64.29

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 correct answers out of 14 questions result in a score of 64.29%.

token_count: 369

caption_vocabulary_size: 254

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 90

candidate_caption: The interior showcases a stylish entryway leading into a living area, combining bohemian, Mediterranean, and contemporary design elements. The foreground features a vibrant red oriental-style rug with intricate geometric patterns in pink, blue, yellow, white, and gold, extending diagonally across large dark charcoal square tiles. To the left stands a glossy forest green wooden console table with elegant curved legs, adorned with decorative items including a modern rectangular lamp with a beige shade, clear crystal sculptures resembling geodes or clusters of crystals, a small green ceramic horse figurine, a black bowl, and a framed landscape painting hanging on the wall above it. A tall golden vertical decor piece with thin rods stands next to the table. An arched doorway with a rough-textured stucco finish frames the scene, featuring abstract black metal bars radiating outward from a central point in a sunburst pattern, creating a striking visual effect. Beyond this artistic barrier lies a cozy living space illuminated by natural light streaming through large windows covered with beige Roman shades, revealing an L-shaped seating arrangement with blue sofas featuring white floral patterns. A wooden coffee table sits centrally on a teal-colored rug, holding a potted plant and other small decorative objects. Two large hanging pendant lamps with beige shades complement the room's aesthetic. The background includes a sloped ceiling with exposed wooden beams arranged in parallel lines, painted in a light beige color that adds warmth to the neutral-toned space. On either side of the entrance are walls with smooth finishes, one having a textured appearance. A partially visible window on the right has a black frame and is covered by a rolled-up beige Roman blind, while another window on the left is framed in white and shows a glimpse of the outdoors. The overall composition creates a balanced and inviting atmosphere, blending various textures, colors, and materials throughout the space.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the carpet primarily red?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the table on the left emerald green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the table located in the room visible through the arch?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the lamp to the left of the arch?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the table in the other room small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the light fixture tall and narrow?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a couch in the other room?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the console table against the left wall of the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the carpet primarily red?  
   - yes

2. Is the table on the left emerald green?  
   - no

3. Is the table located in the room visible through the arch?  
   - no

4. Is the lamp to the left of the arch?  
   - yes

5. Is the table in the other room small?  
   - n/a

6. Is the light fixture tall and narrow?  
   - yes

7. Is there a couch in the other room?  
   - yes

8. Is the console table against the left wall of the image?  
   - yes

9. Does the image show indoors?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a photograph?  
    - n/a

12. Does the image have high contrast?  
    - n/a

13. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 13  

Score = (8/13) × 100 ≈ 61.54

score: 61.54

reasons: The score is calculated based on the number of 'yes' or 'no' answers provided, excluding 'n/a' responses. Out of 13 questions, 8 have definitive answers, resulting in a score of approximately 61.54%.

token_count: 368

caption_vocabulary_size: 237

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 93

candidate_caption: A dynamic action shot captures an athlete performing a squat lift at an outdoor weightlifting competition. The central figure, a muscular man with short dark hair styled into cornrows, wears reflective blue-tinted sunglasses and has a focused expression as he squats on textured rubber flooring marked with pink and white lines. He's dressed in a black sleeveless tank top featuring a cartoon graphic of a strong bear holding red barbells, with 'COLADA STR' (likely 'Colada Strength') printed below in white letters. His outfit includes camouflage-patterned shorts over a black leggings base layer, complemented by sky-blue Nike athletic shoes with yellow accents. Blue knee sleeves adorn both knees, adding a splash of color to his workout attire. A small tattoo reading 'DADDY'S GIRL' in cursive script is visible on his left upper arm, while another intricate floral design graces his right side. The barbell, held horizontally above his head with both hands gripping it, displays ROGUE branded circular weights in green (55 lb) and orange-red (25 lb). In the midground, a woman with long blonde hair wearing a gray cap and black shirt stands next to him, observing the lift. She also wears a purple wristband on her right wrist. Various pieces of gym equipment, including rowing machines labeled 'ROGUE', are scattered around the area. The background reveals more participants and spectators engaged in different activities under the bright sunlight filtering through trees. Black bleachers filled with empty seats rise behind the scene, creating shadows that add depth to the composition. The overall atmosphere is intense and competitive, highlighting the athleticism and determination of the lifter amidst this bustling crossfit or powerlifting environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'ROGUE'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Does the orange weight have number '55' on it?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the shoes the person is wearing blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person positioned in the bottom center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person lifting weights to the left of another person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look focused?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the barbell large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the weights on the barbell circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in a squatting position?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a woman in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person holding a barbell overhead?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an outdoor scene?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Does the image contain the text 'ROGUE'?  
   - yes

2. Does the orange weight have number '55' on it?  
   - no

3. Are the shoes the person is wearing blue?  
   - yes

4. Is the person positioned in the bottom center of the image?  
   - n/a

5. Is the person lifting weights to the left of another person?  
   - n/a

6. Does the person look focused?  
   - yes

7. Is the background blurred?  
   - n/a

8. Is the barbell large?  
   - n/a

9. Are the weights on the barbell circular?  
   - yes

10. Is there only one person in a squatting position?  
    - yes

11. Is there a woman in the image?  
    - yes

12. Is the person holding a barbell overhead?  
    - yes

13. Does the image show an outdoor scene?  
    - yes

14. Is the image a photograph?  
    - n/a

15. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 15  

Score = (9/15) × 100 = 60

score: 60.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 15 questions were answered correctly, resulting in a score of 60%.

token_count: 345

caption_vocabulary_size: 252

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 102

candidate_caption: A movie poster for 'Snatch' featuring six men standing in a row against a plain white background, with a small white dog with black patches in the foreground. The title 'snatch' is prominently displayed at the top center in large bold black sans-serif font. Each character is dressed in distinctive attire, creating a visually diverse group. From left to right: a man wearing sunglasses, a beige trench coat over brown sweater, tan vest, and checkered tie; next to him is a man in a navy blue suit with a light blue striped tie and no tie; followed by a man in a dark blue blazer over a red and white striped shirt with light gray trousers; then a bearded man in a royal blue jacket over a red shirt with gray pants and black shoes, holding a brown leather hat in his left hand and a leash in his right; next is a man in a shiny black leather jacket with reflective material and blue jeans; finally, on the far right, a man in a light brown overcoat over a darker shirt and blue pants. In the front, slightly off-center, a small white dog with black patches stands on hind legs, looking directly at the camera. Below the characters, cast names are listed in black uppercase letters: BENICIO DEL TORO DENIS FARINA VINNIE JONES BRAD PITT RADE SHERBEERGIA JASON STATHAM. Further down, credits include SCREEN GEMS PRESENTS IN ASSOCIATION WITH SKA FILMS A MATTHEW VAUGHN PRODUCTION A FILM BY GUY RITCHIE "SNATCH" PRODUCED BY MATTHEW VAUGHN. Additional details about the film's rating and soundtrack information appear at the bottom. At the very bottom, the website sony.com/snatch and the phrase coming soon are written in bold text. Logos for DPA and Dolby are also present.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'text', 'question': "Does the text 'coming soon' appear in the image?"}
 {'answer': 'Yes', 'category': 'color', 'question': 'Is the background color white?'}
 {'answer': 'Yes', 'category': 'color', 'question': "Is dog's leash brown?"}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is there a dog below the center of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the tall person in the blue suit to the left of the dog?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a Screen Gems logo in the image?'}
 {'answer': 'No', 'category': 'emotion', 'question': 'Is anyone smiling in the image?'}
 {'answer': 'Yes', 'category': 'proper noun', 'question': "Is Brad Pitt holding the dog's leash?"}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the dog smaller than the people surrounding it?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there a total of six people in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a dog in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': "Is the text 'coming soon' below the dog?"}
 {'answer': 'Yes', 'category': 'image type', 'question': 'Is the image a movie poster?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a high contrast color palette?'}]

openai_answers: 1. Does the text 'coming soon' appear in the image?  
   - yes

2. Is the background color white?  
   - yes

3. Is dog's leash brown?  
   - yes

4. Is there a dog below the center of the image?  
   - yes

5. Is the tall person in the blue suit to the left of the dog?  
   - n/a

6. Is there a Screen Gems logo in the image?  
   - yes

7. Is anyone smiling in the image?  
   - n/a

8. Is Brad Pitt holding the dog's leash?  
   - n/a

9. Is the dog smaller than the people surrounding it?  
   - yes

10. Are there a total of six people in the image?  
    - yes

11. Is there a dog in the image?  
    - yes

12. Is the text 'coming soon' below the dog?  
    - n/a

13. Is the image a movie poster?  
    - yes

14. Does the image have a high contrast color palette?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 14  

Score = (9/14) × 100 = 64.29

score: 64.29

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 14 questions were answered correctly, resulting in a score of 64.29%.

token_count: 390

caption_vocabulary_size: 229

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 107

candidate_caption: A 3D rendering of a playful and colorful still life scene features two wooden shelves against a vibrant lime green (#b4c14a) wall, creating a cheerful atmosphere with even lighting. The top shelf displays various objects, including a set of books in yellow (#e5c67d), light blue, and white covers stacked horizontally, positioned centrally. Atop this stack sits a smooth, reflective metallic silver sphere (#9ea6aa) that catches light reflections, adding depth to the composition. To its left stands a tall black cylindrical object resembling dark leather or fabric, next to which is a beige wood-textured cylinder. On the far right side, an orange vase with a white band at the rim and subtle swirling patterns contains a stylized plant with large oval-shaped leaves transitioning from dark forest green (#3f3921) at the base to lighter lime green towards the tips, featuring three curved segments visible on each leaf. Near the back of the top shelf rests another striped object resembling a ball, colored in navy blue and white diagonally. In front of these items is a small circular red ball placed near the edge of the bottom shelf, while a pale blue spherical object sits further back on the same shelf. Below, a coral-colored (#cf6467) cylindrical container with rounded edges and four horizontal orange stripes holds writing instruments - a royal blue pen with a glossy finish, a bright pink pencil with a red eraser, and a yellow stick-like object. To the right of this pencil holder is a greenish-yellow (#cfa25e) egg-shaped object. A white notebook with a blue ribbon-bound spiral binding mechanism lies open on the bottom shelf, slightly tilted forward. Small decorative spheres are scattered around, including a coral-red one near the pen holder and a sky blue one on the lower shelf, enhancing the whimsical nature of the scene. The background wall transitions from lime green at the top to soft pastel shades of peach and lavender (#ab8dc3) below, adding warmth and contrast. The overall color palette includes vibrant hues such as lime green, coral pink, sky blue, charcoal black, ivory white, gold (#cf6467), steel gray (#96998b), and muted sage green (#95907f). The composition is balanced and symmetrical, with soft shadows enhancing the three-dimensional effect and giving it a modern, minimalist feel reminiscent of contemporary graphic design trends.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background color light green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the orange vase on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the yellow cup to the left of the orange vase?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the metal ball large?'}
 {'answer': 'no', 'category': 'entity shape', 'question': 'Is the orange vase spherical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two books below the metal ball?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a plant in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the yellow book on top of the blue book?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a 3D rendering?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is the background color light green?  
   - yes

2. Is the orange vase on the right side of the image?  
   - yes

3. Is the yellow cup to the left of the orange vase?  
   - n/a

4. Is the metal ball large?  
   - n/a

5. Is the orange vase spherical?  
   - no

6. Are there two books below the metal ball?  
   - yes

7. Is there a plant in the image?  
   - yes

8. Is the yellow book on top of the blue book?  
   - n/a

9. Does the image show indoors?  
   - n/a

10. Does the image have a warm color palette?  
    - yes

11. Is the image a 3D rendering?  
    - yes

12. Does the image have high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 12  

Score = (8/12) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of questions answered correctly out of the total number of questions. In this case, 8 questions were answered correctly out of 12, resulting in a score of 66.67%.

token_count: 484

caption_vocabulary_size: 277

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 109

candidate_caption: A cozy indoor scene featuring a polished wooden desk with visible grain patterns in warm brown tones, creating a rustic yet modern atmosphere. On the left side of the desk sits an open silver MacBook Pro displaying a dark-themed photo editing software interface, specifically Lightroom, showing multiple panels with settings, filters, and tools. The main screen features a vertical photograph preview of hanging cymbals or drum heads against a dark background, with intricate details such as metallic surfaces, reflective points, and shadows highlighted by soft lighting. To the right of the laptop is a black adjustable desk lamp with a glossy round shade that emits a warm white glow, illuminating nearby objects. Next to the lamp stands a small cylindrical vase containing dried baby's breath flowers arranged in a bouquet-like style. A white ceramic mug adorned with a delicate floral pattern featuring blue and red flowers on its surface rests near the center-right of the desk. In front of the mug lies a silver wristwatch with a black face and metal link bracelet, while a pair of silver rings with various designs rests nearby. A sleek black smartphone with rounded edges and a smooth matte finish is placed diagonally towards the bottom left corner of the desk. The background consists of floor-length sage green curtains with subtle geometric patterns along their bottom edge, softly illuminated by ambient light from the window. On the far left, part of a dark bookshelf filled with books and files is partially visible, adding depth to the composition. The overall lighting is dim but focused, creating a calm and concentrated mood suitable for work or study. The color palette includes deep charcoal (RGB(29, 23, 19)), muted olive green (RGB(108, 118, 92)), rich umber (RGB(124, 85, 44)), soft khaki (RGB(145, 132, 109)), cool gray-blue (RGB(140, 149, 158)), and slate gray (RGB(135, 142, 155)). These colors contribute to the balanced exposure, moderate contrast, and low saturation of the image, emphasizing both shadowed areas and highlights within the workspace.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the cellphone black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the curtains green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the laptop in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the lamp on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the cup to the right of the laptop?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the phone to the left of the laptop?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there flowers in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a cup in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the cup placed on the table?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the phone small?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the cellphone black?  
   - yes

2. Are the curtains green?  
   - yes

3. Is the laptop in the center of the image?  
   - n/a

4. Is the lamp on the right side of the image?  
   - yes

5. Is the cup to the right of the laptop?  
   - yes

6. Is the phone to the left of the laptop?  
   - yes

7. Is the background blurred?  
   - n/a

8. Are there flowers in the image?  
   - yes

9. Is there a cup in the image?  
   - yes

10. Is the cup placed on the table?  
    - yes

11. Is the phone small?  
    - n/a

12. Does the image have a warm color palette?  
    - yes

13. Is the image a photograph?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 13  

Score = (9/13) × 100 = 69.23

score: 69.23

reasons: The score is calculated based on the number of questions answered with 'yes' compared to the total number of questions. Out of 13 questions, 9 were answered affirmatively, resulting in a score of 69.23%.

token_count: 424

caption_vocabulary_size: 254

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 114

candidate_caption: A close-up 3D animated scene depicts an emotional moment between two elderly characters in a hospital room. The character on the right, Carl Fredricksen, has short gray hair with white strands, thick white eyebrows, large blue eyes with reflective highlights, and prominent cheekbones. He wears square black-framed glasses that magnify his eyes slightly due to their size and shape. His expression is serious, contemplative, and concerned as he leans forward to look at the other character. Carl's skin tone is light peach with subtle wrinkles, particularly around the forehead and eyes, showing signs of aging. He sports a prominent round red nose and a large ear that stands out due to its pinkish-red hue. Carl is dressed in a dark brown textured tweed jacket with a subtle checkered pattern over a crisp off-white shirt with three visible buttons, fastened by a dark brown belt. The character on the left, Ellie, has white hair styled neatly back, wearing small rectangular tortoiseshell frames glasses. She is seated or lying down, facing Carl, with her cheeks rosy and blushed, indicating possible illness or discomfort. The background features two transparent IV bags hanging from thin silver tubes on either side of them against a muted dusty rose-colored wall. A window covered with vertical cream-colored curtains adorned with intricate floral patterns in shades of peach, beige, orange, and yellow allows soft natural light to filter through, casting gentle shadows and warm illumination across the scene. This lighting creates a tender atmosphere and enhances the emotional depth of the interaction. The overall mood is touching and heartfelt, emphasizing the connection between the two characters in this cozy yet clinical setting. The color palette includes soft pinks, warm browns, creams, grays, and touches of green and orange, contributing to the emotional weight of the scene while maintaining a balanced and neutral visual effect.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': "Is the man's suit's color dark brown?"}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the man on the right side of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the woman to the left of the man?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Does the man look sad?'}
 {'answer': 'Yes', 'category': 'proper noun', 'question': "Is the character's name Carl?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the woman on the left large in the image?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': "Are the man's glasses rectangular?"}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the man wearing a suit?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there IV bags in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from an animated film?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the man's suit's color dark brown?  
     - yes

   - Is the man on the right side of the image?  
     - yes

   - Is the woman to the left of the man?  
     - yes

   - Does the man look sad?  
     - no

   - Is the character's name Carl?  
     - yes

   - Is the woman on the left large in the image?  
     - n/a

   - Are the man's glasses rectangular?  
     - no

   - Are there two people in the image?  
     - yes

   - Is the man wearing a suit?  
     - no

   - Does the image show indoors?  
     - yes

   - Does the image have a warm color palette?  
     - yes

   - Are there IV bags in the image?  
     - yes

   - Is the image from an animated film?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 9
   - Total Number of Questions: 13

   Score = (9/13) × 100 = 69.23

score: 69.23

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 13 questions were answered correctly, resulting in a score of 69.23%.

token_count: 373

caption_vocabulary_size: 240

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 117

candidate_caption: A still life photograph features a cluttered white table with various items. In the left foreground, there's a clear glass vase filled with fresh yellow tulips and green leaves. The tulips have bright yellow petals with some slightly open buds, adding vibrancy to the scene. Their stems are visible through the transparent material of the vase. To the right of the vase, an open silver MacBook laptop with a distinctive white Apple logo on its back panel is positioned angled towards the camera but slightly blurred due to depth of field. Next to the laptop, there's a white ceramic mug containing a light brown beverage, likely coffee or tea, with a black pen or straw inside. Below these two items, a black smartphone with a white front screen and partially visible charging cable with red accents lies face down. To the far right, a spiral-bound notebook with a metallic spiral binding and a pink strap or wire is partially visible. A small round gray object, possibly a coin or cap, can be seen near the bottom center of the image. The background consists of a dark wall, providing contrast to the lighter objects on the table. Soft natural lighting from the left side illuminates the scene evenly, creating a calm and serene mood while emphasizing the vivid colors of the flowers against the neutral tones of the other elements.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Are the flowers yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the charging cord red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the laptop on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the cup in front of the laptop?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the logo of the company Apple?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the vase large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the cup round?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than one flower in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a vase in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the MacBook placed on the table?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is there a cup on the table?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the flowers in a vase?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Are the flowers yellow?  
   - yes

2. Is the charging cord red?  
   - n/a

3. Is the laptop on the right side of the image?  
   - yes

4. Is the cup in front of the laptop?  
   - n/a

5. Is the background blurred?  
   - n/a

6. Is the logo of the company Apple?  
   - yes

7. Is the vase large?  
   - n/a

8. Is the cup round?  
   - n/a

9. Are there more than one flower in the image?  
   - yes

10. Is there a vase in the image?  
    - yes

11. Is the image taken indoors?  
    - n/a

12. Is the MacBook placed on the table?  
    - yes

13. Is there a cup on the table?  
    - yes

14. Are the flowers in a vase?  
    - yes

15. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 15  

Score = (10/15) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. There are 10 'yes' answers out of 15 questions, resulting in a score of 66.67%.

token_count: 260

caption_vocabulary_size: 159

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 121

candidate_caption: A majestic, historical building is covered in vibrant autumn foliage, creating a stunning mosaic of reds (#c44e3a), oranges, yellows (#d8b645), and greens (#2f7d32) that contrast beautifully with its dark brick walls and ornate stone details. The structure features multiple stories with arched windows framed by black iron bars or wooden frames. The upper part of the facade showcases intricate architectural elements such as decorative spires, balconies, and stone carvings, including a prominent central tower topped with a dark spire. A tall, weathered brick chimney rises from the center of the roofline, adding to the vintage aesthetic. The terracotta-tiled gable roofs are steeply pitched and feature dark mortar lines between tiles, enhancing their textured appearance. In front of the building, there's neatly trimmed greenery and two circular blue signs on thin poles; one indicates pedestrian crossing information while another appears to be a parking sign. A white object, possibly a sculpture or chair, is partially visible at the bottom right corner. The overcast sky provides soft, diffused lighting, highlighting the rich colors of the ivy without harsh shadows. The overall composition focuses on the interplay between the classical architecture and the natural beauty of the fall foliage, resulting in a serene yet striking visual effect that captures the essence of autumn in an urban setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the building covered with multi-colored plants?'}
 {'answer': 'Yes', 'category': 'color', 'question': 'Does the building have red plants on it?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is there a tree on the right side of the image?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the building in the center of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the tree to the right of the building?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Are there slight image compression artifacts visible in the image?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the blue sign circullar?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there more than two windows visible in the building?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a pole or signpost in front of the building?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Is the image taken outdoors?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Is it daytime in the image?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image predominantly consist of autumn colors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is the building covered with multi-colored plants?  
   - yes

2. Does the building have red plants on it?  
   - yes

3. Is there a tree on the right side of the image?  
   - n/a

4. Is the building in the center of the image?  
   - n/a

5. Is the tree to the right of the building?  
   - n/a

6. Are there slight image compression artifacts visible in the image?  
   - n/a

7. Is the blue sign circular?  
   - yes

8. Are there more than two windows visible in the building?  
   - yes

9. Is there a pole or signpost in front of the building?  
   - yes

10. Is the image taken outdoors?  
    - yes

11. Is it daytime in the image?  
    - n/a

12. Does the image have a warm color palette?  
    - yes

13. Does the image predominantly consist of autumn colors?  
    - yes

14. Is the image a photograph?  
    - n/a

15. Does the image have high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 15  

Score = (9/15) × 100 = 60

score: 60.0

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. There are 9 'yes' answers out of 15 questions, resulting in a score of 60%.

token_count: 279

caption_vocabulary_size: 202

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 126

candidate_caption: A modern office workspace designed with a focus on relaxation and collaboration features two distinct areas. On the left side of the image, a man wearing a gray long-sleeve shirt, black pants, and brown shoes sits on a bright yellow bean bag chair against a plain white wall. He holds an Apple MacBook laptop with its logo visible, appearing focused as he works. The floor in this area is covered with green carpeting, adding vibrancy to the space. To his right, there are two white Adirondack-style wooden chairs placed on the same grassy surface. Between these chairs stands a small wooden stump table holding some magazines or books. Above this seating area hangs a unique cluster light fixture with five exposed bulbs attached to three wires, emitting warm yellow glow. The background showcases a large white dry erase board covered in various diagrams, text notes, and handwritten annotations in red and orange ink. A projection screen displays a digital interface resembling a spreadsheet or database with tables and fields labeled 'Name', 'Value', and 'Description'. Near the top left corner of the whiteboard, the word 'GARDEN' is written in bold black letters. Two teal blue water bottles with green caps are mounted on the wall near the man, secured by a white plastic holder. The overall lighting is bright and even, provided by both natural light filtering through ceiling lights and artificial sources, creating a well-lit environment conducive to both work and relaxation.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text 'GARDEN' on the wall?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the wall white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the chair white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the bean bag chair yellow?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the projector on top of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bean bag chair in the bottom left corner of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person sitting to the left of the white chairs?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the wooden table near the wall?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking at the laptop screen?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have compression artifacts?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bean bag chair large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two white chairs?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person sitting on the bean bag chair?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a natural color grading?'}]

openai_answers: 1. Is the text 'GARDEN' on the wall?  
   - yes

2. Is the color of the wall white?  
   - yes

3. Is the chair white?  
   - yes

4. Is the bean bag chair yellow?  
   - yes

5. Is the projector on top of the image?  
   - n/a

6. Is the bean bag chair in the bottom left corner of the image?  
   - n/a

7. Is the person sitting to the left of the white chairs?  
   - yes

8. Is the wooden table near the wall?  
   - no

9. Is the person looking at the laptop screen?  
   - yes

10. Does the image have compression artifacts?  
    - n/a

11. Is the bean bag chair large?  
    - n/a

12. Are there two white chairs?  
    - yes

13. Is there a person in the image?  
    - yes

14. Is the person sitting on the bean bag chair?  
    - yes

15. Does the image show indoors?  
    - yes

16. Is the image a photograph?  
    - n/a

17. Does the image have a natural color grading?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 17  

Score = (11/17) × 100 = 64.71

score: 64.71

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. There are 11 'yes' answers out of 17 questions, resulting in a score of 64.71%.

token_count: 289

caption_vocabulary_size: 195

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 134

candidate_caption: A captivating food photograph showcases three homemade Swiss rolls (Swiss buns) elegantly presented on an ornate cream-colored ceramic plate adorned with delicate autumnal floral patterns in shades of yellow, orange, green, and rust red. Each bun is topped with a perfectly spiraled layer of smooth white whipped cream frosting, crowned by a thin, golden-brown cookie or wafer, generously dusted with fine powder sugar. The plate sits on a warm-toned wooden surface, creating a cozy atmosphere. To the left stands a large white ceramic cup featuring the text 'VANILLA Latte' in gold sans-serif font, followed by smaller print reading 'FRESHLY BREWED'. Behind it, a clear glass jar filled with various colorful measuring spoons creates visual interest. One spoon displays a vibrant pink base with stylized strawberry motifs, while another features a prominent crimson red mushroom design. A charcoal gray cat-shaped plastic decoration rests inside a lavender mug decorated with playful unicorn illustrations and pastel confetti designs near its rim. Natural light streams from a window to the right, illuminating the scene and highlighting the textures and colors of the baked goods and their surroundings. In the blurred background, hints of bare winter trees suggest an outdoor setting, enhancing the rustic charm of this inviting kitchen space.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Vanilla Latte'?"}
 {'answer': 'no', 'category': 'color', 'question': 'Is the cat figure gray?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the cup in the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the pastries in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the jar behind the plate?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the cat figure to the right of the jar?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the plate large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the plate circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three pastries?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a cup in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the cat figurine placed on a cup?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the image contain the text 'Vanilla Latte'?  
   - yes

2. Is the cat figure gray?  
   - yes

3. Is the cup in the left side of the image?  
   - yes

4. Are the pastries in the center of the image?  
   - n/a

5. Is the jar behind the plate?  
   - n/a

6. Is the cat figure to the right of the jar?  
   - n/a

7. Is the background blurred?  
   - yes

8. Is the plate large?  
   - n/a

9. Is the plate circular?  
   - n/a

10. Are there three pastries?  
    - yes

11. Is there a cup in the image?  
    - yes

12. Is the cat figurine placed on a cup?  
    - yes

13. Does the image show indoors?  
    - yes

14. Does the image have a warm color palette?  
    - yes

15. Is the image a photograph?  
    - yes

16. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 16  

Score = (10/16) × 100 = 62.5

score: 62.5

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, divided by the total number of questions. This gives a percentage score of 62.5%.

token_count: 259

caption_vocabulary_size: 200

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 137

candidate_caption: The scene from the movie 'Scarface', directed by Brian De Palma, features Al Pacino as Tony Montana and an ensemble cast in a tense indoor setting. The composition is right-heavy with medium contrast lighting creating a balanced exposure. In the foreground, there's a large floral arrangement on a coffee table featuring white roses, pink gerberas, and other flowers in various shades of cream, red, and green foliage. A clear glass containing a light-colored liquid sits nearby. In the midground, three men are visible; two are seated on a beige sofa while one stands behind them. The man on the left wears a light beige double-breasted suit jacket over a dark gray shirt with rolled-up sleeves and a matching tie, his hair slicked back and face turned slightly to the right. He's extending his right arm, resting it on Tony Montana's shoulder in a gesture of comfort or conversation. Tony Montana is reclining on the right side of the sofa wearing a light gray suit jacket with well-fitted lapels, paired with a black shirt and a patterned tie in brown, gold, and blue hues. His short dark hair frames his face as he looks at the first man. On the far left, another man lounges on the sofa in a light gray suit with a striped tie, appearing thoughtful as he rests his head on his hand. Behind them, a fourth man stands near a tall Gothic-style window with stone moldings, dressed in a beige buttoned-up shirt with a high collar and chest pocket, looking neutral and observing the interaction. The background showcases deep orange-red walls adorned with framed classical artwork depicting scenes involving nude figures in dynamic poses. A small antique wooden console table with a golden bust sculpture adds to the room's opulent decor. Through the windows, trees are visible outside, providing natural daylight illumination. The overall mood is intense and dramatic, typical of 1980s cinema, enhanced by the rich color palette dominated by warm tones and the strategic use of shadows.

captioned_by: pg-captioner

ground_truth: [{'answer': 'no', 'category': 'color', 'question': "Is the color of the left-most man's suit light grey?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the wall color rust red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the man in the white suit sitting in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the man in the dark grey suit on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the man in the white suit to the left of the man in the dark grey suit?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the man in the dark grey suit looking serious?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have film grain?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there four men in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a bouquet of flowers in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the man in the grey suit on the sofa?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a screenshot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the color of the left-most man's suit light grey?  
   - Answer: yes

2. Is the wall color rust red?  
   - Answer: yes

3. Is the man in the white suit sitting in the center of the image?  
   - Answer: n/a

4. Is the man in the dark grey suit on the right side of the image?  
   - Answer: yes

5. Is the man in the white suit to the left of the man in the dark grey suit?  
   - Answer: n/a

6. Is the man in the dark grey suit looking serious?  
   - Answer: n/a

7. Does the image have film grain?  
   - Answer: n/a

8. Are there four men in the image?  
   - Answer: yes

9. Is there a bouquet of flowers in the image?  
   - Answer: yes

10. Is the man in the grey suit on the sofa?  
    - Answer: yes

11. Is the image taken indoors?  
    - Answer: yes

12. Does the image have a warm color palette?  
    - Answer: yes

13. Is the image a screenshot from a film?  
    - Answer: yes

14. Does the image have high contrast?  
    - Answer: no

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 14  

Score = (9/14) × 100 = 64.29

score: 64.29

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 14 answers were correct, resulting in a score of 64.29%.

token_count: 403

caption_vocabulary_size: 243

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 138

candidate_caption: A close-up wildlife photograph captures a peacock amidst dense foliage, creating a serene and natural scene. The bird is positioned slightly to the left of center, its head turned to face the camera with an alert expression. Its plumage displays vibrant colors, primarily royal blue on its head transitioning into emerald green and hints of forest green towards the body, with intricate patterns of iridescent blue-green feathers that blend seamlessly into the surrounding environment. The peacock's distinctive features are highlighted by the lighting: a small, sharp beak colored in light grayish-white with a hint of pink at its base, large dark eye surrounded by white patches extending from the sides of its head down to the neck, and a prominent crest of fine, feathered filaments tipped in deep navy blue (RGB(22, 44, 60)) and black, each ending in delicate tips of light brown. These feathers form two distinct plumes - one larger and more prominent than the other. A striking black-and-white facial stripe runs from above the eye down to the beak, adding to the peacock's majestic appearance. The foreground consists of blurred green leaves and stems in various shades of lime (RGB(168, 172, 143)), sage (RGB(140, 154, 132)), and olive, partially obscuring parts of the bird and contributing to the shallow depth of field. This creates a soft, dreamy quality to the scene while emphasizing the subject. The background consists of darker tones suggesting additional foliage and branches, rendered as smooth blurs due to the shallow depth of field. Hints of sunlight filter through the canopy, casting dappled shadows and highlights across the scene, enhancing the three-dimensional effect and creating a high-contrast interplay between illuminated areas and deeper shadows. The overall color palette includes deep forest greens (RGB(15, 25, 27)), muted charcoal blacks (RGB(33, 37, 36)), pale slate grays (RGB(152, 164, 157)), and rich teals (RGB(35, 73, 89), RGB(72, 91, 84)). Natural daylight provides balanced exposure with medium contrast and moderate saturation, highlighting the vivid hues of the peacock's feathers against the subdued backdrop of foliage. The composition follows the rule of thirds, with the peacock's head and upper body occupying most of the frame, drawing attention to its striking plumage and regal presence within this lush woodland setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the peacock's head blue?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a peacock in the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the peacock in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the peacock's head turned left?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image depict an outdoor scene?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the peacock looking alert?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a dark color palette?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is there any vignetting effect in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the peacock's crest fan-shaped?"}]

openai_answers: 1. Is the peacock's head blue?  
   - yes

2. Is there a peacock in the image?  
   - yes

3. Is the background blurred?  
   - yes

4. Is the peacock in the center of the image?  
   - no

5. Is the peacock's head turned left?  
   - no

6. Does the image depict an outdoor scene?  
   - yes

7. Is the peacock looking alert?  
   - yes

8. Does the image have a dark color palette?  
   - yes

9. Is there any vignetting effect in the image?  
   - n/a

10. Is the peacock's crest fan-shaped?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 6  
Total Number of Questions: 10  

Score = (6/10) × 100 = 60

score: 60.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 6 out of 10 questions were answered correctly, resulting in a score of 60%.

token_count: 502

caption_vocabulary_size: 286

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 139

candidate_caption: A photograph captures a vintage gold Mercedes-Benz convertible car parked at a modernist-style gas station, likely in Germany during the 1980s or early 1990s. The scene is set on a sunny day with natural daylight illuminating the area. The mid-century gas station features a distinctive curved white canopy that extends over multiple fuel pumps, supported by cylindrical gray concrete columns. Three signs above the pumps read 'Super Plus,' 'Diesel,' and another 'Super E5' in bold red text against an orange background. To the left of the car, there are various advertisements including Coca-Cola, Citi (with German text), and others displayed on glass panels of the shop entrance. Above the door, there's a red awning with 'Shop' written in white letters. A terracotta pot containing a trimmed bush sits near this area. In the foreground, light beige paving stones form the road surface, leading up to the gas station. Behind it stands a large brick building with a steeply pitched gable roof covered in interlocking clay tiles arranged in a herringbone pattern. The facade combines white-painted brickwork with exposed brick sections, featuring two small rectangular windows and a narrow window slot below one chimney. A prominent red brick chimney rises from the center of the building, flanked by smaller chimneys. The right side of the building showcases a mix of materials, including white stucco accents around some windows and decorative lattice work. On the far right, a tall signpost displays 'AVIA' in bold red letters on a white background. Surrounding the main structure are lush green trees and bushes, adding vibrancy to the scene. One large leafy palm-like plant grows to the right of the signpost. The overall mood is calm and nostalgic, capturing a moment of everyday life with balanced exposure and moderate contrast.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Shop'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Coca-Cola'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the car golden brown?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the AVIA sign red and white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the car in the bottom center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the shop to the left of the car?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the car large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the roof of the gas station rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one car in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a house in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the car next to the bushes?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Does the image contain the text 'Shop'?  
   - yes

2. Does the image contain the text 'Coca-Cola'?  
   - yes

3. Is the car golden brown?  
   - n/a

4. Is the AVIA sign red and white?  
   - yes

5. Is the car in the bottom center of the image?  
   - n/a

6. Is the shop to the left of the car?  
   - yes

7. Is the car large?  
   - n/a

8. Is the roof of the gas station rectangular?  
   - no

9. Is there one car in the image?  
   - yes

10. Is there a house in the image?  
    - no

11. Is the car next to the bushes?  
    - n/a

12. Does the image show daylight?  
    - yes

13. Is the image a photograph?  
    - yes

14. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 14  

Score = (9/14) × 100 = 64.29

score: 64.29

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 14 questions were answered correctly, resulting in a score of 64.29%.

token_count: 373

caption_vocabulary_size: 239

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 151

candidate_caption: A photograph of the iconic Disney castle taken during twilight, showcasing its medieval Gothic architecture with an enchanting blend of colors. The central focus is on the main spire, which rises majestically against a clear sky transitioning from deep blue at the top to lighter shades near the horizon. The castle's structure features multiple turrets and towers, each adorned with intricate details such as pointed arches, ornate stonework, and decorative elements like finials and flags. The primary spire stands tall at the center, surrounded by smaller spires, creating a symmetrical composition. The exterior walls are painted in various shades of royal purple (#4c3a72), cerulean blue (#4560b8), and lavender (#ae9cc1) hues, while golden yellow lights accentuate specific architectural elements like windows, archways, and bases. A large central clock face, prominently positioned above the arched entrance, displays golden numbers and hands within a white circular frame with a dark outline. The castle's battlements and crenellations add texture and depth to the scene. Small, warmly lit lamps line the paved walkway leading up to the grand entrance, enhancing the magical atmosphere. In front of the castle, there are vintage-style street lamps with globe-shaped bulbs emitting a warm amber glow, casting soft light onto the surrounding area. The foreground includes stone steps and railings, with a silhouette of a statue depicting two figures, one pointing upwards, adding a human element to the scene. The overall mood is whimsical and serene, enhanced by the low natural lighting of dusk and the artificial illumination that highlights the castle's architectural beauty and creates a harmonious blend of cool and warm tones throughout the scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the castle in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the street lights to the left of the castle?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the location Disney World?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the castle large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than two street lights visible in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there an arched entrance to the castle?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a statue in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show dusk?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sky light blue?  
   - yes

2. Is the castle in the center of the image?  
   - yes

3. Are the street lights to the left of the castle?  
   - n/a

4. Is the location Disney World?  
   - n/a

5. Is the castle large?  
   - yes

6. Are there more than two street lights visible in the image?  
   - n/a

7. Is there an arched entrance to the castle?  
   - yes

8. Is there a statue in the image?  
   - yes

9. Does the image show dusk?  
   - yes

10. Is the image a photograph?  
    - yes

11. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 11  

Score = (7/11) × 100 = 63.64

score: 63.64

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, out of the total number of questions. There are 7 'yes' answers out of 11 questions, resulting in a score of 63.64%.

token_count: 345

caption_vocabulary_size: 231

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 170

candidate_caption: A dynamic action shot captures two male triathletes in mid-race during a competitive outdoor running event, with a third athlete partially visible on the right side wearing bright green shorts. The runner on the left is identified as Michalek Cze from Czech Republic, wearing a sleek navy blue sleeveless triathlon suit adorned with white text reading 'MICHALEK CZE' across the chest, along with sponsor logos including 'Czech Triathlon Union', 'TRI-X', 'KOLON', and 'GUNNAR'. His short hair is damp, suggesting recent swimming or high exertion, and he runs with intense focus, his muscular arms and legs visible through the tight-fitting material. He wears neon yellow running shoes with vibrant orange laces and black accents, featuring intricate designs that add to their eye-catching appearance. A black tattoo-like design resembling wings adorns his lower leg, while an additional 'CWCT' marking appears near his ankle. The runner on the right, representing Lithuania (LTU), sports a vibrant red-yellow gradient triathlon suit transitioning into sunflower yellow at the thighs, ending in crimson red shorts with subtle wavy patterns. His calves bear the number '23' in black, while his ankles display 'ITA' (likely Italy) in bold sans-serif font. On his legs are numbers '999' and '4' in black. He wears distinctive sunglasses with multi-colored lenses reflecting yellow, olive, and light blue hues, and a white headband wrapped around his forehead. Both athletes have various temporary tattoos on their legs, arms, and feet. They run on a paved surface bordered by metal barricades arranged vertically in alternating patterns of orange and white stripes. Behind them, banners read 'World Triathlon' in white text on a sky-blue background and 'Uzbekistan Triathlon Federation' in dark teal text on white backgrounds, indicating the international nature of the event. The foreground features several orange traffic cones placed horizontally along the course path, adding depth and structure to the scene. In the background, there are tall trees under a clear cerulean blue sky with faint wisps of clouds on the upper left corner. The natural daylight creates a vivid and energetic atmosphere, highlighting the athletes' determination and the intensity of the race. The photograph employs a shallow depth of field, keeping the runners sharply focused against the slightly blurred background elements, emphasizing the competitive environment of this high-energy sporting event.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the text 'CZE' appear on the runner's uniform?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the word 'Uzbekistan' visible on a sign in the image?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the number '53' on the right leg of the runner in black uniform?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the runner's uniform on the right yellow and red?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is one of the runners on the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a sign in the background on the left side?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the runner in the green shorts in front of the runner in the yellow and red uniform?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the runner in the yellow and red uniform looking focused?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background slightly blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Are the runners large in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three runners in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there road cones in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the runner in the dark uniform behind another runner?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image showing an outdoor scene?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a bright color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Does the text 'CZE' appear on the runner's uniform?  
   - yes

2. Is the word 'Uzbekistan' visible on a sign in the image?  
   - yes

3. Is the number '53' on the right leg of the runner in black uniform?  
   - no

4. Is the sky blue?  
   - yes

5. Is the runner's uniform on the right yellow and red?  
   - yes

6. Is one of the runners on the left side of the image?  
   - yes

7. Is there a sign in the background on the left side?  
   - n/a

8. Is the runner in the green shorts in front of the runner in the yellow and red uniform?  
   - n/a

9. Is the runner in the yellow and red uniform looking focused?  
   - n/a

10. Is the background slightly blurred?  
    - yes

11. Are the runners large in the image?  
    - n/a

12. Are there three runners in the image?  
    - yes

13. Are there road cones in the image?  
    - yes

14. Is the runner in the dark uniform behind another runner?  
    - n/a

15. Is the image showing an outdoor scene?  
    - yes

16. Does the image have a bright color palette?  
    - yes

17. Is the image a photograph?  
    - yes

18. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 18  

Score = (12/18) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of correct answers provided in relation to the total number of questions. Out of 18 questions, 12 were answered correctly, resulting in a score of 66.67%.

token_count: 490

caption_vocabulary_size: 300

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 172

candidate_caption: A candid street photograph taken from an eye-level perspective captures two individuals in motion, both running away from the camera on a grayish paved sidewalk arranged in a herringbone pattern with alternating light gray (RGB(179, 181, 180)) and darker gray tiles forming a diamond-like grid. The central figure is wearing a light purple hoodie with a visible hood pulled up over their head, dark pants, and black sneakers with white soles, creating a strong contrast against the muted background. Their body language suggests mid-stride movement, emphasizing speed. To the right, another runner or walker is partially visible but heavily blurred due to rapid motion, dressed in a colorful striped shirt featuring horizontal patterns in shades of teal blue, forest green, amber yellow, navy blue, and beige, paired with charcoal gray pants and dark shoes. In the foreground, there's a vibrant scarlet red car, likely a hatchback model, moving towards the left side of the frame. Its design is slightly out of focus due to motion blur, with reflections visible on its windows and chrome detailing on its bumper and tail lights. The background consists of an urban residential area characterized by a multi-story building with a concrete facade painted in pale grayish-blue tones (RGB(112, 129, 140)). Large rectangular windows with thin white frames are evenly spaced across multiple floors, some covered by curtains or blinds. Several balconies adorn the upper stories, adding architectural interest with wooden decks painted in soft mint green (RGB(151, 169, 170)), coral pink, and brown stripes. Some balconies feature railings made of horizontal metal bars painted in contrasting colors like navy blue, while others have decorative elements such as plants. Faint outlines of trees can be seen behind the buildings, suggesting the presence of natural elements within this cityscape. The overall mood is dynamic yet somewhat melancholic, captured under overcast daylight conditions that result in soft, diffused lighting throughout the scene. The color palette includes cool hues dominated by slate gray (RGB(132, 142, 152)), deep maroon (RGB(52, 43, 51)), sage green (RGB(113, 127, 115)), steel blue (RGB(124, 156, 176)), and muted mauve (RGB(118, 106, 111)), contributing to the subdued atmosphere despite the evident activity. The composition follows the rule of thirds, with diagonal lines created by the runners' paths and vehicle tracks, enhancing the sense of depth and urban hustle.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the car on the left red?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's hoodie gray?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person running in the middle of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person closer to the camera than the cars?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a car in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the car on the left red?  
     - yes

   - Is the person's hoodie gray?  
     - no

   - Is the person running in the middle of the image?  
     - n/a

   - Is the person closer to the camera than the cars?  
     - n/a

   - Is there a car in the image?  
     - yes

   - Are there two people in the image?  
     - yes

   - Does the image show outdoors?  
     - yes

   - Is the image a photograph?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 8

   Score = (5/8) × 100 = 62.5

score: 62.5

reasons: The score was calculated based on the number of correct answers (5) out of the total number of questions (8). The formula used was (5/8) × 100, resulting in a score of 62.5.

token_count: 511

caption_vocabulary_size: 311

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 177

candidate_caption: A vibrant nighttime urban scene featuring multiple neon signs on the El Cortez Hotel building, with an American flag visible atop the structure. The foreground showcases a person walking along the sidewalk dressed in dark clothing, including a black shirt, pants, and shoes, holding a lit cigarette near their mouth while carrying a small object. A young tree with green leaves stands slightly off-center to the right, its branches extending into the frame, partially obscuring the view of the hotel facade. The midground displays the lower level of the two-story El Cortez Hotel building, painted white with brown trim around the windows and doors. Above the ground floor, large electric blue neon sign reads 'EL CORTEZ HOTEL' in bold, sans-serif font, accompanied by smaller red text below stating 'COFFEE SHOP & BAR FREE PARKING'. To the right of this main sign, a vertical neon sign glows brightly in orange-yellow, spelling out 'GAMBLING' in capital letters. Below the main sign, another illuminated sign advertises 'FLOOR SHOWS' in bright yellow-gold against a red background. Three framed pictures or posters are visible on the building's facade; one prominently displays 'ALWAYS A WINNER' in white text on a green backdrop, while another shows a figure in a suit with arms crossed above a Starbucks logo emblem. The background reveals more of the upper building structure, including additional windows and a metal framework supporting the larger neon sign. String lights connect nearby buildings horizontally across the scene, adding warmth and festivity to the atmosphere. The sky is completely dark, enhancing the visibility and impact of the neon lights. The overall mood is lively and nostalgic, typical of Las Vegas nightlife, with high contrast between the brightly lit signs and the surrounding darkness, creating a dynamic visual effect that emphasizes the architectural elements and signage of this iconic establishment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'El Cortez HOTEL'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'FLOOR SHOWS' visible in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the neon sign at the top center red?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the 'GAMBLING' sign on the right side of the image?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the white building on the left side of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person walking on the sidewalk?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken at night?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. **Answer Each Question:**

   - "Does the image contain the text 'El Cortez HOTEL'?"  
     Answer: yes

   - "Is the text 'FLOOR SHOWS' visible in the image?"  
     Answer: yes

   - "Is the neon sign at the top center red?"  
     Answer: n/a

   - "Is the 'GAMBLING' sign on the right side of the image?"  
     Answer: yes

   - "Is the white building on the left side of the image?"  
     Answer: n/a

   - "Is there a tree in the image?"  
     Answer: yes

   - "Is there a person walking on the sidewalk?"  
     Answer: yes

   - "Is the image taken at night?"  
     Answer: yes

   - "Is the image color graded with high saturation?"  
     Answer: n/a

2. **Calculate Score:**

   - Number of Correct Answers: 6
   - Total Number of Questions: 9

   Score = (6/9) × 100 = 66.67

score: 66.67

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 6 out of 9 questions were answered correctly, resulting in a score of 66.67%.

token_count: 373

caption_vocabulary_size: 231

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 182

candidate_caption: A whimsical digital illustration of a cat in a vibrant floral pattern, lying down with its body curved slightly to the right against an off-white background (#f3edec). The cat's large, expressive eyes are prominent, looking directly at the viewer, conveying a calm yet curious expression. Its fur is intricately designed with various flowers and leaves, creating a seamless blend that emphasizes both the feline form and natural elements. Dominating the upper part of the cat's body is a large pink daisy-like flower with layered petals transitioning from light to dark shades of pink, featuring a bright green center surrounded by intricate white striations. Small orange blossoms and clusters of red-orange stars dot the cat's face and body, while golden yellow blooms add warmth to the composition. Green leaves and stems intertwine throughout the design, connecting different floral elements and adding depth to the piece. A small purple butterfly adds an extra touch of nature near the cat's head. The color palette includes vivid shades of pink, orange, yellow, lavender, forest green, sky blue, and white, all harmoniously blended together. The overall mood is serene and enchanting, with soft lighting and high saturation enhancing the vibrancy of the colors. The flat, two-dimensional style of the artwork creates a balanced composition, focusing attention on the intricate details and interplay between the organic shapes of the cat and the surrounding flora. The artist's signature appears in black cursive script near the bottom left corner of the illustration.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there a signature in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the largest flower on the cat pink?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the cat in the center of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the cat looking relaxed?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the cat large in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the cat's ears pointy?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a butterfly in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the cat lying down?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a vibrant color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a painting?'}]

openai_answers: 1. Is there a signature in the image?  
   - yes

2. Is the background color white?  
   - no

3. Is the largest flower on the cat pink?  
   - yes

4. Is the cat in the center of the image?  
   - n/a

5. Is the cat looking relaxed?  
   - yes

6. Is the cat large in the image?  
   - n/a

7. Is the cat's ears pointy?  
   - n/a

8. Is there a butterfly in the image?  
   - yes

9. Is the cat lying down?  
   - yes

10. Does the image have a vibrant color palette?  
    - yes

11. Is the image a painting?  
    - no

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 11  

Score = (7/11) × 100 = 63.64

score: 63.64

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 7 out of 11 questions were answered correctly, resulting in a score of 63.64%.

token_count: 299

caption_vocabulary_size: 190

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 183

candidate_caption: The scene captures an urban setting in Missouri, United States of America, during daylight hours with soft natural lighting. The main focus is a large, multi-layered mural painted on the side of a building, showcasing various grayscale figures engaged in different activities such as playing musical instruments, riding horses, dancing, and socializing. The left section features a prominent figure wearing sunglasses, a white jacket with gold chain necklaces reading 'TURF' and 'LOUIS,' while another character wears a bandana over their face. In the center-right part of the mural, there's a yellow banner with bold black text reading "IN GOD WE TRUST," followed by "NINE TIMES" above a stylized 9-shaped symbol. Below this are more lines of text stating "S&P CLUB EST 1991 R.I.P LOUIV." Other visible elements include a small wooden structure with broken glass panels positioned centrally near the bottom of the mural, surrounded by construction materials like wood planks and metal beams stacked atop a trailer. To the right of the mural, there's additional graffiti-style artwork featuring multiple people in various poses, including some holding microphones and others playing drums. A partially visible street lamp extends horizontally across one corner of the building's top edge. The foreground includes a grassy area with patches of wild grass, small white flowers, and scattered debris. A blue-painted wooden structure or deck is partially visible in the lower-left corner. The overall color palette consists mainly of muted tones like gray, brown, beige, and charcoal, creating a nostalgic and culturally rich atmosphere. The composition employs a wide aspect ratio typical of widescreen formats, capturing both the extensive mural work and surrounding urban elements, emphasizing the historical significance and cultural richness of the depicted community space.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'IN GOD WE TRUST'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the mural predominantly grey?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is there a light blue building on the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the mural painted on the wall?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the blue building to the left of the mural?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the mural on the right closer than the mural in the center?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the mural large?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is there text on the mural?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there graffiti in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is this image a shot from the movie?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'IN GOD WE TRUST'?  
   - yes

3. Is the mural predominantly grey?  
   - yes

4. Is there a light blue building on the left side of the image?  
   - n/a

5. Is the mural painted on the wall?  
   - yes

6. Is the blue building to the left of the mural?  
   - n/a

7. Is the mural on the right closer than the mural in the center?  
   - n/a

8. Is the image sharp?  
   - n/a

9. Is the mural large?  
   - yes

10. Is there text on the mural?  
    - yes

11. Does the image show outdoors?  
    - yes

12. Is there graffiti in the image?  
    - yes

13. Is this image a shot from the movie?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 13  

Score = (9/13) × 100 = 69.23

score: 69.23

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 13 questions were answered correctly, resulting in a score of 69.23%.

token_count: 355

caption_vocabulary_size: 244

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 186

candidate_caption: A dramatic scene from a period piece set in the 1800s, captured with low-key lighting that creates strong shadows and highlights facial expressions. The composition is right-heavy, focusing on two men engaged in an intense conversation in the foreground. On the left, a man with thick curly dark brown hair, a full beard, and mustache wears a black tailcoat with a white shirt and bow tie. He faces slightly to the right, his expression serious as he looks downward. On the right, another man with short dark hair styled in loose curls, deep-set eyes, and a stern expression leans forward towards the first man. He's dressed in a black tailcoat with a high-collared white shirt featuring puffy sleeves and a large white bow tie. A light-colored vest with intricate patterns adorns him, buttoned up to the neck, and he holds a glass of amber liquid, possibly wine or brandy, close to his chest. In the midground, several elegantly dressed individuals are mingling. To the center-left, a woman with her hair styled in an elaborate updo adorned with a sparkling tiara and earrings stands near a partially open wooden doorframe. She wears a cream-colored gown with gold embroidery, a square neckline, and a fitted bodice cinched at the waist by a delicate belt. Her necklace features a prominent central gemstone surrounded by smaller stones, reflecting soft light. To her right, another woman in a beige dress with lace details stands holding a drink. Further back, a man in a black suit with gold buttons observes the scene, while a woman in a white gown with yellow gloves watches the interaction intently. The background showcases a dimly lit room with warm beige walls and a doorway leading to a darker space where more people can be seen socializing. The overall color palette consists of muted tones like charcoal (#191618), tan (#cbb9a4), sienna (#7f6d59), taupe (#6b5e47), slate gray (#585d60), and cool gray (#75776e). The atmosphere suggests tension and intrigue within this sophisticated yet somber gathering, reminiscent of Jane Austen's era or historical drama set in England during the Regency period (1801-1810).

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the color of the man's shirt white?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the door dark brown?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the man with a stern expression in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the woman with the yellow gloves on the right side of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the man in the foreground look serious?'}
 {'answer': 'no', 'category': 'blur', 'question': 'Is the background slightly blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person on the left larger than the person on the right?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the doorway rectangular?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the man in the center holding a drink?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the color of the man's shirt white?  
   - yes

2. Is the door dark brown?  
   - n/a

3. Is the man with a stern expression in the center of the image?  
   - no

4. Is the woman with the yellow gloves on the right side of the image?  
   - yes

5. Does the man in the foreground look serious?  
   - yes

6. Is the background slightly blurred?  
   - n/a

7. Is the person on the left larger than the person on the right?  
   - n/a

8. Is the doorway rectangular?  
   - n/a

9. Is the man in the center holding a drink?  
   - no

10. Does the image show indoors?  
    - yes

11. Does the image have a warm color palette?  
    - yes

12. Is the image a shot from a film?  
    - yes

13. Does the image have low brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 13  

Score = (8/13) × 100 ≈ 61.54

score: 61.54

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 13 questions were answered correctly, resulting in a score of approximately 61.54%.

token_count: 457

caption_vocabulary_size: 284

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 196

candidate_caption: A cinematic still from a 1980s-inspired film captures a contemplative scene set in an interior space, likely a hotel room or waiting area. The composition is left-heavy with a woman seated on a wooden chair positioned slightly to the right of center against a light gray wall (#b3beb4) with subtle horizontal lines. She wears an off-white (#d1c9ba) military-style jacket with black buttons, epaulets, and two breast pockets featuring button flaps. A matching wide belt cinches her waist. Her wide-legged trousers are secured by a gold buckle at her side. Small gold earrings adorn her ears, while a watch graces her left wrist. The woman's short dark hair frames her face as she gazes directly at the camera with an engaged expression, mouth slightly open as if speaking or reacting. Her left hand rests casually on her lap while her right arm extends outward towards the camera, fingers spread apart. To her left, there is a small table holding a teal vase filled with vibrant yellow flowers, their petals slightly curled at the tips. On the right side, a dark brown wooden console table supports various items including a tall cylindrical metal coffee maker with a black handle, white cups on saucers, a silver pitcher, two lemons, oranges, bananas, and a stack of plates. A brass-colored lamp with a beige shade provides warm lighting, casting soft shadows on the wall and highlighting textures in the foreground. Above the lamp hangs a partially visible picture frame with a thin black border. The overall mood is calm yet intense, enhanced by the soft artificial lighting that creates gentle shadows. The color palette includes shades of light gray (RGB(152, 150, 148)), deep charcoal (RGB(22, 20, 19)), muted slate blue (RGB(70, 80, 89)), cool grayish-brown (RGB(101, 97, 94)), warm taupe (RGB(116, 96, 83)), and rich russet (RGB(132, 102, 71)). The low contrast and moderate saturation contribute to the introspective atmosphere of this quiet moment, captured with a wide lens and a medium frame size using a Panavision H series lens on an ARRI ALEXA Mini LF camera.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the color of the lamp's shade beige?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the wall white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the flowers yellow?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person sitting on a chair?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the lamp to the right of the person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the table large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the vase holding the flowers round?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two lemons on the table?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a flower vase in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the color of the lamp's shade beige?  
   - yes

2. Is the wall white?  
   - no

3. Is the color of the flowers yellow?  
   - yes

4. Is the person sitting on a chair?  
   - yes

5. Is the lamp to the right of the person?  
   - yes

6. Does the person look serious?  
   - n/a

7. Is the image sharp?  
   - n/a

8. Is the table large?  
   - n/a

9. Is the vase holding the flowers round?  
   - n/a

10. Are there two lemons on the table?  
    - yes

11. Is there a flower vase in the image?  
    - yes

12. Is the image taken indoors?  
    - yes

13. Is the image a shot from a film?  
    - yes

14. Does the image have low brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 14  

Score = (9/14) × 100 = 64.29

score: 64.29

reasons: The score is calculated based on the number of questions answered with a definitive 'yes' or 'no' (9) out of the total number of questions (14). The 'n/a' responses are not considered in the calculation.

token_count: 465

caption_vocabulary_size: 282

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

#### Sample 197

candidate_caption: A movie poster featuring two characters, Hermione Granger (left) and Ron Weasley (right), standing in a dense forest setting. Hermione has long, wavy light brown hair with subtle highlights that flow behind her shoulders, framing her face as she looks intensely towards the viewer with a serious expression. She wears a textured teal knitted hoodie with intricate patterns on the sleeves and cuffs, layered over a dark blue scarf featuring maroon accents. Her hands are partially visible wearing dark gloves. Ron has short, reddish-brown hair and is positioned slightly to the right of center, peeking out from behind a large tree trunk. He wears a red and black plaid jacket over a darker layer and has a determined look. The lighting creates dramatic shadows and highlights their faces, emphasizing the tense atmosphere. The background features tall, slender trees stretching vertically through the frame, creating a sense of depth and seclusion. A pale yellow tent is barely visible among the misty scenery, suggesting an unknown presence or campsite. Horizontal branches across the foreground add to the forest's natural barrier effect. Text at the bottom reads 'TRUST NO ONE' in white serif font, followed by '#P7 PART 1 11.19' in metallic silver with a decorative style reminiscent of swords crossing through letters. Additional text includes 'HEYDAY FILMS', 'IMAX', and 'www.HarryPotter.com'. The overall color palette consists of cool hues like dark green, teal, gray, and midnight blue, contributing to the mysterious and suspenseful mood of the poster. The high contrast between illuminated areas and deep shadows enhances the cinematic quality and atmospheric feel typical of film noir photography.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'text', 'question': "Does the image contain the text 'TRUST NO ONE'?"}
 {'answer': 'Yes', 'category': 'text', 'question': "Does the image contain the text '11.19'?"}
 {'answer': 'Yes', 'category': 'color', 'question': "Is the woman's scarf red?"}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person on the right closer to the camera than the person on the left?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the man looking serious?'}
 {'answer': 'Yes', 'category': 'proper noun', 'question': "Is the character's name Hermione?"}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the tree beside the man large?'}
 {'answer': 'No', 'category': 'entity', 'question': 'Is there a tent in the image?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the movie's name 'Harry Potter and the Deathly Hallows: Part 1'?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a promotional poster?'}]

openai_answers: 1. Does the image contain the text 'TRUST NO ONE'?  
   - yes

2. Does the image contain the text '11.19'?  
   - yes

3. Is the woman's scarf red?  
   - no

4. Is the person on the right closer to the camera than the person on the left?  
   - n/a

5. Is the man looking serious?  
   - no

6. Is the character's name Hermione?  
   - yes

7. Is the tree beside the man large?  
   - yes

8. Is there a tent in the image?  
   - yes

9. Are there two people in the image?  
   - yes

10. Does the image show outdoors?  
    - yes

11. Does the image have a cool color palette?  
    - yes

12. Is the movie's name 'Harry Potter and the Deathly Hallows: Part 1'?  
    - n/a

13. Is the image a promotional poster?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 13  

Score = (9/13) × 100 ≈ 69.23

score: 69.23

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 13 questions were answered correctly, resulting in a score of approximately 69.23%.

token_count: 336

caption_vocabulary_size: 235

score_bin: 60-70

evaluated_by: gpt-4o-2024-08-06

### Scores in 70-80 Bin

```python
                                     candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
2    A surreal digital illustration features a cent...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     281      70-80  gpt-4o-2024-08-06
4    A close-up photograph captures an intimate mom...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     252      70-80  gpt-4o-2024-08-06
7    A promotional graphic featuring a vibrant cont...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     260      70-80  gpt-4o-2024-08-06
8    A cozy kitchen scene with an emphasis on vinta...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     186      70-80  gpt-4o-2024-08-06
10   An elderly man with short, slightly tousled gr...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     127      70-80  gpt-4o-2024-08-06
12   A nature photograph captures an enchanting aut...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     265      70-80  gpt-4o-2024-08-06
14   A cinematic portrait photograph captures a man...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     184      70-80  gpt-4o-2024-08-06
16   This animated scene from 'The Simpsons' movie ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     329      70-80  gpt-4o-2024-08-06
18   A landscape photograph capturing an ancient st...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     245      70-80  gpt-4o-2024-08-06
19   A vintage-style illustration with a forest gre...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     190      70-80  gpt-4o-2024-08-06
22   A close-up anime-style illustration depicts a ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     258      70-80  gpt-4o-2024-08-06
26   A stunning night-time landscape photograph fea...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     276      70-80  gpt-4o-2024-08-06
27   A promotional poster for the Amazon original m...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     216      70-80  gpt-4o-2024-08-06
31   A close-up photograph of a beautifully plated ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     152      70-80  gpt-4o-2024-08-06
32   A landscape photograph capturing a serene yet ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     209      70-80  gpt-4o-2024-08-06
35   A scene from the animated series 'Scooby-Doo' ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     245      70-80  gpt-4o-2024-08-06
41   An intense moment from an ice hockey game capt...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     160      70-80  gpt-4o-2024-08-06
42   A modern, minimalist Hanukkah invitation card ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     186      70-80  gpt-4o-2024-08-06
44   The scene depicts an intense conversation betw...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     224      70-80  gpt-4o-2024-08-06
56   A cinematic scene set in a Parisian subway sta...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     210      70-80  gpt-4o-2024-08-06
60   A dynamic photograph captures a sleek, metalli...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     241      70-80  gpt-4o-2024-08-06
61   Three individuals are interacting warmly in an...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     242      70-80  gpt-4o-2024-08-06
65   An aerial photograph captures a vibrant modern...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     285      70-80  gpt-4o-2024-08-06
66   A close-up portrait of a young woman with long...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     271      70-80  gpt-4o-2024-08-06
69   A close-up shot of a black Sony smartphone hel...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     227      70-80  gpt-4o-2024-08-06
71   A close-up shot of a middle-aged man with long...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     211      70-80  gpt-4o-2024-08-06
72   The scene from 'The Wrong Missy' captures a li...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     261      70-80  gpt-4o-2024-08-06
74   The image is divided into two sections, each s...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     268      70-80  gpt-4o-2024-08-06
81   A full-body street fashion photograph taken in...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     255      70-80  gpt-4o-2024-08-06
82   A black-and-white still from a 1930s film feat...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     200      70-80  gpt-4o-2024-08-06
85   A serene landscape photograph captures an intr...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     251      70-80  gpt-4o-2024-08-06
91   A dramatic scene from the movie 'The Witches' ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     183      70-80  gpt-4o-2024-08-06
92   A photograph taken inside a large industrial h...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     183      70-80  gpt-4o-2024-08-06
95   A black-and-white photograph captures an intim...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     194      70-80  gpt-4o-2024-08-06
96   The scene from the movie 'Jojo Rabbit', direct...  pg-captioner  [{'answer': 'no', 'category': 'color', 'questi...  ...                     238      70-80  gpt-4o-2024-08-06
97   A dynamic, abstract photograph capturing the e...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     218      70-80  gpt-4o-2024-08-06
99   A dynamic scene from the video game 'Assassin'...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     260      70-80  gpt-4o-2024-08-06
104  A vibrant photograph captures seven knights ri...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     254      70-80  gpt-4o-2024-08-06
113  A close-up shot captures a person's hand holdi...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     267      70-80  gpt-4o-2024-08-06
116  A photograph capturing a serene moment of a wo...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     185      70-80  gpt-4o-2024-08-06
119  A close-up photograph of a breakfast plate fea...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     177      70-80  gpt-4o-2024-08-06
123  A movie poster for 'Zombieland Double Tap' fea...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     293      70-80  gpt-4o-2024-08-06
127  A surreal, ethereal photograph captures an ang...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     246      70-80  gpt-4o-2024-08-06
128  An elderly woman with deeply wrinkled skin sit...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     211      70-80  gpt-4o-2024-08-06
130  A cinematic scene from the movie 'Joker', feat...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     245      70-80  gpt-4o-2024-08-06
133  A landscape photograph captures an adventurous...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     301      70-80  gpt-4o-2024-08-06
135  A black-and-white historical photograph captur...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     198      70-80  gpt-4o-2024-08-06
142  A breathtaking landscape photograph captures a...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     329      70-80  gpt-4o-2024-08-06
146  A vibrant red British-style telephone booth st...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     330      70-80  gpt-4o-2024-08-06
150  A nighttime urban scene captures a bustling pu...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     209      70-80  gpt-4o-2024-08-06
158  A digital rendering depicts an intense cosmic ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     224      70-80  gpt-4o-2024-08-06
161  A vibrant underwater photograph captures a div...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     261      70-80  gpt-4o-2024-08-06
168  A photograph of an underground subway station ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     259      70-80  gpt-4o-2024-08-06
171  A photograph captures a serene moment of a wom...  pg-captioner  [{'answer': 'yes', 'category': 'position', 'qu...  ...                     247      70-80  gpt-4o-2024-08-06
181  A cozy bedroom scene featuring a light wooden ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     207      70-80  gpt-4o-2024-08-06
185  A cinematic still from 'The Amazing Spider-Man...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     220      70-80  gpt-4o-2024-08-06
187  A close-up shot of a casino blackjack table, c...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     210      70-80  gpt-4o-2024-08-06

[57 rows x 10 columns]
```

#### Sample 2

candidate_caption: A surreal digital illustration features a central female figure with long, straight teal hair sitting cross-legged on the ground. She has pale skin adorned with multiple small red eyes arranged in vertical rows across her face, neck, arms, and legs, creating an eerie effect. The woman wears a blindfold made of white fabric strips over her eyes, with small red horns protruding from her temples. Her expression is pained or contemplative as she covers her face with one hand. She's dressed in a form-fitting light blue strapless top that blends seamlessly into the background, leaving only her upper body visible. Her limbs are bound by white bands, some covered in blood stains. Woven through her fingers and wrapped around her body are more straps bearing the same pattern of red marks. In front of her, she holds a vivid crimson red demon-like head with yellow eyes, bared teeth, and pointed ears, its tentacle-like structures draping down towards her lap. Surrounding the woman are five ethereal fish-like creatures with flowing tails and fins in pastel shades of lavender purple, sky blue, mint green, soft pink, and light turquoise. These fantastical beings float above and around her, adding to the otherworldly atmosphere. Some fish have translucent bodies transitioning between colors like periwinkle (RGB(137, 138, 160)) and mauve (RGB(140, 119, 124)). The entire scene is set against a solid black background (RGB(3, 4, 5)), providing high contrast that makes the colorful elements stand out prominently. The artwork employs a sticker-like quality with a white border surrounding the central figures, enhancing the surrealistic feel and giving it a dreamlike appearance reminiscent of Japanese anime style. The color palette includes muted tones such as charcoal gray (RGB(59, 62, 61)), warm beige (RGB(181, 159, 145)), slate gray (RGB(93, 92, 89)), steel blue (RGB(116, 148, 167)), and dark brown (RGB(68, 54, 52)). This composition creates a striking visual impact, balancing vibrant colors against a dark backdrop and evoking a sense of mystery and tranquility amidst the chaotic elements.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the hair's color light green?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the character located in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the character sitting?'}
 {'answer': 'yes', 'category': 'emotion', 'question': "Is the character's expression neutral?"}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the character's size relatively large in the context of the image?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the character's hair long?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one character in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a fish in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the character holding a red head?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a pastel color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an illustration?'}]

openai_answers: 1. Is the hair's color light green?  
   - no

2. Is the character located in the center of the image?  
   - yes

3. Is the character sitting?  
   - yes

4. Is the character's expression neutral?  
   - no

5. Is the character's size relatively large in the context of the image?  
   - n/a

6. Is the character's hair long?  
   - yes

7. Is there only one character in the image?  
   - yes

8. Is there a fish in the image?  
   - yes

9. Is the character holding a red head?  
   - yes

10. Does the image have a pastel color palette?  
    - yes

11. Is the image an illustration?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 11  

Score = (8/11) × 100 ≈ 72.73

score: 72.73

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 11 questions were answered correctly, resulting in a score of approximately 72.73%.

token_count: 457

caption_vocabulary_size: 281

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 4

candidate_caption: A close-up photograph captures an intimate moment between two individuals seated in the front seat of an off-white car, likely on their wedding day. The man, positioned on the left side of the frame, has short light brown hair slicked back, green eyes, and a trimmed beard and mustache. He is wearing a black tuxedo jacket with satin lapels over a crisp white shirt featuring a large white bow tie, silver cufflinks, and a black leather strap watch on his left wrist. His right hand is raised high towards the car's roof compartment, pointing upwards with a focused expression as he looks slightly upward and to the left. The woman, positioned on the right side of the frame, has blonde hair styled in an elegant low bun adorned with a simple pearl headband. She is dressed in an exquisite white wedding dress with delicate ruffled shoulder details and cap sleeves, complemented by sparkling drop earrings featuring dangling pearls. Her face is turned slightly towards the man, with bright blue eyes looking up attentively. Both are leaning forward, engaged in something outside the car window, with joyful expressions suggesting excitement or anticipation. The lighting is soft and natural, coming from the right side through the car windows, illuminating their faces evenly and creating a warm atmosphere. The interior of the car features beige walls with subtle texture and part of the sunroof visible at the top left corner. A glimpse of the vehicle's dark exterior can be seen through a partially open window on the far left edge. The color palette includes shades of cream (RGB(221, 213, 188)), taupe (RGB(100, 89, 70)), olive gray (RGB(111, 107, 82)), sage green (RGB(124, 140, 121)), khaki (RGB(138, 120, 87)), and deep teal (RGB(31, 38, 32)). This cinematic still suggests a formal event, possibly set in Copenhagen, Denmark during the 2010s, capturing the joyous and celebratory mood of the couple as they embark on this significant occasion together.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the background color off-white?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the person with the white bow tie on the left side of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the person with the white dress to the right of the person with the black suit?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the woman smiling?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a car in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the man pointing with his finger?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show inside the car?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with a neutral palette?'}]

openai_answers: 1. Is the background color off-white?  
   - yes

2. Is the person with the white bow tie on the left side of the image?  
   - yes

3. Is the person with the white dress to the right of the person with the black suit?  
   - yes

4. Is the woman smiling?  
   - n/a

5. Are there two people in the image?  
   - yes

6. Is there a car in the image?  
   - yes

7. Is the man pointing with his finger?  
   - yes

8. Does the image show inside the car?  
   - yes

9. Does the image have a warm color palette?  
   - yes

10. Is the image a shot from a film?  
    - n/a

11. Is the image color graded with a neutral palette?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 11  

Score = (8/11) × 100 = 72.73

score: 72.73

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 11 questions were answered correctly, resulting in a score of 72.73%.

token_count: 425

caption_vocabulary_size: 252

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 7

candidate_caption: A promotional graphic featuring a vibrant contrast between a bright red background on the left side (#ff0000) and a solid black right side, with a split composition creating two distinct areas. The left side showcases a young woman in a joyful pose against the vivid red backdrop, wearing a form-fitting black sports bra with thin straps forming an 'X' shape across her chest and high-waisted black athletic shorts or leggings. Her long brown hair is tied back into a sleek ponytail that flows behind her to the right, appearing slightly windswept and partially covering her face. She smiles broadly, leaning slightly forward with her head tilted to the left, exuding energy and enthusiasm. White earbuds are visible in both ears, with white cables trailing down her neck and body, connected to a small silver smartphone held in both hands near her hips. The woman's skin tone appears tan with a slight glow, highlighting her smooth complexion. On the right side, bold text reads 'MOTIVATION MUSIC' in large, uppercase white letters (#ffffff), positioned diagonally from bottom left to top right within a red brushstroke-like overlay. Above this main title, the word 'PLAYLIST' appears in smaller, regular white font at the top of the black section. Additional design elements include a white starburst icon in the bottom right corner and thin white oval loops intersecting near the center-right area. A torn paper effect with rough edges frames parts of the image, adding a dynamic feel to the composition. The lighting is bright and even, emphasizing the subject's features and attire while casting soft shadows that enhance the overall energetic mood. The color palette includes shades of reddish-brown (#8f3c21), warm beige (#e4d2bc), dark gray (#5c5657), muted rose (#ae6e70), and cool grays (#7d8989, #787978), contributing to the modern, eye-catching aesthetic of the motivational music playlist advertisement.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'MOTIVATION MUSIC'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the word 'PLAYLIST' present in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': "Is the color of the text 'MOTIVATION MUSIC' white?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the word 'PLAYLIST' at the top right corner of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'MOTIVATION MUSIC' to the right of the person?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person smiling?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the text slightly out of focus?'}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the person larger than the text 'MOTIVATION MUSIC'?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the white paintbrush stroke at the bottom rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the person's head tilted to the left?"}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a poster?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'MOTIVATION MUSIC'?  
   - yes

3. Is the word 'PLAYLIST' present in the image?  
   - yes

4. Is the color of the text 'MOTIVATION MUSIC' white?  
   - yes

5. Is the person in the left side of the image?  
   - yes

6. Is the word 'PLAYLIST' at the top right corner of the image?  
   - no

7. Is the text 'MOTIVATION MUSIC' to the right of the person?  
   - yes

8. Is the person smiling?  
   - yes

9. Is the text slightly out of focus?  
   - n/a

10. Is the person larger than the text 'MOTIVATION MUSIC'?  
    - n/a

11. Is the white paintbrush stroke at the bottom rectangular?  
    - n/a

12. Is there only one person in the image?  
    - yes

13. Is there a person in the image?  
    - yes

14. Is the person's head tilted to the left?  
    - yes

15. Does the image have a warm color palette?  
    - yes

16. Is the image a poster?  
    - n/a

17. Does the image have high contrast?  
    - yes

18. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 13  
Total Number of Questions: 18  

Score = (13/18) × 100 = 72.22

score: 72.22

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 13 out of 18 questions were answered correctly, resulting in a score of 72.22%.

token_count: 399

caption_vocabulary_size: 260

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 8

candidate_caption: A cozy kitchen scene with an emphasis on vintage and rustic elements, featuring a white ceramic farmhouse sink with vertical fluting and curved gold faucet centrally positioned against a backdrop of glossy forest green tiles arranged in a subway pattern. The countertop above the sink is white marble-like material with subtle veining patterns. On the counter, there are fresh green pears with yellow skin patches, a white dish towel with red stripes draped over its edge, labeled 'LINEN', a lit candle in a brown ceramic holder, a tan jar with a lid, and various small containers including one labeled 'MARIUS FABRE'. To the left, there's a potted plant with thin green leaves and pink-purple flowers wrapped in crinkled brown paper. A wooden chair partially enters from the bottom left corner. Above the sink, a dark green open shelf holds several decorative items, including a taxidermied duck with iridescent teal head feathers, a terracotta pot with a cactus-like plant, and a framed picture depicting two people riding horses. Hanging from the shelf is a clear glass pendant light with a brass fixture and twisted red cord, along with a beige brush with natural bristles suspended by a black string. The background consists entirely of glossy forest green tiles that create a striking contrast with the other elements. Warm lighting enhances the inviting atmosphere, highlighting the textures and colors throughout the space.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'LINEN'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the tiles color green?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the sink white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the towel hanging near the sink?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the faucet in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the duck figurine above the faucet?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the brown plant pot to the right and above the faucet?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the faucet large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the sink rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three pears in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one duck figurine?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a framed picture in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a duster in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the white towel hanging over the cabinet?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette include green tones?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'LINEN'?  
   - yes

3. Is the tiles color green?  
   - yes

4. Is the color of the sink white?  
   - yes

5. Is the towel hanging near the sink?  
   - yes

6. Is the faucet in the center of the image?  
   - yes

7. Is the duck figurine above the faucet?  
   - yes

8. Is the brown plant pot to the right and above the faucet?  
   - yes

9. Is the faucet large?  
   - n/a

10. Is the sink rectangular?  
    - n/a

11. Are there three pears in the image?  
    - n/a

12. Is there one duck figurine?  
    - yes

13. Is there a framed picture in the image?  
    - yes

14. Is there a duster in the image?  
    - yes

15. Is the white towel hanging over the cabinet?  
    - n/a

16. Does the image show indoors?  
    - yes

17. Does the image have a warm color palette?  
    - yes

18. Does the image's color palette include green tones?  
    - yes

19. Is the image a photograph?  
    - n/a

20. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 15  
Total Number of Questions: 20  

Score = (15/20) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 15 out of 20 questions were answered correctly, resulting in a score of 75%.

token_count: 280

caption_vocabulary_size: 186

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 10

candidate_caption: An elderly man with short, slightly tousled gray hair and black-framed rectangular glasses is walking while carrying white folders with yellow spines under his left arm. He is dressed in a navy blue suit jacket over a light blue dress shirt, complemented by a light gray textured tie featuring small dots. His expression is neutral as he faces slightly to the right of the camera. The lighting is soft and even indoor illumination, typical of an office or institutional setting. A prominent reflection of the man can be seen on the glass panel to his right, created by an escalator. This reflection adds depth to the composition and emphasizes the professional atmosphere. In the background, there are minimal visible elements such as fluorescent lights arranged in squares on the ceiling, contributing to the overall professional mood of the photograph. The color palette consists mainly of cool tones like whites, grays, and blues, creating a balanced exposure with medium contrast and saturation.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the tie grey?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the reflection of the person to the right of the actual person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking serious?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the folder rectangular?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is the person holding papers?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a neutral color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the tie grey?  
   - yes

2. Is the person on the left side of the image?  
   - n/a

3. Is the reflection of the person to the right of the actual person?  
   - yes

4. Is the person looking serious?  
   - yes

5. Is the folder rectangular?  
   - yes

6. Is the person holding papers?  
   - yes

7. Is the image taken indoors?  
   - yes

8. Does the image have a neutral color palette?  
   - yes

9. Is the image a photograph?  
   - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 9  

Score = (7/9) × 100 = 77.78

score: 77.78

reasons: The score is calculated based on the number of 'yes' answers out of the total number of questions. There are 7 'yes' answers out of 9 questions, resulting in a score of 77.78%.

token_count: 185

caption_vocabulary_size: 127

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 12

candidate_caption: A nature photograph captures an enchanting autumnal scene in what appears to be a forest clearing, showcasing a chipmunk standing upright on its hind legs among vibrant fall foliage and mushrooms near Portland, Oregon. The chipmunk is positioned slightly left of center, facing forward with its front paws resting on its chest and tail extended behind it. Its fur features distinctive light brown and white stripes, with a soft gray tail blending into the background. The animal's cheeks are puffed out as if chattering or vocalizing, adding life to the composition. To the right of the chipmunk are two mushrooms; a larger one with a bright red cap adorned with numerous evenly spaced white spots ranging from small dots to slightly elongated shapes. The mushroom's cap shows a gradient color change from deep red at the base to golden yellow towards the edge. Beside this stands a smaller mushroom with a similar appearance but fewer spots. Both have creamy white stems that contrast beautifully against their caps. The foreground consists of lush green grass interspersed with fallen leaves in various shades of crimson (RGB(191, 40, 42)), burgundy (RGB(119, 44, 36)), pink (RGB(197, 95, 99), RGB(150, 75, 69)), burnt sienna (RGB(155, 89, 56)), and olive green (RGB(120, 123, 84)). These leaves cover the ground densely, creating a rich tapestry that adds texture and depth to the scene. Thin branches extend diagonally across the frame, bearing deep burgundy leaves arranged in alternating patterns along dark reddish-brown stems. In the background, there's a soft bokeh effect created by the blurred foliage in vibrant autumn colors like forest green, amber yellow, and maroon, enhancing the dreamy quality of the image. Sunlight filters through the canopy, casting dappled shadows and highlights throughout the scene, emphasizing the textures and colors while maintaining a naturalistic mood. The overall lighting is warm and sunny, contributing to the magical atmosphere of this tranquil woodland setting during early springtime.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is there red in the image?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the large mushroom on the right side of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the small mushroom to the left of the large mushroom?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the chipmunk looking curious?'}
 {'answer': 'Yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the large mushroom of the same size as the chipmunk?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the smaller mushroom's top spherical?"}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two mushrooms in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a chipmunk in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the chipmunk standing on the grass?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is there red in the image?  
   - yes

2. Is the large mushroom on the right side of the image?  
   - yes

3. Is the small mushroom to the left of the large mushroom?  
   - yes

4. Is the chipmunk looking curious?  
   - n/a

5. Is the background blurred?  
   - yes

6. Is the large mushroom of the same size as the chipmunk?  
   - n/a

7. Is the smaller mushroom's top spherical?  
   - n/a

8. Are there two mushrooms in the image?  
   - yes

9. Is there a chipmunk in the image?  
   - yes

10. Is the chipmunk standing on the grass?  
    - yes

11. Does the image show outdoors?  
    - yes

12. Does the image have a warm color palette?  
    - yes

13. Is the image a photograph?  
    - yes

14. Does the image have high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of questions answered correctly out of the total number of questions. In this case, 10 out of 14 questions were answered correctly, resulting in a score of 71.43%.

token_count: 429

caption_vocabulary_size: 265

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 14

candidate_caption: A cinematic portrait photograph captures a man with dark skin, short black hair, and a full beard standing slightly to the right of center within an elegant interior setting. He is dressed in a well-fitted charcoal gray suit jacket over a crisp white dress shirt paired with a diagonally striped tie featuring shades of gold, black, and white. The lighting is low-key and warm, coming from the left side, creating dramatic shadows on his face while highlighting his facial features, particularly his expressive brown eyes and prominent cheekbones. His expression is serious yet confident as he looks directly at the camera with a slight turn to the right, conveying a sense of contemplation or engagement. To the right of the subject are tall golden columns with vertical ridges, adding texture and depth to the composition. In the background, there are blurred elements suggesting an opulent room, including ornate architectural details such as arches and chandeliers. The ceiling appears detailed with a patterned design, illuminated by warm lights. This creates a high-contrast effect between the brightly lit areas and darker surroundings, emphasizing the rich textures and colors of the scene. The overall mood is intense and dramatic, enhanced by the muted color palette dominated by deep blacks, rich browns, golds, and creams, with low saturation and luminance contributing to a moody atmosphere reminiscent of 1960s London.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the background dark?'}
 {'answer': 'Yes', 'category': 'color', 'question': "Is the person's suit grey?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in front of the columns?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the person smiling?'}
 {'answer': 'Yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the person large in the image?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the background dark?  
   - yes

2. Is the person's suit grey?  
   - yes

3. Is the person in the center of the image?  
   - no

4. Is the person in front of the columns?  
   - yes

5. Is the person smiling?  
   - no

6. Is the background blurred?  
   - yes

7. Is the person large in the image?  
   - n/a

8. Is there one person in the image?  
   - yes

9. Does the image show indoors?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a shot from a film?  
    - n/a

12. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 12  

Score = (9/12) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 12 questions were answered correctly, resulting in a score of 75%.

token_count: 274

caption_vocabulary_size: 184

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 16

candidate_caption: This animated scene from 'The Simpsons' movie depicts a bustling street view of Springfield, a quintessential American city setting. The composition balances various elements across a wide frame with a 1.78 aspect ratio, creating a deep depth of field that emphasizes the urban landscape extending into the distance. In the foreground on the right side, a large cartoonish burger character dominates the view. This exaggerated figure has a white face with a prominent red nose, oversized round eyes with white sclera and black pupils, and teal-colored hair styled in wild, wavy tufts framing its head like an elf-like hat. Its mouth is wide open in a cheerful grin, revealing sharp teeth set against a pink tongue and lips. The character's hands are wrapped in white gloves as it holds onto a massive bun adorned with small white sesame seeds scattered across its surface. A white band around the bottom displays the text 'KRUSTY BURGER' in bold, crimson red letters outlined in dark brown. The midground showcases a typical American main street lined with multi-story buildings painted in vibrant colors such as lavender purple, sky blue, mustard yellow, forest green, amber orange, and light gray. Each building features large windows, storefronts with awnings, and varied signage. Some buildings have distinctive details like air conditioning units, fire escape stairs, and utility vents. On both sides of the street, numerous yellow-skinned human characters dressed in casual attire can be seen engaging in various activities such as walking, standing, driving vehicles, or interacting near lampposts, parking meters, and bus stop signs. The road itself is marked with clear white lines dividing lanes, including two central yellow dashed lines running down the center. Various vehicles populate the scene, including an orange sedan parked on the left curb, a turquoise compact car moving away from the camera, a green pickup truck, a red sports car driven by Bart Simpson in his iconic yellow outfit (skirt and shoes), a police car with flashing lights, and other cars along the road. Streetlights line the sidewalks, casting shadows under daylight conditions, while pedestrians stand at crosswalks. In the background, more distant buildings extend further up the street, creating depth and perspective. The overall mood is lively and chaotic, capturing the essence of a busy day in this fictional North American town known for its quirky residents and offbeat humor. The lighting is bright and even, characteristic of daytime scenes in animated productions, highlighting the vividness of the colors and contributing to the high-contrast, saturated visual style of the series.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'KRUSTY BURGER'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the Krusty Burger text red?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is there a yellow road line in the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the police car at the top left corner of the image?'}
 {'answer': 'no', 'category': 'position', 'question': 'Is the red car in the top part of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the man standing on the sidewalk to the left of the Krusty Burger sign?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the Krusty Burger character smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the Krusty Burger sign large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than three cars in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a yellow man in the middle of the street?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the green car stopped at a crosswalk?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a street?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the road straight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'KRUSTY BURGER'?  
   - yes

3. Is the color of the Krusty Burger text red?  
   - yes

4. Is there a yellow road line in the image?  
   - yes

5. Is the police car at the top left corner of the image?  
   - n/a

6. Is the red car in the top part of the image?  
   - no

7. Is the man standing on the sidewalk to the left of the Krusty Burger sign?  
   - n/a

8. Is the Krusty Burger character smiling?  
   - yes

9. Is the Krusty Burger sign large?  
   - yes

10. Are there more than three cars in the image?  
    - yes

11. Is there a yellow man in the middle of the street?  
    - n/a

12. Is the green car stopped at a crosswalk?  
    - n/a

13. Does the image show a street?  
    - yes

14. Is the road straight?  
    - n/a

15. Is the image from a cartoon?  
    - yes

16. Is the image color graded with high saturation?  
    - yes

17. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 17  

Score = (12/17) × 100 = 70.59

score: 70.59

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 12 out of 17 questions were answered correctly, resulting in a score of 70.59%.

token_count: 512

caption_vocabulary_size: 329

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 18

candidate_caption: A landscape photograph capturing an ancient stone arch bridge spanning from the left to the right side of the frame during sunset, taken from a low angle to emphasize its grandeur. The weathered gray stonework of the bridge features multiple large arches supported by thick pillars, creating a rhythmic pattern that leads the eye diagonally across the composition. Ivy grows sporadically on some sections of the bridge's surface, adding touches of greenery to the historic structure. In the foreground, a rocky riverbed flows rapidly over moss-covered stones and boulders, creating white water cascades with smooth, blurred edges due to a long exposure technique. Small ripples and gentle currents add texture to the moving water, which appears almost ethereal in its silky appearance. A person stands near the center-right of the bridge, providing scale and emphasizing its impressive height. To the right, beyond the bridge, there are several buildings including a prominent church or cathedral with a tall bell tower featuring a dome-shaped roof topped by a cross, surrounded by smaller structures with red-tiled roofs. The background showcases layered mountain ranges covered in lush green forests, their peaks softly illuminated by the setting sun, casting gentle shadows and highlights. The sky above is filled with scattered clouds illuminated by the warm hues of the sunset, transitioning from deep orange and golden yellow near the horizon to soft blue higher up. This dramatic lighting enhances the serene yet majestic mood of the scene, highlighting textures in both natural elements and architectural details. The color palette includes slate gray, forest green, amber yellow, sky blue, charcoal black, and peach tones, all contributing to the tranquil atmosphere. The overall composition follows the rule of thirds, balancing the man-made marvel of the bridge against the raw beauty of nature, resulting in a visually striking and harmonious image that evokes a sense of timeless history and awe-inspiring scenery.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky in the image orange and blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the bridge grey?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the tower to the right of the bridge?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bridge large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the bridge arched?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there multiple arches on the bridge?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a river in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'no', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the sky in the image orange and blue?  
   - yes

2. Is the bridge grey?  
   - yes

3. Is the tower to the right of the bridge?  
   - yes

4. Is the bridge large?  
   - yes

5. Is the bridge arched?  
   - yes

6. Are there multiple arches on the bridge?  
   - yes

7. Is there a river in the image?  
   - yes

8. Does the image show outdoors?  
   - yes

9. Does the image have a warm color palette?  
   - yes

10. Is the image a photograph?  
    - yes

11. Is the image color graded with high saturation?  
    - n/a

12. Does the image have high contrast?  
    - n/a

13. Does the image have low brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 10 out of 13 questions were answered correctly, resulting in a score of approximately 76.92%.

token_count: 374

caption_vocabulary_size: 245

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 19

candidate_caption: A vintage-style illustration with a forest green (#556b2f) background featuring a distressed texture, creating a retro feel. The central focus is a large cream-colored moon face with exaggerated features, including closed eyes, thick eyebrows, a small curved nose, and slightly open mouth forming a cheerful smile. The moon's surface has subtle white and light gray textures representing continents and landmasses, giving it a smooth appearance with visible cracks and creases. Surrounding the moon are four stylized dark purple flowers with yellow centers, each featuring smiling faces. Two large flowers frame the sides of the moon, while two smaller ones appear at the bottom. Each flower has five petals arranged symmetrically around its circular center, with black leaves extending outward. Yellow lines radiate from behind the moon, adding depth to the composition. Bold text in retro font style is arranged around the central figure, reading "YOU DON'T LIVE ON EARTH" arched across the top, "ONE EARTH" below it with a golden yellow gradient and white highlights, followed by "ONE FAMILY" at the bottom centered, and "YOU ARE PASSING THROUGH" curved beneath it. The text uses a bold, curvy sans-serif font reminiscent of psychedelic art, with alternating colors of amber yellow and deep purple outlines. The overall mood is positive, whimsical, and uplifting, with high contrast between the vibrant elements and the muted background, evoking a sense of optimism and global unity through its nostalgic aesthetic.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the text 'ONE EARTH' appear in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color green?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color mainly orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the central face in the middle of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'ONE EARTH' at the top of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'ONE FAMILY' below the face?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'You don't live on Earth' above the text 'ONE EARTH'?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the face in the image smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the Earth face large in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there six flowers in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there Earth in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the text around the face?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an illustration?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a vintage color grading?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the text 'ONE EARTH' appear in the image?  
   - yes

3. Is the background color green?  
   - yes

4. Is the text color mainly orange?  
   - no

5. Is the central face in the middle of the image?  
   - yes

6. Is the text 'ONE EARTH' at the top of the image?  
   - no

7. Is the text 'ONE FAMILY' below the face?  
   - yes

8. Is the text 'You don't live on Earth' above the text 'ONE EARTH'?  
   - yes

9. Is the face in the image smiling?  
   - yes

10. Is the Earth face large in the image?  
    - yes

11. Are there six flowers in the image?  
    - no

12. Is there Earth in the image?  
    - yes

13. Is the text around the face?  
    - yes

14. Does the image have a warm color palette?  
    - no

15. Is the image an illustration?  
    - yes

16. Does the image have a vintage color grading?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 16  

Score = (12/16) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of correct answers out of the total questions. In this case, 12 out of 16 questions were answered correctly, resulting in a score of 75%.

token_count: 296

caption_vocabulary_size: 190

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 22

candidate_caption: A close-up anime-style illustration depicts a young girl with shoulder-length straight light brown hair, styled in soft waves cascading over her face from multiple angles, creating depth and texture. She has large, expressive dark grayish-brown eyes with prominent white highlights in the pupils and black irises, giving them an intense sparkle that reflect light. Her eyebrows are slightly furrowed, conveying concern or sadness. A small drop of sweat is visible on her lower lip, emphasizing her distressed state. The lighting is dramatic and moody, coming from the left side of the frame, casting strong shadows across her face and body, particularly on the right side while leaving the left illuminated. This creates a striking two-toned effect that accentuates her contemplative expression. The girl's mouth is slightly open, revealing a hint of teeth and tongue, adding to the overall sense of unease. She wears a cream-colored hoodie with subtle shading lines indicating folds, paired with a striped scarf featuring alternating diagonal stripes in muted pink and beige tones wrapped tightly around her neck. To her left, partially visible, is a dark olive green backpack with visible straps, buckles, and loops, resting on what appears to be another seat. Another blurred figure can be seen sitting beside it. The background consists of indistinct shapes suggesting a public space like a bus or train interior, with hints of blue-gray plastic seats reflecting light. On the far left, there's a glimpse of a reflective metallic surface, possibly part of an airplane window. The color palette includes warm beige (#e4c8a1), deep charcoal (#343435), muted lavender (#7f6b72), steel blue (#7082a0), terracotta (#ae7465), and slate gray (#5d6773). The shallow depth of field keeps the focus squarely on the character's emotional display while maintaining a dreamy, atmospheric quality reminiscent of Japanese animation styles.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the girl's hair brown?"}
 {'answer': 'no', 'category': 'position', 'question': "Is the girl's face in the center of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bag to the left of the girl?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the girl looking sad?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the girl large relative to the overall image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the bag rectangular?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a girl in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the girl seated?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have warm tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an animation?'}]

openai_answers: 1. **Is the girl's hair brown?**  
   - yes

2. **Is the girl's face in the center of the image?**  
   - n/a

3. **Is the bag to the left of the girl?**  
   - yes

4. **Is the girl looking sad?**  
   - yes

5. **Is the background blurred?**  
   - yes

6. **Is the girl large relative to the overall image?**  
   - n/a

7. **Is the bag rectangular?**  
   - n/a

8. **Is there a girl in the image?**  
   - yes

9. **Is the girl seated?**  
   - n/a

10. **Does the image have warm tones?**  
    - yes

11. **Is the image an animation?**  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 11  

Score = (8/11) × 100 ≈ 72.73

score: 72.73

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. There are 8 'yes' answers out of 11 questions, resulting in a score of approximately 72.73%.

token_count: 386

caption_vocabulary_size: 258

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 26

candidate_caption: A stunning night-time landscape photograph featuring a prominent lighthouse as the central focus, taken from a low angle looking up along a wooden boardwalk leading towards it. The boardwalk, made of weathered light brown wood with visible grain patterns and horizontal metal rails along its edges, starts in the foreground and curves slightly to the right before straightening out towards the middle ground. It is surrounded by tall grasses and reeds on both sides, their blades illuminated softly by ambient moonlight, adding texture and depth to the scene. In the midground, a tall cylindrical lighthouse stands vertically, its classic black-and-white alternating rings creating a striking contrast against the dark background. Atop this structure, an intense beam of light emanates outward from the topmost section of the tower, casting a warm golden glow that illuminates parts of the surrounding vegetation. Near the base of the lighthouse, several trees are silhouetted against the starry sky, including slender evergreens with dark green foliage transitioning into lighter shades at the tips. To the right of the lighthouse, a small white building with bright windows can be seen partially obscured by trees. The background showcases a breathtakingly clear, deep blue night sky speckled with countless stars of varying brightness and colors. Dominating the left side of the frame is the Milky Way galaxy, depicted as a dense band of stars stretching diagonally across the upper part of the image, with its core richly populated with stars and interspersed with darker dust clouds. This celestial feature glows in shades of midnight blue (#262c2e), pale grayish-brown (#a49d9c), and warm taupe (#826b5f). The overall color palette includes deep navy (#1c2128), cool slate gray (#6a7273), muted sage (#84856f), soft periwinkle (#9494ae), and muted khaki (#7b7969), contributing to the tranquil yet awe-inspiring mood of the scene. The composition follows the rule of thirds, drawing attention to both the Milky Way's majestic presence and the lighthouse's focal role as natural beacons.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky dark?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the lighthouse in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the lighthouse above the path?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the lighthouse tall?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the lighthouse cylindrical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one lighthouse?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a lighthouse in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the lighthouse emitting light?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show night?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette have dark tones?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sky dark?  
   - yes

2. Is the lighthouse in the center of the image?  
   - yes

3. Is the lighthouse above the path?  
   - yes

4. Is the image sharp?  
   - n/a

5. Is the lighthouse tall?  
   - yes

6. Is the lighthouse cylindrical?  
   - yes

7. Is there one lighthouse?  
   - yes

8. Is there a lighthouse in the image?  
   - yes

9. Is the lighthouse emitting light?  
   - yes

10. Does the image show night?  
    - yes

11. Does the image's color palette have dark tones?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have low brightness?  
    - n/a

14. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 14  

Score = (11/14) × 100 = 78.57

score: 78.57

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, out of the total number of questions. There are 11 'yes' answers out of 14 questions, resulting in a score of 78.57%.

token_count: 432

caption_vocabulary_size: 276

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 27

candidate_caption: A promotional poster for the Amazon original movie 'Being The Ricardos' featuring actor Clark Gregg as Howard Wrenke. The close-up portrait shows his face from a front angle, slightly turned to the left, with short light brown hair neatly styled back and black-framed rectangular glasses accentuating his blue eyes. He has a gentle smile and is looking off-camera to the right. His attire includes a gray suit jacket over a white shirt and a gray bow tie adorned with small square geometric patterns in darker shades of gray, creating an elegant look against the smooth teal background (#008080). The lighting is soft and even, highlighting his facial features without harsh shadows, emphasizing the natural texture of his skin including pores and subtle wrinkles around the mouth and cheeks. At the top center, 'AMAZON ORIGINAL MOVIE' is displayed in bold white sans-serif font. To the right of his head, 'Clark GREGG is Howard WENKE' appears in white italic serif text, while below it, 'Being The Ricardos' is written in elegant white cursive script. At the bottom right, 'WRITTEN AND DIRECTED BY Aaron SORKIN' is shown in white uppercase letters, withAaron spelled out in a unique italicized style. Additional information reads 'IN SELECT THEATERS DEC 10' and 'DEC 21 prime video', both in white uppercase sans-serif font. In the lower-left corner, an R-rated logo is visible. The overall mood of the poster is professional yet approachable, with balanced gamma, medium contrast, and natural saturation levels, focusing attention on the subject's thoughtful expression and formal attire.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Amazon Original Movie'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the face in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'Being the Ricardos' to the right of the person's face?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking smiling?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the name 'Clark Gregg' mentioned?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the face in the image large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the bow tie around the person's neck square patterned?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'prime video' positioned towards the bottom of the image?"}
 {'answer': 'yes', 'category': 'relation', 'question': "Is 'Clark Gregg is' above 'Howard Wenke' in the text?"}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'text', 'question': 'Is the movie written and directed by Aaron Sorkin?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a movie poster?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'Amazon Original Movie'?  
   - yes

3. Is the background color light blue?  
   - no

4. Is the face in the center of the image?  
   - n/a

5. Is the text 'Being the Ricardos' to the right of the person's face?  
   - no

6. Is the person looking smiling?  
   - yes

7. Is the name 'Clark Gregg' mentioned?  
   - yes

8. Is the face in the image large?  
   - n/a

9. Is the bow tie around the person's neck square patterned?  
   - yes

10. Is there only one person in the image?  
    - yes

11. Is the text 'prime video' positioned towards the bottom of the image?  
    - yes

12. Is 'Clark Gregg is' above 'Howard Wenke' in the text?  
    - no

13. Does the image have a cool color palette?  
    - yes

14. Is the movie written and directed by Aaron Sorkin?  
    - yes

15. Is the image a movie poster?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 15  

Score = (11/15) × 100 = 73.33

score: 73.33

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 11 out of 15 questions were answered correctly, resulting in a score of 73.33%.

token_count: 332

caption_vocabulary_size: 216

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 31

candidate_caption: A close-up photograph of a beautifully plated dish featuring a large piece of pan-fried fish, likely salmon or trout, placed diagonally on an oval white plate with a delicate cracked texture pattern in beige and light brown hues. The fish has a golden-brown crust with visible grill marks, giving it an appetizing appearance. It's garnished with finely chopped fresh green chives, scattered capers, caramelized onion slices, diced tomato pieces, and a creamy yellow sauce that pools around its base. A wooden-handled metal serving spatula is positioned horizontally at the left edge of the plate, partially submerged in the sauce. The plate rests on a clean white tablecloth, with indistinct background elements such as wine glasses and utensils slightly out of focus, suggesting a fine dining setting. Natural lighting illuminates the scene from above and slightly to the right, highlighting the textures and colors of the food while creating soft shadows. This creates an inviting atmosphere typical of a gourmet restaurant, emphasizing the freshness and gourmet presentation of this enticing seafood dish.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sauce yellow in color?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the fork on the left side of the plate?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the fork to the left of the fish?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the fish large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the plate round?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there a single fish in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a fork in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the fish on the plate?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a close-up shot?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a natural color grading?'}]

openai_answers: 1. Is the sauce yellow in color?  
   - yes

2. Is the fork on the left side of the plate?  
   - n/a

3. Is the fork to the left of the fish?  
   - n/a

4. Is the background blurred?  
   - yes

5. Is the fish large?  
   - yes

6. Is the plate round?  
   - no

7. Is there a single fish in the image?  
   - yes

8. Is there a fork in the image?  
   - no

9. Is the fish on the plate?  
   - yes

10. Is the image a photograph?  
    - yes

11. Is the image a close-up shot?  
    - yes

12. Does the image have a natural color grading?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 12  

Score = (9/12) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 12 questions were answered correctly, resulting in a score of 75%.

token_count: 210

caption_vocabulary_size: 152

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 32

candidate_caption: A landscape photograph capturing a serene yet dynamic scene of Mount Fuji set against a vibrant sunset sky over the ocean near its base in Japan, specifically Izu Oshima Island. The foreground features two large, rugged rock formations emerging from turbulent deep blue-green waters with white frothy waves crashing against their bases. These weathered rocks are textured and jagged, creating a stark contrast with the swirling sea below. A thin rope or chain extends from the left rock to the right one, adding an interesting human element to the natural setting. The midground showcases choppy seas with gentle ripples and small waves, while the background is dominated by Mount Fuji itself. Its iconic conical shape rises sharply from the horizon, its dark gray slopes contrasting beautifully with the warm hues of the sky above. White snow patches adorn its peak, highlighting its steep contours. A thick blanket of mist or low-hanging clouds partially obscures the lower part of the mountain, enhancing its majestic presence. Several smaller islands or rocky outcrops are visible on the horizon to the right, appearing as dark silhouettes against the lighter atmosphere. The sky transitions from a soft peach at the top through golden yellow near the horizon to deeper shades of orange, blending into light purple and lavender tones. Scattered clouds add texture and depth to the expansive view. The overall mood is tranquil yet awe-inspiring, enhanced by the natural lighting of the setting sun that bathes the entire scene in a balanced palette of cool blues, warm oranges, and grays, creating high luminance and moderate saturation.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky color orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the mountain one the right of the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the rocks in the foreground?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the mountain in the image called Mount Fuji?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the mountain large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the mountain triangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two large rocks in the sea?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a mountain in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the sea in front of the mountain?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sky color orange?  
   - yes

2. Is the mountain one the right of the center of the image?  
   - n/a

3. Are the rocks in the foreground?  
   - yes

4. Is the mountain in the image called Mount Fuji?  
   - yes

5. Is the mountain large?  
   - yes

6. Is the mountain triangular?  
   - yes

7. Are there two large rocks in the sea?  
   - yes

8. Is there a mountain in the image?  
   - yes

9. Is the sea in front of the mountain?  
   - yes

10. Does the image show outdoors?  
    - yes

11. Does the image have a warm color palette?  
    - yes

12. Is the image a photograph?  
    - yes

13. Is the image color graded with high saturation?  
    - no

14. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 14  

Score = (11/14) × 100 = 78.57

score: 78.57

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 14 questions were answered correctly, resulting in a score of 78.57%.

token_count: 311

caption_vocabulary_size: 209

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 35

candidate_caption: A scene from the animated series 'Scooby-Doo' featuring five main characters standing in front of double metal security doors labeled 'DOUBLE MAXIMUM SECURITY'. The group consists of Velma Dinkley, Shaggy Rogers, Daphne Blake, Fred Jones, and Scooby-Doo. Velma wears an orange sweater with pleats at the bottom, red skirt, maroon tights, and orange socks with brown Mary Jane shoes, along with rectangular glasses. She stands next to Scooby-Doo, who is dressed as a jack-o'-lantern wearing an orange shirt with triangular eyes and a jagged mouth carved into it, green hat with a feather, brown pants, black shoes, and a watch on his left wrist. Shaggy has brown hair and wears a pumpkin costume over his regular outfit, including a tall, pointed beige hat resembling a witch's hat. Daphne sports a purple dress with a green scarf, headband, matching leggings, purple shoes, and her signature long red wavy hair tied back with a blue bandana. Fred is dressed in a white long-sleeve shirt with a bright orange scarf around his neck, blue jeans, and brown shoes, with blonde hair. They all appear ready for adventure, with varied expressions ranging from neutral to slightly concerned. The background shows light gray stone walls with darker outlines and small rectangular blocks visible, giving a cave-like feel. Above the entrance are large metallic double doors with bolts and rivets, dark gray in color (#1c3b53). To the right of the door frame, there's a small control panel with two buttons - one red and one green, accompanied by a circular camera lens. The sign above reads 'DOUBLE MAXIMUM SECURITY' in bold, uppercase white letters against a vibrant crimson red background. The lighting is even and soft throughout the scene, creating a balanced exposure typical of 2D animation style, which gives the illustration a clean, cartoonish appearance while maintaining high saturation and moderate contrast.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the text say 'DOUBLE MAXIMUM SECURITY'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is there any orange color in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the wall color primarily light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the door in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the man with the white shirt on the left side?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the man in a pumpkin costume to the left of the door?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the character in green scarf to the left of the character in white shirt?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Are the characters looking serious?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the door large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the pumpkin costume round?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there five characters in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a dog in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the text above the door?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the dog character's name Scooby-Doo?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is there text in the image?  
   - yes

2. Does the text say 'DOUBLE MAXIMUM SECURITY'?  
   - yes

3. Is there any orange color in the image?  
   - yes

4. Is the wall color primarily light blue?  
   - no

5. Is the door in the center of the image?  
   - n/a

6. Is the man with the white shirt on the left side?  
   - no

7. Is the man in a pumpkin costume to the left of the door?  
   - n/a

8. Is the character in green scarf to the left of the character in white shirt?  
   - no

9. Are the characters looking serious?  
   - no

10. Is the door large?  
    - yes

11. Is the pumpkin costume round?  
    - n/a

12. Are there five characters in the image?  
    - yes

13. Is there a dog in the image?  
    - yes

14. Is the text above the door?  
    - yes

15. Is the dog character's name Scooby-Doo?  
    - yes

16. Is the image from a cartoon?  
    - yes

17. Does the image have high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 17  

Score = (12/17) × 100 = 70.59

score: 70.59

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 12 correct answers out of 17 questions, resulting in a score of 70.59%.

token_count: 406

caption_vocabulary_size: 245

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 41

candidate_caption: An intense moment from an ice hockey game captured in a dynamic action shot. The focal point is Thomas Bate, wearing jersey number 21 with 'Thomas Bate' written in cursive script on his back, in black with red and gray accents. He has a navy blue helmet with white text reading 'Rebel at heart'. His posture suggests he's either skating or pushing forward while holding a blue and black hockey stick with both hands. In the midground, player number 14 stands over Bate, wearing a similar black uniform with team logo and red stripes along the sleeves and pants. Player number 20 lies on the ice beneath them, dressed in a white jersey with red accents, including a bold 'STELTON' patch across the chest. This player wears a vibrant red helmet labeled 'STEELTON' and has fallen face-first towards the bottom right corner of the frame. Both players wear black helmets with clear visors and protective gear, including gloves and pants branded with 'Bauer'. The scene is well-lit by bright artificial indoor arena lighting, highlighting the players against the stark white ice surface marked with faint blue lines indicating the playing area. The overall mood is energetic and competitive, capturing the raw intensity typical of professional sports photography.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the ice color white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the helmet of the player on the left black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the fallen player on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the player in the white jersey on the ground?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have artifacts?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the player's helmet round?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three players in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a hockey stick in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is one player standing over another player?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an ice hockey game?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette include black and white tones?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Is the ice color white?  
   - yes

3. Is the color of the helmet of the player on the left black?  
   - n/a

4. Is the fallen player on the right side of the image?  
   - yes

5. Is the player in the white jersey on the ground?  
   - yes

6. Does the image have artifacts?  
   - n/a

7. Is the player's helmet round?  
   - n/a

8. Are there three players in the image?  
   - yes

9. Is there a hockey stick in the image?  
   - yes

10. Is one player standing over another player?  
    - yes

11. Does the image show an ice hockey game?  
    - yes

12. Does the image's color palette include black and white tones?  
    - yes

13. Is the image a photograph?  
    - n/a

14. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. In this case, 10 out of 14 questions were answered with 'yes', resulting in a score of 71.43%.

token_count: 253

caption_vocabulary_size: 160

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 42

candidate_caption: A modern, minimalist Hanukkah invitation card features a vibrant sky blue background (RGB(135, 206, 235)) with a subtle texture resembling paper grain. The design centers around large, bold white text that reads 'LIGHTS LATKES AND Libations' in various fonts. 'LIGHTS' and 'LATKES' are displayed using a classic serif font similar to Arial or Helvetica, while 'Libations' employs an elegant cursive script reminiscent of calligraphy. Above this main text are six stylized candles with golden flame illustrations at their tops, each featuring a light blue base representing the wick. The candles are evenly spaced horizontally across the top of the card, adding a festive touch. Below the main text, there's a smaller line of text in white serif font that says 'PLEASE JOIN US AS WE LIGHT THE CANDLES ON THE FIRST NIGHT OF HANUKKAH FIVE O'CLOCK IN THE EVENING • THE MAYER RESIDENCE'. Three small circular symbols separate each word in this section. The overall composition is clean and centered, with high contrast between the crisp white text and the soft blue background, creating a celebratory mood suitable for a holiday gathering. The flat lighting and lack of shadows emphasize the two-dimensional nature of the design, focusing attention on the typography and candle graphics.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'LIGHTS LATKES'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color light blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color white?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the phrase 'LIGHTS LATKES' in the upper half of the image?"}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'HANUKKAH' in the lower half of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the phrase 'HANUKKAH' below the phrase 'please join us'?"}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the text 'Libations' large?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there flame icons?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there eight flames in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there any icon of candles or flames in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the text in the bottom aligned center?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an invitation?'}]

openai_answers: 1. **Answer Each Question:**

   - Is there any text in the image?  
     - yes

   - Does the image contain the text 'LIGHTS LATKES'?  
     - yes

   - Is the background color light blue?  
     - yes

   - Is the text color white?  
     - yes

   - Is the phrase 'LIGHTS LATKES' in the upper half of the image?  
     - yes

   - Is the text 'HANUKKAH' in the lower half of the image?  
     - yes

   - Is the phrase 'HANUKKAH' below the phrase 'please join us'?  
     - no

   - Is the text 'Libations' large?  
     - n/a

   - Are there flame icons?  
     - yes

   - Are there eight flames in the image?  
     - no

   - Is there any icon of candles or flames in the image?  
     - yes

   - Is the text in the bottom aligned center?  
     - yes

   - Is the image an invitation?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 10
   - Total Number of Questions: 13

   Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of correct answers out of the total questions. With 10 correct answers out of 13 questions, the score is approximately 76.92%.

token_count: 269

caption_vocabulary_size: 186

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 44

candidate_caption: The scene depicts an intense conversation between two characters in a high-tech industrial setting, reminiscent of a secret laboratory or server room. The foreground features the back view of a man with short blonde hair, wearing a black suit jacket over a white shirt collar, seated facing another character on the right side of the frame. This individual has their head slightly turned to the left, showing only the left profile of his face. He appears relaxed yet attentive, leaning back in his dark metal chair with thin legs. The midground showcases a man with shoulder-length blond hair styled backward, smiling confidently while reclining in a black plastic chair. He's dressed in a beige blazer with notched lapels over a brown vest and patterned shirt featuring diamond-shaped designs in gold, amber yellow, and brown. His hands are clasped together on his lap, emphasizing his composed demeanor. The background reveals rows of intricate machinery filled with cables, wires, and metallic structures, creating a maze-like appearance with red lights interspersed throughout. Multiple workstations equipped with open laptops displaying complex data streams, graphs, and coding information add depth to the scene. A large, closed door centrally positioned at the far end serves as a focal point amidst the technical environment. The floor is concrete, reflecting light softly from above. The lighting is soft and diffused, coming from above and slightly behind the camera, casting gentle shadows that enhance the textures of the clothing and surroundings. The overall color palette consists of muted tones like beige, dark gray, black, and touches of amber yellow, contributing to the serious mood of the scene. The composition balances both characters and the surrounding technological elements, creating a sense of intrigue and tension typical of a tense interrogation setup or high-stakes negotiation within a futuristic context.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is the text displayed on computer screens?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the jacket of the person on the right beige?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the floor color light grey?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person sitting on a chair to the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person sitting with their back facing the camera?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in the beige jacket in front of the person with their back facing the camera?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person in the beige jacket smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the room large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a computer in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person in the beige jacket facing the person with their back to the camera?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a still from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the text displayed on computer screens?  
   - yes

2. Is the jacket of the person on the right beige?  
   - yes

3. Is the floor color light grey?  
   - n/a

4. Is there a person sitting on a chair to the left side of the image?  
   - yes

5. Is there a person sitting with their back facing the camera?  
   - yes

6. Is the person in the beige jacket in front of the person with their back facing the camera?  
   - no

7. Is the person in the beige jacket smiling?  
   - yes

8. Is the room large?  
   - n/a

9. Are there two people in the image?  
   - yes

10. Is there a computer in the image?  
    - yes

11. Is the person in the beige jacket facing the person with their back to the camera?  
    - yes

12. Does the image show indoors?  
    - yes

13. Does the image have a warm color palette?  
    - yes

14. Is the image a still from a film?  
    - n/a

15. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 15  

Score = (11/15) × 100 = 73.33

score: 73.33

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 11 out of 15 questions were answered correctly, resulting in a score of 73.33%.

token_count: 353

caption_vocabulary_size: 224

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 56

candidate_caption: A cinematic scene set in a Parisian subway station at night, featuring actor Keanu Reeves in profile view on the right side of the frame. He has shoulder-length dark hair and a well-groomed beard with a mix of light stubble, appearing contemplative as he faces left. Wearing a black suit jacket over a black shirt with a visible collar and tie, his expression is serious and thoughtful. The lighting is soft and artificial, casting gentle shadows on his face while highlighting its contours. To the left, a modern teal-colored subway train is stationed on the tracks, its windows illuminated from within, revealing warm yellowish lights inside. The platform's reflective floor shows alternating rectangular tiles in dark green and brown hues, creating a glossy appearance that reflects the overhead lights and colors from surrounding elements. The background includes the curved tiled ceiling of the underground station, adorned with rows of evenly spaced circular lights arranged diagonally, creating a rhythmic pattern that adds depth to the composition. The walls are covered with various posters, graffiti, and advertisements taped to white tiles, contributing to an urban atmosphere. A partially visible figure in a beige coat can be seen walking away from the camera towards the center-left of the frame. The overall color palette consists of muted tones like forest green, midnight blue, charcoal gray, pale yellow, and off-white, with low saturation and luminance, enhancing the somber mood. The wide-angle shot emphasizes the depth and dimensionality of the setting, typical of film stills from the 2020s era, capturing the essence of urban nightlife and introspection in this unique Parisian environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there text on the wall in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's clothing black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the train to the left of the person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the train blurry?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a train in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}]

openai_answers: 1. Is there text on the wall in the image?  
   - Answer: yes

2. Is the person's clothing black?  
   - Answer: yes

3. Is the person on the right side of the image?  
   - Answer: yes

4. Is the train to the left of the person?  
   - Answer: yes

5. Is the person looking serious?  
   - Answer: yes

6. Is the train blurry?  
   - Answer: n/a

7. Is there one person in the image?  
   - Answer: no

8. Is there a train in the image?  
   - Answer: yes

9. Is the image a shot from a film?  
   - Answer: yes

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 9  

Score = (7/9) × 100 = 77.78

score: 77.78

reasons: The score is calculated based on the number of correct answers out of the total number of questions. There were 7 correct answers out of 9 questions, resulting in a score of 77.78%.

token_count: 325

caption_vocabulary_size: 210

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 60

candidate_caption: A dynamic photograph captures a sleek, metallic gunmetal gray sports car (likely a Lamborghini Murcielago) in motion within a modern tunnel. The car is positioned slightly to the right of center, moving away from the camera at an angle towards the left side of the frame. It features a large black rear wing with sharp edges and multiple horizontal slats, glossy surfaces reflecting the surrounding lights, and two prominent red circular tail lights illuminated. The vehicle's design showcases sharp lines, aerodynamic curves, and a low-slung profile. A license plate reading 'PET BULLS' is visible at the back, while dual chrome exhaust pipes are prominently displayed beneath the rear bumper. The smooth concrete floor of the tunnel shows subtle vertical grooves running parallel along its length, creating a blurred effect due to high speed. Bright rectangular fluorescent lights are evenly spaced along the ceiling, casting reflections on the car's polished surface and creating a striking contrast against the dark surroundings. The tunnel walls are white with subtle vertical ridges, curving gently as they recede into the distance, emphasizing the sense of speed and depth. This curved structure creates a visually appealing perspective, drawing attention inward. In the background, additional light fixtures can be seen further down the tunnel. The overall mood is intense and energetic, enhanced by the high-contrast lighting and the car's aggressive stance. The color palette includes shades of charcoal gray (#2d2b2c), cool blue-gray (#8e9ca6), muted slate (#7a848c), steel blue (#7084aa), pewter (#9895a3), and warm beige (#aeaba0). The composition effectively conveys a powerful sense of speed, movement, and performance, capturing the essence of automotive engineering in an industrial setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the text say 'PET BULL' on the license plate?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the car black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the interior of the tunnel white and black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the car in the center of the image?'}
 {'answer': 'no', 'category': 'position', 'question': 'Is the car on the right side of the road?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the bright lights on the ceiling above the car?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the tunnel curving?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the car Lamborghini?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the car large?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a car in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the car driving inside a tunnel?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the text say 'PET BULL' on the license plate?  
   - no

2. Is the color of the car black?  
   - no

3. Is the interior of the tunnel white and black?  
   - n/a

4. Is the car in the center of the image?  
   - no

5. Is the car on the right side of the road?  
   - n/a

6. Are the bright lights on the ceiling above the car?  
   - yes

7. Is the tunnel curving?  
   - yes

8. Is the car Lamborghini?  
   - yes

9. Is the car large?  
   - n/a

10. Is there a car in the image?  
    - yes

11. Is the car driving inside a tunnel?  
    - yes

12. Does the image have a cool color palette?  
    - yes

13. Is the image a photograph?  
    - yes

14. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 10 out of 14 questions were answered correctly, resulting in a score of 71.43%.

token_count: 357

caption_vocabulary_size: 241

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 61

candidate_caption: Three individuals are interacting warmly in an indoor swimming pool filled with clear, aqua-green water. The man, positioned slightly to the right of center, has short dark hair and a trimmed beard. He's partially submerged up to his chest, supporting a young child who is riding on his back. The child, blonde and curly, wears a vibrant royal blue swimsuit jacket with yellow text 'NO' visible on the upper front, along with matching shorts. Both have expressive faces; the man looks upwards with a slight smile, while the child appears curious as he gazes forward with mouth open, revealing teeth. To the left of the man stands a woman with her back to the camera, wearing a glossy black one-piece swimsuit with thin straps and rounded scoop neckline. Her long, dark brown hair is tied back in a high ponytail, and she smiles broadly while looking at him. She accessorizes with small diamond-shaped stud earrings, a delicate gold necklace with the word "te amo" (which translates from Spanish to English as "I love you") written in cursive script, and a wedding ring on her left hand. Her right arm rests gently on the man's shoulder, providing support. The playful atmosphere is enhanced by colorful pool toys visible in the background, including green and yellow objects, alongside some floating items such as a green caddy and yellow balloons. The setting includes a patterned floor with tiles and rectangular panels painted in various shades of beige and light brown, creating depth. Natural or artificial lighting illuminates the scene evenly, casting soft shadows and highlighting the subjects against the blurred background, which also features a wall with three evenly spaced rectangular cavities. The water's surface creates gentle ripples around them, adding texture to the image. The overall mood is joyful and familial, capturing a candid moment of connection between the three individuals during what seems to be a swim lesson or recreational activity.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the color of the woman's swimming suit black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the man on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the woman to the left of the man?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the child on top of the man's shoulders?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the woman smiling?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the child looking curious?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the person in the image Michael Phelps?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a child in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a bright color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the color of the woman's swimming suit black?  
   - yes

2. Is the man on the right side of the image?  
   - yes

3. Is the woman to the left of the man?  
   - yes

4. Is the child on top of the man's shoulders?  
   - yes

5. Is the woman smiling?  
   - yes

6. Is the child looking curious?  
   - yes

7. Is the person in the image Michael Phelps?  
   - n/a

8. Are there three people in the image?  
   - yes

9. Is there a child in the image?  
   - yes

10. Does the image show indoors?  
    - yes

11. Does the image have a bright color palette?  
    - yes

12. Is the image a photograph?  
    - n/a

13. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 10 out of 13 questions were answered correctly, resulting in a score of approximately 76.92%.

token_count: 382

caption_vocabulary_size: 242

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 65

candidate_caption: An aerial photograph captures a vibrant modern urban landscape in North Korea, showcasing a diverse array of high-rise buildings against a hazy sky. The central focus is on a unique, futuristic building to the left, characterized by its distinctive curvilinear design with alternating horizontal layers of light steel blue (#87a7b9) and white balconies creating an illusion of movement and fluidity. This structure features a spherical golden object perched atop its pinnacle, resembling a satellite or globe, surrounded by intricate metal structures resembling antennas or cables. To its right stand two prominent red-orange high-rise towers with white trimmings, featuring circular designs at their tops and vertical lines running down their facades. Each tower has multiple sections separated by glass panels and decorative elements, including gold-colored symbols near the center. Adjacent to these are several other tall buildings painted in shades of terracotta (#bb726d), off-white (#f0e3dd), and slate gray (#727c85), adding variety to the skyline. On the far right, there's a striking circular building with a flat roof, composed of concentric rings of glass and white structural elements, including large windows arranged symmetrically along its facade. In the foreground, well-maintained roads with clear lane markings curve around the base of the skyscrapers, leading towards the heart of the city. A wide multi-lane road runs horizontally across the bottom, bordered by grassy areas and lush green trees lining both sides of the riverbank. Below this, a series of sports courts can be seen, including a tennis court with teal markings. The background reveals a densely packed cityscape extending into the distance, blending into the misty atmosphere with various heights of buildings fading into a soft haze due to atmospheric conditions. The overall color palette includes sky blue (#87a7b9), terracotta (#bb726d), light steel blue (#84abb4), slate gray (#727c85), white (#f0e3dd), and charcoal gray (#48494a), contributing to a balanced exposure that highlights architectural details without harsh shadows. The scene evokes a sense of modern development and growth in a bustling metropolitan area, while maintaining a calm ambiance under natural daylight conditions.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the left a building blue and white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the orange and white buildings on the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the orange buildings to the right of the blue building?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the blue building tall?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the primary road in the image straight?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there tennis courts in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the left a building blue and white?  
     - yes

   - Are the orange and white buildings on the center of the image?  
     - yes

   - Are the orange buildings to the right of the blue building?  
     - yes

   - Is the blue building tall?  
     - n/a

   - Is the primary road in the image straight?  
     - no

   - Are there tennis courts in the image?  
     - yes

   - Does the image show daylight?  
     - yes

   - Is the image a photograph?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 6
   - Total Number of Questions: 8

   Score = (6/8) × 100 = 75

score: 75.0

reasons: The score was calculated based on the number of correct answers out of the total questions. There were 6 correct answers out of 8 questions, resulting in a score of 75%.

token_count: 448

caption_vocabulary_size: 285

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 66

candidate_caption: A close-up portrait of a young woman with long, wavy brown hair flowing over her shoulders in an outdoor setting during golden hour. She has striking light blue eyes that are intensely gazing directly at the camera, surrounded by thick, dark eyebrows. Her expression is contemplative and slightly pensive as she looks directly into the lens. The lighting is natural and warm, coming from behind the subject, creating a soft halo effect around her head and casting gentle shadows on her face. This backlighting highlights her facial features, particularly her eyes, which have an almost ethereal quality due to the reflections. Her skin tone appears warm and sun-kissed, with subtle freckles visible on her nose and cheeks. A small mole or beauty mark is noticeable near her left eye. Her lips are slightly parted, revealing a hint of teeth, adding to the thoughtful mood. The woman's right hand is raised near her mouth, with fingers gently touching her lips, showcasing well-manicured nails painted in white polish. She wears two thin black bracelets on her wrist - one composed of several loops stacked together and another simpler bracelet - along with a delicate necklace featuring a teardrop-shaped pendant made of white shell material set against a black background. The background consists of blurred greenery, including bushes and trees, suggesting a field or garden setting. The sky above is clear and pale yellowish-beige, transitioning to light blue higher up, indicating late afternoon sunlight. The overall color palette includes warm tones like sandy beige (#e2c29f), deep umber (#4b3621), rich sienna (#a36d3c), muted khaki (#84755b), earthy taupe (#6e6347), and sage green (#8ba5ac), contributing to a serene atmosphere. The composition centers the woman's face against this softly lit backdrop, emphasizing the intimate feel of the photograph. The shallow depth of field keeps the focus on her expressive gaze while maintaining a dreamlike quality in the surroundings.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky color light yellow?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the woman in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there a tree to the right of the person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking attentive?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person occupying a large portion of the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the person's necklace in a shape of tear?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a warm color grading?'}]

openai_answers: 1. Is the sky color light yellow?  
   - yes

2. Is the woman in the center of the image?  
   - yes

3. Is there a tree to the right of the person?  
   - n/a

4. Is the person looking attentive?  
   - yes

5. Is the background blurred?  
   - yes

6. Is the person occupying a large portion of the image?  
   - n/a

7. Is the person's necklace in a shape of tear?  
   - yes

8. Is there one person in the image?  
   - yes

9. Does the image show daylight?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a photograph?  
    - yes

12. Is the image color graded with high saturation?  
    - n/a

13. Does the image have a warm color grading?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. The 'n/a' responses are not counted as correct answers. The formula used is: (Number of Correct Answers / Total Number of Questions) × 100.

token_count: 404

caption_vocabulary_size: 271

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 69

candidate_caption: A close-up shot of a black Sony smartphone held by a hand with light skin tone, gripping it from the left side at the base. The phone's screen displays text in white against a dark blue background (#1e2f3b) with a subtle grid pattern and lighter dots creating a dotted texture. At the top center of the screen, there are five small white circular icons arranged horizontally, representing signal strength. Below this, large white sans-serif numbers '19:55' indicate the time in a digital clock style. Underneath, centered on the screen, is a larger text box with rounded corners containing 'Unknown Number' in sky blue (#5caed0), followed by bold white letters reading 'EWA FLIGHT 226' within a darker blue rectangular border, and '9pm' beneath it. The bottom right corner of the screen features a partial icon of a speaker symbol. The brand name 'SONY' is visible above the display in uppercase white letters. The hand holding the phone has a natural skin tone with visible textures and creases, emphasizing its realistic appearance. The background is blurred with indistinct shapes and colors, suggesting an indoor setting like an office or airplane cabin at night, possibly over North America or China. The lighting appears to be artificial and low-key, creating soft shadows that highlight the details of both the hand and the phone while maintaining focus on the device itself. The overall color palette includes deep navy blues, charcoal blacks, off-whites (#d7d4cc), slate grays (#a8adac), and muted browns (#73625c), contributing to a high-contrast, slightly tense atmosphere reminiscent of future settings in science fiction films.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the text contain 'EWA FLIGHT 226'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'Unknown Number' present?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the large text color white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the phone in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the thumb on the right side of the phone?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the phone large in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the phone rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one phone in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a hand in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the phone being held by a hand?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a dark color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a screenshot?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Does the text contain 'EWA FLIGHT 226'?  
   - yes

2. Is the text 'Unknown Number' present?  
   - yes

3. Is the large text color white?  
   - yes

4. Is the phone in the center of the image?  
   - n/a

5. Is the thumb on the right side of the phone?  
   - no

6. Is the background blurred?  
   - yes

7. Is the phone large in the image?  
   - n/a

8. Is the phone rectangular?  
   - yes

9. Is there one phone in the image?  
   - yes

10. Is there a hand in the image?  
    - yes

11. Is the phone being held by a hand?  
    - yes

12. Does the image have a dark color palette?  
    - yes

13. Is the image a screenshot?  
    - no

14. Does the image have low brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 14  

Score = (11/14) × 100 = 78.57

score: 78.57

reasons: The score is calculated based on the number of correct answers out of the total questions. In this case, 11 out of 14 questions were answered correctly, resulting in a score of 78.57%.

token_count: 343

caption_vocabulary_size: 227

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 71

candidate_caption: A close-up shot of a middle-aged man with long, dark hair and facial hair, taken from a front angle slightly to the left, showcasing his intense expression as he looks over his right shoulder towards something off-frame. His weathered face displays prominent scars across his forehead and cheekbone, adding texture and depth to his character's appearance. The man has wide-open eyes with dark eyeliner or makeup enhancing them, emphasizing his focused gaze. He is wearing black leather clothing with intricate designs on the shoulder area, which blends into the background due to the shallow depth of field. Natural daylight illuminates his face from the left side, creating strong highlights and shadows that accentuate the contours of his features, including furrowed brows and thick, dark eyebrows. His skin tone is medium brown with visible pores and fine lines, particularly around the cheekbones. The background consists of an out-of-focus structure, possibly part of a building or archway, positioned diagonally from the bottom left to the upper right, along with a blurred sky featuring scattered white clouds against a light blue backdrop. This creates a dramatic effect, drawing attention to the subject while maintaining a sense of location. The overall mood is tense and serious, enhanced by high contrast lighting that emphasizes the textures of his skin, hair, and attire. The color palette includes earthy tones like deep browns, blacks, and warm beige, contributing to the realistic style of the photograph. The composition uses leading lines created by the architectural element in the midground to draw focus towards the subject's face, resulting in a dynamic visual impact typical of cinematic photography, suggesting this could be a scene from a movie or TV series.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in front of the brown structure?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the person's face large in the image?"}
 {'answer': 'no', 'category': 'entity', 'question': 'Does the man have a scar on his face?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person turned to the left?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image showing outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sky blue?  
   - yes

2. Is the person in the center of the image?  
   - n/a

3. Is the person in front of the brown structure?  
   - yes

4. Does the person look serious?  
   - yes

5. Is the background blurred?  
   - yes

6. Is the person's face large in the image?  
   - yes

7. Does the man have a scar on his face?  
   - yes

8. Is there only one person in the image?  
   - yes

9. Is the person turned to the left?  
   - no

10. Is the image showing outdoors?  
    - yes

11. Is the image a shot from a film?  
    - yes

12. Does the image have high contrast?  
    - yes

**Score Calculation:**

Number of Correct Answers: 9  
Total Number of Questions: 12  

Score = (9/12) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. Out of 12 questions, 9 were answered with 'yes', resulting in a score of 75%.

token_count: 334

caption_vocabulary_size: 211

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 72

candidate_caption: The scene from 'The Wrong Missy' captures a lively poolside party at a resort in Oahu, Hawaii. In the foreground, two main characters stand prominently. On the left, a middle-aged man with light brown hair wears a crisp white shirt with thin vertical blue stripes and rolled-up sleeves. He holds a tall glass filled with a pale yellow cocktail garnished with a vibrant magenta orchid flower and mint leaves, his expression neutral yet slightly concerned as he gazes off-camera to his right. To his right stands a woman with long, wavy brown hair cascading over her shoulders, wearing an elegant sleeveless bright red dress with subtle pleats around the waistline. Her arms are crossed confidently across her chest as she looks directly at the camera with a slight smile. The midground features a group of people engaged in conversation under large beige sun umbrellas, creating a casual social setting. One person holds a bottle of beer, while others enjoy drinks or snacks. They're dressed in summer attire such as patterned tops, shorts, and sundresses in various colors like green, blue, pink, and white. White lounge chairs with turquoise towels draped over them are visible on the stone-tiled patio area. In the background, there's a clear blue swimming pool bordered by modern outdoor furniture, including contemporary woven chairs with dark metal frames and white cushions. Beyond the pool, tropical vegetation and palm trees add to the exotic atmosphere. The resort building's open design reveals warmly lit interiors through its transparent walls, featuring wooden beams and columns supporting a pergola-like structure with lattice work. Large windows allow natural daylight to illuminate the space, casting soft shadows and highlighting the vibrant colors of the scene. The overall mood is relaxed and sociable, captured in warm hues and balanced lighting typical of daytime scenes, emphasizing the leisurely ambiance of this high-end resort gathering.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the woman's dress red?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the towels light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the swimming pool in the background?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the man standing to the left of the woman?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the man looking serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the umbrella large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the foreground?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the man holding a drink?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a swimming pool in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the woman's dress red?  
   - yes

2. Are the towels light blue?  
   - no

3. Is the swimming pool in the background?  
   - yes

4. Is the man standing to the left of the woman?  
   - yes

5. Is the man looking serious?  
   - yes

6. Is the background blurred?  
   - n/a

7. Is the umbrella large?  
   - yes

8. Are there two people in the foreground?  
   - yes

9. Is the man holding a drink?  
   - yes

10. Does the image show outdoors?  
    - yes

11. Is there a swimming pool in the image?  
    - yes

12. Is the image a shot from a film?  
    - yes

13. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of correct answers out of the total number of questions. There were 10 correct answers out of 13 questions, resulting in a score of approximately 76.92%.

token_count: 375

caption_vocabulary_size: 261

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 74

candidate_caption: The image is divided into two sections, each showcasing different types of cooked meat dishes. In the top section, there's a close-up view of sliced braised beef brisket with an enticingly crispy, dark charcoal exterior that extends beyond the visible frame. The interior reveals moist, tender pinkish-brown meat slices with visible marbling and juicy textures. A generous coating of coarse salt granules adorns the outer surface of the brisket, adding texture and hinting at its smoky flavor profile. Some areas feature rich browned spots, indicating careful slow cooking to perfection. The beef appears well-seasoned, with visible grill marks enhancing its appearance. To the right of this section, partially sliced pieces of smoked steak are displayed, showcasing their succulent texture and varying shades from light beige to deep reds. The lower section presents a plate with several components arranged on it. On the left side, six vibrant green asparagus spears lie diagonally across the plate, roasted to perfection with charred tips and golden-brown edges suggesting they were grilled or roasted in olive oil. The asparagus has a slightly crisp exterior while maintaining some tenderness inside, with visible seasoning particles and small bits of herbs. Next to the asparagus, there's a generous serving of creamy potato salad, topped generously with vibrant red paprika powder, which adds both color and visual interest. Small diced celery pieces can be seen peeking through the mashed potatoes, giving the dish added freshness. On the far right, more sliced smoked steak is visible, displaying a similar dark, crispy exterior and tender interior. This steak piece shows layers of juicy meat beneath a thick, charred crust with deep reddish-brown hues, emphasizing the depth of flavors in this hearty meal. The background of the upper section features blurred kitchen elements like containers and utensils, while the lower section includes indistinct objects that might be part of the dining setup. Both images use natural lighting coming from the front-left side, highlighting the appetizing details of the food without harsh shadows. The overall composition focuses closely on the delicious, mouthwatering nature of these culinary creations, showcasing their textures and colors vividly.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is there a green vegetable in the image?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is there meat in the top portion of the image?'}
 {'answer': 'No', 'category': 'relative position', 'question': 'Is the potato salad to the left of the meat in the bottom image?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Is the image divided into two sections?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the potato salad portion small?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Are the asparagus spears long and thin?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there brisket in the image?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show food?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is there a green vegetable in the image?  
   - yes

2. Is there meat in the top portion of the image?  
   - yes

3. Is the potato salad to the left of the meat in the bottom image?  
   - no

4. Is the image divided into two sections?  
   - yes

5. Is the potato salad portion small?  
   - n/a

6. Are the asparagus spears long and thin?  
   - yes

7. Is there brisket in the image?  
   - yes

8. Does the image show food?  
   - yes

9. Is the image a photograph?  
   - n/a

10. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 10  

Score = (7/10) × 100 = 70

score: 70.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 7 out of 10 questions were answered correctly, resulting in a score of 70.

token_count: 435

caption_vocabulary_size: 268

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 81

candidate_caption: A full-body street fashion photograph taken in an urban setting features a person standing confidently in the center of a paved road with light gray zebra crosswalk lines. The individual is dressed in an ivory-colored ribbed knit outfit consisting of a sleeveless top with a prominent circular keyhole cutout at the chest, paired with a high-necked beige sweater featuring vertical ridges and wide lapels. This ensemble includes matching vertical-striped high-waisted skirt with a front slit revealing their left leg. They are accessorized with black round sunglasses with dark lenses and gold rims, multiple small earrings including a visible gold hoop earring on one ear, and delicate ankle bracelets. In their hands, they hold a structured pale yellow handbag with smooth leather texture and a thin silver chain strap. On their feet are sky blue pointed-toe heels with ankle straps and slight heels. Their bald head is adorned with several small golden hairpins. The background showcases classic European architecture with cream-colored buildings displaying rectangular windows, cornices, and balconies. A row of orange and white striped traffic cones labeled 'TOUT' are aligned diagonally behind them to the left. Two modern cars are parked alongside the street; a glossy black Mercedes-Benz on the left with its headlights illuminated, featuring LED-like lights around its thin edges, and an Audi on the right with a visible license plate reading 'GA 5'. Several people can be seen conversing or going about their business amidst the construction barriers. The lighting is natural daylight under slightly overcast conditions, providing even illumination across the scene and creating a balanced exposure that highlights both the subject and the surrounding environment. The overall color palette consists primarily of neutral tones like ivory, taupe, and beige, complemented by accents of lemon yellow and powder blue, contributing to the stylish and sophisticated mood of the image.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the license plate of the car on the right contain 'GA'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the handbag yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's coat light beige?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person standing in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a black car on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person standing in front of two cars?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person closer to the camera than the buildings?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurry?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the yellow handbag small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the handbag rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there four traffic cones?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a neutral color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Does the license plate of the car on the right contain 'GA'?  
   - yes

2. Is the color of the handbag yellow?  
   - yes

3. Is the person's coat light beige?  
   - yes

4. Is the person standing in the center of the image?  
   - yes

5. Is there a black car on the left side of the image?  
   - yes

6. Is the person standing in front of two cars?  
   - yes

7. Is the person closer to the camera than the buildings?  
   - yes

8. Is the background blurry?  
   - no

9. Is the yellow handbag small?  
   - n/a

10. Is the handbag rectangular?  
    - n/a

11. Are there four traffic cones?  
    - n/a

12. Does the image show outdoors?  
    - yes

13. Does the image have a neutral color palette?  
    - yes

14. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 14  

Score = (11/14) × 100 = 78.57

score: 78.57

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, out of the total number of questions. There are 11 'yes' answers out of 14 questions, resulting in a score of 78.57%.

token_count: 367

caption_vocabulary_size: 255

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 82

candidate_caption: A black-and-white still from a 1930s film features actors Leslie Howard and Marion Davies in a medium shot, standing closely together and engaged in conversation while holding martini glasses. The scene is set indoors, likely within a mansion or formal living room, creating an elegant atmosphere typical of early Hollywood cinema. Leslie Howard, positioned on the left, wears a classic tuxedo with a bow tie and has short, neatly combed gray hair. He faces slightly right, looking at Marion with a gentle smile. His expression appears friendly as he holds his glass near his mouth, his other hand partially visible in his pocket. Marion Davies, on the right, is dressed in a dark fur-collared dress adorned with a beaded necklace and earrings. She holds her glass up high, facing slightly left towards Leslie. Her hair is styled in loose waves characteristic of the era, and she wears a long chain necklace that hangs down the front of her dress. Both are well-lit by soft artificial light, which creates a balanced exposure and highlights their facial expressions without harsh shadows. In the background, there's a large circular mirror with an ornate frame on the upper right corner, and a decorative metallic object, possibly a lamp base or sculpture, can be seen on a piece of furniture to the right of the subjects. A patterned curtain adds depth to the setting. The overall mood is sophisticated and celebratory, capturing a moment of interaction between the two characters in this luxurious environment. The composition is centered, focusing on the intimate exchange between the actors.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'FXM'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the image black and white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the man on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the woman on the right of the man?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the man smiling?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the woman look attentive?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image blurry?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the man holding a glass?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the woman facing the man?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a woman in the image?'}
 {'answer': 'Yes', 'category': 'image type', 'question': 'Is the image a shot from an old film?'}
 {'answer': 'Yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Does the image contain the text 'FXM'?  
   - n/a

2. Is the image black and white?  
   - yes

3. Is the man on the left side of the image?  
   - yes

4. Is the woman on the right of the man?  
   - yes

5. Is the man smiling?  
   - yes

6. Does the woman look attentive?  
   - n/a

7. Is the image blurry?  
   - no

8. Are there two people in the image?  
   - yes

9. Is the man holding a glass?  
   - yes

10. Is the woman facing the man?  
    - yes

11. Does the image show indoors?  
    - yes

12. Is there a woman in the image?  
    - yes

13. Is the image a shot from an old film?  
    - yes

14. Does the image have low brightness?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of questions answered correctly out of the total number of questions. In this case, 10 out of 14 questions were answered, resulting in a score of 71.43%.

token_count: 312

caption_vocabulary_size: 200

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 85

candidate_caption: A serene landscape photograph captures an intricate cave interior with natural lighting, creating a high contrast between shadowed areas and illuminated sections. The foreground features large, dark brown rocks with rough textures, forming jagged edges and sharp angles that create silhouettes against the brighter background. A calm pool of water occupies the midground, its surface smooth and reflective in shades of forest green (#1b4d3f), turquoise (#87c2a8), and sky blue (#7fb0e9). Gentle ripples distort this mirror-like appearance near where a vertical log or tree trunk partially submerged in the water creates circular patterns of light reflections. To the left, a slender waterfall cascades down from an opening above, forming fine streams that create a misty effect as they hit the still water below. This flowing water has a striking azure blue hue (#3c5da5) due to long exposure photography techniques, which results in a soft glow around its base. The cavern's walls are composed of rugged rock formations with various shades of grayish-brown (#6b6044), beige (#dac69a), and olive green (#6c6933). These textured surfaces showcase a rich tapestry of colors and shapes, including crevices, protrusions, and small indentations that add depth and character to the scene. On the right side, sunlight filters through an opening in the dense tropical vegetation outside the cave, casting bright highlights on vibrant green foliage and illuminating the rocky ground scattered with stones of different sizes. The interplay between light and shadow enhances the three-dimensional quality of the scene, emphasizing the raw beauty of this untouched natural setting. The color palette includes deep forest greens, earthy browns, cool blues, warm yellows, and touches of slate gray, contributing to the tranquil mood of the image while highlighting the raw beauty of this pristine wilderness area.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the water turquoise?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the cave entrance on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the waterfall to the left side of the image?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the cave large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the shape of the cave entrance irregular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Does the image show more than one rock?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a waterfall in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the water turquoise?  
   - yes

2. Is the cave entrance on the right side of the image?  
   - n/a

3. Is the waterfall to the left side of the image?  
   - yes

4. Is the cave large?  
   - n/a

5. Is the shape of the cave entrance irregular?  
   - n/a

6. Does the image show more than one rock?  
   - yes

7. Is there a waterfall in the image?  
   - yes

8. Does the image show outdoors?  
   - n/a

9. Is the image a photograph?  
   - yes

10. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 10  

Score = (7/10) × 100 = 70

score: 70.0

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. There are 7 'yes' answers out of 10 questions, resulting in a score of 70.

token_count: 376

caption_vocabulary_size: 251

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 91

candidate_caption: A dramatic scene from the movie 'The Witches' featuring an actress in a vintage-inspired, glamorous costume. She stands at the center of the frame with her arms outstretched to the sides, creating a powerful and commanding presence. The woman wears a one-shoulder dark purple gown with a flowing cape-like overlay extending from her left shoulder down to her waist. A striking gold snake charm adorns her right shoulder, adding an element of mystery and allure. Her look is completed with long, textured opera-length gloves in matching deep purple, reaching above her elbows. Her platinum blonde hair is styled in soft waves reminiscent of classic 1950s Hollywood glamour, framing her face perfectly. The makeup includes bold red lipstick, smoky eye makeup with hints of blue and black eyeshadow, and defined eyebrows. Her expression is serious and intense as she looks directly at the camera, conveying confidence and poise. The background features richly paneled wood with vertical columns, framed paintings or windows on either side, and golden decorative elements, suggesting an opulent setting such as a grand hall or courtroom within a mansion. Dark wooden furniture is partially visible below, enhancing the luxurious atmosphere. The lighting is warm and even, highlighting her facial features and attire without casting harsh shadows, contributing to the overall mysterious and dramatic mood of the scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the woman's hair blonde?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look serious?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person large in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Are the person's arms extended outward?"}
 {'answer': 'yes', 'category': 'relation', 'question': 'Does the woman have a scar on the face?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image showing indoors?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the woman standing in the center of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is the woman wearing gloves?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette include gold tones?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a screenshot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the woman's hair blonde?  
   - yes

2. Is the person in the center of the image?  
   - yes

3. Does the person look serious?  
   - yes

4. Is the person large in the image?  
   - n/a

5. Is there one person in the image?  
   - yes

6. Are the person's arms extended outward?  
   - yes

7. Does the woman have a scar on the face?  
   - n/a

8. Is the image showing indoors?  
   - yes

9. Is the woman standing in the center of the image?  
   - yes

10. Is the woman wearing gloves?  
    - yes

11. Does the image have a warm color palette?  
    - yes

12. Does the image's color palette include gold tones?  
    - yes

13. Is the image a screenshot from a film?  
    - yes

14. Does the image have high contrast?  
    - n/a

15. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 15  

Score = (11/15) × 100 = 73.33

score: 73.33

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. In this case, 11 out of 15 questions were answered with 'yes', resulting in a score of 73.33%.

token_count: 267

caption_vocabulary_size: 183

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 92

candidate_caption: A photograph taken inside a large industrial hangar showcases an Embraer 190 E-Freighter aircraft, model E190F. The plane is predominantly white with blue accents on its tail fin, which features a yellow emblem resembling an arrow or feather design. The aircraft's cargo door is open, revealing the interior compartment filled with various equipment and containers. A sign reading 'E-FREIGHTER' in bold, uppercase letters in yellow on a white background is visible inside the open cargo hold. The text 'EMBRAER 190' appears in black near the nose of the aircraft, while 'E-FREIGHTER' and 'E190F' are printed in blue on the fuselage. The scene is well-lit by natural light streaming through the tall windows and open hangar doors on the right side, supplemented by overhead artificial lighting. The polished concrete floor reflects the bright lights and the aircraft, creating a glossy appearance that adds depth to the image. In front of the airplane, there is a black rectangular platform covered with fabric. The hangar's ceiling consists of a grid-like structure made up of numerous metal beams and trusses supported by vertical columns. Yellow safety lines run diagonally across the ceiling, adding contrast to the metallic framework. Various pieces of maintenance equipment, workstations, and tools are scattered around the hangar floor, indicating ongoing operations. The overall mood is technical and professional, highlighting the functionality and operational aspects of this modern freighter aircraft within a busy yet orderly workshop environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text 'E-FREIGHTER' visible on the airplane?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the airplane mostly white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the airplane inside a hangar?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the nose of the airplane in the center of the image?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the airplane large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one airplane in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the cargo door of the airplane open?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'text', 'question': "Is the aircraft's model name E190F?"}
 {'answer': 'yes', 'category': 'text', 'question': 'Is the manufacturer of the aircraft Embraer?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high brightness?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have natural color grading?'}]

openai_answers: 1. Is the text 'E-FREIGHTER' visible on the airplane?  
   - yes

2. Is the airplane mostly white?  
   - yes

3. Is the airplane inside a hangar?  
   - yes

4. Is the nose of the airplane in the center of the image?  
   - n/a

5. Is the airplane large?  
   - yes

6. Is there only one airplane in the image?  
   - yes

7. Is the cargo door of the airplane open?  
   - yes

8. Does the image show indoors?  
   - yes

9. Does the image have a cool color palette?  
   - n/a

10. Is the aircraft's model name E190F?  
    - yes

11. Is the manufacturer of the aircraft Embraer?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have high brightness?  
    - n/a

14. Does the image have natural color grading?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of questions answered correctly out of the total number of questions. In this case, 10 out of 14 questions were answered correctly, resulting in a score of 71.43%.

token_count: 305

caption_vocabulary_size: 183

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 95

candidate_caption: A black-and-white photograph captures an intimate moment between two individuals holding a transparent umbrella covered in raindrops, creating a romantic and cozy atmosphere. The couple is centered in the frame, facing each other closely with their noses almost touching, conveying affection through their expressions. Their heads are tilted towards one another, forming a tender connection that fills the entire composition. The woman on the left has long, wavy hair flowing down past her shoulders, partially visible under the umbrella, while the man on the right wears a light-colored short-sleeved button-up shirt. Soft natural lighting gently illuminates their faces from above, highlighting their profiles without harsh shadows. The clear umbrella dominates the foreground of the image, adorned with numerous small to medium-sized raindrops scattered across its surface, adding texture and depth to the scene. This water droplet pattern creates a sparkling effect and enhances the sense of recent rainfall or ongoing drizzle. A thin metal handle is clearly seen being held by either person, anchoring the focus on the couple beneath it. The background is blurred due to shallow depth of field, consisting of indistinct shapes and out-of-focus elements that suggest an outdoor setting, possibly trees or structures. This soft backdrop emphasizes the closeness of the subjects within the frame. The overall mood is warm, intimate, and nostalgic, enhanced by the high contrast typical of black-and-white photography and the balanced luminance throughout the image.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the image in black and white?'}
 {'answer': 'Yes', 'category': 'color', 'question': 'Is the umbrella transparent?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is there an umbrella in the center of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Is the woman's head to the left of the man's head?"}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Are the people in the image displaying affection?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image blurry?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the image noisy?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the umbrella large?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the umbrella dome-shaped?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there an umbrella in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Are the people standing under the umbrella?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low color saturation?'}]

openai_answers: 1. Is the image in black and white?  
   - yes

2. Is the umbrella transparent?  
   - yes

3. Is there an umbrella in the center of the image?  
   - yes

4. Is the woman's head to the left of the man's head?  
   - yes

5. Are the people in the image displaying affection?  
   - yes

6. Is the image blurry?  
   - n/a

7. Is the image noisy?  
   - n/a

8. Is the umbrella large?  
   - n/a

9. Is the umbrella dome-shaped?  
   - n/a

10. Are there two people in the image?  
    - yes

11. Is there an umbrella in the image?  
    - yes

12. Are the people standing under the umbrella?  
    - yes

13. Does the image show outdoors?  
    - yes

14. Is the image a photograph?  
    - yes

15. Does the image have low color saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 15  

Score = (11/15) × 100 = 73.33

score: 73.33

reasons: The score is calculated based on the number of 'yes' answers, which indicate correct or affirmative responses, divided by the total number of questions. In this case, 11 out of 15 questions were answered with 'yes', resulting in a score of 73.33%.

token_count: 283

caption_vocabulary_size: 194

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 96

candidate_caption: The scene from the movie 'Jojo Rabbit', directed by Taika Waititi, features a close-up of two characters in a room with muted colors and soft indoor lighting. In the foreground, a young boy with fair skin, short curly blonde hair, and striking green eyes stands slightly to the right of center. He has an anxious expression with his mouth slightly open as if speaking or reacting, looking directly at the camera. His eyebrows are furrowed, adding to his concerned look. The boy wears a light tan scout shirt with black shoulder epaulettes, a pointed collar, and a distinctive red neckerchief tied into a knot. To his left, standing partially behind him, is an adult figure dressed in a mustard yellow Nazi uniform with four gold buttons down the front, multiple pockets with flaps, and breast pocket details. A wide brown leather belt with visible stitching around the metal buckle cinches his waist, while a brown leather strap with a silver metallic clasp crosses diagonally over his chest from left shoulder to right hip area. A red Nazi armband with a white swastika emblem is visible on the adult's left arm. The background shows an indoor setting with blurred elements, including a green-framed window with a golden handle on the far left edge of the frame, a framed picture featuring floral designs on the wall, and other indistinct objects. A Nazi flag can also be seen. The overall mood is tense and somber, enhanced by the warm hues and low contrast of the color palette dominated by earthy tones such as olive green, khaki, dark brown, forest green, and brick red. The shallow depth of field keeps the focus on the boy's face while providing context through the background elements, creating a realistic yet dramatic style typical of historical war dramas set during World War II.

captioned_by: pg-captioner

ground_truth: [{'answer': 'no', 'category': 'color', 'question': 'Is the uniform mustard brown?'}
 {'answer': 'no', 'category': 'color', 'question': 'Is the belt brown?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the child standing on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the boy in front of the adult?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the boy looking confused?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the adult in the image larger than the boy?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the belt buckle rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a swastika in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have warm color tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}]

openai_answers: 1. Is the uniform mustard brown?  
   - no

2. Is the belt brown?  
   - yes

3. Is the child standing on the right side of the image?  
   - yes

4. Is the boy in front of the adult?  
   - yes

5. Is the boy looking confused?  
   - no

6. Is the background blurred?  
   - yes

7. Is the adult in the image larger than the boy?  
   - n/a

8. Is the belt buckle rectangular?  
   - n/a

9. Are there two people in the image?  
   - yes

10. Is there a person in the image?  
    - yes

11. Is there a swastika in the image?  
    - yes

12. Is the image taken indoors?  
    - yes

13. Does the image have warm color tones?  
    - yes

14. Is the image a shot from a film?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 14  

Score = (11/14) × 100 = 78.57

score: 78.57

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 14 questions were answered correctly, resulting in a score of 78.57%.

token_count: 369

caption_vocabulary_size: 238

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 97

candidate_caption: A dynamic, abstract photograph capturing the essence of speed in an urban setting at night. The central focus is on a dark-colored car in rapid motion, its sleek silhouette blurred as it speeds through an intersection or street corner. Positioned slightly to the right of center, the car's illuminated yellow headlights dominate the scene, casting bright light onto the surrounding area and creating a stark contrast against the dark asphalt. Reflections from nearby neon signs and building lights dance across the car's glossy surface, adding depth and movement to the composition. Surrounding the main subject are numerous streaks of color representing city lights, ranging from white, green, blue, red, orange, and yellow hues, all horizontal and diagonal across the frame. These light trails create a sense of blur and dynamism, emphasizing the high-speed motion of both the car and its surroundings. The background features indistinct outlines of buildings or structures, further enhanced by these colorful light trails that give the impression of tall buildings or advertisements glowing with various neon colors. The overall mood is energetic and intense, achieved through the use of low-key lighting and high contrast between the brightly lit elements and the darker surroundings. This creates a visually striking effect that captures the feeling of velocity and the bustling nature of an urban environment at night. The image has a balanced exposure despite the apparent underexposure, allowing details in both highlights and shadows to be visible. The color palette includes deep blacks (#130c0e), midnight blues (#2a4f6b), forest greens (#5d7e53), warm yellows (#ddcb8c), burnt oranges, and touches of periwinkle blue (#a8ad9a), contributing to the vibrant yet somewhat mysterious atmosphere.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the car black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the car in the center of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a car in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken at night?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the car black?  
     - yes

   - Is the car in the center of the image?  
     - no

   - Is there a car in the image?  
     - yes

   - Is the image taken at night?  
     - yes

   - Does the image have a cool color palette?  
     - yes

   - Is the image a photograph?  
     - yes

   - Is the image color graded with high saturation?  
     - n/a

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 7

   Score = (5/7) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of correct answers (5) out of the total number of questions (7). The formula used is (5/7) × 100, resulting in a score of 71.43.

token_count: 344

caption_vocabulary_size: 218

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 99

candidate_caption: A dynamic scene from the video game 'Assassin's Creed: Odyssey' depicting an intense battle in an autumnal setting. The central focus is on two warriors engaged in close combat near a riverbank. In the foreground, a Greek soldier wearing intricate gold armor with elaborate carvings and designs is partially submerged in water, his face showing distress and fear as he reaches upwards towards another warrior above him. This fallen soldier wears a white skirt with blue accents and golden arm guards, with only his head visible above the waterline. His arms are spread wide open, creating splashes around him. The main character stands dominantly over him, holding a spear pointed downward in his right hand while wearing a golden helmet adorned with a red feather plume, a red cloak flowing behind him, and a determined expression. He also wears a leather belt with arrows and quivers attached to his back, adding realism to his attire. The midground shows multiple soldiers fighting, some running towards the center of action while others advance from both sides. These soldiers wear various types of ancient Greek armor, including helmets with plumes, shields with distinct patterns, and swords, contributing to the chaotic atmosphere. The background features a scenic landscape filled with trees displaying vibrant autumn foliage in shades of amber yellow, burnt orange, forest green, and rust red. Rocky outcrops can be seen among the vegetation. The sky is partly cloudy with soft, fluffy clouds illuminated by warm sunlight streaming from the left side, casting dramatic shadows across the battlefield and enhancing the vivid colors of the environment. The lighting creates high contrast and emphasizes the textures and details of the characters' clothing, weapons, and natural scenery, contributing to the overall intensity of the scene. The color palette includes earthy tones like olive green, tan, and charcoal gray, complemented by bright hues of sunset, emphasizing the historical theme of the artwork. The entire composition captures the raw energy and brutality of ancient warfare, showcasing the game's epic narrative set against a backdrop of nature transitioning into autumn.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person at the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are there people behind the fighter in the center?'}
 {'answer': 'yes', 'category': 'emotion', 'question': "Is there an expression of anger on the central person's face?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person in the center larger than others?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than five people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there water in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the central person fighting with another person?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a digital artwork?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with warm tones?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is the sky blue?  
   - n/a

2. Is there a person at the center of the image?  
   - yes

3. Are there people behind the fighter in the center?  
   - yes

4. Is there an expression of anger on the central person's face?  
   - yes

5. Is the person in the center larger than others?  
   - n/a

6. Are there more than five people in the image?  
   - yes

7. Is there water in the image?  
   - yes

8. Is the central person fighting with another person?  
   - yes

9. Does the image show outdoors?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a digital artwork?  
    - yes

12. Is the image color graded with warm tones?  
    - yes

13. Does the image have high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. The 'n/a' responses are not counted as correct answers. The formula used is (Number of Correct Answers / Total Number of Questions) × 100.

token_count: 405

caption_vocabulary_size: 260

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 104

candidate_caption: A vibrant photograph captures seven knights riding horses through an outdoor medieval reenactment event, positioned in front of a large crowd and tall trees under clear blue skies. The scene is bathed in natural daylight, creating high contrast between the brightly colored costumes and the verdant surroundings. Each knight wears ornate armor and carries distinctive flags with various crests and emblems, including symbols such as lions, dragons, eagles, and heraldic designs. From left to right, the first knight rides a white horse adorned with black and gold armor and a cape featuring circular patterns, holding a black flag with a red lion emblem on a wooden staff. Next is a knight on a gray horse wearing golden armor with intricate designs and a horned silver helmet, carrying a yellow flag with a brown eagle. The third knight, mounted on a brown horse with a white blaze, dons black chainmail armor with gold accents and a white cape with small triangular cut-outs, bearing a white banner displaying a black eagle or dragon silhouette. The fourth knight rides a dark brown steed with a white blaze, clad in elaborate red and gold armor with a flowing crimson cloak, holding a red flag with golden dragon motifs. The fifth knight, atop a light brown horse with a white blaze, sports navy blue armor with red and green trimmings and a forest green cape, bearing a purple flag with a red lion design. The sixth knight, mounted on a black horse, wears metallic silver armor with prominent shoulder plates, a closed visor helmet, and a cape with intricate embroidery, carrying a black flag with a white stag or bull symbol. The seventh knight, on a black horse, completes the lineup with charcoal gray armor embellished with brass details, a unique horn-like helmet, and a cape featuring alternating vertical stripes of royal blue and forest green, topped with a large feather plume in vivid red, yellow, and green hues. Behind them, spectators fill wooden benches and stand areas, attentively watching the procession. Large banners with various designs and text are visible among the crowd, one reading 'Deutscher Ritterturnier' in white serif font on a blue and white striped background. In the background, tall trees provide a lush backdrop, while large tents with conical roofs display colorful shields with various heraldry symbols, including blue and white triangles over red lines on beige backgrounds. One tent features a shield with red and white stripes. The overall mood is festive, celebratory, and historical, capturing the essence of a lively medieval renaissance festival where the past meets present in a picturesque setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is there a golden yellow flag?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the cape of the right-most knight emerald green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are all the knights positioned in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the knight with the golden horns to the left of the knight with the red feathers?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the building on the right side of the image large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there seven knights in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a horse in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the knight with red feathers mounted on a horse?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an outdoor scene?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is there a golden yellow flag?  
   - yes

2. Is the cape of the right-most knight emerald green?  
   - no

3. Are all the knights positioned in the center of the image?  
   - n/a

4. Is the knight with the golden horns to the left of the knight with the red feathers?  
   - yes

5. Is the background blurred?  
   - no

6. Is the building on the right side of the image large?  
   - n/a

7. Are there seven knights in the image?  
   - yes

8. Is there a horse in the image?  
   - yes

9. Is the knight with red feathers mounted on a horse?  
   - yes

10. Does the image show an outdoor scene?  
    - yes

11. Is the image a photograph?  
    - yes

12. Does the image have high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 12  

Score = (9/12) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 12 questions were answered correctly, resulting in a score of 75%.

token_count: 519

caption_vocabulary_size: 254

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 113

candidate_caption: A close-up shot captures a person's hand holding a black Panasonic R-90 cassette recorder with a Sony Type-R cassette tape inserted. The scene is lit by soft daylight, creating gentle shadows on the fingers and emphasizing their texture against the dark device. The hand is positioned horizontally across the frame, gripping the sides of the recorder firmly. The cassette tape is centered within a transparent plastic slot, featuring two large circular spindles surrounded by white plastic casing. It displays the 'Panasonic' brand name in bold red letters at the top, followed by smaller white text reading 'R-90', indicating its model. Below this, there's a green meter-like scale marked with numbers ranging from 0 to 10 in increments of 1, likely representing recording time or volume levels. A prominent white arrow pointing diagonally downward towards the left side points towards the cassette tape inside. On the upper right corner of the device, there's a diamond-shaped speaker grille composed of small circular holes arranged uniformly, with a textured pattern enhancing acoustic output. To the left of the cassette slot, various buttons and controls are visible, including a red LED indicator light above a REC/BAT switch labeled with white sans-serif font. The word 'SONY' appears vertically along the left edge of the device in white capital letters, while 'REC/PLAY' is printed near the top right in white text. An orange button with a cross symbol sits near the top of the device. The background is blurred and indistinct, suggesting an outdoor setting such as a forest or park in England, Europe during the night. This shallow depth of field keeps the focus solely on the hand and cassette player, while the color palette includes muted tones like dark brown (#2b281a), olive drab (#3c4338), sage green (#7f8476), taupe (#64624d), khaki (#89826e), and slate gray (#70898c). The overall mood is nostalgic and focused, enhanced by low gamma, contrast, saturation, luminance, and brightness settings that contribute to the vintage feel of the image.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Panasonic'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color brown?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the music player black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the music player in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the cassette player in the hand?'}
 {'answer': 'no', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the object large in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the object rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one hand in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the hand holding the cassette player?'}
 {'answer': 'no', 'category': 'general', 'question': 'Is the image showing an indoor scene?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a dark color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'Panasonic'?  
   - yes

3. Is the background color brown?  
   - n/a

4. Is the music player black?  
   - yes

5. Is the music player in the center of the image?  
   - no

6. Is the cassette player in the hand?  
   - yes

7. Is the background blurred?  
   - yes

8. Is the object large in the image?  
   - n/a

9. Is the object rectangular?  
   - yes

10. Is there one hand in the image?  
    - yes

11. Is the hand holding the cassette player?  
    - yes

12. Is the image showing an indoor scene?  
    - no

13. Does the image have a dark color palette?  
    - yes

14. Is the image a shot from a film?  
    - n/a

15. Does the image have low brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 15  

Score = (11/15) × 100 = 73.33

score: 73.33

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 15 questions were answered correctly, resulting in a score of 73.33%.

token_count: 424

caption_vocabulary_size: 267

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 116

candidate_caption: A photograph capturing a serene moment of a woman pouring sake into a traditional Japanese ceramic bowl, taken from a slightly elevated angle to her right. The woman is dressed in a black blazer with distinctive white trim along the shoulders and buttons, which adds a formal touch to the scene. Her focused expression and neatly styled brown hair partially obscured by bangs are visible as she holds a rustic-textured dark brown ceramic teapot in both hands. The saucer-like bowl, positioned on a light wooden table, has a unique patterned design featuring shades of beige, off-white, and black swirls, giving it an earthy appearance. To the right of the woman stands a tall, slender bottle of sake with a textured beige label displaying large black Japanese calligraphy characters '海山' (Umiyama), accompanied by a small red stamp or seal below. On the far right side of the table is a clear wine glass designed for tasting, empty and ready for use. The lighting is soft and warm, creating a cozy atmosphere while highlighting the textures of the objects without casting harsh shadows. The background is blurred, showing hints of greenery and indistinct shapes that suggest an indoor setting, possibly a restaurant or bar. This composition emphasizes the ceremonial act of sake serving while maintaining a balanced exposure and natural color palette dominated by shades of beige, black, forest green, and reddish-brown.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there text on the bottle?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the bottle black?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the woman's outfit black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bottle placed on a table?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the woman in the background?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bottle to the right of the teapot?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the light-colored cup to the left of the glass?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the woman smiling?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bottle tall?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the cup cylindrical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two cups on the table?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a teapot in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the woman pouring something into the cup?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have warm color tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there text on the bottle? - yes
2. Is the bottle black? - no
3. Is the woman's outfit black? - yes
4. Is the bottle placed on a table? - yes
5. Is the woman in the background? - no
6. Is the bottle to the right of the teapot? - yes
7. Is the light-colored cup to the left of the glass? - yes
8. Is the woman smiling? - n/a
9. Is the background blurred? - yes
10. Is the bottle tall? - yes
11. Is the cup cylindrical? - no
12. Are there two cups on the table? - no
13. Is there a teapot in the image? - yes
14. Is the woman pouring something into the cup? - yes
15. Is the image taken indoors? - yes
16. Does the image have warm color tones? - yes
17. Is the image a photograph? - yes
18. Does the image have high contrast? - n/a

Score Calculation:
- Number of Correct Answers: 13
- Total Number of Questions: 18

Score = (13/18) × 100 = 72.22

score: 72.22

reasons: The score is calculated based on the number of correct answers out of the total questions. In this case, 13 out of 18 questions were answered correctly, resulting in a score of 72.22%.

token_count: 280

caption_vocabulary_size: 185

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 119

candidate_caption: A close-up photograph of a breakfast plate featuring two Eggs Benedict dishes. The round dark gray ceramic plate has a subtle textured surface with a smooth rim, containing five distinct food items arranged symmetrically. Two identical Eggs Benedict meals are placed centrally on golden-brown toasted English muffins, each consisting of a fluffy poached egg with slightly runny yolk, a generous layer of bright yellow Hollandaise sauce that's been lightly browned and sprinkled with red paprika or spice, and a pinkish-orange slice of smoked salmon beneath the eggs. To the left side of the main dish are several grilled mushroom slices with charred edges, their light beige color enhanced by finely chopped green herbs. At the top center of the plate sits a small white ramekin filled with cooked beans garnished with fresh chopped parsley. On the right side of the main dish, there's a scoop of creamy whipped potatoes, also sprinkled with finely chopped herbs. The meal is presented on a wooden table with visible grain patterns, adding warmth to the scene. In the background, partially visible black chairs can be seen, suggesting an indoor dining setting. Natural lighting from the left illuminates the food, highlighting its textures and colors, creating soft shadows and enhancing the appetizing appearance of the meal.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the cheese yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the plate grey?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the white bowl at the top center of the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurry?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bowl small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the plate circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two pieces of bread with cheese?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there any bread in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show food?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bowl of beans in the center of the plate?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the color of the cheese yellow? - yes
2. Is the color of the plate grey? - yes
3. Is the white bowl at the top center of the image? - yes
4. Is the background blurry? - n/a
5. Is the bowl small? - yes
6. Is the plate circular? - yes
7. Are there two pieces of bread with cheese? - no
8. Is there any bread in the image? - yes
9. Does the image show food? - yes
10. Does the image have a warm color palette? - yes
11. Is the bowl of beans in the center of the plate? - yes
12. Is the image a photograph? - yes
13. Does the image have high contrast? - n/a

Score: (10/13) × 100 = 76.92

score: 76.92

reasons: The score is calculated based on the number of 'yes' responses to the questions, excluding those marked as 'n/a'. Out of 13 questions, 10 were answered 'yes', resulting in a score of 76.92%.

token_count: 255

caption_vocabulary_size: 177

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 123

candidate_caption: A movie poster for 'Zombieland Double Tap' featuring actor Avan Jogia in a vibrant, energetic composition. He is positioned slightly off-center to the right, with his hands clasped together in a namaste or prayer-like gesture near his chest, exuding a friendly and welcoming demeanor. Avan has light brown hair styled loosely, with strands falling freely around his face, and dark eyebrows. His face shows a warm smile, revealing teeth and conveying a relaxed expression. He sports a well-groomed beard and mustache. He's wearing a white button-up shirt with three visible buttons partially undone, layered under a red patterned cardigan with intricate designs in black, gold, green, and orange threads. Around his neck are several necklaces, including black beaded ones, a thin black cord necklace, and an ornate brass-colored pendant. On his left wrist is a black bracelet adorned with colorful beads. A small earring is visible on his left ear. Avan also wears a black watch on his left wrist. He holds an acoustic guitar diagonally across his body from bottom left to upper right. The guitar has a rich reddish-brown finish with noticeable scratches, wear marks, and a worn-out appearance. Its sound hole is black, surrounded by a beige rim and six strings extending upwards. The background features a bright forest green color (#228B22) with large neon orange outlines of letters forming the word "ZOMBIELAND," accompanied by vibrant yellow highlights and vertical T-shaped stripes. Red splatter patterns resembling blood are scattered throughout, adding an action-packed element. Text at the top reads 'FROM THE DIRECTOR OF VENOM AND WRITERS OF DEADPOOL' in bold white uppercase letters. Below the character, 'AVAN JOGIA' appears in bold white text. The title 'ZOMBIELAND DOUBLE TAP' is prominently displayed in large, stylized letters with a glowing orange outline and green shadow effect, giving it a 3D appearance. The release date 'IN THEATERS OCTOBER 18' is shown below the title in white text. The bottom right corner includes the 'R' rating logo. The overall style is graphic and promotional, with high contrast, vivid colors, and an adventurous mood typical of comic book art styles.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'AVAN JOGIA'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'IN THEATERS' present in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color green?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the color of the text 'DOUBLE TAP' yellow?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the guitar located at the bottom of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'IN THEATERS' below the text 'DOUBLE TAP'?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the guitar large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there blood splashes in the image?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a movie poster?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the image contain the text 'AVAN JOGIA'?  
   - yes

2. Is the text 'IN THEATERS' present in the image?  
   - yes

3. Is the background color green?  
   - yes

4. Is the color of the text 'DOUBLE TAP' yellow?  
   - no

5. Is the person in the center of the image?  
   - no

6. Is the guitar located at the bottom of the image?  
   - no

7. Is the text 'IN THEATERS' below the text 'DOUBLE TAP'?  
   - yes

8. Is the person smiling?  
   - yes

9. Is the guitar large?  
   - n/a

10. Is there one person in the image?  
    - yes

11. Are there blood splashes in the image?  
    - yes

12. Does the image have a warm color palette?  
    - yes

13. Is the image a movie poster?  
    - yes

14. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 14  

Score = (11/14) × 100 = 78.57

score: 78.57

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 14 questions were answered correctly, resulting in a score of 78.57%.

token_count: 469

caption_vocabulary_size: 293

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 127

candidate_caption: A surreal, ethereal photograph captures an angelic figure kneeling in contemplation or prayer inside an old-fashioned room. The central focus is on a person with large, intricately designed white wings spread behind them, partially obscured by semi-transparent lace curtains adorned with delicate floral patterns in shades of forest green (#1c251f), sage green (#a5b09e), olive drab (#6d7f67), khaki (#8c9b82), and golden yellow (#ba9c3b). The angel's body, viewed from behind at a slight angle to the left, is illuminated by a warm amber glow emanating from their hands as they hold a small candle close to their face. This creates a soft halo effect around their head and upper torso, casting gentle shadows that accentuate their serene expression. They are dressed in light-colored clothing featuring matching subtle floral embroidery. Behind the angel, tall windows with multiple panes allow natural daylight to filter through, creating a diffused lighting effect that bathes the scene in a dreamy ambiance. A traditional radiator runs horizontally beneath the window frame, its ribbed surface casting intricate shadows. Through the sheer curtains, glimpses of bare trees outside suggest an autumn or winter setting. The color palette includes muted tones like slate gray (#4d6259), powder blue (#95b0af), and taupe (#8c9382), contributing to the somber yet mystical atmosphere. To the right, part of another room is visible, showing some furniture including a wooden chair. The overall mood is one of introspection and tranquility, enhanced by the low-key lighting and high contrast between the bright candlelight and the surrounding darkness. The composition balances the celestial presence against the domestic backdrop, resulting in a captivating visual narrative that blends reality with fantasy.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the lamp in person's hands warm-colored?"}
 {'answer': 'yes', 'category': 'color', 'question': "Are person's wings white?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person standing near the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in front of the window?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person in the image looking down?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have film grain?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a chair in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the light source coming from in front of the person?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with low saturation?'}]

openai_answers: 1. Is the lamp in person's hands warm-colored?  
   - yes

2. Are person's wings white?  
   - yes

3. Is the person standing near the center of the image?  
   - n/a

4. Is the person in front of the window?  
   - yes

5. Is the person in the image looking down?  
   - n/a

6. Is the background blurred?  
   - n/a

7. Does the image have film grain?  
   - n/a

8. Is there one person in the image?  
   - yes

9. Is there a chair in the image?  
   - yes

10. Is the light source coming from in front of the person?  
    - yes

11. Does the image show indoors?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have low brightness?  
    - yes

14. Is the image color graded with low saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. There are 10 'yes' answers out of 14 questions, resulting in a score of 71.43%.

token_count: 362

caption_vocabulary_size: 246

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 128

candidate_caption: An elderly woman with deeply wrinkled skin sits on a bed in a dimly lit, rustic room, wearing a black headscarf and a gray vest over a black and white striped shirt with maroon cuffs visible underneath. Her expression is reflective as she gazes slightly to her right, with her hands resting on a lace-covered bedside table. The table holds various personal items including a framed photograph of a bearded man (labeled 'MIRCEA LUMIN BICA') with text reading 'ANULII MARE DE PECA 1905-1980' printed in beige cursive font, a white mug, a small glass globe containing a miniature house, and a potted plant. To her left are colorful pillows, one with a yellow duck design, another with blue and red patterns, and a fluffy white teddy bear partially tucked under blankets. Behind her is a tapestry with vibrant floral patterns in crimson red, forest green, ivory white, sky blue, midnight blue, and charcoal gray against a dark background, adorned with religious iconography. A large framed painting depicting a classical scene with several figures is prominently displayed above. Smaller icons and pictures are attached to the wall around the main tapestry, contributing to the warm, nostalgic atmosphere. Natural light streams through a window draped with yellow curtains featuring blue floral designs, illuminating parts of the room and casting soft shadows. The overall mood is contemplative and serene, enhanced by the balanced exposure and moderate contrast, capturing a moment of quiet reflection in this cozy, traditional setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the headscarf black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the top pillow white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the woman seated in the left half of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the icon on the wall?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there a cup on the table?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the plant located on the table?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look contemplative?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person large compared to the objects on the table?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the pillows rectangular?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the woman's hand on the table?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is the color of the headscarf black?  
   - yes

2. Is the top pillow white?  
   - n/a

3. Is the woman seated in the left half of the image?  
   - n/a

4. Is the icon on the wall?  
   - yes

5. Is there a cup on the table?  
   - yes

6. Is the plant located on the table?  
   - yes

7. Does the person look contemplative?  
   - yes

8. Is the background sharp?  
   - n/a

9. Is the person large compared to the objects on the table?  
   - n/a

10. Are the pillows rectangular?  
    - yes

11. Is the woman's hand on the table?  
    - yes

12. Is the image indoors?  
    - yes

13. Is the image a photograph?  
    - n/a

14. Does the image have low brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. In this case, 10 out of 14 questions were answered with 'yes', resulting in a score of 71.43%.

token_count: 313

caption_vocabulary_size: 211

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 130

candidate_caption: A cinematic scene from the movie 'Joker', featuring actor Joaquin Phoenix as The Joker, standing on an elevated surface in the center of a chaotic city street at night. He is dressed in a striking crimson red suit with notched lapels, paired with a mustard yellow waistcoat and a dark green shirt underneath. His shoulder-length curly hair appears wet and disheveled, and his face is painted white with bold red clown makeup including a wide smile and dark circles around the eyes. Joker's expression is intense and focused, looking downward slightly to the left. His arms are outstretched; one arm extends forward while the other is raised higher, creating a dynamic pose. To his right, there is a partially visible white ambulance with its emergency lights flashing red and blue, adding to the urgency of the scene. The vehicle's interior shows glimpses of the driver's hand gripping the steering wheel. In the midground, a large crowd of people, many wearing masks or face paint resembling the Joker character, are seen cheering, raising their hands, and holding up signs. Some hold white banners or flags, contributing to the atmosphere of excitement and chaos. Smoke or fog fills the air, obscuring parts of the background and enhancing the tense mood. The setting is a bustling urban environment with tall buildings, illuminated windows, and various neon signs creating a vibrant yet eerie ambiance. One prominent sign reads "CAFE" in block letters, while another displays "ROCKS". Streetlights cast warm light across the scene, emphasizing the high contrast between bright areas and deep shadows. The overall color palette includes rich shades of crimson red, amber yellow, forest green, charcoal black, and pale skin tones, with low luminance and high saturation, enhancing the dramatic effect. The composition creates a sense of depth and movement, capturing the raw emotion and intensity of this pivotal moment in the film.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the person's suit red?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the ambulance car to the left of the person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person appear to be joyful?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'no', 'category': 'proper noun', 'question': "Is the actor's name Joaquin Phoenix?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the person's right hand extended forward?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a crowd of people in the background?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the person's suit red?  
   - yes

2. Is the person in the center of the image?  
   - yes

3. Is the ambulance car to the left of the person?  
   - no

4. Does the person appear to be joyful?  
   - no

5. Is the background blurred?  
   - n/a

6. Is the actor's name Joaquin Phoenix?  
   - yes

7. Is the person's right hand extended forward?  
   - yes

8. Is there a crowd of people in the background?  
   - yes

9. Does the image show outdoors?  
   - yes

10. Is the image a shot from a film?  
    - yes

11. Does the image have high contrast?  
    - yes

12. Is the image color graded with high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 12  

Score = (9/12) × 100 = 75

score: 75.0

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 9 correct answers out of 12 questions, resulting in a score of 75%.

token_count: 379

caption_vocabulary_size: 245

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 133

candidate_caption: A landscape photograph captures an adventurous scene in Patagonia, Chile or Argentina, featuring a vast, open field with sparse vegetation dominated by dry yellowish-green grasses and patches of burnt orange-brown shrubs. The foreground showcases various low-lying plants, including small evergreen bushes with dark green leaves and thin brown stems, creating a rich texture across the scene. In the midground stands a person facing away from the camera, dressed in a bright blue quilted puffer jacket with horizontal stitching patterns, its fabric slightly textured and reflective under natural light. The hood is up, obscuring their face, but revealing a black glove on one hand as they hold a DSLR or mirrorless camera to their eye, likely capturing the stunning vista before them. Their charcoal gray pants feature a practical front pocket secured by a yellow zipper, from which a dark gray pouch hangs with a prominent silver clasp. A small utility belt with multiple pockets adorns their waist, containing essential items. Surrounding them are dense forests of tall pine trees, some appearing dead or dormant, with bare branches adding vertical lines to the composition. The background is dominated by imposing snow-capped mountains rising sharply from the valley floor, their rugged peaks covered in white snow and jagged ridges highlighted against the overcast sky. One prominent glacier flows between steep slopes, its surface partially obscured by mist and clouds, enhancing the sense of depth and isolation. Wisps of fog gently diffuse the lower parts of the mountain range, while scattered tree tops emerge through gaps between the peaks, contributing to the dramatic effect. The lighting is soft and diffused due to the cloudy weather, casting gentle shadows across the entire scene. The color palette includes shades of azure blue (RGB(126, 161, 178)), forest green (RGB(47, 46, 34)), earthy browns (RGB(101, 82, 63), RGB(105, 93, 66)), muted yellows (RGB(138, 123, 72)), slate grays (RGB(99, 94, 98)), and cool blues (RGB(79, 125, 156), RGB(92, 129, 165)). The overall mood is tranquil yet adventurous, emphasizing the vastness and beauty of nature while capturing the essence of outdoor exploration in this pristine wilderness setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the person's jacket blue?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person standing in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the mountains behind the person?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person looking at the mountains?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image showing outdoors?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there snow in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the mountains triangular in shape?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have natural color grading?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background slightly blurred?'}]

openai_answers: 1. Is the person's jacket blue?  
   - yes

2. Is the person standing in the center of the image?  
   - n/a

3. Are the mountains behind the person?  
   - yes

4. Is the person looking at the mountains?  
   - yes

5. Is the image showing outdoors?  
   - yes

6. Is there snow in the image?  
   - yes

7. Is there a person in the image?  
   - yes

8. Are the mountains triangular in shape?  
   - n/a

9. Does the image have natural color grading?  
   - yes

10. Is the background slightly blurred?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 10  

Score = (7/10) × 100 = 70

score: 70.0

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. There are 7 'yes' answers out of 10 questions, resulting in a score of 70%.

token_count: 475

caption_vocabulary_size: 301

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 135

candidate_caption: A black-and-white historical photograph captures an exciting scene on a sandy beach, featuring a vintage biplane in flight, a race car on the ground, and a man hanging from the aircraft's wing. The biplane, marked '145' near its tail fin and 'MABLE BODIE' along its side, is flying slightly above the ocean waves with its two wings supported by multiple struts forming an intricate lattice structure. A person hangs from one of the wings, suspended mid-air, wearing dark pants, a light-colored shirt, and shoes, seemingly performing an aerial maneuver or stunt. Below them, an early 20th-century single-seater race car with large spoked wheels and a streamlined body speeds across the smooth sand, leaving a trail behind as it moves away from the camera. The car bears the number '10' prominently displayed at its rear. The driver is visible inside the vehicle, facing forward. In the foreground, part of another vehicle is blurred due to motion. The background shows a calm sea meeting the horizon under a partly cloudy sky, with gentle waves rolling onto the shore. Faint structures are barely discernible along the right edge of the coastline, adding depth to the composition. The natural daylight provides even illumination throughout the scene, highlighting the subjects against the bright backdrop. The overall mood is adventurous and dynamic, capturing a moment of high energy and thrill typical of early aviation photography. The image exhibits noticeable graininess characteristic of older photographic techniques, contributing to its vintage appearance.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there text on the airplane?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the image in black and white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the car in the center right of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person hanging under the airplane?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the part of the car in the right part of the image blurred?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have some visible scratches?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there an airplane in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is there text on the airplane? - yes
   - Is the image in black and white? - yes
   - Is the car in the center right of the image? - n/a
   - Is the person hanging under the airplane? - yes
   - Is the part of the car in the right part of the image blurred? - yes
   - Does the image have some visible scratches? - n/a
   - Is there an airplane in the image? - yes
   - Is the image taken outdoors? - yes
   - Is the image a photograph? - yes

2. **Calculate Score:**

   - Number of Correct Answers: 7
   - Total Number of Questions: 9

   Score = (7/9) × 100 = 77.78

score: 77.78

reasons: The score was calculated based on the number of correct answers provided out of the total number of questions. There were 7 correct answers out of 9 questions, resulting in a score of 77.78%.

token_count: 301

caption_vocabulary_size: 198

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 142

candidate_caption: A breathtaking landscape photograph captures a tranquil winter scene during sunset or sunrise in Iceland's Arctic region. The foreground features a snow-covered field with uneven terrain, dotted with dark brown wooden fence posts arranged diagonally from bottom left to upper right. These posts support wire mesh fences that are partially obscured by the thick layer of white snow. Shadows cast by the fencing create intricate patterns across the snowy surface, adding depth to the scene. A small wooden structure, possibly a bridge or gate, is visible among the scattered debris. In the midground, rolling hills covered in snow stretch horizontally across the image, their surfaces textured with gentle slopes and ridges. Small structures like houses or barns peek through the snowfall, indicating human habitation amidst this serene wilderness. Power lines run parallel to the fence line, cutting across the landscape and creating interesting geometric shapes against the snowy backdrop. The background showcases rugged mountains with sharp peaks and jagged edges, blanketed in snow and bathed in soft sunlight. These towering peaks dominate the horizon, displaying varying shades of blue-gray (RGB(108, 130, 163)) and white (RGB(244, 246, 242)), with some areas showing exposed rock formations and shadows accentuating their contours. The sky above is a dramatic canvas dominated by large cumulus clouds with voluminous textures and layered appearances, casting dynamic shadows and highlights. These clouds vary in density and transparency, creating a gradient effect from light beige at the base to deeper grays towards the top. Through these gaps, brilliant golden rays of sunlight pierce through, producing an intense lens flare effect consisting of multiple circular light spots in hues of yellow, orange, pink, purple, and green. This phenomenon creates a surreal atmosphere, illuminating the entire scene with warm tones while contrasting sharply with the cool colors below. The color palette includes rich blues (RGB(30, 57, 116) and RGB(108, 130, 163)), crisp whites (RGB(244, 246, 242)), deep greens (RGB(34, 77, 50)), and earthy browns (RGB(79, 69, 43)), contributing to the overall vibrant yet serene mood of the image. The composition follows the rule of thirds, balancing the expansive sky with the majestic mountain range and peaceful valley below. The lighting is natural daylight, enhanced by the low angle of the sun near the horizon, which casts elongated shadows and adds warmth to the cold environment. This interplay between harsh arctic conditions and captivating visuals results in a harmonious blend of nature's raw beauty and human presence, evoking feelings of awe and tranquility characteristic of the 'Arctic Summer' phenomenon in Iceland's northernmost regions.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Are the clouds of shades of grey?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the sun in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the mountains below the clouds?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a snowy landscape?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the sun behind the mountains?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have lens flare artifacts?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than three fence posts visible in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Are the clouds of shades of grey?  
   - yes

2. Is the sun in the center of the image?  
   - n/a

3. Are the mountains below the clouds?  
   - yes

4. Does the image show a snowy landscape?  
   - yes

5. Does the image have a cool color palette?  
   - yes

6. Is the sun behind the mountains?  
   - n/a

7. Does the image have lens flare artifacts?  
   - yes

8. Are there more than three fence posts visible in the image?  
   - yes

9. Is the image a photograph?  
   - yes

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 9  

Score = (7/9) × 100 = 77.78

score: 77.78

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. There are 7 'yes' answers out of 9 questions, resulting in a score of 77.78%.

token_count: 549

caption_vocabulary_size: 329

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 146

candidate_caption: A vibrant red British-style telephone booth stands prominently on the left side of the frame, featuring clear glass windows arranged in a 12-paned grid pattern with decorative muntins above each pane. The booth's roof is topped with a golden crown emblem, symbolizing royalty, while 'URBAN BEST PRACTICES AREA' is inscribed below it in gold serif font. A small sign reading 'UBPA' appears above the door, accompanied by the organization's logo in purple and blue colors. Inside the booth, various magazines and books are displayed through the glass panes, including one titled 'APRIL' and another showing a person wearing a black jacket and white shirt. Adjacent to the phone booth is a sleek, modern silver escalator extending diagonally from the bottom right towards the top center-right of the image. This stainless steel structure has a curved shape at its beginning, transitioning into a straight line as it ascends. It features evenly spaced steps, dark gray railings, and metallic handrails that reflect light. Black structural supports angle outward from the base of the escalator, creating a dynamic composition. Behind these elements is a multi-story urban building characterized by its contemporary design, featuring alternating sections of vertical wooden slats (light brown) and large reflective glass panels framed by thin white metal borders. These windows have dark frames and some include black metal balustrades visible inside. Large windows covered in tinted or smoked glass add to the building's sophisticated appearance. The pavement beneath consists of neatly arranged rectangular gray stone tiles interspersed with smaller square grates containing metallic covers, forming a cohesive surface area. Green shrubs are planted along the edge of the walkway near the base of the escalator, adding a touch of nature to the scene. In the background, lush green trees provide a natural contrast to the modern architecture, with hints of an ongoing construction site visible, including yellow crane arms and parts of buildings under development. The sky above is clear and pale blue, suggesting fair weather. Natural daylight illuminates the entire scene evenly, highlighting architectural details and creating a bright, inviting atmosphere. The overall color palette includes vibrant shades of cherry red (#d32222), rich mahogany (#7c4b39), slate gray (#8a8f98), warm tan (#ae8971), muted taupe (#848484), and soft sage green (#9ca496), contributing to a balanced and visually appealing composition that juxtaposes traditional and contemporary elements within this urban setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text on the red phone booth?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the phone booth red?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the phone booth in front of the escalator?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the phone booth rectangular?'}]

openai_answers: 1. Is there any text on the red phone booth?  
   - yes

2. Is the phone booth red?  
   - yes

3. Is the phone booth in front of the escalator?  
   - n/a

4. Is there a tree in the image?  
   - yes

5. Does the image show outdoors?  
   - yes

6. Is the image a photograph?  
   - n/a

7. Is the phone booth rectangular?  
   - yes

**Score Calculation:**

Number of Correct Answers: 5  
Total Number of Questions: 7  

Score = (5/7) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 5 out of 7 questions were answered correctly, resulting in a score of 71.43.

token_count: 504

caption_vocabulary_size: 330

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 150

candidate_caption: A nighttime urban scene captures a bustling public square with a wide, rectangular paved area in the foreground, featuring dark gray stone tiles arranged symmetrically with visible joints. The midground showcases well-lit street lamps casting warm light across the walkway and surrounding grassy areas, illuminating people walking or standing. A large tree with dense green foliage stands to the right, its leaves brightly lit by ambient lighting, adding vibrancy to the scene. The background consists of multiple multi-story buildings, their facades illuminated by various neon signs and lights. On the left, a building displays 'first.bg' in yellow letters atop, while another features 'LEB VHC' in blue and red below it, accompanied by a blue star-like symbol within an outline. To the far right, a prominent McDonald's sign with bright golden yellow arches is visible on top of a building, creating a stark contrast against the dark sky. The central portion of the image shows more activity, with silhouettes of individuals scattered throughout the park, engaged in different activities such as sitting on benches or walking along pathways. Some people are seated at tables under storefronts, indicating commercial establishments below. The overall atmosphere is lively yet calm, characterized by low natural light complemented by artificial illumination from streetlights, building facades, and signage. The color palette includes deep blues of the night sky, amber yellows from the lights, whites from the illuminated signs, and greens from the trees, contributing to a balanced and visually appealing composition that highlights both the urban elements and the serene ambiance of the evening setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'first bg' in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the dominant color of the sky dark blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the buildings in the background?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the McDonald's logo above the buildings?"}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the image noisy?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more two buildings in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the lamp post in front of the buildings?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Is the text 'first bg' in the image?  
   - no

3. Is the dominant color of the sky dark blue?  
   - yes

4. Are the buildings in the background?  
   - yes

5. Is the McDonald's logo above the buildings?  
   - no

6. Is the image noisy?  
   - n/a

7. Are there more than two buildings in the image?  
   - yes

8. Is the lamp post in front of the buildings?  
   - yes

9. Does the image show outdoors?  
   - yes

10. Is the image a photograph?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 10  

Score = (7/10) × 100 = 70

score: 70.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 7 out of 10 questions were answered correctly, resulting in a score of 70.

token_count: 316

caption_vocabulary_size: 209

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 158

candidate_caption: A digital rendering depicts an intense cosmic scene featuring a large, bright sun dominating the upper half of the composition. The sun is rendered with intricate details, showcasing vibrant shades of fiery orange, yellow, and red hues that emphasize its dynamic surface activity. Prominent solar flares radiate outward from various points on the sun's surface, creating an electrifying atmosphere. These flares are characterized by bright loops and jagged lines extending into space, adding to the dramatic effect. The sun's texture appears turbulent and energetic, filled with complex patterns of darker areas (dark brown #7d2e0f) interspersed with lighter patches (bright orange #ff8c00) representing varying stages of combustion. A prominent halo of golden yellow light surrounds the sun, blending seamlessly into the dark background and enhancing the sense of depth. Below the celestial body lies the lower portion of a planet, likely Earth, which occupies the bottom third of the frame. This planet's surface is depicted in deep black (#000000), suggesting the presence of landmasses or oceans obscured by darkness or atmospheric density. A thin layer of greenish-yellow light emanates from the edge of the planet, transitioning into a gradient of yellow as it extends upwards. This ethereal glow creates a stark contrast against the pitch-black void of space surrounding them, emphasizing the vastness between these two celestial bodies. The background consists entirely of a dark, nearly black void dotted sparsely with small white stars scattered across the expanse, providing context to the immense scale of the scene. The overall mood is both awe-inspiring and slightly ominous, capturing the raw power and beauty of our solar system juxtaposed with the vast emptiness of outer space.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the sun bright orange?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky around the sun black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the sun in the middle of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the planet in the lower half of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the planet obstructing the sun?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background sharp and clear?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show space?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a sun in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a planet in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the color of the sun bright orange?  
   - yes

2. Is the sky around the sun black?  
   - yes

3. Is the sun in the middle of the image?  
   - no

4. Is the planet in the lower half of the image?  
   - yes

5. Is the planet obstructing the sun?  
   - n/a

6. Is the background sharp and clear?  
   - n/a

7. Does the image show space?  
   - yes

8. Is there a sun in the image?  
   - yes

9. Is there a planet in the image?  
   - yes

10. Is the image a photograph?  
    - no

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 10  

Score = (7/10) × 100 = 70

score: 70.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 7 out of 10 questions were answered correctly, resulting in a score of 70.

token_count: 343

caption_vocabulary_size: 224

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 161

candidate_caption: A vibrant underwater photograph captures a diverse coral reef scene, showcasing an adventurous snorkeler exploring its depths. The central figure, positioned in the midground on the left side of the frame, wears a light gray long-sleeve wetsuit with black pants secured by a white belt featuring a silver buckle. Their outfit is complemented by large black flippers extended behind them and modern black-framed goggles with a white lens. The diver's golden blonde hair flows freely in the water, adding to the dynamic feel of the composition. They appear to be swimming horizontally towards the right, reaching out gently towards the lush coral formations with their right hand while touching the water surface with their left arm. In the foreground, a massive expanse of corals dominates the right half of the image, displaying a stunning array of colors including deep purple, lavender, amber yellow, burnt orange, soft pink, brown, and cream hues. Various types of corals create intricate textures and patterns, ranging from branching brain corals to plate-like structures and colonial forms. Among these corals swim numerous small, brightly colored fish, primarily vivid orange and red anthias, some appearing almost translucent against the darker blue background. A striking red fish adds pops of color near the bottom right corner. The background reveals more distant coral reefs extending into the hazy blue waters, creating depth and perspective. Sunlight filters through the water from above, casting gentle beams that illuminate the entire scene and enhance the vividness of the colors. Light rays create a mesmerizing effect as they pass through the water, emphasizing the clarity and tranquility of this pristine marine ecosystem. The overall mood is serene yet adventurous, highlighting the beauty and biodiversity of the oceanic environment. The color palette includes sky blue (#a2d3f0), deep navy (#161e27), pale peach (#dfc7b9), rich brown (#624d43), sage green (#8ca190), and warm tan (#94726f), contributing to the lively atmosphere of this underwater paradise.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Are there orange fish in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': "Are the woman's flippers black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person located on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the coral reef to the right of the person?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person in the image wearing a snorkel mask?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image clear and sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the coral reef large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than five fish in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person swimming near the coral reef?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an underwater scene?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Are there orange fish in the image?  
   - yes

2. Are the woman's flippers black?  
   - yes

3. Is the person located on the left side of the image?  
   - yes

4. Is the coral reef to the right of the person?  
   - yes

5. Is the person in the image wearing a snorkel mask?  
   - n/a

6. Is the image clear and sharp?  
   - n/a

7. Is the coral reef large?  
   - yes

8. Are there more than five fish in the image?  
   - yes

9. Is there a person in the image?  
   - yes

10. Is the person swimming near the coral reef?  
    - yes

11. Does the image show an underwater scene?  
    - yes

12. Is the image a photograph?  
    - yes

13. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. The 'n/a' responses are not counted as correct answers.

token_count: 406

caption_vocabulary_size: 261

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 168

candidate_caption: A photograph of an underground subway station taken from a central perspective, showcasing a modern and vibrant design with strong neon green lighting as the primary color scheme. The foreground features a metallic gray platform edge with visible grating patterns, leading into the midground where rows of sleek, contemporary metal benches are aligned along both sides. Hanging from the ceiling are large rectangular fluorescent lights emitting bright emerald green light, arranged in a V-shaped pattern that creates a striking visual effect against the dark background. These lights form curved shapes at their edges and cast reflections on the smooth floor tiles, creating a tunnel-like atmosphere. Two digital signs hang prominently above the platform; one displays 'ELDBROCKEN' in bold red letters on a black background, while the other shows information about 'Förbiförsalning 1-2'. A white analog clock face is also present, indicating time. On the right wall, large green-tinted panels extend towards the vanishing point, reflecting the ambient glow and featuring partially legible text such as 'HAFENSTADT UNDERTBAHN' near the bottom right corner. Blurred orange and amber light trails streak across this wall, suggesting the rapid passage of a train, adding dynamic motion to the scene. In the distance, several blurred figures can be seen walking away from the camera, enhancing the sense of depth and movement. The overall composition creates a high contrast between the vivid neon greens and deep blacks, emphasizing the architectural details and modern aesthetic of the station. The lighting is artificial and cool-toned, dominated by various shades of green that contribute to the energetic mood of the space, while the floor reflects these colors, adding texture to the scene. The image has high gamma, contrast, saturation, luminance, and brightness, particularly focused around the green tones, resulting in a visually striking and almost surreal environment that captures the essence of urban transit spaces.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text 'Elbbrücken' visible in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the dominant color in the image green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a clock near the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the clock to the right of the text 'Elbbrücken'?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there light fixtures visible in the image?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image depict an indoor setting?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the text 'Elbbrücken' visible in the image?  
     - no

   - Is the dominant color in the image green?  
     - yes

   - Is there a clock near the center of the image?  
     - n/a

   - Is the clock to the right of the text 'Elbbrücken'?  
     - n/a

   - Are there light fixtures visible in the image?  
     - yes

   - Is the image color graded with high saturation?  
     - yes

   - Does the image depict an indoor setting?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 7

   Score = (5/7) × 100 = 71.43

score: 71.43

reasons: The score was calculated based on the number of correct answers provided out of the total number of questions. Five out of seven questions were answered correctly, resulting in a score of 71.43%.

token_count: 384

caption_vocabulary_size: 259

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 171

candidate_caption: A photograph captures a serene moment of a woman performing yoga on top of large, dark gray rocks in a natural setting, likely near an ocean shore. The scene is set against a dramatic backdrop of overcast sky filled with various shades of light to medium blue-gray clouds (#848f96), creating a tranquil atmosphere. The composition follows the rule of thirds, with the subject positioned slightly off-center towards the right, emphasizing both the person and the expansive landscape. In the foreground, several large, uneven rocks dominate the lower half of the frame, their surfaces showing varying textures and shades ranging from charcoal black (#1d1c19) to slate gray (#6b7272). These rocks create depth and lead the viewer's eye upwards to the central figure. The woman sits cross-legged in the lotus position, her body angled slightly forward as she holds up her arms above her head to form an elegant, symmetrical arch. She wears a vibrant orange sports bra-style top with short sleeves and matching shorts, which contrasts sharply with the muted tones of the surroundings and adds a pop of color to the scene. Her expression appears calm and focused, with eyes gazing upward, enhancing the sense of peace and meditation. Her dark hair falls freely around her face and shoulders, contrasting beautifully with her bright outfit. The lighting is soft and diffused due to the cloudy conditions, providing even illumination across the entire scene without harsh shadows or highlights, allowing all elements to be clearly visible. The overall color palette includes shades of beige (#e3ddd9), deep brown (#4a332d), warm tan (#b18160), cool teal (#7cb0ab), and forest green (#2a5c44), contributing to the balanced exposure and neutral white balance of the image. The composition creates a harmonious blend between human presence and nature, evoking feelings of tranquility and connection with the environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'position', 'question': 'Is the person sitting on a rock in the center of the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the woman's outfit orange?"}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person higher than the rocks in the foreground?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look calm?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person relatively small compared to the rocks?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the rock rounded?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with a cool palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the person sitting on a rock in the center of the image?  
   - no

2. Is the sky blue?  
   - yes

3. Is the woman's outfit orange?  
   - yes

4. Is the person higher than the rocks in the foreground?  
   - yes

5. Is the background blurred?  
   - no

6. Does the image show daylight?  
   - yes

7. Is there a person in the image?  
   - yes

8. Does the person look calm?  
   - yes

9. Is the person relatively small compared to the rocks?  
   - n/a

10. Is there only one person in the image?  
    - yes

11. Is the rock rounded?  
    - n/a

12. Is the image color graded with a cool palette?  
    - yes

13. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 10 out of 13 questions were answered correctly, resulting in a score of approximately 76.92%.

token_count: 379

caption_vocabulary_size: 247

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 181

candidate_caption: A cozy bedroom scene featuring a light wooden rectangular tray with rounded handles made of thick rope placed on a bed with light gray bedding that shows subtle wrinkles, creases, and folds. The tray contains a white ceramic bowl filled with breakfast food consisting of granola, bananas, almonds, chia seeds, coconut yogurt, and a silver fork resting horizontally across it. To the right of the bowl is a white ribbed ceramic mug containing a transparent liquid being poured from a clear glass pitcher with a black handle. The pitcher is filled with an infused tea or fruit water containing slices of orange, yellow lemons, and green herbs. A person's hand, wearing a beige long-sleeved pajama sleeve with thin horizontal stripes in shades of cream and light brown, is seen pouring the drink from above. An open MacBook Air sits on the left side of the tray, displaying the 'F.R.I.E.N.D.S' logo in black text on a white background. Small warm white fairy lights are intertwined around the tray, adding to the ambiance. An open magazine lies diagonally on the bed towards the bottom left corner, partially visible with text reading "BUSINESS NEWS" at the top in bold black sans-serif font and a full-page photo below. The headboard features a natural wood frame with visible grain patterns, complementing the neutral color palette of the room. Two large dark gray pillows are neatly arranged against the headboard, matching the slightly wrinkled sheets. The overall mood is relaxed and comfortable, enhanced by soft natural lighting coming from the left side and creating a balanced composition with medium contrast and saturation.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'FRIENDS'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the bed sheet grey?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the tray brown?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the laptop on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the food tray on the bed?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is there a plate on the tray?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the food tray large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the food tray rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two pillows?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a magazine in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is someone pouring juice into the cup?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded naturally?'}]

openai_answers: 1. Does the image contain the text 'FRIENDS'?  
   - yes

2. Is the bed sheet grey?  
   - yes

3. Is the color of the tray brown?  
   - yes

4. Is the laptop on the left side of the image?  
   - yes

5. Is the food tray on the bed?  
   - yes

6. Is there a plate on the tray?  
   - no

7. Is the food tray large?  
   - n/a

8. Is the food tray rectangular?  
   - yes

9. Are there two pillows?  
   - yes

10. Is there a magazine in the image?  
    - yes

11. Is someone pouring juice into the cup?  
    - no

12. Does the image show indoors?  
    - yes

13. Is the image a photograph?  
    - n/a

14. Is the image color graded naturally?  
    - n/a

**Score Calculation:**

Number of Correct Answers: 10  
Total Number of Questions: 14  

Score = (10/14) × 100 = 71.43

score: 71.43

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 10 out of 14 questions were answered correctly, resulting in a score of 71.43%.

token_count: 322

caption_vocabulary_size: 207

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 185

candidate_caption: A cinematic still from 'The Amazing Spider-Man' features Andrew Garfield as Spider-Man, positioned on the right side of the frame in a close-up shot. He wears his iconic red and black Spider-Man costume with intricate web patterns visible across the chest area, extending to cover most of his torso. His expression is serious and contemplative, with eyes looking downward and slightly parted lips revealing light pink lips. The lighting is low-key and dramatic, creating high contrast between light and shadow on his face, emphasizing the texture and details of the superhero suit while casting shadows on one side of his face. The background shows an interior room setting with dark gray walls adorned with various framed pictures, posters, and a small mirror or picture near the top-right corner. A prominent poster featuring a circular pattern is partially legible, reading "THE MIRACLE OF LIFE." To the left, there's a framed abstract artwork depicting an owl, while another poster hangs above it. A closed white door with a brass handle is visible on the far right. On the left wall, a string of small round objects, possibly decorative beads or hooks, hangs vertically. The overall mood is intense and somber, enhanced by the color palette dominated by deep reds (#3e1c22), blacks (#121312, #111516), grays (#6b6a67, #747474), and muted browns (#63555d). The scene appears to take place during dusk or nightfall, with minimal ambient light contributing to the moody atmosphere. The composition focuses primarily on Spider-Man's upper body, capturing the essence of his character within this intimate, personal moment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in front of the door?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look sad?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background wall blurred?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the actor's name Andrew Garfield?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is there a poster on the background wall?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a dark color palette?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the person wearing a red suit?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have low brightness?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Is the person on the right side of the image?  
   - yes

3. Is the person in front of the door?  
   - n/a

4. Does the person look sad?  
   - n/a

5. Is the background wall blurred?  
   - n/a

6. Is the actor's name Andrew Garfield?  
   - yes

7. Is there only one person in the image?  
   - yes

8. Is there a poster on the background wall?  
   - yes

9. Does the image show indoors?  
   - yes

10. Does the image have a dark color palette?  
    - yes

11. Is the person wearing a red suit?  
    - yes

12. Is the image a shot from a film?  
    - yes

13. Does the image have low brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 13  

Score = (10/13) × 100 ≈ 76.92

score: 76.92

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 10 out of 13 questions were answered correctly, resulting in a score of approximately 76.92%.

token_count: 332

caption_vocabulary_size: 220

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

#### Sample 187

candidate_caption: A close-up shot of a casino blackjack table, captured from an extreme close-up angle using a long lens. The focus is on two playing cards in the foreground: a King of Diamonds with intricate red, black, yellow, and white design featuring a crown motif and diamond patterns; and a 9 of Diamonds displaying nine distinct red diamond symbols arranged in three vertical columns, each containing three diamonds. These cards are partially overlapping at the bottom left corner of the frame, revealing their faces clearly. In the midground, hands are visible dealing cards on the textured beige surface of the table, which features faint geometric patterns resembling lines or waves radiating outward from the center. The background includes text printed on the table's felt surface, reading 'JACK PAYS 3 TO 2' in bold black uppercase letters near the top right, followed by ' Dealer Must Soft 17' below it in mixed case letters. Another section reads 'ONCE' in light pink capital letters. A dark purple band encircles the edge of the table, with 'PAYS' printed in white within this border. The lighting is soft and artificial, creating subtle shadows and highlights that emphasize the texture of the table and the details of the cards while maintaining a shallow depth of field. This cinematic style photograph has a balanced exposure with moderate contrast and saturation, capturing the intensity and suspense typical of a high-stakes card game setting. The color palette consists mainly of warm hues like beige (#d1b59a), brown (#514c43), and dark gray (#6f6668), contributing to the overall mood of concentration and anticipation associated with the game.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'PAYS 3 TO 2'?"}
 {'answer': 'yes', 'category': 'color', 'question': "Is the table's color beige?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the card numbers red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the king of diamonds on the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the hands at the top center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the card with number 9 above the king card?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the hand above the cards?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Soft 17'?"}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the hand placing the card on the table?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an indoor scene?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a hand in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there playing cards in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'PAYS 3 TO 2'?  
   - yes

3. Is the table's color beige?  
   - yes

4. Are the card numbers red?  
   - yes

5. Is the king of diamonds on the left side of the image?  
   - yes

6. Are the hands at the top center of the image?  
   - n/a

7. Is the card with number 9 above the king card?  
   - no

8. Is the hand above the cards?  
   - n/a

9. Is the background blurred?  
   - yes

10. Does the image contain the text 'Soft 17'?  
    - yes

11. Is the hand placing the card on the table?  
    - n/a

12. Does the image show an indoor scene?  
    - yes

13. Is there a hand in the image?  
    - yes

14. Are there playing cards in the image?  
    - yes

15. Is the image a shot from a film?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 15  

Score = (11/15) × 100 = 73.33

score: 73.33

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 15 questions were answered correctly, resulting in a score of 73.33%.

token_count: 328

caption_vocabulary_size: 210

score_bin: 70-80

evaluated_by: gpt-4o-2024-08-06

### Scores in 80-90 Bin

```python
                                     candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
5    A high-contrast, black-and-white movie poster ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     227      80-90  gpt-4o-2024-08-06
6    A high-angle aerial photograph captures an int...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     255      80-90  gpt-4o-2024-08-06
9    A movie poster for 'The Secret Life of Pets' f...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     263      80-90  gpt-4o-2024-08-06
11   A serene nature photograph features a large tr...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     203      80-90  gpt-4o-2024-08-06
15   A promotional poster advertising a Christmas s...  pg-captioner  [{'answer': 'Yes', 'category': 'text', 'questi...  ...                     255      80-90  gpt-4o-2024-08-06
17   A digital advertisement graphic designed in a ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     226      80-90  gpt-4o-2024-08-06
20   A photograph capturing a serene moment in natu...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     281      80-90  gpt-4o-2024-08-06
21   A close-up black-and-white portrait of a man w...  pg-captioner  [{'answer': 'Yes', 'category': 'position', 'qu...  ...                     199      80-90  gpt-4o-2024-08-06
30   A vibrant cartoon-style illustration of the nu...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     190      80-90  gpt-4o-2024-08-06
33   A cinematic scene from 'The Twilight Saga: Bre...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     237      80-90  gpt-4o-2024-08-06
37   A breathtaking night sky landscape photograph ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     232      80-90  gpt-4o-2024-08-06
45   A close-up portrait photograph captures a youn...  pg-captioner  [{'answer': 'Yes', 'category': 'position', 'qu...  ...                     210      80-90  gpt-4o-2024-08-06
49   A photograph of two white public buses parked ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     190      80-90  gpt-4o-2024-08-06
53   A promotional advertisement poster for 'Spring...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     254      80-90  gpt-4o-2024-08-06
67   A dynamic live performance photograph captures...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     208      80-90  gpt-4o-2024-08-06
70   A close-up animated scene from the movie 'Robi...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     251      80-90  gpt-4o-2024-08-06
79   A vibrant and synchronized group performance i...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     255      80-90  gpt-4o-2024-08-06
80   A close-up photograph of a bouquet of pink tul...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     253      80-90  gpt-4o-2024-08-06
86   The photograph captures a bustling urban scene...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     235      80-90  gpt-4o-2024-08-06
94   A dynamic photograph captures a silver sports ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     225      80-90  gpt-4o-2024-08-06
98   A striking photograph captures a bright golden...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     207      80-90  gpt-4o-2024-08-06
101  A powerful graphic design poster featuring a c...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     175      80-90  gpt-4o-2024-08-06
103  A promotional advertisement for a kids' fashio...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     244      80-90  gpt-4o-2024-08-06
106  A top-down view of two bowls filled with diffe...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     169      80-90  gpt-4o-2024-08-06
112  A minimalist photograph captures a weathered w...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     259      80-90  gpt-4o-2024-08-06
118  A striking portrait photograph of a man with v...  pg-captioner  [{'answer': 'yes', 'category': 'position', 'qu...  ...                     165      80-90  gpt-4o-2024-08-06
124  A photograph captures an urban scene dominated...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     292      80-90  gpt-4o-2024-08-06
125  A high-angle photograph captures an impressive...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     225      80-90  gpt-4o-2024-08-06
129  A photograph of a large military vehicle, like...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     200      80-90  gpt-4o-2024-08-06
141  A breathtaking landscape photograph captures a...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     252      80-90  gpt-4o-2024-08-06
145  A digital artwork featuring a pair of over-ear...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     126      80-90  gpt-4o-2024-08-06
148  A traditional Japanese woodblock print depicts...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     231      80-90  gpt-4o-2024-08-06
153  A cinematic shot from a movie scene featuring ...  pg-captioner  [{'answer': 'yes', 'category': 'position', 'qu...  ...                     237      80-90  gpt-4o-2024-08-06
154  A landscape photograph capturing a dramatic sk...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     236      80-90  gpt-4o-2024-08-06
155  A close-up photograph captures a single white ...  pg-captioner  [{'answer': 'yes', 'category': 'entity', 'ques...  ...                     183      80-90  gpt-4o-2024-08-06
157  A photograph captures a cyclist from behind as...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     237      80-90  gpt-4o-2024-08-06
162  A photograph of a modern, minimalist room with...  pg-captioner  [{'answer': 'yes', 'category': 'general', 'que...  ...                     258      80-90  gpt-4o-2024-08-06
163  An abstract photograph featuring an intense bl...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     136      80-90  gpt-4o-2024-08-06
165  A photograph capturing an expansive solar farm...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     178      80-90  gpt-4o-2024-08-06
166  A retro-style typographic design features the ...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     169      80-90  gpt-4o-2024-08-06
173  A vintage black-and-white photograph features ...  pg-captioner  [{'answer': 'yes', 'category': 'entity', 'ques...  ...                     177      80-90  gpt-4o-2024-08-06
174  A vertical landscape photograph captures a dra...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     241      80-90  gpt-4o-2024-08-06
178  A serene landscape photograph captures a vibra...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     276      80-90  gpt-4o-2024-08-06
180  A striking photograph captures a large statue ...  pg-captioner  [{'answer': 'yes', 'category': 'position', 'qu...  ...                     252      80-90  gpt-4o-2024-08-06
190  A conceptual photograph captures eight individ...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     275      80-90  gpt-4o-2024-08-06
192  An animated scene from 'The Princess and the F...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     219      80-90  gpt-4o-2024-08-06
193  A vibrant movie poster for 'Starsky & Hutch' f...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     292      80-90  gpt-4o-2024-08-06
198  A romantic wedding photograph captures an inti...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     237      80-90  gpt-4o-2024-08-06

[48 rows x 10 columns]
```

#### Sample 5

candidate_caption: A high-contrast, black-and-white movie poster for 'Nightmare Alley' featuring a close-up of Bradley Cooper's face dominating the frame. He is wearing a formal white dress shirt with a subtle textured pattern and a large, neatly tied bow tie. The lighting is dramatic, casting strong shadows that emphasize his facial features including deep-set eyes, thick eyebrows, and a slightly squinted expression. His short dark hair is styled back, revealing a forehead with prominent vertical wrinkles. A thin mustache and slight stubble are visible on his jawline, adding texture to his appearance. The background is plain light gray with a double exposure effect, creating a blurred ghostly overlay on the right side of his face, which adds depth and a surreal quality to the composition. This ethereal effect enhances the mysterious and intense mood of the poster. On the left side, cast names such as Bradley Cooper, Cate Blanchett, Toni Collette, Willem Dafoe, Richard Jenkins, Rooney Mara, Ron Perlman, Mary Steenburgen, and David Strathairn are listed in white sans-serif font. The title 'NIGHTMARE ALLEY' appears at the bottom center in bold gold serif text. Below this, additional credits and production details are presented in smaller white text, including mentions of Guillermo Del Toro as director and Searchlight Pictures as producer. At the bottom, the release information 'ONLY IN THEATERS DECEMBER 17' is displayed in bold orange text, along with the Regal logo. The overall style is highly contrasted and dramatically lit, creating a cinematic atmosphere that emphasizes the film's psychological thriller genre.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'NIGHTMARE ALLEY'?"}
 {'answer': 'yes', 'category': 'color', 'question': "Is the man's photo black and white?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the text on the bottom left side of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person in the image look serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Does the image have blurred parts?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have artifacts?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the actor's name Bradley Cooper?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the bow tie in the image angular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'NIGHTMARE ALLEY' located below the names of the actors?"}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a monochromatic color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a movie poster?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'NIGHTMARE ALLEY'?  
   - yes

3. Is the man's photo black and white?  
   - yes

4. Is the text on the bottom left side of the image?  
   - n/a

5. Does the person in the image look serious?  
   - yes

6. Does the image have blurred parts?  
   - yes

7. Does the image have artifacts?  
   - n/a

8. Is the actor's name Bradley Cooper?  
   - yes

9. Is the bow tie in the image angular?  
   - yes

10. Is there one person in the image?  
    - yes

11. Is there a person in the image?  
    - yes

12. Is the text 'NIGHTMARE ALLEY' located below the names of the actors?  
    - yes

13. Does the image have a monochromatic color palette?  
    - yes

14. Is the image a movie poster?  
    - yes

15. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 13  
Total Number of Questions: 15  

Score = (13/15) × 100 = 86.67

score: 86.67

reasons: The score is calculated based on the number of correct answers provided in relation to the total number of questions. Out of 15 questions, 13 were answered correctly, resulting in a score of 86.67%.

token_count: 334

caption_vocabulary_size: 227

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 6

candidate_caption: A high-angle aerial photograph captures an intense nighttime scene of a large bonfire surrounded by dense crowds, creating a dramatic and festive atmosphere. The central focus is on the bright flames emanating from a circular pile of burning wood and other materials, including wooden planks and pallets, emitting thick smoke that rises into the night sky. This fiery blaze dominates the composition, casting a warm glow over the surrounding area in shades of amber yellow (#d8a12c) and orange-red (#ca4e2f), contrasting starkly with the cool purples and blues (#6c5b7f) of the ambient lighting. The fire's raw energy is palpable as it illuminates the uneven, dark brown soil beneath it, which appears dry and dusty, revealing patches of mud or water stains. Radiant beams of light in vibrant colors like blue, green, purple, pink, red, and white illuminate the crowd from above and slightly behind, creating dynamic patterns across the smoke-filled air. These artificial lights enhance the visual spectacle, emphasizing the texture of the earthy ground and the movement within the crowd. The people are densely packed around the perimeter, forming concentric circles that extend outward to the edges of the frame, adding depth and scale to the scene. They are dressed in brightly colored winter clothing such as jackets, coats, scarves, hats, and gloves, suggesting cold weather conditions. Some individuals are capturing moments with smartphones or cameras, while others appear engaged in conversation or watching the fire intently. The background reveals more distant groups fading into darkness, creating a sense of vastness beyond the immediate circle. The overall mood is energetic and celebratory, emphasized by the vivid color palette dominated by warm hues against the darker surroundings. The composition follows the rule of thirds, with the bonfire occupying the lower third of the frame, drawing attention upward and outwards to the encircling crowd and extending shadows.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the fire orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the fire in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the people surrounding the fire?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the fire large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the shape of the fire roughly circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than fifty people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there fire in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the people standing around the fire?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is this an outdoor scene?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image a shot from above?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the fire orange?  
   - yes

2. Is the fire in the center of the image?  
   - n/a

3. Are the people surrounding the fire?  
   - yes

4. Is the fire large?  
   - yes

5. Is the shape of the fire roughly circular?  
   - yes

6. Are there more than fifty people in the image?  
   - yes

7. Is there fire in the image?  
   - yes

8. Are the people standing around the fire?  
   - yes

9. Is this an outdoor scene?  
   - yes

10. Is the image a photograph?  
    - n/a

11. Is the image a shot from above?  
    - yes

12. Does the image have high contrast?  
    - yes

13. Is the image color graded with high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 13  

Score = (11/13) × 100 ≈ 84.62

score: 84.62

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 13 questions were answered correctly, resulting in a score of approximately 84.62%.

token_count: 386

caption_vocabulary_size: 255

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 9

candidate_caption: A movie poster for 'The Secret Life of Pets' features a close-up view of a brown and white dog character, likely representing Chewbacca from Star Wars, occupying the right half of the frame against a plain white background. The dog's face is partially visible, focusing on his large, glossy black nose which dominates the lower part of the image with its intricate texture resembling reptile scales or rough human skin. Above the nose are his eyes, which have a slightly narrowed expression, giving him an annoyed or skeptical look. His eyebrows are thick and slightly furrowed, adding to his stern appearance. The fur around his eyes and forehead is rendered in realistic shades of warm reddish-brown with smooth transitions between colors, creating depth and dimension. A distinctive white patch outlines his eye area, forming a prominent eyebrow shape above each eye. His fur around the ears is light brown and fluffy. At the top left corner, bold black text reads 'Wonder what they do all day?' in a simple sans-serif font. Below this, there is a red rectangle containing the text 'THE SECRET LIFE OF' in white uppercase letters, followed by 'ILLUMINATION PRESENTS' in gray uppercase letters next door. Underneath these logos, the title 'PETS' is displayed in large, blocky letters colored in various shades of blue (#5e7d8e), with unique letter spacing and style. Notably, the letter 'E' contains a yellow silhouette of a cat inside a birdcage, adding an element of intrigue. Beneath the title, 'IN THEATERS AND REAL D 3D' appears in smaller blue uppercase letters, while at the bottom center, 'JULY 8' is prominently shown in bold red uppercase letters. Additional credits and information are presented in small print near the bottom left corner, including 'Illumination', 'PG rating', and 'Universal Pictures'. The overall design creates a humorous yet mysterious mood, effectively drawing attention to both the main character and the movie's release details through high contrast, vibrant colors, and balanced exposure.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'JULY 8'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color white?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the dog's nose black?"}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'Wonder what they do all day?' at the top of the image?"}
 {'answer': 'yes', 'category': 'position', 'question': "Is the dog's head in the lower part of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'The Secret Life of Pets' above the dog's head?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the dog look irritated?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the word 'Illumination' in the image?"}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the dog's nose large?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the dog's nose round?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one dog in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a dog in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show animation?'}
 {'answer': 'Yes', 'category': 'image type', 'question': 'Is the image a poster?'}
 {'answer': 'Yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'Yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'JULY 8'?  
   - yes

3. Is the background color white?  
   - yes

4. Is the dog's nose black?  
   - yes

5. Is the text 'Wonder what they do all day?' at the top of the image?  
   - yes

6. Is the dog's head in the lower part of the image?  
   - no

7. Is the text 'The Secret Life of Pets' above the dog's head?  
   - n/a

8. Does the dog look irritated?  
   - yes

9. Is the word 'Illumination' in the image?  
   - yes

10. Is the dog's nose large?  
    - yes

11. Is the dog's nose round?  
    - n/a

12. Is there one dog in the image?  
    - yes

13. Is there a dog in the image?  
    - yes

14. Does the image show animation?  
    - yes

15. Is the image a poster?  
    - yes

16. Is the image color graded with high saturation?  
    - n/a

17. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 14  
Total Number of Questions: 17  

Score = (14/17) × 100 = 82.35

score: 82.35

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 14 out of 17 questions were answered correctly, resulting in a score of 82.35%.

token_count: 421

caption_vocabulary_size: 263

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 11

candidate_caption: A serene nature photograph features a large tree as the central focus, positioned slightly off-center in the midground of the composition. The tree's thick trunk, with rough bark texture, rises from a well-maintained grassy lawn that extends into the foreground. Climbing vines adorn the trunk and branches, while dense foliage crowns extend outward, creating intricate patterns of dappled light and shadow. Sunlight filters through the leaves, casting warm highlights on both the upper canopy and lower sections of the tree, emphasizing textures and adding depth to the scene. In the background, a dense forest of various shades of green trees fills the frame, appearing darker due to less direct sunlight compared to the foreground elements. The lighting creates a striking contrast between illuminated areas and shadows, enhancing the natural beauty of this tranquil woodland setting. The overall color palette includes rich forest greens (#2c563e), deep browns (#5b4f3d), olive greens (#8a9c77 and #96965c), muted sage greens (#7b8f76 and #6b7051), golden yellows (#e0c17f), and pale yellow-green hues (#d4dd87). The composition follows the rule of thirds, with the tree's base occupying about one-third of the frame, drawing attention upwards and highlighting its grandeur within the landscape. This balanced arrangement showcases the interplay between light and shadow across different vegetation layers, resulting in an inviting and peaceful atmosphere that evokes a sense of wonder and appreciation for nature's intricate details.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background predominantly green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the tree in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the tree closer to the foreground than the background trees?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is there any artifact in the image?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the tree large?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the tree in the center standing on grass?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the background predominantly green?  
   - yes

2. Is the tree in the center of the image?  
   - no

3. Is the tree closer to the foreground than the background trees?  
   - yes

4. Is there any artifact in the image?  
   - n/a

5. Is the tree large?  
   - yes

6. Is there a tree in the image?  
   - yes

7. Is the tree in the center standing on grass?  
   - yes

8. Does the image show outdoors?  
   - yes

9. Does the image have a warm color palette?  
   - yes

10. Is the image a photograph?  
    - yes

11. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 11 questions were answered correctly, resulting in a score of 81.82.

token_count: 310

caption_vocabulary_size: 203

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 15

candidate_caption: A promotional poster advertising a Christmas sale with a festive design set against a cream-colored background (RGB(245, 240, 219)). At the top center, 'Christmas' is written in bold red cursive font, followed by 'SALE' in large forest green uppercase letters. Scattered around these texts are six distinct stylized snowflakes in varying sizes and intricate patterns, adding to the holiday theme. The main focus is a square photograph framed with a scalloped edge pattern in forest green, reminiscent of postage stamps. Within this frame, a woman stands against a vibrant cherry red backdrop, smiling warmly while holding a black smartphone horizontally in her right hand with a screen facing outward. Her left hand is raised slightly with palm open, gesturing towards something not visible in the frame. She wears a white blazer with double-breasted buttons over a white V-neck top with an asymmetrical hemline featuring two horizontal stripes - one darker and one lighter - at the center. Light blue jeans complete her outfit, and she accessorizes with a delicate gold necklace adorned with small beads or pearls. A Santa hat with red trim and white fur trim sits atop her short brown hair styled straight. Below the photo, there's a message in forest green sans-serif font that reads, 'Get discounts up to 60% off for all gadgets. Valid until the end of the month.' Beneath this text is a rectangular cerise red button (RGB(195, 45, 46)) containing the phrase 'ONLY ONLINE' in white, capitalized letters. Two triangular patterns in crimson red adorn both sides of the poster near the bottom corners, resembling stylized Christmas tree designs with alternating light and dark shades. These geometric shapes create a balanced composition and add visual interest. The overall style is modern and graphic, with high contrast between elements, creating an eye-catching and inviting appearance suitable for online promotion during the Christmas season.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'Yes', 'category': 'text', 'question': "Does the image contain the text 'Christmas SALE'?"}
 {'answer': 'Yes', 'category': 'text', 'question': "Is the text 'Get discounts up to 60% off for all gadgets.' present?"}
 {'answer': 'Yes', 'category': 'color', 'question': 'Is the background color off-white?'}
 {'answer': 'Yes', 'category': 'color', 'question': "Is the color of the text 'SALE' green?"}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'Yes', 'category': 'position', 'question': "Is the text 'Christmas SALE' above the image of the person?"}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Is the 'ONLY ONLINE' text located below the person?"}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Is the person above the 'Get discounts up to 60% off for all gadgets' text?"}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image have green triangular patterns on the sides?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the woman smiling?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the image slightly out of focus?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': "Is the red text box with 'ONLY ONLINE' rectangular?"}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the person holding a phone?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show a Christmas theme?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an advertisement?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'Christmas SALE'?  
   - yes

3. Is the text 'Get discounts up to 60% off for all gadgets.' present?  
   - yes

4. Is the background color off-white?  
   - yes

5. Is the color of the text 'SALE' green?  
   - yes

6. Is the person in the center of the image?  
   - n/a

7. Is the text 'Christmas SALE' above the image of the person?  
   - yes

8. Is the 'ONLY ONLINE' text located below the person?  
   - yes

9. Is the person above the 'Get discounts up to 60% off for all gadgets' text?  
   - yes

10. Does the image have green triangular patterns on the sides?  
    - no

11. Is the woman smiling?  
    - yes

12. Is the image slightly out of focus?  
    - n/a

13. Is the red text box with 'ONLY ONLINE' rectangular?  
    - yes

14. Is there only one person in the image?  
    - yes

15. Is there a person in the image?  
    - yes

16. Is the person holding a phone?  
    - yes

17. Does the image show a Christmas theme?  
    - yes

18. Does the image have a warm color palette?  
    - yes

19. Is the image an advertisement?  
    - yes

**Calculate Score:**

Number of Correct Answers: 17  
Total Number of Questions: 19  

Score = (17/19) × 100 = 89.47

score: 89.47

reasons: The score is calculated based on the number of correct answers provided in relation to the total number of questions. Out of 19 questions, 17 were answered correctly, resulting in a score of 89.47%.

token_count: 385

caption_vocabulary_size: 255

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 17

candidate_caption: A digital advertisement graphic designed in a cartoon style with an informative mood, featuring small moves with ease. The background is white with a subtle light brown grid pattern, framed by a goldenrod yellow border with thin lines forming squares. At the top, there's a window-like interface resembling a browser tab or application window. It has a white header with rounded corners containing 'COMPANY NAME' in bold black uppercase letters. Below this, navigation icons are present on both sides: a red circle (likely representing home), a purple dot (possibly search), two black arrow symbols pointing left and right, and a circular refresh icon accompanied by downward-pointing arrows on either side. The main text reads 'SMALL MOVES WITH EASE' in large, bold navy blue (#1b3d57) uppercase letters centered above the illustration. A cartoon-style image depicts a light gray upholstered armchair with dark gray cross patterns arranged diagonally across its backrest, partially visible through an open cardboard box. Next to it stands a mustard yellow lamp with a triangular shade and wooden base. The cardboard box itself is illustrated as having wheels, colored in goldenrod (#e8c47f) with dark navy blue outlines, creating a sense of motion. Dynamic teal and amber yellow lines surround the box, emphasizing swift movement. To the right of the box, a goldenrod yellow speech bubble contains '50% OFF' in navy blue text, promoting a discount offer. At the bottom of the image, there's a decorative checkered pattern consisting alternating navy blue and white squares, adding depth to the design. The overall composition is balanced and visually appealing, using high contrast and saturation to create an engaging and eye-catching design that effectively conveys information about easy small moves and significant discounts.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'SMALL MOVES WITH EASE'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Does the text '50% OFF' appear in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color of the main section white?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the box's color yellow?"}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'SMALL MOVES WITH EASE' in the top half of the image?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the speech bubble on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the armchair in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the lamp to the left of the armchair?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the chair large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one box in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there four wheels on the box?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a lamp in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the armchair on the box?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the text above the illustration of the box and armchair?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an advertisement?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette include warm tones?"}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'SMALL MOVES WITH EASE'?  
   - yes

3. Does the text '50% OFF' appear in the image?  
   - yes

4. Is the background color of the main section white?  
   - yes

5. Is the box's color yellow?  
   - yes

6. Is the text 'SMALL MOVES WITH EASE' in the top half of the image?  
   - yes

7. Is the speech bubble on the right side of the image?  
   - yes

8. Is the armchair in the center of the image?  
   - n/a

9. Is the lamp to the left of the armchair?  
   - yes

10. Is the chair large?  
    - n/a

11. Is there only one box in the image?  
    - yes

12. Are there four wheels on the box?  
    - n/a

13. Is there a lamp in the image?  
    - yes

14. Is the armchair on the box?  
    - yes

15. Is the text above the illustration of the box and armchair?  
    - yes

16. Is the image an advertisement?  
    - yes

17. Does the image's color palette include warm tones?  
    - yes

18. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 16  
Total Number of Questions: 18  

Score = (16/18) × 100 = 88.89

score: 88.89

reasons: The score was calculated based on the number of correct answers provided in relation to the total number of questions. Out of 18 questions, 16 were answered correctly, resulting in a score of 88.89%.

token_count: 354

caption_vocabulary_size: 226

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 20

candidate_caption: A photograph capturing a serene moment in nature, featuring a woman walking away from the camera through an open meadow dotted with small yellow wildflowers. She is dressed in a flowing white lace dress with short puffed sleeves, a fitted bodice adorned with intricate patterns including scalloped edges and raised dots, and a voluminous skirt that billows slightly as she moves. The fabric appears delicate and textured, catching the sunlight and creating gentle shadows on her figure. Her blonde hair flows freely down her back, adding to the dreamy quality of the scene. In the foreground, several fallen tree branches lie diagonally across the grassy ground, their rough textures and visible bark emphasizing the natural setting. These branches create a complex network of thin twigs and leaves, enhancing the organic feel. The midground showcases the woman walking towards the right side of the frame, her posture relaxed yet graceful, with one hand gently holding the hem of her dress while the other hangs by her side. The background consists of tall trees with thick trunks and dense foliage, some bare branches reaching upwards, casting dappled shadows over the forest floor. A clear patch of pale turquoise sky is faintly visible between the treetops on the left side, contrasting beautifully with the darker tones of the woodland. The lighting is soft and warm, likely indicating late afternoon or early evening, creating a golden hue throughout the scene. This enhances the nostalgic mood, giving the image a timeless quality reminiscent of vintage photography. The color palette includes muted earth tones such as olive green (#6b5e3f), light beige (#d0c7a1), dark brown (#4b3e36), and deep umber (#271f10). The overall composition follows the rule of thirds, with the subject positioned off-center to the right, allowing viewers' eyes to wander through the lush environment. The shallow depth of field keeps the focus on the woman while softly blurring the surrounding details, contributing to the tranquil atmosphere. The interplay of light and shadow creates a balanced exposure, highlighting the harmonious blend of human presence within this untouched natural landscape.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the dress white?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the person near the center of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the fallen tree branch in front of the person?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Does the person look happy?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Are the trees large?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person running from the camera?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the dress white?  
   - yes

2. Is the person near the center of the image?  
   - no

3. Is the fallen tree branch in front of the person?  
   - yes

4. Does the person look happy?  
   - n/a

5. Are the trees large?  
   - yes

6. Is there one person in the image?  
   - yes

7. Is there a person in the image?  
   - yes

8. Is the person running from the camera?  
   - no

9. Does the image show outdoors?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 11 questions were answered correctly, resulting in a score of 81.82%.

token_count: 425

caption_vocabulary_size: 281

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 21

candidate_caption: A close-up black-and-white portrait of a man with shoulder-length, slightly messy dark hair that falls naturally around his face, revealing striking facial features. He has a full beard with thick, textured strands in shades of charcoal gray (#2c2524), interspersed with white highlights, giving it depth and dimension. His expression is contemplative as he looks slightly downward to the right, with furrowed brows and visible lines on his forehead adding texture to his appearance. The lighting is soft and diffused, illuminating his face evenly without harsh shadows while casting gentle shadows that accentuate his features. He wears a dark suit jacket with noticeable lapels over a black shirt and matching tie, though only partially visible in the frame. Both hands are prominently positioned near his mouth, with fingers gently pressed together in a prayer-like gesture or thoughtful pose, displaying natural skin texture, subtle veins, knuckles, and fingernails. The background is heavily blurred, creating a bokeh effect that emphasizes the subject's introspective demeanor. This shallow depth of field keeps the focus entirely on him, enhancing the intimate atmosphere of the photograph. The overall mood is calm and reflective, captured through high contrast between light and shadow and balanced luminance across various shades of gray (#8e8d89, #6f6967). The composition follows the rule of thirds, positioning the subject off-center to the left, resulting in an engaging and visually appealing image.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'position', 'question': 'Is the person on the left side of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Are the person's hands near their face?"}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the person appearing thoughtful?'}
 {'answer': 'Yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': "I don't know", 'category': 'proper noun', 'question': "Is the actor's name Keanu Reeves?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person taking up half of the image?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': "Is the person's pose showing folded hands?"}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': "Is the person's face turned slightly to the right?"}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a monochrome color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the person on the left side of the image?  
   - yes

2. Are the person's hands near their face?  
   - yes

3. Is the person appearing thoughtful?  
   - yes

4. Is the background blurred?  
   - yes

5. Is the actor's name Keanu Reeves?  
   - n/a

6. Is the person taking up half of the image?  
   - n/a

7. Is the person's pose showing folded hands?  
   - yes

8. Is there only one person in the image?  
   - yes

9. Is there a person in the image?  
   - yes

10. Is the person's face turned slightly to the right?  
    - yes

11. Does the image have a monochrome color palette?  
    - yes

12. Is the image a photograph?  
    - yes

13. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 13  

Score = (11/13) × 100 ≈ 84.62

score: 84.62

reasons: The score is calculated based on the number of 'yes' answers provided, which indicates the number of correct answers. Out of 13 questions, 11 were answered 'yes', resulting in a score of approximately 84.62%.

token_count: 290

caption_vocabulary_size: 199

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 30

candidate_caption: A vibrant cartoon-style illustration of the number '2020' in bold, stylized numerals, featuring an intricate ocean wave design integrated into each digit. The numbers are arranged in a 2x2 grid pattern against a solid black background, creating high contrast. Each numeral is filled with waves, giving it a dynamic appearance reminiscent of traditional Japanese woodblock prints. The top row contains the numbers '20' and '20', while the bottom row mirrors this arrangement. The waves within the digits are depicted using various shades of blue (sky blue, navy), teal, turquoise, and white to represent foam, with curved lines forming the crest and troughs. Coral pink accents around the edges add warmth to the cool-toned palette. Inside the numerals, there's a colorful sunset or sunrise scene with gradient transitions from yellow at the top through orange near the horizon to dark blue at the bottom. Small white stars, diamonds, and cloud-like shapes adorn the sky, enhancing its whimsical nature. Pink clouds rise above the waterline on both sides of the waves, adding depth and dimension to the scene. The overall composition is centered and balanced, with even lighting and no shadows, emphasizing the flat, two-dimensional style typical of digital illustrations. A clean white outline gives the entire design a sticker-like appearance. The high saturation and brightness make the colors pop against the stark black backdrop, resulting in a cheerful, energetic, and lively mood suitable for celebrating a new decade.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text '2020'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the waves blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the text in the center of the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the image sharp?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the text large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there four numbers in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there an ocean wave in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image colorful?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a predominantly cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an illustration?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have vibrant colors?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text '2020'?  
   - yes

3. Is the background color black?  
   - yes

4. Is the color of the waves blue?  
   - yes

5. Is the text in the center of the image?  
   - yes

6. Is the image sharp?  
   - n/a

7. Is the text large?  
   - n/a

8. Are there four numbers in the image?  
   - yes

9. Is there an ocean wave in the image?  
   - yes

10. Is the image colorful?  
    - yes

11. Does the image have a predominantly cool color palette?  
    - yes

12. Is the image an illustration?  
    - yes

13. Does the image have vibrant colors?  
    - yes

14. Is the image color graded with high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 14  

Score = (12/14) × 100 = 85.71

score: 85.71

reasons: The score is calculated based on the number of correct answers out of the total questions. With 12 correct answers out of 14, the score is 85.71%.

token_count: 294

caption_vocabulary_size: 190

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 33

candidate_caption: A cinematic scene from 'The Twilight Saga: Breaking Dawn - Part 2' features Kristen Stewart as Bella Swan, positioned slightly to the left of center in the frame. She has long, wavy dark brown hair cascading over her shoulders with subtle highlights, framing her face and partially covering it. Her expression is serious, intense, and focused, with furrowed brows and slightly parted lips revealing a hint of teeth. Bella's eyes are a striking red, adding to the dramatic atmosphere. She wears a navy blue tank top with a rounded scoop neckline that fits closely around her upper body, its fabric appearing smooth and slightly reflective under soft natural light. In the midground, there are concrete steps leading downward on the left side, bordered by wooden railings with horizontal slats painted in burnt orange or amber yellow. To the right, a dense forest area with tall trees covered in mossy bark and lush green foliage extends into the background. A modern building structure with a rough-textured dark gray wall featuring faint vertical lines is visible behind the wooden fence, where a person dressed in white can be seen standing near the edge, though they are out of focus. The lighting is soft, diffused daylight, providing even illumination across the scene without harsh shadows. This creates a balanced exposure with medium contrast and saturation, contributing to the tense mood of the moment. The overall color palette includes deep greens, earthy browns, rich blues, warm yellows, and neutral grays, creating a naturalistic and somewhat somber tone. The composition follows the rule of thirds, with Bella occupying most of the foreground space, emphasizing her emotional state against the contrasting backdrop of the outdoor setting and the modern architectural elements.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': "Is the woman's top blue?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person to the left of the center of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the forest behind the woman?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Does the person look serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the wooden railing behind the woman rectangular?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the person standing outdoors?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': "Does the image's color palette have green tones?"}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the character's name Bella Swan?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the character in the foreground?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the woman's top blue?  
   - yes

2. Is the person to the left of the center of the image?  
   - yes

3. Is the forest behind the woman?  
   - yes

4. Does the person look serious?  
   - yes

5. Is the background blurred?  
   - no

6. Is the wooden railing behind the woman rectangular?  
   - yes

7. Is there only one person in the image?  
   - no

8. Is there a tree in the image?  
   - yes

9. Is the person standing outdoors?  
   - yes

10. Does the image show daylight?  
    - yes

11. Does the image's color palette have green tones?  
    - yes

12. Is the character's name Bella Swan?  
    - yes

13. Is the character in the foreground?  
    - yes

14. Is the image a shot from a film?  
    - yes

15. Does the image have high contrast?  
    - no

16. Is the image color graded with high saturation?  
    - no

**Calculate Score:**

Number of Correct Answers: 13  
Total Number of Questions: 16  

Score = (13/16) × 100 = 81.25

score: 81.25

reasons: The score is calculated based on the number of correct answers out of the total questions. With 13 correct answers out of 16, the score is 81.25%.

token_count: 342

caption_vocabulary_size: 237

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 37

candidate_caption: A breathtaking night sky landscape photograph capturing the majestic Milky Way galaxy stretching diagonally across the expansive sky, showcasing its dense cluster of stars in varying shades of midnight blue (#0e1a35), lavender purple (#7b6bc4), indigo (#3f418d), soft pink (#c88da2), and white. The foreground features rugged mountains with dark brown and charcoal gray hues, their jagged peaks creating depth and texture against the deep navy background. A prominent snow-capped peak rises centrally, adding grandeur to the scene. Perched atop one of these rocky outcroppings on the right side is an ancient structure resembling a traditional Tibetan monastery or fortress, illuminated by warm amber lights that cast a golden glow over its weathered walls. This building stands in stark contrast to the cool tones of the surrounding environment, featuring intricate details such as multiple tiers, ornate architectural elements, and small windows emitting a gentle orange-yellow light. The midground consists of more mountain ranges and rocky terrain leading up to the brightly lit edifice, while the background is dominated by the vast expanse of the star-filled sky, with countless smaller stars dotting the upper portion. Two faint diagonal lines of white streaks suggest possible meteor trails, adding dynamic movement to the celestial display. The overall composition balances natural beauty with human presence, evoking awe and tranquility through its high-contrast, vividly saturated color palette enhanced by digital enhancement techniques, emphasizing the interplay between cosmic wonder and human heritage under the tranquil yet majestic night sky.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky color dark blue and purple?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the building at the bottom right corner of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the building located below the starry sky?'}
 {'answer': 'no', 'category': 'entity size', 'question': 'Is the building large within the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one building?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a hill in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the building situated on a hill?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show night time?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the sky color dark blue and purple?  
     - yes

   - Is the building at the bottom right corner of the image?  
     - n/a

   - Is the building located below the starry sky?  
     - yes

   - Is the building large within the image?  
     - n/a

   - Is there only one building?  
     - yes

   - Is there a hill in the image?  
     - yes

   - Is the building situated on a hill?  
     - yes

   - Does the image show night time?  
     - yes

   - Does the image have a cool color palette?  
     - yes

   - Is the image a photograph?  
     - yes

   - Is the image color graded with high saturation?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 9
   - Total Number of Questions: 11

   Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 11 questions were answered correctly, resulting in a score of 81.82%.

token_count: 309

caption_vocabulary_size: 232

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 45

candidate_caption: A close-up portrait photograph captures a young woman with short, straight dark brown hair styled in a bob cut with blunt bangs framing her face, tilted slightly backward. Her head is resting on her right hand, creating an intimate and contemplative pose. The subject has striking blue eyes gazing directly at the camera with a neutral yet pensive expression, lips parted revealing a hint of teeth. She wears a white tank top with thin straps visible on her shoulder and upper arm. The lighting is soft natural daylight, illuminating her smooth skin with a warm undertone and subtle freckles scattered across her cheeks and nose. The background showcases an urban street scene in what appears to be Paris, France. Multi-story buildings characterized by numerous rectangular windows with black iron frames are visible, extending diagonally from bottom left to top right. A blurred vehicle can be seen moving along the gray asphalt road below, which runs horizontally through the midground. Metal poles line both sides of the street, contributing to the depth of field effect. The color palette includes muted tones like light beige (#c9bcb7), deep charcoal (#1d241f), warm tan (#ab8e75), sage green (#4a5b52), steel blue (#a2aab0), and olive drab (#6f7364), creating a balanced and harmonious composition. The shallow depth of field keeps the focus sharply on the subject's face while softly blurring the surroundings, emphasizing the introspective mood of the portrait.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'position', 'question': 'Is the person leaning towards the right side of the image?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Does the person appear to be looking serious?'}
 {'answer': 'Yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have film grain?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': "Is the person's head large in the image?"}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the person leaning on their arm?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the person leaning towards the right side of the image?  
     - yes

   - Does the person appear to be looking serious?  
     - yes

   - Is the background blurred?  
     - yes

   - Does the image have film grain?  
     - n/a

   - Is the person's head large in the image?  
     - yes

   - Is there only one person in the image?  
     - yes

   - Is the person leaning on their arm?  
     - yes

   - Does the image show outdoors?  
     - yes

   - Is the image a photograph?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 8
   - Total Number of Questions: 9

   Score = (8/9) × 100 = 88.89

score: 88.89

reasons: The score was calculated based on the number of correct answers provided out of the total number of questions. The person answered 8 out of 9 questions correctly, resulting in a score of 88.89%.

token_count: 301

caption_vocabulary_size: 210

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 49

candidate_caption: A photograph of two white public buses parked side by side in an outdoor lot. The foreground features the front view of these modern single-decker buses, which have clean white exteriors with prominent black-tinted windshields displaying slight reflections. The bus on the right has its door open, revealing yellow handrails inside and a visible wheelchair accessibility sign. Both buses have large rectangular windows and round headlights, creating reflections of the surroundings. The word 'evolution' appears prominently on their fronts in white sans-serif font. The license plates are clearly visible; the left bus reads 'AE57 FBC', while the right bus displays 'AE56 UTH'. The ground beneath them is uneven dirt or gravel, showing tire tracks indicating recent use or movement. In the midground, another white bus can be seen partially hidden behind the main ones, adding depth to the scene. The background showcases a partly cloudy sky transitioning from light blue at the top to warmer tones near the horizon, suggesting late afternoon or early evening. Silhouettes of trees with dense foliage frame the upper edges of the image. A teal-colored double-decker bus is visible among the greenery, providing contrast and further emphasizing the location's diversity in vehicle types. The natural daylight illuminates the entire scene evenly, highlighting the textures and details of the buses and their surroundings without casting harsh shadows.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'eVolution'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky color light blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the buses in the foreground white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the right bus closer to the camera compared to the left bus?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the left bus on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the double-decker bus behind the other buses?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': "Is the license plate of the left bus 'AE57 FBC'?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Are the buses large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the buses rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three buses in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a double-decker bus in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'eVolution' written on the front of the right bus?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'Yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'Yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the image contain the text 'eVolution'?  
   - yes

2. Is the sky color light blue?  
   - yes

3. Are the buses in the foreground white?  
   - yes

4. Is the right bus closer to the camera compared to the left bus?  
   - no

5. Is the left bus on the left side of the image?  
   - yes

6. Is the double-decker bus behind the other buses?  
   - yes

7. Is the license plate of the left bus 'AE57 FBC'?  
   - yes

8. Are the buses large?  
   - yes

9. Are the buses rectangular?  
   - yes

10. Are there three buses in the image?  
    - yes

11. Is there a double-decker bus in the image?  
    - yes

12. Is the text 'eVolution' written on the front of the right bus?  
    - yes

13. Does the image show daylight?  
    - yes

14. Does the image show outdoors?  
    - yes

15. Does the image have a cool color palette?  
    - n/a

16. Is the image a photograph?  
    - yes

17. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 15  
Total Number of Questions: 17  

Score = (15/17) × 100 = 88.24

score: 88.24

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 15 correct answers out of 17 questions, resulting in a score of 88.24%.

token_count: 272

caption_vocabulary_size: 190

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 53

candidate_caption: A promotional advertisement poster for 'Spring Beauty Salon' features a cartoon-style illustration of a smiling female stylist on the right side against a background with a large light peach (#f3b086) oval shape extending from the top left to the bottom center, creating depth without overwhelming space. The stylist has short, wavy peach-colored hair styled in a casual bun with loose strands framing her face, which is simplified with small black dots for eyes and an open-mouthed smile revealing white teeth. She wears a pale yellow V-neck t-shirt under a sky blue apron with dark teal straps, depicted in bold outlines. In her right hand, she holds a pair of black-handled silver scissors crossed over her body at chest level, while her left arm crosses over her body, gripping a teal hair straightener with its handle pointing downward. Her arms are positioned across her chest, emphasizing professionalism. The text 'Spring Beauty Salon' is prominently displayed in bold, black, rounded sans-serif font in the top left corner, arranged in three lines with each word stacked vertically. Below this, 'PROMO SERVICE 50%' appears in uppercase black letters, followed by 'www.spring.com' in smaller black text. Decorative black squiggly lines frame the edges of the poster, adding a playful touch to the design. These include two curved lines near the top corners and another zigzag line extending diagonally from the bottom right towards the upper left. A larger wave-like line extends from the bottom left corner upwards to the middle right area, curving around the subject's waist. The overall composition is balanced with bright and even lighting, using a clean white background that enhances readability. The color palette includes shades of beige (#f4e6d5), deep brown (#1e1718), warm taupe (#7c6469), soft pink (#bb9a94), and muted green (#82878b), contributing to the modern and inviting aesthetic of the ad.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text 'Spring Beauty Salon' in the image?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'PROMO SERVICE 50%' written in all caps?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color white?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's hair red?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person on the right side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'Spring Beauty Salon' at the top of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the website URL below the text 'PROMO SERVICE 50%'?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the hair of the person to the right of the text 'Spring Beauty Salon'?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the person depicted in a medium size relative to the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Does the person hold scissors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an advertisement?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image use a pastel color palette?'}]

openai_answers: 1. Is the text 'Spring Beauty Salon' in the image?  
   - yes

2. Is the text 'PROMO SERVICE 50%' written in all caps?  
   - yes

3. Is the background color white?  
   - yes

4. Is the person's hair red?  
   - no

5. Is the person on the right side of the image?  
   - yes

6. Is the text 'Spring Beauty Salon' at the top of the image?  
   - yes

7. Is the website URL below the text 'PROMO SERVICE 50%'?  
   - yes

8. Is the hair of the person to the right of the text 'Spring Beauty Salon'?  
   - yes

9. Is the person smiling?  
   - yes

10. Is the person depicted in a medium size relative to the image?  
    - n/a

11. Is there one person in the image?  
    - yes

12. Does the person hold scissors?  
    - yes

13. Is the image an advertisement?  
    - yes

14. Does the image use a pastel color palette?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 14  

Score = (12/14) × 100 = 85.71

score: 85.71

reasons: The score is calculated based on the number of correct answers out of the total questions. With 12 correct answers out of 14, the score is 85.71%.

token_count: 394

caption_vocabulary_size: 254

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 67

candidate_caption: A dynamic live performance photograph captures three performers on stage during an energetic concert or worship event. The central figure, a woman with light brown hair tied back in a low ponytail, wears a denim jacket over a light sage green dress featuring intricate white geometric patterns and ruffled tiered hemlines. She sings passionately into a black wireless microphone held close to her mouth, her eyes closed in expression and left hand gently resting near her chest. To her right stands another woman singing into a handheld microphone; she has long wavy dark brown hair and is dressed in a loose-fitting charcoal gray t-shirt with 'GRACE' printed in white text on the upper right chest area and faded blue jeans with torn knees. On the left side of the frame, a man plays an acoustic guitar while singing into his own microphone. He wears a navy blue baseball cap with a small emblem visible on its front panel, a black t-shirt with a yellow emblem on the left chest, and light steel blue jeans rolled up at the ankles. A watch adorns his left wrist as he strums the instrument. Each performer uses a mounted stand equipped with multiple devices including black tablet-like screens displaying sheet music and digital tablets. In the foreground, blurred silhouettes of raised hands from the audience add depth and context to the scene. The background features dim lighting with hints of stage equipment, including a drum set partially visible behind the guitarist. Strong artificial spotlights create high contrast, casting bright highlights on the performers against a predominantly dark backdrop, emphasizing their presence and creating a vibrant atmosphere.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background dark?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the central singer's jacket denim blue?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person playing the guitar on the left side of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person in the center smiling?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the person in the foreground blurred?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three people on the stage?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a guitar in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person at the center holding a microphone?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a performance?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high contrast?'}]

openai_answers: 1. Is the background dark?  
   - yes

2. Is the central singer's jacket denim blue?  
   - yes

3. Is there a person in the center of the image?  
   - yes

4. Is the person playing the guitar on the left side of the image?  
   - yes

5. Is the person in the center smiling?  
   - n/a

6. Is the person in the foreground blurred?  
   - yes

7. Are there three people on the stage?  
   - yes

8. Is there a guitar in the image?  
   - yes

9. Is the person at the center holding a microphone?  
   - yes

10. Does the image show a performance?  
    - yes

11. Does the image have a cool color palette?  
    - n/a

12. Is the image a photograph?  
    - yes

13. Is the image color graded with high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 13  

Score = (11/13) × 100 = 84.62

score: 84.62

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 13 questions were answered correctly, resulting in a score of 84.62.

token_count: 312

caption_vocabulary_size: 208

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 70

candidate_caption: A close-up animated scene from the movie 'Robin Hood' features two anthropomorphic characters in a regal setting. The main character, an anthropomorphic lion with golden brown fur (#8b4513), sits confidently on a wooden throne with a reddish-brown color (#7c393d). The lion wears a large mustard yellow crown adorned with vibrant gemstones including emerald green diamonds (#5ab48e), ruby red gems, and deep maroon stones, as well as smaller orange-red dots along its base. Its attire consists of a sky blue robe with a white fur-trimmed collar featuring black buttons or spots, over a light blue shirt with a subtle crisscross pattern visible at the neckline. The lion's expression is smug and contented, with closed eyes and a wide smile showing sharp teeth, emphasizing his royal demeanor. His thick, curly black mustache extends outward from both sides of his mouth, while thin whiskers are visible. To the left of the lion, behind him, there's a cheerful yellow-green snake with a coiled body wearing a teal hat with a bright orange feathered plume on top. The snake's amber yellow skin shows distinct vertical stripes and has small dark eye holes. It leans forward slightly, its mouth open revealing sharp white teeth and a red tongue sticking out playfully. Both characters are positioned on a richly colored wooden throne with visible grain patterns and curved armrests. The background consists of deep blue curtains (#336ba4) providing contrast to the foreground elements, with partially visible dark brown wooden columns or pillars adding depth to the scene. The lighting is even and flat, typical of traditional hand-drawn animation styles, highlighting the vivid colors and creating a balanced composition. The overall mood is humorous and lighthearted, with high saturation and moderate contrast enhancing the cartoonish aesthetic of this whimsical moment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the wall color blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the character sitting in the middle of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the snake to the left of the lion?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the lion smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the snake smaller than the lion?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the lion's crown circular?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two characters in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the snake wearing a small hat?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the wall color blue?  
   - yes

2. Is the character sitting in the middle of the image?  
   - n/a

3. Is the snake to the left of the lion?  
   - yes

4. Is the lion smiling?  
   - yes

5. Is the snake smaller than the lion?  
   - n/a

6. Is the lion's crown circular?  
   - n/a

7. Are there two characters in the image?  
   - yes

8. Is the snake wearing a small hat?  
   - yes

9. Does the image have a warm color palette?  
   - yes

10. Is the image from a cartoon?  
    - yes

11. Is the image color graded with high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. There are 9 'yes' answers out of 11 questions, resulting in a score of 81.82%.

token_count: 379

caption_vocabulary_size: 251

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 79

candidate_caption: A vibrant and synchronized group performance in an open-air setting, likely a sports complex or stadium in North Korea during the 1980s, captured using a Panavision Platinum camera with a wide lens. The scene features rows of participants dressed uniformly in light yellow button-up shirts adorned with subtle green vertical trim along the center seams and high collars, paired with white belts and pants, creating a striking contrast against their pale skin tones. They hold large circular flower wreaths above their heads, forming intricate patterns across the frame. These wreaths display various shades from pale peach to light orange, adding depth and texture to the composition. The foreground shows six individuals clearly visible, each raising their wreath, while the midground continues this repetitive pattern, emphasizing unity and coordination. In the background, there is a striking gradient of colors transitioning from bright yellow through orange to deep red, suggesting a vast crowd participating in the event. This colorful backdrop creates a visually dynamic atmosphere, with the red area providing stark contrast to the predominantly yellow formation behind it. The lighting is natural daylight, casting hard shadows and highlighting the vividness of the colors used throughout the scene. The overall mood is celebratory, ceremonial, and disciplined, reflecting the coordinated nature of the performance. Participants' expressions are neutral yet focused as they perform, conveying seriousness and purpose. The color palette includes rich hues such as deep maroon (#3e1d21), warm beige (#c8aa69), golden yellow (#f7de6b), earthy brown (#786947), muted gray (#747476), slate blue (#5a666c), soft lavender (#9b90a4), and forest green (#636154). The balanced gamma, medium-high saturation, and even exposure contribute to the clarity and vibrancy of the scene, capturing a moment of collective energy and cultural expression typical of large-scale public events in Asia during that era.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the people in the bottom half of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the yellow flowers in front of the red flowers?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Are the yellow flowers large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the flowers circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than ten people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there flowers in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the people holding flowers?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the background red?  
   - yes

2. Are the people in the bottom half of the image?  
   - n/a

3. Are the yellow flowers in front of the red flowers?  
   - yes

4. Are the yellow flowers large?  
   - yes

5. Are the flowers circular?  
   - yes

6. Are there more than ten people in the image?  
   - yes

7. Are there flowers in the image?  
   - yes

8. Are the people holding flowers?  
   - yes

9. Does the image show outdoors?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a photograph?  
    - n/a

12. Is the image color graded with high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 12  

Score = (10/12) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of 'yes' answers provided, which are considered correct, out of the total number of questions. There are 10 'yes' answers out of 12 questions, resulting in a score of 83.33%.

token_count: 381

caption_vocabulary_size: 255

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 80

candidate_caption: A close-up photograph of a bouquet of pink tulips partially wrapped in cream-colored paper with a deep purple section at the bottom, placed diagonally across snow-covered ground. The flowers are arranged with some buds still closed while others start to open, revealing soft pink petals transitioning from light to deeper shades towards the base. Long green stems extend outward from the bouquet, adding depth to the composition. A prominent oval-shaped label adorns the wrapping paper, featuring 'BOSCOPFIORE' in white sans-serif font against a royal blue background, surrounded by smaller text reading 'RASSOY', 'PASCAK', 'BOSCO', 'FIORE', and 'IL MIO BOSCO'. The lighting comes from the setting sun positioned in the upper right corner, casting warm golden hues over the scene and creating lens flares near the bouquet. This natural illumination enhances the serene mood, highlighting the delicate textures of both the flowers and the smooth surface of the snow beneath. In the midground, there's a blurred view of more snow-covered terrain with subtle ripples and indentations visible. The background showcases indistinct silhouettes of leafless trees and faint outlines of structures or houses against a sky transitioning from pale blue to warm yellow tones as it meets the horizon. A large tree with an intricate network of bare branches stands prominently among other indistinct shapes. The overall color palette includes light pink (#dcb1b9), deep purple (#2c195e), forest green (#7f8e6a), slate gray (#5c5c63), lavender blue (#9593ae), and rich brown (#2a2224), contributing to the tranquil winter atmosphere. The composition follows the rule of thirds, focusing primarily on the flower bouquet while maintaining balance throughout the scene. The shallow depth of field emphasizes the main subject while softly blurring the surroundings, capturing the essence of early spring in a cold environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text 'BOSCO FIORI' in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky light blue in the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bouquet of flowers in the bottom of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the building behind the flowers?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background of the image blurred?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a bouquet of flowers in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the flowers lying on snow?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the text 'BOSCO FIORI' in the image?  
   - Answer: no

2. Is the sky light blue in the image?  
   - Answer: yes

3. Is the bouquet of flowers in the bottom of the image?  
   - Answer: no

4. Is the building behind the flowers?  
   - Answer: yes

5. Is the background of the image blurred?  
   - Answer: yes

6. Is there a bouquet of flowers in the image?  
   - Answer: yes

7. Are the flowers lying on snow?  
   - Answer: yes

8. Does the image show daylight?  
   - Answer: yes

9. Does the image have a warm color palette?  
   - Answer: yes

10. Is the image a photograph?  
    - Answer: yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 10 answers were correct, resulting in a score of 80.

token_count: 392

caption_vocabulary_size: 253

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 86

candidate_caption: The photograph captures a bustling urban scene during sunset, with warm lighting casting soft shadows across the area. In the foreground, two young women stand near tram tracks on a curved sidewalk; one wears a dark plaid coat over an olive green skirt paired with black tights and navy blue ankle boots, carrying a tan shoulder bag, while the other dons a black leather jacket over a blue top, light blue distressed jeans with ripped knees, white sneakers, and listens to music through silver earphones, looking down at her smartphone. The midground features pedestrians walking along the street, some interacting with small red-and-white striped market stalls selling various items, including food kiosks under canvas tents labeled 'KUSINA TIPONA' in white text. A prominent yellow utility box stands near the stalls. Tram tracks curve diagonally from bottom left to center right, with intersecting wires above supported by ornate blue-green metal poles featuring intricate designs. A black diamond-shaped sign with a white capital 'S' is suspended between cables. The background showcases lush green trees with vibrant pink blossoms, creating a natural frame around a large neoclassical building with multiple windows, dormer windows, and decorative elements illuminated from within. To the right, an outdoor advertisement board displays 'MAESTRA' in bold white sans-serif font against a crimson red background. The sky transitions from deep periwinkle (#3e445f) at the top to soft peach and lavender hues near the horizon, with scattered clouds adding texture. The overall mood is lively yet relaxed, capturing the essence of city life as day turns to night.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'MAESTRA' visible in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky light pink and light blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the trees green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the building in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the pole with cables in the top part of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the woman with headphones standing to the right of another woman?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the tram track in the left half of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the woman with headphones looking at her phone?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Are women in the foreground slightly blurred?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the building in the background large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two women standing in the foreground?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a building in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the tram track in front of the building?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Is the text 'MAESTRA' visible in the image?  
   - yes

3. Is the sky light pink and light blue?  
   - no

4. Are the trees green?  
   - yes

5. Is the building in the center of the image?  
   - n/a

6. Is the pole with cables in the top part of the image?  
   - yes

7. Is the woman with headphones standing to the right of another woman?  
   - yes

8. Is the tram track in the left half of the image?  
   - yes

9. Is the woman with headphones looking at her phone?  
   - yes

10. Are women in the foreground slightly blurred?  
    - n/a

11. Is the building in the background large?  
    - yes

12. Are there two women standing in the foreground?  
    - yes

13. Is there a building in the image?  
    - yes

14. Is the tram track in front of the building?  
    - yes

15. Does the image show outdoors?  
    - yes

16. Does the image show daylight?  
    - no

17. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 14  
Total Number of Questions: 17  

Score = (14/17) × 100 = 82.35

score: 82.35

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 14 correct answers out of 17 questions, resulting in a score of 82.35%.

token_count: 325

caption_vocabulary_size: 235

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 94

candidate_caption: A dynamic photograph captures a silver sports car in motion, driving from left to right on an urban street at dusk or night. The car is positioned slightly off-center to the right of the frame, showcasing its sleek coupe design with aerodynamic curves. Its smooth metallic finish reflects the ambient light, creating subtle highlights that emphasize its contours. The vehicle's distinctive features include angular headlights turned on, red taillights brightly illuminated, chrome door handles, side mirrors, and alloy wheels spinning rapidly, casting blurred streaks due to movement. A black-tinted window partially obscures the driver inside. The background consists of tall buildings with illuminated windows and signs, rendered as abstract shapes and colors due to the shallow depth of field and panning technique used to capture the speed of the scene. Bright lights in amber yellow, white, pink, green, blue, purple, and magenta create horizontal lines across the frame, contributing to the sense of rapid movement and energy typical of an urban landscape at night. Additional vehicles are visible but blurred, enhancing the overall impression of high-speed activity. The color palette includes midnight blue (#1c222d), warm beige (#d0a49e), steel gray (#5b6c76), deep burgundy (#5f2b37), rich brown (#7d4a38), and soft lavender (#9f8ea3). The composition follows the rule of thirds, with the car placed towards the lower right quadrant, drawing attention while maintaining balance. The low-key lighting emphasizes the contrast between the dark surroundings and the brightly lit elements, resulting in a visually striking scene that conveys both the speed of city life and the sophisticated aesthetics of modern urban environments.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the car silver metallic?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a car in the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the car to the left of the center?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image showing the outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the car silver metallic?  
     - yes

   - Is the background blurred?  
     - yes

   - Is there a car in the image?  
     - yes

   - Is the car to the left of the center?  
     - no

   - Is the image showing the outdoors?  
     - yes

   - Is the image a photograph?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 6

   Score = (5/6) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers out of the total questions. In this case, 5 out of 6 questions were answered correctly, resulting in a score of 83.33%.

token_count: 339

caption_vocabulary_size: 225

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 98

candidate_caption: A striking photograph captures a bright golden yellow Ferrari 360 Modena parked on a snow-covered road, set against a serene winter forest landscape in the mountains of New Hampshire or Vermont. The car is positioned slightly to the right of center, facing away from the camera, showcasing its rear view with round red tail lights brightly illuminated against the overcast sky. The vehicle's vibrant color stands out vividly against the monochromatic backdrop, creating a high contrast effect. Its sleek design features prominent dual exhaust pipes and silver alloy wheels covered in light powder of snow, indicating recent movement. A distinctive green, white, and red vertical racing stripe runs down the middle of the trunk area. The license plate reads 'GATED' in bold black sans-serif font, adding to the dynamic feel. The surrounding environment includes a smooth, icy road that extends into the distance, bordered by tall trees dusted with snow. Some bare branches of birch trees with their characteristic white bark are visible among evergreen conifers covered in fresh snow, while others display dense foliage. The background reveals faint outlines of distant mountains shrouded in mist under an overcast sky filled with falling snowflakes of varying sizes, creating a soft, diffuse lighting condition across the scene. This adds texture and depth to the composition, emphasizing the wintry setting. The overall mood is calm yet adventurous, capturing the essence of automotive beauty juxtaposed with nature's serenity in this cold, snowy day.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text on the license plate 'GATED'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the car yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the road white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the yellow car on the right side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the forest located in the background of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the yellow car in front of the trees?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the license plate of the car facing the camera?'}
 {'answer': 'no', 'category': 'proper noun', 'question': 'Is the car Ferrari?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the yellow car large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the yellow car's shape aerodynamic?"}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there snow in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is snow covering the road?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a winter day?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have high contrast between the yellow car and the white snow?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'no', 'category': 'image type', 'question': 'Is the image a painting?'}
 {'answer': 'no', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'no', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'no', 'category': 'color grading', 'question': 'Does the image have a vintage color grading?'}]

openai_answers: 1. Is the text on the license plate 'GATED'?  
   - yes

2. Is the car yellow?  
   - yes

3. Is the road white?  
   - yes

4. Is the yellow car on the right side of the image?  
   - yes

5. Is the forest located in the background of the image?  
   - yes

6. Is the yellow car in front of the trees?  
   - yes

7. Is the license plate of the car facing the camera?  
   - no

8. Is the car Ferrari?  
   - yes

9. Is the yellow car large?  
   - n/a

10. Is the yellow car's shape aerodynamic?  
    - yes

11. Is there snow in the image?  
    - yes

12. Is there a tree in the image?  
    - yes

13. Is snow covering the road?  
    - yes

14. Does the image show outdoors?  
    - yes

15. Does the image show a winter day?  
    - yes

16. Does the image have a cool color palette?  
    - yes

17. Does the image have high contrast between the yellow car and the white snow?  
    - yes

18. Is the image a photograph?  
    - yes

19. Is the image a painting?  
    - no

20. Is the image from a cartoon?  
    - no

21. Does the image have high contrast?  
    - yes

22. Is the image color graded with high saturation?  
    - n/a

23. Does the image have a vintage color grading?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 19  
Total Number of Questions: 23  

Score = (19/23) × 100 ≈ 82.61

score: 82.61

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 19 correct answers out of 23 questions, resulting in a score of approximately 82.61%.

token_count: 292

caption_vocabulary_size: 207

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 101

candidate_caption: A powerful graphic design poster featuring a central composition of a one-dollar bill on fire against a textured black background with subtle grunge texture resembling worn paper or fabric. The dollar bill is partially engulfed by intense, bright flames in vivid shades of orange, yellow, and red, creating a striking contrast with its greenish hue. George Washington's portrait is clearly visible through the flames, which are rendered realistically with glowing edges and intricate details like ash gray smoke trails. Above the burning bill, large cream-colored text reads 'MONEY' in a bold, distressed sans-serif font with halftone dots transitioning from white to black. Below the dollar bill, there is cursive-style white text stating 'is not just currency,' followed by smaller uppercase serif text that reads, "IT'S THE INK THAT WRITES THE STORIES OF OUR AMBITIONS THE SILENT NARRATOR OF DREAMS AND DESIRES." A decorative barbed wire line separates this text from the bottom edge of the image. The overall style combines elements of realism and illustration, conveying a strong message about the symbolic nature of money through high contrast, vivid colors, and dramatic lighting effects.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'MONEY'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'one dollar'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'is not just currency' written in cursive font?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color grainy black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the flame color orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the dollar bill in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the text in the bottom half of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the flame on the dollar bill?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the text below the dollar bill?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the dollar bill large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the dollar bill rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one dollar bill?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a dollar bill in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the text obstructed by the flame?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show fire?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a poster?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the image contain the text 'MONEY'?  
   - yes

2. Does the image contain the text 'one dollar'?  
   - no

3. Is the text 'is not just currency' written in cursive font?  
   - yes

4. Is the background color grainy black?  
   - yes

5. Is the flame color orange?  
   - yes

6. Is the dollar bill in the center of the image?  
   - yes

7. Is the text in the bottom half of the image?  
   - yes

8. Is the flame on the dollar bill?  
   - yes

9. Is the text below the dollar bill?  
   - yes

10. Is the dollar bill large?  
    - n/a

11. Is the dollar bill rectangular?  
    - yes

12. Is there one dollar bill?  
    - yes

13. Is there a dollar bill in the image?  
    - yes

14. Is the text obstructed by the flame?  
    - n/a

15. Does the image show fire?  
    - yes

16. Is the image a poster?  
    - yes

17. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 15  
Total Number of Questions: 17  

Score = (15/17) × 100 = 88.24

score: 88.24

reasons: The score is calculated based on the number of correct answers out of the total number of questions. Out of 17 questions, 15 were answered correctly, resulting in a score of 88.24%.

token_count: 235

caption_vocabulary_size: 175

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 103

candidate_caption: A promotional advertisement for a kids' fashion sale features two children positioned in the lower half of the image, leaning on a vintage brown leather suitcase with silver metal corners and rivets. The boy, on the left, has short blonde hair and blue eyes, wearing a navy blue plaid shirt with rolled-up sleeves revealing white inner cuffs. He looks slightly towards the camera with a neutral expression. The girl, on the right, has long wavy reddish-brown hair cascading over her shoulders and bright blue eyes, also wearing a denim jacket with a black-and-white striped sleeve visible at the cuff. She is smiling warmly while wearing a straw hat with a prominent black ribbon band around its base. Both children have their arms crossed and rest them on the top of the suitcase, which shows signs of wear including slight discoloration and creases along the seams. The background is solid goldenrod yellow (#FFD700), creating a warm and inviting atmosphere. At the top of the image, bold black serif text reads 'KIDS FASHION SALE', followed by smaller uppercase letters stating 'DON'T MISS THIS MONTH'S PROMO'. On the left side, within a white arrow-shaped banner pointing to the left, large black sans-serif text displays 'UP TO -30%' against a white background. Below this promotion, the website URL 'www.fashion.com' appears in black lowercase sans-serif font. The overall style of the image is photographic with graphic elements, featuring bright and even lighting that highlights the subjects clearly without harsh shadows. The color palette includes shades of taupe (#7c6b5d), tan (#9f7a59), amber yellow (#d29e4f), steel blue (#62748e), and slate gray (#7a8291), contributing to a cheerful mood suitable for an eye-catching advertisement.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'www.fashion.com'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the text black?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'KIDS FASHION SALE' in the top center of the image?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the children in the lower part of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the boy to the left of the girl?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the 'UP TO -30%' text to the left of the children?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the girl smiling?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the suitcase large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the suitcase rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two children in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the boy leaning his arms on the suitcase?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an advertisement?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Does the image contain the text 'www.fashion.com'?  
   - yes

2. Is the background color yellow?  
   - yes

3. Is the color of the text black?  
   - yes

4. Is the text 'KIDS FASHION SALE' in the top center of the image?  
   - n/a

5. Are the children in the lower part of the image?  
   - yes

6. Is the boy to the left of the girl?  
   - yes

7. Is the 'UP TO -30%' text to the left of the children?  
   - yes

8. Is the girl smiling?  
   - yes

9. Is the suitcase large?  
   - n/a

10. Is the suitcase rectangular?  
    - yes

11. Are there two children in the image?  
    - yes

12. Is the boy leaning his arms on the suitcase?  
    - yes

13. Does the image have a warm color palette?  
    - yes

14. Is the image an advertisement?  
    - yes

15. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 15  

Score = (12/15) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 12 out of 15 questions were answered correctly, resulting in a score of 80%.

token_count: 369

caption_vocabulary_size: 244

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 106

candidate_caption: A top-down view of two bowls filled with different types of food on a blue speckled surface, creating an appetizing scene in this stylized food photography. On the right side is a large white ceramic bowl containing a savory dish of glazed chicken pieces or tofu cubes. The chunks are coated in a thick, glossy reddish-brown sauce made from soy sauce, honey, and possibly chili oil, giving them a sticky appearance. They're generously topped with vibrant green onion slices and scattered red chili flakes, adding both color and visual appeal. The chunks appear crispy on the outside while remaining juicy inside, suggesting they might be fried before being tossed in the rich sauce. To the left, there's a smaller white ceramic bowl filled to the brim with golden-brown potato fries that have a crispy exterior with visible seasonings. Both dishes are placed side by side, creating a balanced composition. A silver fork lies diagonally across the upper part of the frame near the center-right of the background. The lighting is bright and natural, coming from the top-left corner, highlighting the textures and colors of the food without casting harsh shadows. This creates a high-contrast effect that emphasizes the appetizing nature of the meals, making them look freshly prepared and ready to eat.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the table color blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bowl of fries on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bowl of fries placed to the left of the plate?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the bowl of fries large in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the plate circular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two food items in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a fork in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the fork placed near the plate?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the table color blue?  
   - yes

2. Is the bowl of fries on the left side of the image?  
   - yes

3. Is the bowl of fries placed to the left of the plate?  
   - yes

4. Is the bowl of fries large in the image?  
   - no

5. Is the plate circular?  
   - n/a

6. Are there two food items in the image?  
   - yes

7. Is there a fork in the image?  
   - yes

8. Is the fork placed near the plate?  
   - yes

9. Is the image a photograph?  
   - yes

10. Does the image have high contrast?  
    - yes

11. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of correct answers out of the total number of questions. There were 9 correct answers out of 11 questions, resulting in a score of 81.82%.

token_count: 254

caption_vocabulary_size: 169

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 112

candidate_caption: A minimalist photograph captures a weathered wooden dock extending diagonally from the left edge towards the center of the frame, creating a strong leading line. The deck is composed of rectangular planks arranged in parallel lines with visible grain patterns, knots, and slight imperfections, showcasing natural textures and signs of aging. The railings at the top feature evenly spaced horizontal slats with metal bolts securing them along their edges, adding to its rustic charm. The dock's structure includes cross braces and diagonal supports that extend over the water, with one support partially submerged near the bottom right corner. These supporting beams are made of wood with visible grain patterns and weathering, including patches of moss or algae growing on their lower sections, indicating prolonged exposure to moisture. The legs of these structures are firmly planted in the calm body of water below, which appears as a smooth expanse of deep navy blue (#131a19) transitioning into lighter steel blue tones (#9fa4b8). The water surface displays subtle ripples, creating gentle reflections of the dock beneath it, enhancing the serene atmosphere. The background consists entirely of this blurred water, occupying most of the upper two-thirds of the image, with no visible horizon line. This creates a tranquil and contemplative mood through its soft gradient effect. The lighting is diffused and even, suggesting an overcast day or twilight hours, casting minimal shadows and highlighting the texture of the wood without harsh contrasts. The color palette dominates cool hues, including muted browns (#6d5e52), slate grays (#7c898f), and charcoal blacks (#1a1610), contributing to the overall somber yet peaceful ambiance. A slightly vignette effect frames the scene, drawing attention inward and emphasizing the stillness of the moment. The composition follows the rule of thirds, with the dock positioned off-center to the left, allowing ample negative space to emphasize its isolation and connection to nature.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color in the dock brown?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the wooden structure in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the wooden structure positioned above the water?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a wooden dock in the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the water blurred?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have vignetting effect?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the color in the dock brown?  
     - yes

   - Is the wooden structure in the center of the image?  
     - no

   - Is the wooden structure positioned above the water?  
     - yes

   - Is there a wooden dock in the image?  
     - yes

   - Is the water blurred?  
     - yes

   - Does the image have vignetting effect?  
     - yes

   - Is the image taken outdoors?  
     - yes

   - Is the image a photograph?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 7
   - Total Number of Questions: 8

   Score = (7/8) × 100 = 87.5

score: 87.5

reasons: The score is calculated based on the number of correct answers out of the total questions. With 7 correct answers out of 8 questions, the score is 87.5%.

token_count: 384

caption_vocabulary_size: 259

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 118

candidate_caption: A striking portrait photograph of a man with vivid neon green skin, captured from a side angle slightly to the right. The subject's face is turned towards the camera, showcasing his well-groomed beard and mustache with subtle hints of reddish-brown color interspersed within the green paint. He wears round glasses with thin gold metal frames, which reflect some light and add an element of sophistication to his appearance. His short hair is styled neatly back, with volume at the crown and longer strands on the sides, colored in varying shades of forest green that blend seamlessly into the background. The lighting is low-key and dramatic, casting soft shadows that enhance the contours of his face while maintaining a focused illumination on the green tones. This creates high contrast between the illuminated areas and the dark surroundings. The man is dressed in a black turtleneck sweater with a smooth texture, visible ribbed pattern along the edge of the collar, and its fabric appearing tightly woven. The background consists of a dark teal-colored backdrop with a faint textured pattern, providing a stark contrast to the brightly lit subject and emphasizing the surreal quality of the scene. The overall mood is mysterious, artistic, and contemplative, enhanced by the shallow depth of field that keeps the focus solely on the subject against the plain, blurred backdrop.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'position', 'question': 'Is the person positioned on the right side of the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the person colored green?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are glass frames golden?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with green tones?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person looking serious?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the person positioned on the right side of the image?  
     - yes

   - Is the person colored green?  
     - yes

   - Are glass frames golden?  
     - yes

   - Is the image color graded with green tones?  
     - yes

   - Is the person looking serious?  
     - n/a

   - Is there a person in the image?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 6

   Score = (5/6) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers out of the total questions. Five out of six questions were answered correctly, resulting in a score of 83.33%.

token_count: 260

caption_vocabulary_size: 165

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 124

candidate_caption: A photograph captures an urban scene dominated by a large charcoal black brick building with a distinct industrial aesthetic, featuring horizontal lines on its surface indicative of a garage door or loading bay. The man standing casually against this door is positioned slightly left of center in the frame, dressed in a mustard yellow sweater over a light blue collared shirt, white pants, and olive green sneakers. He wears round glasses and has short curly dark hair, accessorized with a small crossbody camera bag hanging from his neck. His hands are tucked into the pockets of his relaxed-fit jeans, creating a contemplative pose as he looks to the right. To his right, there's a smaller black door labeled '1643' in white sans-serif font, flanked by large multi-pane windows with black metal frames. These frosted glass windows show minimal reflections and grid patterns formed by numerous thin vertical wires across their surfaces, some appearing dirty or fogged. A small yellow object, possibly a figurine or hand model, sits atop the sill inside one window, adding a touch of color. Above the main entrance, two rows of three rectangular openings each create a patterned appearance at the top of the facade. Extending horizontally near the upper portion is what appears to be a fire escape ladder. Black cylindrical objects resembling cone-shaped caps or dome-like structures sit at the base of the wall, likely serving as decorative elements or vents. In the foreground, part of a concrete sidewalk extends upwards towards the building, showing signs of wear such as cracks, stains, and patches of grass growing through the seams. Painted markings include 'NO PARKING' in red block letters on the curb, along with a white bicycle symbol indicating bike lanes. On the right edge of the image, a silver Toyota car with prominent angular headlights and a sleek design is partially visible, parked parallel to the street. The background reveals another tall building partially visible on the left side, while a curved street lamp with a gray pole stands out above the main structure. The overall mood is calm and reflective, enhanced by the soft natural daylight that evenly illuminates the scene, casting subtle shadows and highlighting textures such as the weathered asphalt, exposed brickwork, and painted brick patterns on the walls.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the number '1643' visible on the door?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the building black?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's bag black?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person standing on the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the door to the right of the person?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the window to the right and above the door?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the car on the right side of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there power lines in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the number '1643' visible on the door?  
   - yes

2. Is the building black?  
   - yes

3. Is the person's bag black?  
   - yes

4. Is there a person standing on the left side of the image?  
   - yes

5. Is the door to the right of the person?  
   - yes

6. Is the window to the right and above the door?  
   - n/a

7. Is the car on the right side of the image?  
   - yes

8. Are there power lines in the image?  
   - n/a

9. Does the image show outdoors?  
   - yes

10. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 8 out of 10 questions were answered correctly, resulting in a score of 80.

token_count: 446

caption_vocabulary_size: 292

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 125

candidate_caption: A high-angle photograph captures an impressive natural phenomenon as lava meets the ocean, showcasing the power of nature in Hawaii's Big Island. The central focus is a massive plume of white steam rising dramatically from the interaction between molten rock and seawater along the coastline. This dramatic column extends upwards from the dark volcanic shore to the overcast sky, dominating much of the frame and creating a stark contrast against the backdrop. The scene begins with black basaltic lava flowing into the ocean on the right side of the image, where it reacts with saltwater, producing large amounts of steam and hydrochloric gas. The ocean around this point shows turbulent waves crashing against the shoreline, with foam and mist created by the eruption, adding texture to its appearance. To the left, calm blue-gray waters stretch towards the horizon, bordered by a rugged coastline with dark, jagged edges indicating rocky terrain underneath. In the background, the landscape transitions into more barren land with patches of brown vegetation interspersed among dark volcanic rocks extending towards distant hills or low mountains. These formations are partially obscured by light clouds, contributing to the overall dramatic atmosphere. The sky above is filled with thick, dark gray clouds that extend across the entire top half of the image, enhancing the dramatic mood and casting a diffused light over the scene. The color palette includes shades of charcoal black, slate gray, aquamarine, and pure white, with medium contrast, saturation, luminance, and brightness levels. The lighting appears natural yet slightly dimmed due to cloud cover, emphasizing the raw energy of the volcanic activity. The composition follows a diagonal line from the bottom left (ocean) to the upper center-right (plume), capturing the dynamic interplay between Earth's fiery elements and the surrounding environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the smoke white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the smoke located in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the smoke to the right of the ocean?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the image pixelated?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the smoke large?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one body of water visible?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a cloud of smoke in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the smoke coming from the land?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the smoke white?  
   - yes

2. Is the smoke located in the center of the image?  
   - yes

3. Is the smoke to the right of the ocean?  
   - no

4. Is the background blurred?  
   - n/a

5. Is the image pixelated?  
   - n/a

6. Is the smoke large?  
   - yes

7. Is there only one body of water visible?  
   - yes

8. Is there a cloud of smoke in the image?  
   - yes

9. Is the smoke coming from the land?  
   - yes

10. Does the image show outdoors?  
    - yes

11. Does the image have a cool color palette?  
    - yes

12. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 12  

Score = (10/12) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 10 out of 12 questions were answered correctly, resulting in a score of 83.33%.

token_count: 355

caption_vocabulary_size: 225

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 129

candidate_caption: A photograph of a large military vehicle, likely a MAN truck model, taken from a front-left angle in an industrial setting. The vehicle is sandy beige or khaki-colored with rugged tires suitable for off-road conditions. The front of the vehicle features two large windshields with black windscreen wipers and orange-tinted visors. A white paper with black printed text listing "DRIVER'S INSTRUCTIONS" is visible through the windshield. The word 'MAN' is embossed on the vehicle's front panel, and the license plate reads 'PJ60 AB'. The bumper has multiple attachments including metal chains, a tow hook, and four circular headlights integrated into the lower front section. Black side mirrors extend from either side of the windshield. The vehicle has a flatbed cargo area extending towards the back, indicating its use for transporting heavy equipment. In the background, another similar vehicle can be seen further along, parked parallel to the first one. To the right side of the main vehicle stands a partially visible white semi-truck with black accents. The scene includes a light gray corrugated metal building wall with vertical panels on the left, featuring an open door and a wall-mounted light fixture above it. The sky appears overcast with patches of blue visible among soft, fluffy clouds. The ground consists of paved concrete with some dirt and debris near the base of the vehicles. The overall lighting is natural daylight under partly cloudy skies, providing even illumination across the scene and highlighting the utilitarian mood of the location.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text on the vehicle?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the text 'PJ 60 AB' appear in the image?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'MAN' visible on the vehicle?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the vehicle beige?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky visible in the image light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the vehicle in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the vehicle to the right of the white building?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there a white vehicle to the right of the main vehicle?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the vehicle large?'}
 {'answer': 'no', 'category': 'count', 'question': 'Are there two vehicles in the foreground?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a vehicle in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the main vehicle parked on the ground?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an outdoor scene?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken during the day?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is there any text on the vehicle?  
   - yes

2. Does the text 'PJ 60 AB' appear in the image?  
   - no

3. Is the text 'MAN' visible on the vehicle?  
   - yes

4. Is the color of the vehicle beige?  
   - yes

5. Is the sky visible in the image light blue?  
   - n/a

6. Is the vehicle in the center of the image?  
   - n/a

7. Is the vehicle to the right of the white building?  
   - yes

8. Is there a white vehicle to the right of the main vehicle?  
   - yes

9. Is the vehicle large?  
   - yes

10. Are there two vehicles in the foreground?  
    - no

11. Is there a vehicle in the image?  
    - yes

12. Is the main vehicle parked on the ground?  
    - yes

13. Does the image show an outdoor scene?  
    - yes

14. Is the image taken during the day?  
    - yes

15. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 13  
Total Number of Questions: 15  

Score = (13/15) × 100 = 86.67

score: 86.67

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 13 correct answers out of 15 questions, resulting in a score of 86.67%.

token_count: 303

caption_vocabulary_size: 200

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 141

candidate_caption: A breathtaking landscape photograph captures a serene crater lake nestled within rugged, rocky terrain on both sides. The foreground is dominated by uneven ground covered with moss-covered rocks of various sizes, scattered twigs, dried leaves, and patches of yellowish-brown grass. Dark charcoal gray rocks are interspersed among the vegetation, creating a rich tapestry of earthy hues including deep umber (RGB(50, 38, 32)), warm tan (RGB(174, 139, 99)), and soft beige (RGB(199, 186, 167)). A prominent cluster of moss-covered stones in the lower right corner stands out against the textured surface, illuminated by sunlight. In the midground, a calm, reflective body of water occupies the center of the composition, its surface mirroring the surrounding trees and sky. The lake's emerald green color contrasts sharply with the earthy tones of the land. Surrounding the lake are steep cliffs adorned with sparse trees showing autumnal colors or early spring foliage, including deciduous species with bare branches and coniferous trees displaying shades of forest green and light brown. These cliffs create a natural amphitheater effect around the tranquil scene. The background features tall, slender trees silhouetted against a dramatic sky filled with large, fluffy cumulus clouds. Patches of clear cerulean blue sky peek through the cloud cover, adding depth to the scene. Sunlight pours from behind these formations, casting vibrant rays that create lens flares and glows across the landscape, particularly noticeable as a striking crimson red light flare on the left side of the image. This backlighting enhances the textures and colors, giving the scene an ethereal quality and highlighting the contrast between the dark rock faces and the bright sky. The overall mood is peaceful yet awe-inspiring, enhanced by the interplay of natural elements and the dynamic lighting conditions, resulting in high contrast and saturation throughout the composition.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the water green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the sun near the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the lake below the horizon line?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Are there lens flares in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there a rocks in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the trees surrounding the lake?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show nature?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is the sky blue?  
   - yes

2. Is the water green?  
   - yes

3. Is the sun near the center of the image?  
   - n/a

4. Is the lake below the horizon line?  
   - n/a

5. Are there lens flares in the image?  
   - yes

6. Are there rocks in the image?  
   - yes

7. Are the trees surrounding the lake?  
   - yes

8. Does the image show nature?  
   - yes

9. Does the image have a warm color palette?  
   - yes

10. Is the image a photograph?  
    - yes

11. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. Out of 11 questions, 9 were answered 'yes', resulting in a score of 81.82%.

token_count: 388

caption_vocabulary_size: 252

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 145

candidate_caption: A digital artwork featuring a pair of over-ear wireless headphones with iridescent, holographic reflections in vibrant colors such as cyan, magenta, yellow, green, orange, and red. The headphones are positioned centrally within a white rectangular frame that has a subtle light pink outline, creating an abstract and futuristic composition. This frame is set against a solid black background (#0e1012) with soft vertical streaks of grayish-white light adding depth and dimension to the scene. The lighting is bright and even, highlighting the reflective surfaces of the headphones and making their colors pop against the dark backdrop. The overall style is modern and surrealistic, with high contrast between the colorful headphones and the dark surroundings, resulting in a visually striking and dynamic effect. The design creates a sense of movement and energy, emphasizing the innovative and cutting-edge nature of the product while maintaining a sophisticated aesthetic suitable for promotional or artistic purposes.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Are the headphones colorful?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the headphones in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the frame with the headphones positioned in the center of the image?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there headphones in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Are the headphones on the frame?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image a digital illustration?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. **Answer Each Question:**

   - Are the headphones colorful?  
     - yes

   - Are the headphones in the center of the image?  
     - yes

   - Is the frame with the headphones positioned in the center of the image?  
     - yes

   - Is the background blurred?  
     - no

   - Are there headphones in the image?  
     - yes

   - Are the headphones on the frame?  
     - yes

   - Is the image a digital illustration?  
     - yes

   - Is the image color graded with high saturation?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 7
   - Total Number of Questions: 8

   Score = (7/8) × 100 = 87.5

score: 87.5

reasons: The score was calculated based on the number of correct answers out of the total questions. With 7 correct answers out of 8 questions, the score is 87.5%.

token_count: 183

caption_vocabulary_size: 126

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 148

candidate_caption: A traditional Japanese woodblock print depicts a serene landscape with bamboo stalks and leaves, embodying simplicity and tranquility. The composition follows the rule of thirds, creating a balanced visual appeal. In the foreground, several elongated bamboo leaves in slate gray (#7e6b59) extend diagonally across the canvas, their pointed tips adding depth to the scene. These leaves have fine black veins running along them, contrasting sharply against the lighter background. A stylized bamboo stem dominates the left side of the midground, painted in light olive green (#84896f) with subtle horizontal lines indicating nodes or segments. The bamboo's smooth texture is rendered through delicate brushstrokes, emphasizing its organic nature. To the right, a large circular shape resembling the sun occupies most of the frame, depicted as a gradient from burnt sienna (#d37b48) at the top to ivory white (#ebe8c8) at the bottom. This warm element provides a stark contrast to the cool tones of the bamboo. The background features a soft gradient sky transitioning from off-white (#ece4ca) at the top to pale beige (#e2dcc1) near the horizon, enhancing the overall calm atmosphere. At the very bottom, there are two gentle rolling hills or wave-like formations in sage green (#858e78), adding texture and grounding the composition. The color palette includes muted shades of charcoal gray (#646464), light beige (#dcbcbc), and olive green (#84896f), contributing to the harmonious and tranquil mood of the artwork. The lighting is diffused and even throughout, providing a sense of calmness typical of traditional East Asian art. The minimalistic approach emphasizes the beauty and elegance of natural elements, inviting contemplation and evoking a peaceful atmosphere reminiscent of classical Chinese or Japanese ink wash paintings.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sun in the image orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the large orange sun near the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the orange sun behind the bamboo leaves?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there bamboo leaves in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a bamboo stalk in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a painting?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}]

openai_answers: 1. Is the sun in the image orange?  
   - yes

2. Is the large orange sun near the center of the image?  
   - no

3. Is the orange sun behind the bamboo leaves?  
   - yes

4. Are there bamboo leaves in the image?  
   - yes

5. Is there a bamboo stalk in the image?  
   - yes

6. Is the image a painting?  
   - yes

7. Does the image have a warm color palette?  
   - yes

**Calculate Score:**

Number of Correct Answers: 6  
Total Number of Questions: 7  

Score = (6/7) × 100 = 85.71

score: 85.71

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 6 out of 7 questions were answered correctly, resulting in a score of 85.71%.

token_count: 366

caption_vocabulary_size: 231

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 153

candidate_caption: A cinematic shot from a movie scene featuring two characters in an intense interaction, taken with an over-the-shoulder perspective. The main focus is on a middle-aged man with short dark hair styled slightly messy, slightly wet strands falling naturally around his forehead. He has a serious and contemplative expression, looking slightly to his left towards another person whose face is partially visible on the right edge of the frame. His skin shows fine wrinkles and texture, particularly around his eyes and forehead, adding depth to his character's appearance. Small stubble on his jawline emphasizes his rugged look. He wears a gray crew-neck shirt that appears soft and textured, illuminated by low-key lighting which casts dramatic shadows across his face, highlighting its contours and creating a high contrast effect. His features are accentuated by the teal-tinted light reflecting off his cheekbones, contrasting with the warm hues illuminating parts of his face. The background is blurred, suggesting a futuristic or industrial setting with cool-toned colors, dimly lit structures, and circular lights contributing to the mysterious atmosphere. Warm amber lights create bokeh effects against the predominantly blue-green tones, hinting at possible control panels or screens. On the far right side of the frame, there's another figure partially cut off, revealing only their shoulder-length blonde hair, implying the presence of another character in conversation. The overall mood is tense and introspective, enhanced by the low gamma, muted saturation, and neutral white balance. The color palette consists of deep charcoal (#121413), slate gray (#2c3b34), taupe (#5e544d), khaki (#6f6444), steel blue (#738886), and ecru (#ebdad1) hues, emphasizing the somber tone of the scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'position', 'question': 'Is the person on the left facing right?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person on the right side closer to the camera than the person on the left?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person on the left look serious?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is one person facing another person?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image indoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with a teal and orange palette?'}]

openai_answers: 1. Is the person on the left facing right?  
   - yes

2. Is the person on the right side closer to the camera than the person on the left?  
   - n/a

3. Does the person on the left look serious?  
   - yes

4. Is the background blurred?  
   - yes

5. Are there two people in the image?  
   - yes

6. Is one person facing another person?  
   - yes

7. Is the image indoors?  
   - n/a

8. Does the image have a cool color palette?  
   - yes

9. Is the image a shot from a film?  
   - yes

10. Is the image color graded with a teal and orange palette?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 8 out of 10 questions were answered correctly, resulting in a score of 80.

token_count: 354

caption_vocabulary_size: 237

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 154

candidate_caption: A landscape photograph capturing a dramatic sky filled with large, fluffy cumulus clouds spanning across the frame. The lower portion of the image showcases dark gray and almost black clouds with intricate textures visible in their shadows, creating depth through varying densities and shapes that appear soft yet distinct against the background. These shadowy areas add depth to the scene while maintaining a somber mood. Moving upwards, the middle section features lighter gray clouds illuminated from behind by sunlight, giving them a slightly golden hue (#b5a27d) and softer appearance as they transition into brighter shades. These partially lit clouds have more defined edges and voluminous forms, adding complexity to the composition. The uppermost part of the image is dominated by a clear expanse of deep teal blue sky (#2f4c56), free from any visible stars or celestial bodies, providing a striking contrast to the white clouds below. The lighting is natural, casting subtle highlights on the cloud edges and creating a high-contrast effect between the bright clouds and darker foreground. This interplay between light and shadow enhances the texture and form of the clouds, resulting in a visually striking scene. The overall color palette includes shades of midnight blue (#191c1e), slate blue (#204c59), teal (#48748c), and various grays, contributing to the tranquil yet dynamic atmosphere. The composition follows the rule of thirds, with the horizon line placed in the upper third of the image, allowing ample negative space above the clouds. Small wisps of smoke-like formations are visible among the clouds, particularly towards the top right corner, adding additional visual interest and enhancing the sense of movement within the static sky. The balanced exposure captures fine details in both highlights and shadows, emphasizing the serene yet powerful nature of this atmospheric view. The image has been processed with high saturation and moderate luminance, resulting in vibrant colors and an ethereal quality to the scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the sky blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the clouds in the center of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there clouds in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an outdoor scene?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have vignetting effect?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the color of the sky blue?  
     - yes

   - Are the clouds in the center of the image?  
     - yes

   - Are there clouds in the image?  
     - yes

   - Does the image show an outdoor scene?  
     - yes

   - Does the image have vignetting effect?  
     - n/a

   - Does the image have a cool color palette?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 6

   Score = (5/6) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 5 out of 6 questions were answered correctly, resulting in a score of 83.33%.

token_count: 380

caption_vocabulary_size: 236

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 155

candidate_caption: A close-up photograph captures a single white plumeria flower with a vibrant yellow center, surrounded by lush dark green leaves. The flower is centered in the frame, slightly off-center to the right, with its petals displaying subtle gradient coloration from pure white edges to soft yellow towards the center. Water droplets adorn the petals, enhancing their delicate appearance and adding a fresh, dewy look. The flower stands out prominently against the dense foliage that fills the background, creating a serene and natural atmosphere. The surrounding leaves are oval-shaped with smooth surfaces, varying in shades of forest green (#0a1b0e) and olive green (#3c5d2f). Some leaves show slight blurring due to shallow depth of field, while others appear more in focus, emphasizing the texture and sheen of the wet leaves. The lighting is low-key and diffused, likely overcast daylight or early morning light, which casts gentle shadows and highlights the textures of both the flower and leaves. This creates high contrast between the bright flower and darker surroundings, emphasizing the central subject. The overall mood is calm and tranquil, with a balanced composition and moderate saturation that emphasizes the vivid colors of the flower. The color palette includes white, lemon yellow (#d7ae6d), deep forest green, olive green, charcoal gray (#3b4034), and slate blue (#9daeb5), contributing to the image's rich, earthy tones and tranquil ambiance.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'entity', 'question': 'Is there a flower in the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the flower in the center of the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the flower white and yellow?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the flower surrounded by leaves?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image have vignetting effect?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Does the image's color palette have green tones?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoor scenery?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is there a flower in the image?  
   - yes

2. Is the flower in the center of the image?  
   - no

3. Is the flower white and yellow?  
   - yes

4. Is the flower surrounded by leaves?  
   - yes

5. Does the image have vignetting effect?  
   - n/a

6. Does the image's color palette have green tones?  
   - yes

7. Does the image show outdoor scenery?  
   - yes

8. Is the image a photograph?  
   - yes

**Calculate Score:**

Number of Correct Answers: 7  
Total Number of Questions: 8  

Score = (7/8) × 100 = 87.5

score: 87.5

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 7 out of 8 questions were answered correctly, resulting in a score of 87.5%.

token_count: 293

caption_vocabulary_size: 183

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 157

candidate_caption: A photograph captures a cyclist from behind as they ascend a sandy path with stone steps, leading towards an unseen destination. The cyclist is wearing a bright red long-sleeve jersey featuring large white circular logos on both sides, creating striking contrast against their skin tone. Below the circle logo on the lower back of the jersey is a black-and-white checkered pattern resembling racing flags or tape strips. They are also wearing black cycling tights that extend to their calves, paired with vibrant blue shoes. A white helmet with 'DEKRA' text visible in bold, sans-serif font adorns their head. The cyclist's hands grip the handlebars of a dark-colored road bike with thin tires, its frame partially visible beneath them. The foreground shows the rough texture of beige sand with visible footprints and tire tracks, indicating recent use. Flanking both sides of the staircase are dense tufts of dry grass, adding depth and texture to the scene. Weathered wooden fences run parallel to the stairs, forming a natural boundary between the vegetation and the path. At the top of the stairs stands a tall flagpole with a small flag. The sky above is overcast with light grayish-blue tones (#c3d5d3) and wispy clouds stretching across it, providing soft, diffused lighting that enhances the earthy tones of the landscape. The overall color palette includes shades of sandy brown (#b6a39e), charcoal gray (#686460), pale taupe (#ab9f90), sage green (#7a8974), steel blue (#76858a), and muted olive (#75645f). The composition follows the rule of thirds, creating a sense of journey and adventure while emphasizing the cyclist's determination and effort as they navigate this challenging terrain.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the cyclist wearing a red t-shirt?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bicycle in the lower part of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the cyclist facing away from the camera?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there grass in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there stairs in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the cyclist using a bicycle?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the bicycle on the sand?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the helmet round?'}]

openai_answers: 1. Is the cyclist wearing a red t-shirt?  
   - yes

2. Is the bicycle in the lower part of the image?  
   - n/a

3. Is the cyclist facing away from the camera?  
   - yes

4. Is there one person in the image?  
   - yes

5. Does the image show outdoors?  
   - yes

6. Is there grass in the image?  
   - yes

7. Are there stairs in the image?  
   - yes

8. Is the cyclist using a bicycle?  
   - yes

9. Is the bicycle on the sand?  
   - yes

10. Is the helmet round?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 8 out of 10 questions were answered correctly, resulting in a score of 80%.

token_count: 354

caption_vocabulary_size: 237

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 162

candidate_caption: A photograph of a modern, minimalist room with large floor-to-ceiling windows featuring dark gray frames, showcasing an outdoor view of dense foliage obscured by thick fog or mist. The foreground includes part of a wooden desk on the left side, adorned with several decorative items such as ceramic vases in muted tones of olive green and sage green, and a white remote control partially visible among other indistinct objects. The midground features a small square coffee table with a light wood top and black metal legs, positioned centrally between the bed and window. A potted succulent plant with thin, elongated leaves sits atop the table, which rests on a circular black and white patterned rug. To the right, there is a beige tufted ottoman next to the coffee table. On the far right side of the image, a comfortable-looking bed dominates the scene, covered in crumpled white sheets and multiple pillows, including one with a black geometric diamond pattern and another featuring alternating horizontal stripes. Behind the bed, more bedding in shades of off-white and taupe adds depth to the composition. The background reveals a serene outdoor landscape through the expansive glass windows, with tree branches barely discernible due to the heavy mist. Dark brown Roman blinds in warm umber (#28271f) color are partially rolled up on the windows, creating soft shadows that add texture to the space. The ceiling above has two symmetrical, cylindrical-shaped black recessed lighting fixtures mounted parallel to each other. Natural daylight filters softly through the foggy atmosphere, casting gentle shadows and highlighting textures throughout the room. The overall mood is calm and introspective, enhanced by the neutral color palette dominated by cool grays (#c2cec1), warm browns (#7e6d5a), deep blacks (#27221c), and subtle hints of pale pink (#d8c9ca). The low contrast and low saturation contribute to the tranquil ambiance of this contemporary interior design.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the table in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the table closer to the bottom of the image than the top?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a remote control in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the blinds beige?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the potted plant on the table?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Does the image show indoors?  
   - yes

2. Is the table in the center of the image?  
   - yes

3. Is the table closer to the bottom of the image than the top?  
   - yes

4. Is there a remote control in the image?  
   - yes

5. Are the blinds beige?  
   - no

6. Is the potted plant on the table?  
   - yes

7. Is the image a photograph?  
   - yes

**Calculate Score:**

Number of Correct Answers: 6  
Total Number of Questions: 7  

Score = (6/7) × 100 = 85.71

score: 85.71

reasons: The score is calculated based on the number of correct answers out of the total number of questions. With 6 correct answers out of 7 questions, the score is 85.71%.

token_count: 391

caption_vocabulary_size: 258

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 163

candidate_caption: An abstract photograph featuring an intense blend of deep teal, vibrant orange, burnt sienna, white, and crimson red hues. The central focus is a blurred face slightly to the right of center, with closed eyes and a neutral expression, rendered in warm tones that stand out against the cooler background. Surrounding this face are dynamic light trails in bright orange-yellow, creating swirling patterns throughout the composition. These glowing lines form shapes reminiscent of flowers or abstract forms, adding depth and movement to the scene. The background consists of dark blue and black colors mixed with streaks of teal and hints of light cyan, enhancing the overall abstract feel. Swirling textures and blurred elements in these cool colors add complexity to the image. The lighting is high contrast with vivid saturation, contributing to the surreal and ethereal mood. The shallow depth of field keeps the focus on the distorted facial features while maintaining a sense of motion and fluidity throughout the piece. The composition creates a dreamlike atmosphere, emphasizing movement and blending colors harmoniously to produce an artwork rich in visual intrigue and artistic expression.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is there a predominant color of orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look calm?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Do artifacts appear in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image highly abstract?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an art?'}]

openai_answers: 1. Is there a predominant color of orange?  
   - yes

2. Is the person in the center of the image?  
   - no

3. Does the person look calm?  
   - yes

4. Do artifacts appear in the image?  
   - yes

5. Is the image highly abstract?  
   - yes

6. Is the image color graded with high saturation?  
   - yes

7. Is the image an art?  
   - yes

**Calculate Score:**

Number of Correct Answers: 6  
Total Number of Questions: 7  

Score = (6/7) × 100 = 85.71

score: 85.71

reasons: The score is calculated based on the number of 'yes' responses, which are considered correct answers in this context. Out of 7 questions, 6 were answered with 'yes', resulting in a score of 85.71%.

token_count: 213

caption_vocabulary_size: 136

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 165

candidate_caption: A photograph capturing an expansive solar farm with rows of dark blue photovoltaic panels arranged in a grid-like pattern, occupying the foreground. The panels are supported by white frames, creating repetitive geometric shapes that extend diagonally from left to right, reflecting sunlight and casting subtle shadows on their surfaces. Between the solar panels, patches of dense forest green shrubbery add texture and depth to the scene. In the midground, a large industrial facility consisting of multiple white and steel gray buildings is visible, including a tall cylindrical chimney adorned with alternating horizontal red and white stripes. To the right of this structure stands a modern wind turbine, characterized by its sleek white design with three blades. Each blade features orange-red tips and extends outward symmetrically from the central column, creating Y-shaped configurations. A small rectangular section containing black text reading 'PUMA' near the top of one of the blades suggests advanced technology or monitoring equipment. The background consists of a clear sky blue (#7ba5cc) without any clouds, providing a serene backdrop that emphasizes the clean energy infrastructure. The overall composition highlights the coexistence of renewable energy sources (solar and wind) with traditional industrial structures, showcasing progress towards sustainable power generation under natural daylight conditions.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the turbine on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the wind turbine to the right of the chimney?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the chimney to the right of the building?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a chimney in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there solar panels in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three propellers on the wind turbine?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is there a building below the wind turbine?'}]

openai_answers: 1. Is the sky light blue?  
   - yes

2. Is the turbine on the right side of the image?  
   - yes

3. Is the wind turbine to the right of the chimney?  
   - yes

4. Is the chimney to the right of the building?  
   - n/a

5. Is there a chimney in the image?  
   - yes

6. Are there solar panels in the image?  
   - yes

7. Are there three propellers on the wind turbine?  
   - yes

8. Is the image taken outdoors?  
   - yes

9. Is the image a photograph?  
   - yes

10. Is there a building below the wind turbine?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 8 out of 10 questions were answered correctly, resulting in a score of 80%.

token_count: 246

caption_vocabulary_size: 178

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 166

candidate_caption: A retro-style typographic design features the motivational quote 'Goodness is the Best Virtue' in large, bold, flowing cursive script centered on an amber yellow background (RGB(249, 198, 128)). The text is rendered in burnt orange (RGB(233, 114, 39)), creating high contrast against the light background. Each word has a thick dark brown outline (RGB(94, 48, 16)) that adds depth and dimension to the composition. The letters have rounded edges typical of vintage typography, giving them a playful yet elegant appearance. The words are stacked vertically with slight spacing between each line, enhancing readability while maintaining visual impact. Decorative swirls in burnt orange surround the main text at various positions - one near the top left corner, another extending from the bottom right, and a curved element emerging from the bottom center-left. These elements add a touch of elegance without detracting from the primary message. The overall mood is uplifting, positive, and encouraging, enhanced by the warm color palette and nostalgic style reminiscent of mid-20th century graphic design. The flat lighting effect creates no shadows or highlights, focusing attention solely on the typographic elements.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Goodness is the Best Virtue'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the text in the center of the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'Virtue' in the bottom part of the image?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a digital illustration?'}]

openai_answers: 1. **Answer Each Question:**

   - "Does the image contain the text 'Goodness is the Best Virtue'?"  
     Answer: yes

   - "Is the background color yellow?"  
     Answer: yes

   - "Is the text color orange?"  
     Answer: yes

   - "Is the text in the center of the image?"  
     Answer: yes

   - "Is the text 'Virtue' in the bottom part of the image?"  
     Answer: yes

   - "Is the image a digital illustration?"  
     Answer: n/a

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 6

   Score = (5/6) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 5 out of 6 questions were answered correctly, resulting in a score of 83.33%.

token_count: 240

caption_vocabulary_size: 169

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 173

candidate_caption: A vintage black-and-white photograph features two children riding on a donkey against a plain, light-colored backdrop with subtle texture and faint vertical lines, creating a neutral setting that highlights the subjects. The donkey stands facing slightly to the left, its head turned towards the camera, showcasing a well-fitted bridle with multiple metal buckles, straps, and D-rings around its snout and ears. The animal's coat appears rough and textured, with visible mane along its back. Two children are seated on the donkey; the older child, positioned to the right, wears a white dress with puffy sleeves, a high collar, and a large bow in her curly hair tied at the sides. She holds the younger child, who sits in front of her, wearing overalls with stripes and buttons, and sandals. Both children have serious expressions. The younger child grasps the reins with both hands, while the older one places one arm protectively around the younger one. The saddle is adorned with various leather straps, including a prominent one running diagonally across the donkey's body. A thin braided rope hangs down from the saddle, adding intricate detail. The lighting is soft and even, typical of studio photography, providing clear visibility of all elements without harsh shadows. The overall mood is nostalgic and somber, capturing a moment of quiet companionship between the children and their mount.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'entity', 'question': 'Is there a donkey in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there two children in the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the donkey positioned below the children?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is one child sitting behind the other child?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image in black and white?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Are there visible scratches or marks on the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the donkey's ear pointed?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is one of the children looking serious?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the donkey saddled?'}]

openai_answers: 1. Is there a donkey in the image?  
   - yes

2. Are there two children in the image?  
   - yes

3. Is the donkey positioned below the children?  
   - yes

4. Is one child sitting behind the other child?  
   - yes

5. Is the image in black and white?  
   - yes

6. Is the image a photograph?  
   - yes

7. Are there visible scratches or marks on the image?  
   - n/a

8. Is the donkey's ear pointed?  
   - n/a

9. Is one of the children looking serious?  
   - yes

10. Is the donkey saddled?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 8 out of 10 questions were answered correctly, resulting in a score of 80.

token_count: 279

caption_vocabulary_size: 177

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 174

candidate_caption: A vertical landscape photograph captures a dramatic mountainous scene with natural daylight illuminating the entire composition, creating high contrast between light and shadow areas. The foreground features a narrow, winding dirt path (hex color #bba28f) that starts from the bottom center of the frame, leading up along a steep cliff face covered in vibrant forest green grasses (#2a3d23). The path is flanked by dense patches of evergreen shrubs on both sides, their dark olive-green needles contrasting sharply against the rocky terrain. Small yellow wildflowers are scattered throughout the lush grassy area, adding pops of color to the scene. The midground showcases a rugged cliff formation rising sharply from the left side, its rough texture highlighted by the sunlight. This jagged rock face displays intricate details of erosion patterns and visible strata, creating a sense of depth and complexity. Darker areas where soil has been exposed reveal layers of sedimentary rock beneath the surface. In the background, tall, jagged mountains dominate the view, stretching across the entire width of the image. These peaks have steep faces and sharp ridges, painted in various shades of steel blue-gray (#6c8aa0), slate gray (#67829d), and gunmetal gray (#4e646c). Patches of snow cling to their surfaces, particularly noticeable on the lower slopes and crevices, emphasizing the harsh conditions of this high-altitude environment. A clear azure sky (#5ea1bc) fills the top portion of the frame, transitioning slightly darker near the horizon due to atmospheric perspective. The overall mood is serene yet awe-inspiring, capturing the raw beauty of nature in an unspoiled wilderness setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the grass green?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the mountains gray?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the path in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the green foliage to the left of the path?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image showing outdoors?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there multiple mountains in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the path irregularly shaped?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a natural color palette?'}]

openai_answers: 1. Is the grass green?  
   - yes

2. Are the mountains gray?  
   - yes

3. Is the path in the center of the image?  
   - yes

4. Is the green foliage to the left of the path?  
   - n/a

5. Is the image showing outdoors?  
   - yes

6. Are there multiple mountains in the image?  
   - yes

7. Is the image a photograph?  
   - yes

8. Is the path irregularly shaped?  
   - yes

9. Does the image have a natural color palette?  
   - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 9  

Score = (8/9) × 100 = 88.89

score: 88.89

reasons: The score is calculated based on the number of correct answers out of the total number of questions. There were 8 correct answers out of 9 questions, resulting in a score of 88.89.

token_count: 340

caption_vocabulary_size: 241

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 178

candidate_caption: A serene landscape photograph captures a vibrant crimson-red brick building with a distinctive Gothic Revival architectural style, set against a backdrop of lush greenery on both sides. The building, likely part of the Ljubljana Castle complex in Slovenia, features multiple stories and is adorned with a turquoise-green copper roof that gleams under the bright daylight. Its facade showcases a symmetrical design with rectangular windows framed by white muntins, each divided into four smaller panes by thin dark brown wooden bars. A central tower rises above the main structure, topped with pointed red finials reminiscent of battlements or turrets. The roofline is punctuated by small chimneys and antennas. In front of this imposing edifice stands a dense array of trees and shrubs, including willows hanging over the water's edge, tall evergreens, and deciduous species displaying various shades from forest to lime green. Some plants show yellowish hues, indicating seasonal change. The foreground features a calm river or lake, its surface mirroring the surrounding foliage and sky, creating a harmonious blend of colors ranging from deep olive green (#6c5f2e) to goldenrod yellow (#d5aa4b). The sky above is a vivid cerulean blue (#7cb9ce), dotted with fluffy cumulus clouds that add depth and texture to the scene. Natural sunlight illuminates the entire composition evenly, highlighting the vivid colors without harsh shadows and casting dappled light across the tree branches. On the far right side of the image, a glimpse of another structure peeks through the treeline, while a low concrete wall runs along the shoreline. The overall color palette includes rich reds (#a54444), varied greens (#8ba26c, #3f4920, #6c5f2e), azure blues (#7cb9ce, #89b1da), and subtle purples (#7c729e), contributing to the tranquil mood of this picturesque setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the building red?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the building in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the sky in the top of the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there clouds in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there water in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the building behind the trees?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high brightness?'}]

openai_answers: 1. Is the building red?  
   - yes

2. Is the sky blue?  
   - yes

3. Is the building in the center of the image?  
   - n/a

4. Is the sky in the top of the image?  
   - n/a

5. Are there clouds in the image?  
   - yes

6. Is there water in the image?  
   - yes

7. Is the building behind the trees?  
   - yes

8. Does the image show outdoors?  
   - yes

9. Does the image show daylight?  
   - yes

10. Is the image a photograph?  
    - yes

11. Does the image have high brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, divided by the total number of questions. Out of 11 questions, 9 were answered 'yes', resulting in a score of 81.82%.

token_count: 400

caption_vocabulary_size: 276

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 180

candidate_caption: A striking photograph captures a large statue of an Indian deity, likely Lakshmi or Durga, taken from a low angle looking up. The figure is depicted with numerous arms radiating outward in a symmetrical pattern, each arm holding different symbols such as lotus flowers, spiritual objects, and instruments like drums. The central face shows a serene expression with closed eyes and slightly parted lips, painted in natural hues. Adorned with intricate golden decorations on its attire, which features a grid-like pattern of alternating white and gold squares, the statue's hands are joined in a traditional 'Anjali Mudra' prayer position at the center. The deity wears elaborate jewelry including bracelets, rings, ankle bracelets, and earrings, all highlighted by the backlighting. A small bird perches near the base of one foot, adding a touch of life to this otherwise static composition. The statue sits cross-legged, emphasizing its divine nature. The background consists of a clear sky transitioning from soft pinkish-purple (RGB(197, 171, 196)) near the horizon to deep blue (RGB(46, 62, 124)) higher up, with scattered wispy clouds visible on the right side. The sun is positioned behind the statue, creating a dramatic silhouette effect that emphasizes the contours and details of the figure while casting bright light and lens flare effects around it. This backlighting creates a halo effect around the statue, accentuating its divine aura against the contrasting sky. The overall mood is mystical and reverent, enhanced by the interplay between the illuminated edges of the statue and the darker shadows. The color palette includes shades of deep purple (RGB(29, 24, 35)), pale lavender (RGB(197, 171, 196)), muted rose (RGB(148, 102, 113)), rich brown (RGB(116, 81, 57)), and soft pink (RGB(181, 156, 180)). These colors contribute to the harmonious yet powerful visual impact of the image, capturing the essence of the deity in a moment of tranquil majesty.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'position', 'question': 'Is the statue in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the sun behind the statue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Does the image show lens flare?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than five arms visible?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the statue in the center of the image?  
     Answer: n/a

   - Is the sun behind the statue?  
     Answer: yes

   - Is the sky blue?  
     Answer: yes

   - Does the image show lens flare?  
     Answer: yes

   - Are there more than five arms visible?  
     Answer: yes

   - Does the image show outdoors?  
     Answer: yes

2. **Calculate Score:**

   - Number of Correct Answers: 5
   - Total Number of Questions: 6

   Score = (5/6) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers out of the total questions. Five out of six questions were answered correctly, resulting in a score of 83.33%.

token_count: 422

caption_vocabulary_size: 252

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 190

candidate_caption: A conceptual photograph captures eight individuals working together to paint a large wall with bright crimson red (#a03d41) paint on a stark white surface, creating a striking contrast. The scene is divided horizontally into two distinct halves, emphasizing the minimalist composition. In the foreground, three people are actively involved in painting using rollers and brushes. One person stands on a light beige wooden ladder positioned slightly left of center, wearing a vivid scarlet red top (#c92f23), black pleated skirt, knee-high black socks, and black boots while applying paint. To their right, another individual in a charcoal gray sweater over a white shirt pairs with a high-waisted black mini-skirt featuring a broad red belt, and vibrant red ankle-length socks paired with black pointed-toe shoes holds a roller brush. On the far left, a young girl wears an oversized black long-sleeve sweatshirt with a subtle sheen, a matching short pleated skirt secured by a wide scarab-colored waistband, and knee-high red socks under her black boots, reaching up to apply paint. Four additional participants can be seen in various positions around the lower half of the wall; one kneels near the bottom right corner adjusting their dark gray jacket over a lighter cream-colored dress or pants with a black belt, while others hold rollers or buckets of paint. Atop the white section towards the upper right sits two more individuals dressed casually - one in off-white attire and the other in a loose-fitting off-white sweater and black pants. Their postures suggest they might be observing or taking a break from painting. Four white plastic buckets filled with crimson red paint are strategically placed near each painter, with some tipped over and spilling. The floor beneath them matches the painted wall color, unifying the entire space. Natural, even lighting illuminates the scene without harsh shadows, enhancing the clarity of details and colors. This creates a balanced exposure that emphasizes both the collaborative effort and the visual impact of the contrasting colors. The overall mood is creative, dynamic, and engaging, capturing a moment where seven individuals come together to transform a plain wall through coordinated activity against the backdrop of the crisp red background (#b29ba8).

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background color red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a person on a ladder in the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is a person in black pants sitting on top of the wall?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person in the black skirt to the left of the person on the ladder?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the ladder tall?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the paint bucket cylindrical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than five people in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person on the ladder painting the wall?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a dominant red color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the background color red?  
   - yes

2. Is there a person on a ladder in the image?  
   - yes

3. Is a person in black pants sitting on top of the wall?  
   - yes

4. Is the person in the black skirt to the left of the person on the ladder?  
   - yes

5. Is the ladder tall?  
   - n/a

6. Is the paint bucket cylindrical?  
   - n/a

7. Are there more than five people in the image?  
   - yes

8. Is the person on the ladder painting the wall?  
   - yes

9. Does the image have a dominant red color palette?  
   - yes

10. Is the image a photograph?  
    - yes

11. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 11  

Score = (9/11) × 100 = 81.82

score: 81.82

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 9 out of 11 questions were answered correctly, resulting in a score of 81.82%.

token_count: 441

caption_vocabulary_size: 275

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 192

candidate_caption: An animated scene from 'The Princess and the Frog' features a large, friendly alligator with light brown skin (#a67c52) partially submerged in dark water. The alligator's face shows an amused expression with its mouth wide open, revealing sharp white teeth arranged in two horizontal rows against its pinkish-purple interior, and a bright pink tongue protruding. Its eyes are half-closed, giving it a mischievous look, while black eyebrows arch above them. A small green frog with lighter green markings sits contentedly on the alligator's nose, looking up at the camera with big, expressive eyes and a slight smile. The background depicts a dimly lit bayou setting during dusk or nightfall, characterized by tall cypress trees with dark trunks and sparse branches hanging down. Dense vegetation frames both sides of the foreground, with large leaves visible near the bottom left corner, adding depth to the scene. The sky transitions from deep purple (#3e2f49) at the top to lighter shades near the horizon, suggesting twilight or early evening. Soft, diffused lighting creates gentle highlights and shadows across the characters and environment, enhancing the whimsical mood. Gentle ripples surround the alligator's body, emphasizing its presence in this tranquil yet slightly eerie atmosphere. The overall color palette includes earthy tones like forest green (#526d5b), muted purples, browns, and grays, with high contrast between illuminated areas and darker surroundings, contributing to the mysterious yet playful ambiance of this iconic Disney scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the alligator dark green?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the frog on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the frog on top of the alligator's nose?"}
 {'answer': 'no', 'category': 'emotion', 'question': 'Is the frog looking attentive?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the alligator large compared to the frog?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two animals in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show an outdoor scene?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the frog small?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the alligator in water?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from an animated film?'}]

openai_answers: 1. Is the alligator dark green?  
   - no

2. Is the frog on the right side of the image?  
   - n/a

3. Is the frog on top of the alligator's nose?  
   - yes

4. Is the frog looking attentive?  
   - no

5. Is the alligator large compared to the frog?  
   - yes

6. Are there two animals in the image?  
   - yes

7. Does the image show an outdoor scene?  
   - yes

8. Is the frog small?  
   - yes

9. Is the alligator in water?  
   - yes

10. Is the image from an animated film?  
    - yes

**Calculate Score:**

Number of Correct Answers: 8  
Total Number of Questions: 10  

Score = (8/10) × 100 = 80

score: 80.0

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 8 out of 10 answers were correct, resulting in a score of 80%.

token_count: 309

caption_vocabulary_size: 219

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 193

candidate_caption: A vibrant movie poster for 'Starsky & Hutch' featuring two main characters against a golden-yellow background with subtle smoke effects, creating a dramatic and action-oriented feel. On the left is Ben Stiller's character, dressed in a brown leather jacket over a light blue shirt with an open collar, wearing dark aviator sunglasses with thick frames and brown tinted lenses. He holds a black semi-automatic pistol with his right hand at chest level, pointing it upward, while his left arm crosses over his body. His expression is serious and confident. On the right is Owen Wilson's character, with voluminous blonde hair styled in layers falling over his forehead and ears, wearing a brown leather jacket over a plaid shirt with shades of orange, red, and beige. He holds a large revolver with both hands near his face, displaying a surprised or shocked look. Below them are three cheerleader-like figures in orange and white uniforms, one standing confidently with her arms crossed, another adjusting her pom-pom, and the third leaning forward with her hands on her hips. To the right are additional characters: a man in a white disco outfit with a mustache (partially visible), and another character wearing a lavender hat, purple sunglasses, and a fur-collared coat. In the bottom right corner, there's a classic red Chevrolet Nova coupe with white stripes, chrome details, including four round headlights, a prominent grille, and fog lights below, sporting a yellow California license plate reading '5GT DWN'. The car's wheels feature black tires with silver rims. The entire scene is set within a rectangular frame bordered by a thick white line with rounded corners against a solid deep red backdrop (#c7003b). Text at the top reads 'BEN STILLER' on the left and 'OWEN WILSON' on the right in bold white uppercase letters. At the center-bottom, the title 'STARSKY & HUTCH' is displayed in large, bold white letters with a black outline, followed by the tagline 'The original partners in crime.' in smaller white text. A small note at the bottom-right corner states '15 contains hard drug references' in white. Additional credits appear as small, glowing orange text along the bottom edge, including mentions of Mirage Enterprises LLC and Miramax Film Corp. The website 'www.filmfactory.co.uk/stosky' appears at the very bottom in white.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'STARSKY & HUTCH'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color mostly red?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the car's color red?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the hat on the right side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the white text near the bottom of the image?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person on the left looking confident?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the actor on the left Ben Stiller?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the car small in the image?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two main characters on the poster?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the name of the blonde actor Owen Wilson?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a movie poster?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Does the image contain the text 'STARSKY & HUTCH'?  
   - yes

2. Is the background color mostly red?  
   - no

3. Is the car's color red?  
   - yes

4. Is the person in the hat on the right side of the image?  
   - yes

5. Is the white text near the bottom of the image?  
   - yes

6. Is the person on the left looking confident?  
   - yes

7. Is the actor on the left Ben Stiller?  
   - yes

8. Is the car small in the image?  
   - n/a

9. Are there two main characters on the poster?  
   - yes

10. Is the name of the blonde actor Owen Wilson?  
    - yes

11. Is the image a movie poster?  
    - yes

12. Does the image have high contrast?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 12  

Score = (10/12) × 100 = 83.33

score: 83.33

reasons: The score is calculated based on the number of correct answers out of the total questions. There were 10 correct answers out of 12 questions, resulting in a score of 83.33%.

token_count: 486

caption_vocabulary_size: 292

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

#### Sample 198

candidate_caption: A romantic wedding photograph captures an intimate moment between bride and groom standing closely together against a rustic light brown brick wall with visible mortar lines. The groom, on the left, wears a classic black tuxedo with a white shirt, black bow tie, and a white rose boutonniere composed of small white flowers and greenery pinned to his left lapel. His short curly dark hair frames his face as he looks down at the bride with a slight smile. He holds her hand gently in his right hand while his left hand rests casually by his side, displaying a ring on one finger. The bride, on the right, is dressed in an elegant ivory-colored fitted bodice dress with long sleeves, a deep V-neckline, and a sparkling silver beaded belt cinching the waist. Her hair is styled in soft curls cascading over her shoulders, partially covered by a sheer veil that drapes elegantly behind her head. She smiles warmly while leaning into the groom, holding a bouquet of green stems in her left hand. A cylindrical modern wall-mounted light fixture emits a warm yellow glow from its open end, illuminating the couple's upper bodies and casting gentle shadows on their faces. Behind them, large arched windows with multiple panes are partially open, revealing glimpses of the interior space beyond. To the far left, a door frame can be seen, adding depth to the composition. The overall mood is tender and joyful, enhanced by the low-key lighting and sepia-toned color palette dominated by shades of ecru (#c6bda), rich umber (#2e271f), muted olive (#5a5748), warm khaki (#7a7059), deep taupe (#50403d), and sage green (#83837e).

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the color of the woman's dress white?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the window frame white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the light positioned above the couple?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the brick wall behind the couple?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Do both individuals look happy?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the light in the image small?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the light cylindrical?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image wearing a suit?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person wearing a dress holding flowers?'}
 {'answer': 'no', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the color of the woman's dress white?  
     - Answer: no

   - Is the color of the window frame white?  
     - Answer: n/a

   - Is the light positioned above the couple?  
     - Answer: yes

   - Is the brick wall behind the couple?  
     - Answer: yes

   - Do both individuals look happy?  
     - Answer: yes

   - Is the light in the image small?  
     - Answer: yes

   - Is the light cylindrical?  
     - Answer: yes

   - Are there two people in the image?  
     - Answer: yes

   - Is there a person in the image wearing a suit?  
     - Answer: yes

   - Is the person wearing a dress holding flowers?  
     - Answer: yes

   - Does the image show outdoors?  
     - Answer: no

   - Does the image have a warm color palette?  
     - Answer: yes

   - Is the image a photograph?  
     - Answer: yes

2. **Calculate Score:**

   - Number of Correct Answers: 11
   - Total Number of Questions: 13

   Score = (11/13) × 100 = 84.62

score: 84.62

reasons: The score is calculated based on the number of correct answers out of the total questions. With 11 correct answers out of 13 questions, the score is 84.62%.

token_count: 356

caption_vocabulary_size: 237

score_bin: 80-90

evaluated_by: gpt-4o-2024-08-06

### Scores in 90-100 Bin

```python
                                     candidate_caption  captioned_by                                       ground_truth  ... caption_vocabulary_size  score_bin       evaluated_by
1    A vintage-style coffee label features an ornat...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     232     90-100  gpt-4o-2024-08-06
24   A vibrant promotional poster for a beauty cont...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     248     90-100  gpt-4o-2024-08-06
38   A dynamic, low-angle photograph captures a you...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     273     90-100  gpt-4o-2024-08-06
47   A high-contrast black-and-white graphic design...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     169     90-100  gpt-4o-2024-08-06
57   A movie poster for 'Eddie The Eagle' featuring...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     241     90-100  gpt-4o-2024-08-06
58   A dramatic landscape photograph captures an ea...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     271     90-100  gpt-4o-2024-08-06
68   A vibrant and cheerful invitation photograph s...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     352     90-100  gpt-4o-2024-08-06
75   The scene is an anime-style illustration depic...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     222     90-100  gpt-4o-2024-08-06
76   The photograph showcases a modern shower area ...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     207     90-100  gpt-4o-2024-08-06
77   An animated news broadcast scene in an anime-s...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     263     90-100  gpt-4o-2024-08-06
88   A close-up view of a futuristic heart monitor ...  pg-captioner  [{'answer': 'Yes', 'category': 'text', 'questi...  ...                     222     90-100  gpt-4o-2024-08-06
105  A vibrant urban landscape photograph captures ...  pg-captioner  [{'answer': 'yes', 'category': 'entity', 'ques...  ...                     261     90-100  gpt-4o-2024-08-06
110  A product label for 'FRESH COTTON' scented soy...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     236     90-100  gpt-4o-2024-08-06
115  A breathtaking landscape photograph captures a...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     308     90-100  gpt-4o-2024-08-06
120  A cinematic scene from 'Mortal Kombat' feature...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     178     90-100  gpt-4o-2024-08-06
122  A realistic urban night scene captures four tr...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     250     90-100  gpt-4o-2024-08-06
140  A close-up portrait photograph of a person wit...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     222     90-100  gpt-4o-2024-08-06
167  A photograph taken during twilight showcases t...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     262     90-100  gpt-4o-2024-08-06
191  A photograph captures a serene Mediterranean-s...  pg-captioner  [{'answer': 'yes', 'category': 'color', 'quest...  ...                     196     90-100  gpt-4o-2024-08-06
194  A dramatic outdoor photograph captures an inte...  pg-captioner  [{'answer': 'Yes', 'category': 'color', 'quest...  ...                     257     90-100  gpt-4o-2024-08-06
195  A close-up photograph captures the striking de...  pg-captioner  [{'answer': 'yes', 'category': 'text', 'questi...  ...                     221     90-100  gpt-4o-2024-08-06

[21 rows x 10 columns]
```

#### Sample 1

candidate_caption: A vintage-style coffee label features an ornate frame with goldenrod (#d4a964) text on a rich black background. The label has an asymmetrical layout with curved upper and lower sections, creating a balanced yet dynamic composition. At the top center, 'NELSON'S' is prominently displayed in bold uppercase serif font, arched slightly upward within the decorative frame. Below this, 'FINEST SELECTED GROUND' arches over in a similar style but larger size, also using a gold-colored serif typeface. Further down, 'PURE' is written in smaller uppercase letters flanked by the numbers '19' on the left and '24' on the right, both positioned horizontally at the bottom of the label. The word 'COFFEE' dominates the lower center in extra-large, bold uppercase serif letters. Each section of the text is enclosed in elaborate scrollwork and floral motifs, adding to its classic appearance. These intricate designs feature smooth curves and decorative elements extending outward from each corner, enhancing the overall elegance of the piece. At the very bottom, 'ROASTED BY NELSON COFFEE CO.' appears in smaller gold serif font. The entire design is framed by cream-colored outlines, providing high contrast against the dark backdrop and emphasizing the luxurious feel. The color palette includes shades of gold (RGB(255, 215, 0), RGB(179, 141, 74), RGB(209, 157, 100)), dark brown (RGB(33, 22, 13)), tan (RGB(181, 136, 95)), and off-white (RGB(229, 223, 212)), creating a warm hue throughout the label. The lighting is even and flat, typical of digital illustrations, ensuring all elements are clearly visible without shadows or highlights. This striking design effectively combines retro typography with intricate borders, resulting in a sophisticated advertisement that exudes quality and craftsmanship.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the text include the word 'COFFEE'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the text yellow or gold?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the emblem in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'PURE' above the text 'COFFEE'?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is 'NELSON'S' at the top of the text frame?"}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'ROASTED BY NELSON COFFEE CO.' below the text 'COFFEE'?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a coffee label?'}
 {'answer': 'yes', 'category': 'color palette', 'question': "Is the image's color palette predominantly dark and gold?"}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a label?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the text include the word 'COFFEE'?  
   - yes

3. Is the background color black?  
   - yes

4. Is the color of the text yellow or gold?  
   - yes

5. Is the emblem in the center of the image?  
   - n/a

6. Is the text 'PURE' above the text 'COFFEE'?  
   - yes

7. Is 'NELSON'S' at the top of the text frame?  
   - yes

8. Is the text 'ROASTED BY NELSON COFFEE CO.' below the text 'COFFEE'?  
   - yes

9. Does the image show a coffee label?  
   - yes

10. Is the image's color palette predominantly dark and gold?  
    - yes

11. Is the image a label?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 11  

Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score was calculated based on the number of correct answers provided in relation to the total number of questions. Out of 11 questions, 10 were answered affirmatively, resulting in a score of 90.91%.

token_count: 390

caption_vocabulary_size: 232

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 24

candidate_caption: A vibrant promotional poster for a beauty contest features three circular portraits of women against a solid goldenrod yellow (#f7d71c) background, arranged horizontally from left to right in descending order of size. Each portrait is framed with dynamic abstract designs in shades of lavender purple (#5b2a8e), bright pink (#e06aa0), coral red (#df6a75), and white, creating an energetic contrast against the vivid backdrop. The largest circle on the left showcases a woman with dark brown hair styled in loose waves, striking makeup including bold hot pink lipstick and well-defined eyebrows, holding a bouquet of five small roses close to her face. Her expression is serene yet confident as she looks directly at the camera. In the center, a blonde-haired woman with light skin and delicate features has pale blue eyes surrounded by clusters of small pink flowers adorning her face, giving her a fresh spring-like appearance. She faces slightly to the right with a calm demeanor. On the right, the smallest circle displays another blonde woman with shoulder-length wavy hair, wearing minimalistic nude-colored clothing, gently holding a large pink orchid near her lips while her eyes are closed, appearing relaxed and joyful. Below the portraits, the text 'BEAUTY CONTEST' is prominently displayed in a gradient fill transitioning from light lavender violet (#c4ccfb) to deep magenta (#b23b9f), followed by 'Participate Now' in elegant cursive script (#443e55). At the bottom, contact information reads 'CALL AT: +1234 0000 5678' in simple sans-serif font (#84396f). The overall design uses high contrast and saturation to create an inviting and eye-catching visual appeal, emphasizing the event's beauty theme through its use of warm tones, floral elements, and contemporary graphic design style.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'BEAUTY CONTEST'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color yellow?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color in shades of purple and red?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'Participate Now' at the bottom?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Are the three women in a horizontal row?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the left woman's portrait larger than the portraits in the center and right?"}
 {'answer': 'no', 'category': 'emotion', 'question': 'Is the central person smiling?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the image slightly out of focus?'}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the text 'BEAUTY CONTEST' large?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the portraits in circular frames?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there three women in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a phone number in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'CALL AT: +1234 0000 5678' below 'Participate Now'?"}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a poster?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Does the image contain the text 'BEAUTY CONTEST'?  
   - yes

3. Is the background color yellow?  
   - yes

4. Is the text color in shades of purple and red?  
   - yes

5. Is the text 'Participate Now' at the bottom?  
   - no

6. Are the three women in a horizontal row?  
   - yes

7. Is the left woman's portrait larger than the portraits in the center and right?  
   - yes

8. Is the central person smiling?  
   - no

9. Is the image slightly out of focus?  
   - n/a

10. Is the text 'BEAUTY CONTEST' large?  
    - yes

11. Are the portraits in circular frames?  
    - yes

12. Are there three women in the image?  
    - yes

13. Is there a phone number in the image?  
    - yes

14. Is the text 'CALL AT: +1234 0000 5678' below 'Participate Now'?  
    - yes

15. Does the image have a warm color palette?  
    - yes

16. Is the image a poster?  
    - yes

**Calculate Score:**

Number of Correct Answers: 15  
Total Number of Questions: 16  

Score = (15/16) × 100 = 93.75

score: 93.75

reasons: The score is calculated based on the number of correct answers out of the total questions. Out of 16 questions, 15 were answered correctly, resulting in a score of 93.75%.

token_count: 372

caption_vocabulary_size: 248

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 38

candidate_caption: A dynamic, low-angle photograph captures a young woman dancing energetically outdoors in an urban setting during bright daylight hours. The scene is taken from a unique perspective, emphasizing her movement with the background slightly blurred due to a shallow depth of field created by a wide-angle lens. She wears a white crop top that reveals her bare midriff, accentuating her tan skin tone, and forest green sweatpants featuring distinctive yellow-green stripes on the elastic waistband tied with a bow. Her dark hair is styled in thick dreadlocks, some extending outward as if flowing with motion, creating a striking silhouette against the sky. Small gold hoop earrings adorn both ears, while thin black wires form earbuds are visible around her neck. In her right hand, she holds a black smartphone, possibly used for music or navigation. A delicate necklace adorns her neck, adding subtle detail. The background showcases a multi-story residential building made of light-colored concrete or stucco with multiple windows reflecting surrounding trees and foliage. Some windows have metal grilles, while others feature air conditioning units mounted on their sills. Vibrant graffiti reading 'PSGONE' in red block letters is visible on one wall, suggesting urban decay and street art culture. A narrow concrete path runs diagonally through the grassy area in front of the building. Lush greenery frames the scene, including tall deciduous trees with dense foliage casting intricate patterns of shadows and highlights across surfaces below. To the right, more vegetation can be seen. The clear azure blue sky provides a stark contrast to the darker tones of the subject and surroundings, enhancing the vividness of colors. Natural sunlight creates strong contrasts and defined shadows, illuminating parts of the woman's body while leaving other areas in shadow, emphasizing textures such as wrinkles in the fabric and shadows cast by tree leaves. This high-contrast lighting creates a dramatic effect, capturing the essence of youthful energy and freedom within an urban environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there text on the wall?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky color light blue?'}
 {'answer': 'yes', 'category': 'color', 'question': "Is the person's top white?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the building behind the person?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the tree standing to the right of the person?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a building in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person holding something in their hand?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. Is there text on the wall?  
   - yes

2. Is the sky color light blue?  
   - yes

3. Is the person's top white?  
   - yes

4. Is the person in the center of the image?  
   - n/a

5. Is the building behind the person?  
   - yes

6. Is the tree standing to the right of the person?  
   - yes

7. Is there a person in the image?  
   - yes

8. Is there a building in the image?  
   - yes

9. Is the person holding something in their hand?  
   - yes

10. Does the image show outdoors?  
    - yes

11. Does the image have a warm color palette?  
    - n/a

12. Is the image a photograph?  
    - yes

13. Does the image have high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 13  

Score = (12/13) × 100 = 92.31

score: 92.31

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 12 out of 13 questions were answered correctly, resulting in a score of 92.31%.

token_count: 390

caption_vocabulary_size: 273

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 47

candidate_caption: A high-contrast black-and-white graphic design illustration featuring a central crab with intricately detailed claws, legs, and antennae, embodying the Cancer zodiac sign. The crab's body showcases fine lines and shading that add texture and depth, while its circular shell prominently displays the Cancer zodiac symbol (♈) in white stylized letters on a black background. Behind the crab is a large full moon rendered using a halftone dot pattern, creating a sense of depth and mystery against the solid black background. This textured backdrop forms an arch around the top of the composition, enhancing the cosmic theme. Curved along the top of the image, Gothic-style text reads 'NURTURING SOULS UNDER THE MOON'S GLOW' in white serif font. Below the crab, there are two dates, 'JUNE 21' on the left and 'JULY 22' on the right, both written in a similar style. At the bottom center, the word 'CANCER' appears in large, bold, white Gothic-style letters, with a small globe icon featuring a grid pattern below it. The overall design has a vintage tattoo aesthetic with clean lines and symmetrical elements, emphasizing its mystical and nurturing mood through the use of monochromatic colors and intricate details.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Cancer'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color black?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the crab in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'Cancer' at the bottom of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'Nurturing Souls Under the Moon's Glow' above the crab?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the crab large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the crab's body circular in shape?"}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'June 21' to the left of the crab?"}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'July 22' to the right of the crab?"}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Is the image monochrome?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a graphic design?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have a high contrast?'}]

openai_answers: 1. Does the image contain the text 'Cancer'?  
   - yes

2. Is the background color black?  
   - yes

3. Is the text color white?  
   - yes

4. Is the crab in the center of the image?  
   - yes

5. Is the text 'Cancer' at the bottom of the image?  
   - yes

6. Is the text 'Nurturing Souls Under the Moon's Glow' above the crab?  
   - yes

7. Is the crab large?  
   - n/a

8. Is the crab's body circular in shape?  
   - yes

9. Is the text 'June 21' to the left of the crab?  
   - yes

10. Is the text 'July 22' to the right of the crab?  
    - yes

11. Is the image monochrome?  
    - yes

12. Is the image a graphic design?  
    - yes

13. Does the image have a high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 13  

Score = (12/13) × 100 = 92.31

score: 92.31

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 12 out of 13 questions were answered correctly, resulting in a score of 92.31%.

token_count: 261

caption_vocabulary_size: 169

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 57

candidate_caption: A movie poster for 'Eddie The Eagle' featuring two main actors, Taron Egerton and Hugh Jackman. The background is a vibrant blue sky with scattered white clouds, creating a bright and uplifting atmosphere. At the top center, the names 'TARON EGERTON' and 'HUGH JACKMAN' are written in bold gray uppercase letters. Below this, the title 'EDDIE THE EAGLE' is prominently displayed in large yellow letters, with each word stacked vertically on different lines. A thin yellow line separates 'THE' from 'EAGLE'. Underneath the title, the text 'FROM PRODUCERS OF KINGSMAN: THE SECRET SERVICE' appears in smaller black uppercase letters within a yellow rectangular banner. Centered below this is the tagline 'INSPIRED BY A DREAM COME TRUE' in light gray uppercase letters. At the bottom of the poster, the release date 'FEBRUARY 26' is shown in navy blue uppercase letters, accompanied by the website 'eddietheeaglemovie.com' in small gray text and the hashtag '#EddieTheEagle' also in navy blue. On the right side of the poster, Taron Egerton is depicted in profile view as Eddie Edwards, a determined ski jumper, crouched on top of a red van. He wears a teal blue ski suit with green stripes on the sleeves and a white bib numbered '24', featuring horizontal red, yellow, and blue racing numbers. His outfit includes a pink helmet with blue goggles attached, gold-framed sunglasses, and white skateboarding shoes. He looks upwards with an intense expression. At the bottom left corner, partially visible inside the driver's window of the same red van, is Hugh Jackman sitting confidently, wearing dark sunglasses with gold frames and a black jacket. His muscular arm rests on the windowsill, revealing tattoos on his forearm. The overall style of the poster is modern and vibrant, with high contrast and saturation, emphasizing the inspirational theme of the film and capturing the essence of the story set against a backdrop of clear skies.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Is the text 'EDDIE THE EAGLE' present in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky color blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the car red?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the car at the bottom of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person on the ski on top of the car?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person in the car smiling?'}
 {'answer': 'yes', 'category': 'proper noun', 'question': 'Is the person in the car Hugh Jackman?'}
 {'answer': 'yes', 'category': 'entity size', 'question': "Is the text 'EDDIE THE EAGLE' large?"}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person on a ski jumping pose in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the text 'INSPIRED BY A DREAM COME TRUE' below 'EDDIE THE EAGLE'?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a bright and vivid color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a movie poster?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high brightness?'}]

openai_answers: 1. Is the text 'EDDIE THE EAGLE' present in the image?  
   - yes

2. Is the sky color blue?  
   - yes

3. Is the color of the car red?  
   - yes

4. Is the person in the car at the bottom of the image?  
   - yes

5. Is the person on the ski on top of the car?  
   - yes

6. Is the person in the car smiling?  
   - n/a

7. Is the person in the car Hugh Jackman?  
   - yes

8. Is the text 'EDDIE THE EAGLE' large?  
   - yes

9. Are there two people in the image?  
   - yes

10. Is there a person on a ski jumping pose in the image?  
    - yes

11. Is the text 'INSPIRED BY A DREAM COME TRUE' below 'EDDIE THE EAGLE'?  
    - yes

12. Does the image show daylight?  
    - yes

13. Does the image have a bright and vivid color palette?  
    - yes

14. Is the image a movie poster?  
    - yes

15. Does the image have high brightness?  
    - yes

**Calculate Score:**

Number of Correct Answers: 14  
Total Number of Questions: 15  

Score = (14/15) × 100 = 93.33

score: 93.33

reasons: The score is calculated based on the number of correct answers provided in relation to the total number of questions. Out of 15 questions, 14 were answered correctly, resulting in a score of 93.33%.

token_count: 425

caption_vocabulary_size: 241

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 58

candidate_caption: A dramatic landscape photograph captures an eagle in flight against a backdrop of a vibrant, fiery sky during sunset or sunrise. The scene is dominated by warm hues, primarily amber yellow (#d39a24) and burnt orange, creating high contrast with the darker elements below. In the foreground, wild grasses and small plants in shades of goldenrod (#d6c78b), olive green (#7f8d4d), and forest green dominate the lower portion, interspersed with patches of tall grasses illuminated by sunlight. A weathered wooden fence made of vertical posts extends horizontally across the middle ground, separating it from the fields beyond. This rustic barrier marks the boundary between the cultivated land and the natural environment, its aged appearance contrasting with the lush vegetation above. The midground features rolling hills covered in patchwork farmland, displaying various crops arranged in geometric patterns like terraces and rows. These fields transition through different stages of cultivation, from rich brown soil to vibrant greens and burnt oranges, indicating diverse agricultural practices. The terrain shows subtle undulations and is dotted with trees and shrubs along the edges, adding depth to the composition. The background showcases distant mountains shrouded in mist, their peaks softened by atmospheric perspective, enhancing the sense of vastness. To the right side of the image, a town or village can be seen nestled among the hills, characterized by clusters of buildings that blend into the landscape. Above, the sky dominates the upper half of the frame with thick clouds forming intricate shapes and textures. Sunbeams pierce through these formations, casting a soft glow over the landscape below. The main subject, a majestic bald eagle, glides dynamically from left to right, its wings fully spread showcasing dark brown feathers with black-tipped feathers extending towards the top edge of the frame. Its white head contrasts sharply with its body, while its sharp talons grip the air. The lighting enhances the vivid colors throughout, emphasizing the interplay between the natural world and the grandeur of nature captured in this awe-inspiring scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the sky color orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the bird positioned in the left side of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the bird above the fields?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the landscape shape irregular?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a bird in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the bird flying over the field?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the sky color orange?  
   - yes

2. Is the bird positioned in the left side of the image?  
   - yes

3. Is the bird above the fields?  
   - yes

4. Is the landscape shape irregular?  
   - yes

5. Is there a bird in the image?  
   - yes

6. Is the bird flying over the field?  
   - yes

7. Does the image show outdoors?  
   - yes

8. Does the image have a warm color palette?  
   - yes

9. Is the image a photograph?  
   - yes

10. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 10  

Score = (9/10) × 100 = 90

score: 90.0

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 10 questions were answered correctly, resulting in a score of 90.

token_count: 410

caption_vocabulary_size: 271

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 68

candidate_caption: A vibrant and cheerful invitation photograph showcases a playful scene by a swimming pool, featuring eleven diverse dogs enjoying a sunny day at what appears to be an outdoor resort or private residence. The composition is divided into two main sections: the text panel on the left and the poolside area with animals on the right. In the foreground, a light beige Labrador Retriever lounges comfortably on a bright yellow inflatable lemon slice float with small red dots in the clear turquoise water of the rectangular pool. To its left, a small white French Bulldog sits near the edge of the pool, while another dog stands nearby. The midground features six lounge chairs arranged along the pool's edge, each with blue cushions adorned with white vertical stripes and matching headrests. Three large dogs sit on these chairs: a St. Bernard with tricolor markings (black, white, and tan) in the center; a Great Dane with black spots on white fur to the left; and a Saluki-like breed with flowing cream-colored fur to the right. A Dachshund with brown skin stands near the edge of the pool, while a Beagle with black and tan markings lingers around the pool's edge. Two additional dachshunds are visible - one standing in the shallow water and another lying down on the concrete surface beside the pool. Behind the lounge chairs, three large sun umbrellas with alternating goldenrod yellow (#f7d87a) and white panels create a striking pattern against the lush green foliage of trees, shrubs, and banana plants. These umbrella-shaped structures feature pointed tops and scalloped edges, adding a retro aesthetic to the scene. Small white side tables hold colorful beach balls, vintage-style mint-green radios, and other decorative items, enhancing the summery atmosphere. The background consists of dense greenery, including various types of bushes and tall evergreen trees, providing a natural backdrop that contrasts beautifully with the modern amenities and creates a serene setting. On the far left, a teal (#1ea8ac) textured square overlay contains bold, uppercase white sans-serif text reading 'JOIN US FOR A JOINT BACH WEEKEND TO CELEBRATE letitia & alonzo BEFORE THEY TIE THE KNOT AUG 12-14 | PALM SPRINGS'. The overall mood is joyful and relaxed, captured in warm daylight with balanced exposure and medium contrast, creating an inviting and celebratory ambiance perfect for a weekend getaway. The color palette includes shades of teal (#1ea8ac), ivory (#e6dbdf), deep charcoal (#2c2723), sage green (#9ba98c), olive drab (#71724b), and taupe (#796052).

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'letitia & alonzo'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the text white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the dog in the pool white?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the umbrella behind the chair?'}
 {'answer': 'yes', 'category': 'text', 'question': 'Is the location Palm Springs?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the pool mat circular?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a swimming pool in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the dog sitting on the floating matress?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image an invitation?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Does the image contain the text 'letitia & alonzo'?  
   - yes

2. Is the color of the text white?  
   - yes

3. Is the color of the dog in the pool white?  
   - no

4. Is the umbrella behind the chair?  
   - yes

5. Is the location Palm Springs?  
   - yes

6. Is the pool mat circular?  
   - yes

7. Is there a swimming pool in the image?  
   - yes

8. Is the dog sitting on the floating mattress?  
   - yes

9. Does the image show outdoors?  
   - yes

10. Is the image an invitation?  
    - yes

11. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 11  

Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score is calculated based on the number of correct answers out of the total questions. Out of 11 questions, 10 were answered correctly, resulting in a score of 90.91.

token_count: 541

caption_vocabulary_size: 352

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 75

candidate_caption: The scene is an anime-style illustration depicting a tranquil yet slightly mysterious atmosphere during twilight or early evening. The foreground features dense, dark green foliage with varying shades of forest green, silhouetted against a warm yellow gradient sky, creating a stark contrast between nature and urban elements. On the right side, there is a large circular mirror-like object with a brown frame that reflects part of an alleyway. Within this reflection, a young girl with long, wavy hair transitioning from pink at the roots to white at the tips is seen running away from the viewer along a dimly lit street. She wears a soft pink sweater with beige knitted details around the cuffs and hemline over a light gray top, paired with a black skirt, brown ankle boots, and has her left leg bent and right arm slightly raised as she moves forward. The midground shows a narrow street bordered by tall fences made of vertical slats and horizontal bars at the top, running parallel to the building's wall on the right. A brightly illuminated window emits a pale yellow glow, contrasting sharply with the surrounding darkness. The background includes buildings with slate-gray rooftops and faint outlines of trees in deep midnight blue shadows, enhancing the depth of field. To the left, a window reveals a bright yellow sunset sky outside, providing a warm, glowing backdrop that contrasts beautifully with the cool tones inside the reflected area. The overall lighting is low-key, with natural illumination from the setting sun complemented by artificial street lights casting a bluish hue on the reflective surface. This creates a high-contrast effect between the bright exterior and the darker interior of the mirrored reflection, emphasizing the serene yet somewhat melancholic mood of the scene.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the sky color yellow?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the person in the reflection on the center right side of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the mirror to the right of the bushes?'}
 {'answer': 'Yes', 'category': 'emotion', 'question': 'Is the person in the reflection running?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the circular mirror large?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the circular mirror round?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there only one person in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a tree in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the person reflected in the mirror?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show a late evening setting?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high saturation?'}]

openai_answers: 1. Is the sky color yellow?  
   - yes

2. Is the person in the reflection on the center right side of the image?  
   - yes

3. Is the mirror to the right of the bushes?  
   - yes

4. Is the person in the reflection running?  
   - yes

5. Is the circular mirror large?  
   - yes

6. Is the circular mirror round?  
   - yes

7. Is there only one person in the image?  
   - yes

8. Is there a tree in the image?  
   - yes

9. Is the person reflected in the mirror?  
   - yes

10. Does the image show a late evening setting?  
    - yes

11. Is the image from a cartoon?  
    - yes

12. Does the image have high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 12  

Score = (11/12) × 100 = 91.67

score: 91.67

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 12 questions were answered correctly, resulting in a score of 91.67%.

token_count: 339

caption_vocabulary_size: 222

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 76

candidate_caption: The photograph showcases a modern shower area with a sophisticated design, featuring large tiles covering the walls in shades of slate blue (#8b9da6), ivory white (#f2f4eb), and warm brown tones (#c38e74) that create a marbled effect with intricate veining patterns. The floor is covered with light hexagonal white ceramic tiles arranged in a neat grid pattern, leading to a built-in seat on the right wall constructed from matching marble-like material. A teal-colored circular drain cover with a decorative pattern is centered at the bottom of the shower floor. Two recessed ceiling lights emit bright white light, creating reflections on the glossy tile surfaces and enhancing the clean atmosphere. The shower's left side features a brass-finished round shower head mounted on an adjustable gold arm extending horizontally from the wall, while a handheld hose with a matching brass finish hangs nearby. A brushed nickel shower control valve with two handles is visible on the glass door, partially reflected in the tiles. A recessed niche in the right wall provides additional storage space, filled with light gray tiles. The overall color palette includes cool hues like powder blue (#a1b0bc) and muted mauve (#96808d), complemented by warm accents such as sandy beige (#cdcec5). The lighting is soft and even, highlighting the textures and colors of the materials used without casting harsh shadows. This balanced composition emphasizes the contemporary aesthetic of the bathroom, focusing on the harmonious blend of natural stone elements, sleek fixtures, and strategic use of reflective surfaces to create a serene and inviting atmosphere.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the main color in the shower area gray?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the shower head on the left side of the image?'}
 {'answer': 'Yes', 'category': 'relative position', 'question': 'Is the bench underneath the handheld shower on the right side of the image?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the shower head large?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the main shower head round?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Are there two shower heads in the image?'}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a bench in the shower area?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the handheld shower attached to the wall?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Is the image taken indoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. **Answer Each Question:**

   - Is the main color in the shower area gray?  
     - yes

   - Is the shower head on the left side of the image?  
     - yes

   - Is the bench underneath the handheld shower on the right side of the image?  
     - yes

   - Is the shower head large?  
     - n/a

   - Is the main shower head round?  
     - yes

   - Are there two shower heads in the image?  
     - yes

   - Is there a bench in the shower area?  
     - yes

   - Is the handheld shower attached to the wall?  
     - yes

   - Is the image taken indoors?  
     - yes

   - Does the image have a cool color palette?  
     - yes

   - Is the image a photograph?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 10
   - Total Number of Questions: 11

   Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 10 out of 11 questions were answered correctly, resulting in a score of 90.91.

token_count: 317

caption_vocabulary_size: 207

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 77

candidate_caption: An animated news broadcast scene in an anime-style cartoon features two main characters against a stylized American flag background. On the right side, there is a female news anchor with light beige hair styled in loose waves cascading over her shoulders, wearing a sleeveless magenta dress with a small circular cutout at the chest revealing part of her neck. She has a pearl necklace adorned with small white beads and gold earrings. A tiny American flag pin is affixed to her left lapel. Her eyes are closed, mouth open as if speaking seriously, with her hands clasped together in front of her chest in a prayer-like gesture. To the upper left corner, there's a smaller inset panel showcasing a male cartoon character named Urkel. He has short black hair with a distinctive fade on the sides, large red-framed glasses with white rims, round pupils, and thick dark outlines. His facial expression appears concerned or skeptical, with raised eyebrows, slightly furrowed brow, and a pointed finger gesturing near his chin. He wears a green jacket with white stripes over a pink shirt with a blue collar and a red tie featuring diagonal stripes. Both characters appear to be positioned behind a rectangular desk or table. The background showcases a distorted version of the American flag with exaggerated colors and shapes, including alternating vibrant shades of crimson (#7d1c36), navy blue (#5b6daa), and bright white (#f9f9fb), arranged diagonally across the frame. Large five-pointed stars in white with navy blue fillings are scattered throughout, some overlapping each other. At the bottom of the screen, there is a bold red banner with 'XMAS UNDER ATTACK!' written in white sans-serif font, spanning horizontally across the width of the image. Below this text, on the far right, the logo 'HAWK NEWS NETWORK' appears in white block letters, stacked vertically within individual rectangles. The overall style is highly saturated and vivid, creating a humorous yet intense atmosphere typical of animated television shows.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'XMAS UNDER ATTACK!'?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Are the background colors red, white, and blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the female character in the center of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there an inset image in the top left corner?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'XMAS UNDER ATTACK!' below the female character?"}
 {'answer': 'yes', 'category': 'position', 'question': "Is the text 'HAWK NEWS NETWORK' in the bottom right corner of the image?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the female character looking serious?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the inset image smaller than the rest of the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the inset image rectangular?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there two characters in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a human character in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a flag in the image?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image from a cartoon?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Does the image contain the text 'XMAS UNDER ATTACK!'?  
   - yes

2. Are the background colors red, white, and blue?  
   - yes

3. Is the text color white?  
   - yes

4. Is the female character in the center of the image?  
   - no

5. Is there an inset image in the top left corner?  
   - yes

6. Is the text 'XMAS UNDER ATTACK!' below the female character?  
   - yes

7. Is the text 'HAWK NEWS NETWORK' in the bottom right corner of the image?  
   - yes

8. Is the female character looking serious?  
   - yes

9. Is the inset image smaller than the rest of the image?  
   - yes

10. Is the inset image rectangular?  
    - yes

11. Are there two characters in the image?  
    - yes

12. Is there a human character in the image?  
    - yes

13. Is there a flag in the image?  
    - yes

14. Is the image from a cartoon?  
    - yes

15. Is the image color graded with high saturation?  
    - yes

**Calculate Score:**

Number of Correct Answers: 14  
Total Number of Questions: 15  

Score = (14/15) × 100 = 93.33

score: 93.33

reasons: The score is calculated based on the number of correct answers out of the total questions. With 14 correct answers out of 15, the score is 93.33%.

token_count: 405

caption_vocabulary_size: 263

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 88

candidate_caption: A close-up view of a futuristic heart monitor screen, reminiscent of 1980s cinema style with a digital interface aesthetic. The background is predominantly black (#131a17), creating high contrast against white text elements. At the top left corner, large bold sans-serif numbers display '30/20' in light gray (#8c9494) and '35' in white. To the right of these numbers, 'HEART RATE' appears in orange (#ae794f) uppercase letters using a unique, slightly distorted sans-serif font with varying stroke thicknesses. Below this, there's a large stylized number '14' in light gray, centered both horizontally and vertically within the frame. At the bottom center, the words 'HEART MONITOR' are prominently displayed in large, bold, white letters using a modern sans-serif font. On the far right side, partial text reading 'BOND. JAMES' can be seen in white uppercase letters. A rectangular graph occupying the lower-right section shows a gradient from dark red at the bottom to black at the top, suggesting a heartbeat line or temperature scale. The lighting is soft and even, illuminating all parts of the screen clearly without harsh shadows or highlights, emphasizing readability while maintaining focus on the central content. The color palette includes muted tones like deep charcoal (#141d1b), warm brown (#5e3329), sage green (#84886d), pale teal (#95acab), slate blue (#7a8686), and khaki (#969a76). The overall composition suggests a tense atmosphere typical of a government building, possibly an office space or control room, where vital health metrics are being monitored during nighttime.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'text', 'question': "Does the image contain the text 'Heart Rate'?"}
 {'answer': 'Yes', 'category': 'color', 'question': 'Is the color of the text white?'}
 {'answer': 'Yes', 'category': 'color', 'question': 'Is the background color dark?'}
 {'answer': 'Yes', 'category': 'position', 'question': "Is the text '30/20' in the top left corner?"}
 {'answer': 'Yes', 'category': 'position', 'question': "Is the number '14' in the center of the image?"}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Is the text 'Heart Monitor' below the number '14'?"}
 {'answer': 'Yes', 'category': 'relative position', 'question': "Is the name 'BOND. JAMES' to the right of the number '14'?"}
 {'answer': 'Yes', 'category': 'text', 'question': "Is the name 'JAMES' present in the text?"}
 {'answer': 'Yes', 'category': 'entity size', 'question': "Is the number '14' large in size?"}
 {'answer': 'Yes', 'category': 'entity', 'question': 'Is there a heart monitor mentioned in the text?'}
 {'answer': 'Yes', 'category': 'relation', 'question': "Is the text 'Heart Monitor' below the heart rate value?"}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show a medical reading?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a screenshot?'}]

openai_answers: 1. Does the image contain the text 'Heart Rate'?  
   - yes

2. Is the color of the text white?  
   - no

3. Is the background color dark?  
   - yes

4. Is the text '30/20' in the top left corner?  
   - yes

5. Is the number '14' in the center of the image?  
   - yes

6. Is the text 'Heart Monitor' below the number '14'?  
   - yes

7. Is the name 'BOND. JAMES' to the right of the number '14'?  
   - yes

8. Is the name 'JAMES' present in the text?  
   - yes

9. Is the number '14' large in size?  
   - yes

10. Is there a heart monitor mentioned in the text?  
    - yes

11. Is the text 'Heart Monitor' below the heart rate value?  
    - yes

12. Does the image show a medical reading?  
    - yes

13. Is the image a screenshot?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 13  

Score = (12/13) × 100 = 92.31

score: 92.31

reasons: The score is calculated based on the number of correct answers out of the total questions. With 12 correct answers out of 13, the score is 92.31%.

token_count: 339

caption_vocabulary_size: 222

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 105

candidate_caption: A vibrant urban landscape photograph captures an intersection of nature and modern architecture, taken during late afternoon sunlight. The foreground features a curved asphalt road with bright yellow lane markings curving from bottom right to upper left, bordered by gray metal guardrails on the left and lush greenery on both sides. A well-maintained grassy median strip separates the road from pedestrian walkways. Small bushes with vibrant red flowers add pops of color near the lower right corner. Two prominent palm trees stand along the right side of the road, their fronds illuminated by warm sunlight casting intricate shadows. A motorcyclist wearing dark clothing rides away from the camera towards the curve in the distance. A bicycle rack is visible along the left edge of the road. In the midground, dense foliage frames the left side of the scene, creating depth and texture. The background showcases towering high-rise buildings dominated by various architectural styles. On the far left stands a beige building with numerous balconies and windows arranged vertically and horizontally, adorned with vertical grid-like patterns. Next to it, a distinctive orange-red rectangular structure with similar window arrangements commands attention. To its right, white residential buildings feature balconies and large glass windows, some reflecting light and showing signs of wear. A modern glass building with a checkered pattern of reflective blue-tinted windows and horizontal lines adds to the skyline's complexity. One tall white building displays '明景园' (Mingjing Yuan) written diagonally in black Chinese characters on its facade. The clear sky above transitions from pale cerulean at the top to softer shades of azure near the horizon, enhancing the serene atmosphere. Warm golden hues bathe the scene as sunlight streams through gaps between nearby structures, casting long shadows across the landscape. This interplay of natural beauty and urban development creates a dynamic yet peaceful mood that highlights the harmony between man-made marvels and nature within this bustling city environment.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'entity', 'question': 'Is there a motorcycle in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is one of the buildings orange?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the road curved?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background clear without blur?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a tall building in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a crosswalk in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the motorcycle on the road?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the road in the bottom part of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the buildings behind the trees?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there more than three buildings in the image?'}]

openai_answers: 1. Is there a motorcycle in the image?  
   - yes

2. Is one of the buildings orange?  
   - yes

3. Is the road curved?  
   - yes

4. Is the background clear without blur?  
   - n/a

5. Is the image a photograph?  
   - yes

6. Does the image show outdoors?  
   - yes

7. Is there a tall building in the image?  
   - yes

8. Is there a crosswalk in the image?  
   - no

9. Is the motorcycle on the road?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the road in the bottom part of the image?  
    - yes

12. Are the buildings behind the trees?  
    - yes

13. Are there more than three buildings in the image?  
    - yes

**Calculate Score:**

Number of Correct Answers: 12  
Total Number of Questions: 13  

Score = (12/13) × 100 = 92.31

score: 92.31

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 12 out of 13 questions were answered correctly, resulting in a score of 92.31%.

token_count: 383

caption_vocabulary_size: 261

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 110

candidate_caption: A product label for 'FRESH COTTON' scented soy wax candle, designed in a vintage-style layout on a light beige background with subtle speckles, creases, and small dark brown marks resembling age or wear. The main title 'FRESH COTTON' is prominently displayed at the top center in large, bold, charcoal gray (RGB(59, 54, 52)) typewriter font, spanning across three lines within a square frame. Below it, there are three sections divided by thin black lines into a grid format, each containing important information about the candle. The leftmost section contains 'Scented Soy Wax Candle' written in regular, slightly italicized sans-serif typeface. To its right, another section states '16 oz / Burn time: 40 hrs' also in regular, slightly italicized sans-serif font. On the far right side of the label, there's a circular seal graphic rendered in cobalt blue (RGB(28, 42, 64)), featuring an illustration of a stylized flame above a hand holding it gently, accompanied by two small stars nearby. Surrounding this central graphic is text reading 'WICK CRAFT SCENTED CANDLES'. Within this circle, the batch number '002' is centered in bold, uppercase letters. Each section has corresponding notes listed vertically: 'TOP NOTES:' mentions 'Bergamot', 'Middle Notes:' lists 'Cotton Blossom', and 'Base Notes:' indicates 'White Musk', all in matching charcoal gray text. The overall color palette includes shades of beige (RGB(236, 220, 201)), charcoal gray, deep brown, and cobalt blue, creating a clean, informative design with medium contrast and low saturation, evoking a nostalgic mood reminiscent of old-fashioned labeling techniques while providing essential details about the candle product.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the text 'White Musk' appear in the image?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the background color beige?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the text color predominantly black?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the batch number positioned on the right?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'Scented Soy Wax Candle' located beneath the text 'FRESH COTTON'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the candle's name 'FRESH COTTON'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the batch number '002'?"}
 {'answer': 'yes', 'category': 'entity shape', 'question': "Is the 'WICK CRAFT' stamp circular?"}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the 'MADE BY' text near the 'WICK CRAFT' stamp?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show a product label?'}]

openai_answers: 1. **Answer Each Question:**

   - Does the text 'White Musk' appear in the image?  
     - yes

   - Is the background color beige?  
     - yes

   - Is the text color predominantly black?  
     - no

   - Is the batch number positioned on the right?  
     - yes

   - Is the text 'Scented Soy Wax Candle' located beneath the text 'FRESH COTTON'?  
     - yes

   - Is the candle's name 'FRESH COTTON'?  
     - yes

   - Is the batch number '002'?  
     - yes

   - Is the 'WICK CRAFT' stamp circular?  
     - yes

   - Is the 'MADE BY' text near the 'WICK CRAFT' stamp?  
     - n/a

   - Does the image show a product label?  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 9
   - Total Number of Questions: 10

   Score = (9/10) × 100 = 90

score: 90.0

reasons: The score was calculated based on the number of correct answers provided in relation to the total number of questions. Out of 10 questions, 9 were answered correctly, resulting in a score of 90.

token_count: 375

caption_vocabulary_size: 236

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 115

candidate_caption: A breathtaking landscape photograph captures an expansive desert scene during sunset, showcasing the rugged beauty of the arid terrain. The composition is dominated by towering rock formations rising dramatically from smooth, golden sandy dunes in the foreground. A prominent formation on the left side casts sharp shadows across its surface, emphasizing its jagged edges and intricate textures. Its weathered exterior displays horizontal layers that tell a geological story, with shades of deep charcoal gray (#1c1719) and burnt sienna (#d38a5f). To its right stands another significant rocky outcrop, featuring vertical ridges and crevices illuminated by warm sunlight, creating a striking contrast between light beige (#e7ded3) and shadowy areas. These formations are surrounded by undulating sandstone surfaces dotted with small plants and sparse vegetation, their thin, elongated leaves adding subtle hints of green to the earthy palette. The midground extends into more extensive flat desert plains interspersed with additional rock formations, while the background fades into distant mountains shrouded in a hazy blue atmosphere, creating depth and perspective. The sky above transitions from pale powder blue at the horizon to deeper cerulean tones higher up, adorned with scattered clouds of varying densities and shapes. Some appear soft and white near the sun's position, while others are denser and darker, adding texture and dimension to the vast expanse. Long shadows stretch diagonally across the sand, suggesting low-angle sunlight typical of early morning or late afternoon. This interplay creates dramatic highlights and deep contrasts throughout the scene, enhancing the three-dimensional quality of the landscape. Small animal tracks and human-made paths add interest to the otherwise unspoiled environment, hinting at movement through this ancient and timeless setting. The color palette includes rich earthy hues like burnt orange (#8e4b34), deep brown (#3b2d25), sandy beige, and slate grays (#6c6d6c), all bathed in the golden glow of natural daylight. The lighting enhances the textures of both rocks and sand, resulting in a high-contrast visual effect that emphasizes the raw beauty of this majestic desert landscape. The overall mood is tranquil yet awe-inspiring, capturing the serene yet stark nature of this desolate environment and evoking feelings of isolation and timelessness.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the color of the sand in the foreground orange?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a large rock formation in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the shadow falling to the right of the rock formation?'}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Are the rock formations large?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Are the major rock formations irregularly shaped?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there multiple rock formations visible?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there sand in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the sand surrounding the rock formations?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Is the image taken outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a warm color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the color of the sand in the foreground orange?  
   - yes

2. Is there a large rock formation in the center of the image?  
   - no

3. Is the shadow falling to the right of the rock formation?  
   - yes

4. Are the rock formations large?  
   - yes

5. Are the major rock formations irregularly shaped?  
   - yes

6. Are there multiple rock formations visible?  
   - yes

7. Is there sand in the image?  
   - yes

8. Is the sand surrounding the rock formations?  
   - yes

9. Is the image taken outdoors?  
   - yes

10. Does the image have a warm color palette?  
    - yes

11. Is the image a photograph?  
    - yes

12. Is the image color graded with high saturation?  
    - n/a

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 12  

Score = (11/12) × 100 = 91.67

score: 91.67

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 11 out of 12 questions were answered correctly, resulting in a score of 91.67%.

token_count: 462

caption_vocabulary_size: 308

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 120

candidate_caption: A cinematic scene from 'Mortal Kombat' features a muscular bald man positioned slightly to the right of center, facing towards the camera with an intense expression. His face is illuminated by vibrant purple light, highlighting his serious demeanor and creating strong shadows on one side of his face while emphasizing his facial contours. The subject wears a black sleeveless top made of shiny material, appearing wet or glossy, which reflects the dramatic lighting and adds texture to the scene. Beads of sweat are visible on his skin, suggesting physical exertion or tension. The background consists of dark, textured stone walls with intricate carvings resembling ancient artifacts, partially obscured in shadow but featuring hints of amber yellow light casting faint glows on some elements. A large, blurred statue can be seen on the left side of the frame, adding depth to the setting. The overall mood is tense and mysterious, enhanced by high contrast, low luminance, and vivid colors dominated by purples and blacks. The composition focuses closely on the character's upper body and head, with shallow depth of field keeping the background out of focus and emphasizing the intensity of the moment. The color palette includes deep blues, rich purples, warm yellows, and muted browns, contributing to the film's atmospheric and dramatic style reminiscent of 1990s cinema.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the background mainly dark?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person positioned in the center-right of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the person to the right of the yellow-lit stone?'}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Does the person look serious?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is the image blurry?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Is there only one person?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the person in front of the wall?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show indoors?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a person in the image?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have dark tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a shot from a film?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with high contrast?'}]

openai_answers: 1. Is the background mainly dark?  
   - yes

2. Is the person positioned in the center-right of the image?  
   - yes

3. Is the person to the right of the yellow-lit stone?  
   - yes

4. Does the person look serious?  
   - yes

5. Is the image blurry?  
   - no

6. Is there only one person?  
   - yes

7. Is the person in front of the wall?  
   - yes

8. Does the image show indoors?  
   - n/a

9. Is there a person in the image?  
   - yes

10. Does the image have dark tones?  
    - yes

11. Is the image a shot from a film?  
    - yes

12. Is the image color graded with high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 11  
Total Number of Questions: 12  

Score = (11/12) × 100 = 91.67

score: 91.67

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 11 out of 12 questions were answered correctly, resulting in a score of 91.67%.

token_count: 265

caption_vocabulary_size: 178

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 122

candidate_caption: A realistic urban night scene captures four transparent umbrellas with raindrops, creating an intricate network of water droplets across their surfaces. The foreground showcases these umbrellas, each heavily laden with droplets ranging from small specks to larger clusters, particularly visible on the right side where the largest umbrella dominates the frame. These umbrellas are positioned diagonally, adding depth and complexity to the composition. In the midground, there is a red traffic light with a pedestrian symbol illuminated in bright white, partially obscured by one of the umbrellas. A black street sign stands nearby, adorned with Japanese characters '本' (meaning "home" or "house") in white sans-serif font. The background reveals modern building facades featuring large glass windows and illuminated signs, including prominent 'STARBUCKS COFFEE' text in bright white neon letters against dark glass panels. Additional neon signs reflect off the wet surfaces of the umbrellas, enhancing the city's vibrant atmosphere. A circular blue directional sign indicating walking on green is also visible through the reflections. The lighting is a mix of artificial sources like streetlights and building lights, casting a cool tone over the entire scene while highlighting specific elements such as the glowing traffic light. The overall mood is calm yet slightly melancholic, enhanced by the high contrast between the brightly lit signage and darker surroundings. The color palette includes shades of charcoal gray (#2e2f30), slate blue (#596d7a), light steel blue (#b0c3cd), warm brown (#6e5e4f), deep taupe (#61585c), and muted lavender (#afadb8). The scene is captured from a slightly upward angle, emphasizing the height of buildings and the presence of multiple layers of umbrellas. This layered perspective creates a sense of depth and complexity within this bustling city environment at night, showcasing both the intimate details of everyday life and the expansive nature of urban spaces.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there any text in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is there any red color in the image?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the overall color tone of the image dark?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there an umbrella in the image?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is there a pedestrian signal light near the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is there an umbrella to the right of the pedestrian signal light?'}
 {'answer': 'no', 'category': 'blur', 'question': 'Is the background blurred?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there four umbrellas in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a pedestrian signal light in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': "Is the pedestrian signal light indicating 'stop'?"}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image taken outdoors?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Is the image color graded with a high contrast?'}]

openai_answers: 1. Is there any text in the image?  
   - yes

2. Is there any red color in the image?  
   - yes

3. Is the overall color tone of the image dark?  
   - yes

4. Is there an umbrella in the image?  
   - yes

5. Is there a pedestrian signal light near the center of the image?  
   - yes

6. Is there an umbrella to the right of the pedestrian signal light?  
   - yes

7. Is the background blurred?  
   - no

8. Are there four umbrellas in the image?  
   - yes

9. Is there a pedestrian signal light in the image?  
   - yes

10. Is the pedestrian signal light indicating 'stop'?  
    - yes

11. Does the image show outdoors?  
    - yes

12. Is the image a photograph?  
    - n/a

13. Is the image taken outdoors?  
    - yes

14. Is the image color graded with a high contrast?  
    - yes

**Calculate Score:**

Number of Correct Answers: 13  
Total Number of Questions: 14  

Score = (13/14) × 100 = 92.86

score: 92.86

reasons: The score is calculated based on the number of correct answers provided out of the total number of questions. In this case, 13 out of 14 questions were answered correctly, resulting in a score of 92.86%.

token_count: 385

caption_vocabulary_size: 250

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 140

candidate_caption: A close-up portrait photograph of a person with closed eyes, exuding serenity and contemplation against a vibrant yellow wall. The subject's face is slightly tilted upwards, with their head leaning back against the bright yellow backdrop, which provides high contrast to their rich cobalt blue (#1e3f8b) pleated fabric top. Their skin tone is warm brown with visible texture, highlighted by shimmering metallic gold eyeshadow that catches the sunlight, complemented by bold hot pink lipstick. The individual has short, textured black hair styled in natural afro curls, framing their face beautifully. They are wearing large, intricate silver feather-shaped earrings that add an elegant touch. The person's arms are raised above their head, with hands clasped together at the top left corner, creating a dynamic pose. The pleated fabric of their top features subtle vertical ridges that add depth and interest to the scene, extending from the high collar up to the sleeves. The lighting is dramatic and natural, with strong backlighting from the sun positioned behind the subject, casting a soft glow around their head and creating lens flares in green, blue, yellow, and white hues. This backlighting creates a striking halo effect around their hair and forehead, emphasizing textures and contours. The shallow depth of field keeps the focus on the subject while blurring the background, where hints of green foliage can be seen through gaps between structures, suggesting an outdoor setting. A small circular window or light source near the bottom edge of the frame adds to the brightness of the scene. The overall mood is peaceful and artistic, enhanced by the vivid colors, balanced exposure with slight overexposure in highlights, and harmonious color palette dominated by royal blue, golden yellow, and various shades of brown.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': "Is the person's shirt blue?"}
 {'answer': 'yes', 'category': 'color', 'question': "Are the person's lips bright pink?"}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the person in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the person's face in front of the bright light source?"}
 {'answer': 'yes', 'category': 'emotion', 'question': 'Is the person relaxed?'}
 {'answer': 'yes', 'category': 'artifacts', 'question': 'Is there lens flare in the image?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a bright color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Are there earrings in the image?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show sunlight?'}
 {'answer': 'yes', 'category': 'blur', 'question': 'Is the background blurred?'}]

openai_answers: 1. "Is the person's shirt blue?"  
   - yes

2. "Are the person's lips bright pink?"  
   - yes

3. "Is the person in the center of the image?"  
   - n/a

4. "Is the person's face in front of the bright light source?"  
   - yes

5. "Is the person relaxed?"  
   - yes

6. "Is there lens flare in the image?"  
   - yes

7. "Does the image have a bright color palette?"  
   - yes

8. "Is the image a photograph?"  
   - yes

9. "Are there earrings in the image?"  
   - yes

10. "Does the image show sunlight?"  
    - yes

11. "Is the background blurred?"  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 11  

Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score is calculated based on the number of 'yes' answers, which are considered correct, out of the total number of questions. There were 10 'yes' answers out of 11 questions, resulting in a score of 90.91%.

token_count: 354

caption_vocabulary_size: 222

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 167

candidate_caption: A photograph taken during twilight showcases the iconic Main Street Plaza Railway station building, captured from a straight-on angle at eye level. The scene is framed by lush green shrubs and a calm body of water in the foreground, reflecting the illuminated structure beautifully. Four ducks can be seen near the edge of the grassy embankment, adding to the tranquil atmosphere. The midground features well-manicured lawns with dense green bushes forming a natural barrier along the curved path leading up to the entrance. Several people are walking or standing around this area, dressed in casual summer attire such as shorts, t-shirts, and light shirts. The background prominently displays the grand Victorian-style structure, characterized by its ornate white facade with intricate architectural details including decorative columns, arches, and an elaborate dome topped with a flagpole. Warm golden lights outline the domed roof and eaves, creating a charming glow against the evening sky. Large windows on either side of the main entrance reveal warmly lit interiors. A sign above the arched entryway reads 'Main Street Plaza Railway' in bold, decorative letters, while another sign nearby indicates it's open 24 hours. Two tall palm trees flank the building, their fronds extending into the frame and providing vertical lines that complement the horizontal layout. The clear sky transitions from a deeper blue at the top to a lighter shade near the horizon, enhancing the serene mood. The overall color palette includes shades of deep umber (#251f1a), pale cerulean (#b3c8d4), warm taupe (#947b6e), muted sage (#6b7b5a), soft beige (#b09a90), and slate gray (#53565d). The lighting creates a balanced exposure with medium contrast and saturation, emphasizing the historical charm and inviting ambiance of this enchanting setting.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': 'Is there text on the building?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky light blue?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the building in the center of the image?'}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Are the palm trees on either side of the building?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the building roof dome-shaped?'}
 {'answer': 'yes', 'category': 'count', 'question': 'Are there many people in the image?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there water in the image?'}
 {'answer': 'yes', 'category': 'relation', 'question': 'Is the building reflected in the water?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have warm tones?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is there text on the building?  
   - yes

2. Is the sky light blue?  
   - yes

3. Is the building in the center of the image?  
   - n/a

4. Are the palm trees on either side of the building?  
   - yes

5. Is the building roof dome-shaped?  
   - yes

6. Are there many people in the image?  
   - yes

7. Is there water in the image?  
   - yes

8. Is the building reflected in the water?  
   - yes

9. Does the image show outdoors?  
   - yes

10. Does the image have warm tones?  
    - yes

11. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 11  

Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 10 out of 11 questions were answered correctly, resulting in a score of 90.91%.

token_count: 369

caption_vocabulary_size: 262

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 191

candidate_caption: A photograph captures a serene Mediterranean-style entrance featuring a vibrant teal green wooden door with six panels, each showing signs of wear and aging, particularly noticeable at its bottom edge where metal plates have chipped off. The door is equipped with a silver handle on the right side and small metallic hinges on both sides. It's set in a bright white stucco wall with visible texture and slight cracks, creating high contrast against the door's color. To the left of the door, a tall, slender cactus with a rough brown trunk and dark green spiky arms extends vertically upwards, partially wrapped by a thin wire or cable. Below it, there's a rectangular white planter box containing green foliage with red flowers. Adjacent to this is a white vertical drainage pipe running along the wall. A white utility box with ribbed texture and a square switch panel is mounted near the base of the cactus. Above the door, an upper-level window reveals a person peeking out from behind curtains. The scene is complemented by lush magenta bougainvillea flowers hanging from the top right corner, adding pops of color to the composition. In front of the door, a small worn concrete step leads up to the threshold. The ground below consists of interlocking grayish-brown cobblestones arranged in a grid pattern, extending into the foreground. Scattered pink petals lie across the pavement, enhancing the tranquil atmosphere of this simple yet visually striking structure.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'color', 'question': 'Is the door green?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the wall white?'}
 {'answer': 'yes', 'category': 'position', 'question': 'Is the cactus on the left side of the image?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the man's head visible at the top of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': 'Is the door to the right of the cactus?'}
 {'answer': 'yes', 'category': 'entity', 'question': 'Is there a plant in the image?'}
 {'answer': 'yes', 'category': 'entity shape', 'question': 'Is the door rectangular?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'yes', 'category': 'color palette', 'question': 'Does the image have a neutral color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}]

openai_answers: 1. Is the door green?  
   - yes

2. Is the wall white?  
   - yes

3. Is the cactus on the left side of the image?  
   - yes

4. Is the man's head visible at the top of the image?  
   - yes

5. Is the door to the right of the cactus?  
   - yes

6. Is there a plant in the image?  
   - yes

7. Is the door rectangular?  
   - yes

8. Does the image show outdoors?  
   - yes

9. Does the image have a neutral color palette?  
   - no

10. Is the image a photograph?  
    - yes

**Calculate Score:**

Number of Correct Answers: 9  
Total Number of Questions: 10  

Score = (9/10) × 100 = 90

score: 90.0

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 9 out of 10 questions were answered correctly, resulting in a score of 90%.

token_count: 292

caption_vocabulary_size: 196

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 194

candidate_caption: A dramatic outdoor photograph captures an intense moment of ice skating on a vast, frozen lake under the golden hour sun. The composition is vertically centered, with a large triangular piece of clear, translucent ice dominating the foreground. This chunk of ice, which appears to be embedded in or floating above the dark teal-colored water beneath, shows intricate textures including trapped bubbles, cracks, and small air pockets. Its sharp edges glisten against the darker blue background, creating a striking contrast. In the midground, a skater dressed entirely in black attire (jacket, pants, and skate shoes) stands gracefully on one leg, leaning forward with arms extended upwards. Their silhouette is sharply defined against the bright sunlight, casting a long shadow towards the camera. The figure's dynamic pose suggests movement and fluidity, capturing the essence of ice skating. The background features towering mountain ranges covered in dense forests at their bases, rising majestically into the sky. These peaks are rendered in various shades of grayish-blue and charcoal (#343d44), with some snow-capped summits visible against the gradient sky. Wispy clouds stretch across the upper portion of the frame, while the sun itself creates a prominent starburst effect near the skater's head, adding drama and intensity to the scene. The lighting is natural daylight from a low angle, casting strong shadows and highlighting the contours of both the ice and the skater. The color palette includes deep navy blues (#172f39), slate grays (#7b8ca3), steel blues (#6c8ea2), warm terracotta tones (#a97261), and rich browns (#5e4c36), all contributing to the serene yet powerful atmosphere. Small white specks scattered across the surface of the icy expanse add texture and depth to the scene. The overall mood is tranquil yet energetic, showcasing the beauty of nature combined with human athleticism.

captioned_by: pg-captioner

ground_truth: [{'answer': 'Yes', 'category': 'color', 'question': 'Is the sky blue?'}
 {'answer': 'Yes', 'category': 'position', 'question': 'Is the person in the top part of the image?'}
 {'answer': 'Yes', 'category': 'entity size', 'question': 'Is the ice chunk large?'}
 {'answer': 'Yes', 'category': 'entity shape', 'question': 'Is the ice chunk triangular?'}
 {'answer': 'Yes', 'category': 'count', 'question': 'Is there one person in the image?'}
 {'answer': 'Yes', 'category': 'relation', 'question': 'Is the person posing on ice?'}
 {'answer': 'Yes', 'category': 'general', 'question': 'Does the image show outdoors?'}
 {'answer': 'Yes', 'category': 'color palette', 'question': 'Does the image have a cool color palette?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}
 {'answer': 'no', 'category': 'color grading', 'question': 'Is the image color graded with high saturation?'}]

openai_answers: 1. Is the sky blue?  
   - yes

2. Is the person in the top part of the image?  
   - no

3. Is the ice chunk large?  
   - yes

4. Is the ice chunk triangular?  
   - yes

5. Is there one person in the image?  
   - yes

6. Is the person posing on ice?  
   - yes

7. Does the image show outdoors?  
   - yes

8. Does the image have a cool color palette?  
   - yes

9. Is the image a photograph?  
   - yes

10. Does the image have high contrast?  
    - yes

11. Is the image color graded with high saturation?  
    - no

**Calculate Score:**

Number of Correct Answers: 10  
Total Number of Questions: 11  

Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score is calculated based on the number of correct answers out of the total number of questions. In this case, 10 out of 11 questions were answered correctly, resulting in a score of 90.91%.

token_count: 382

caption_vocabulary_size: 257

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

#### Sample 195

candidate_caption: A close-up photograph captures the striking design elements of an Alaska Airlines airplane, emphasizing its tail section and part of the fuselage against a vivid blue sky (#87CEEB). The right side of the image showcases the tail wing in crimson red color with intricate details such as rivets, circular panels, and structural lines visible on its metallic surface. Prominently displayed on this wing is the white 'AS' logo representing the University of Alaska Fairbanks Huskies, featuring stylized husky-like imagery that includes sharp teeth, pointed ears, curved fangs, and flowing mane. A small oval-shaped door or panel is visible near the top left corner of the wing. The left side of the image reveals more of the aircraft's sleek wing structure, which transitions from dark gray at the base to black towards the tip, adorned with evenly spaced yellow and white markings along its edge. The lower portion displays the text 'Alaska HORIZON' in bold white sans-serif font. In the background, the bright red body of the aircraft is partially visible, showcasing large white cursive script text reading 'Alaska'. Several small rectangular windows are aligned horizontally near the cockpit area, each framed by thin white borders and black outlines. The scene is well-lit by natural daylight, creating high contrast between the vibrant colors of the aircraft and the clear blue sky, which provides a stark backdrop that enhances the visual impact of the red hue and white detailing. Two antennas protrude from the upper right corner of the tail fin, adding technical detail to the composition. The overall mood is professional and modern, capturing the essence of commercial aviation photography with balanced exposure and saturation levels that emphasize both the technological aspects and brand identity of the Alaska Horizon fleet.

captioned_by: pg-captioner

ground_truth: [{'answer': 'yes', 'category': 'text', 'question': "Does the image contain the text 'Alaska'?"}
 {'answer': 'yes', 'category': 'text', 'question': "Is the text 'HORIZON' on the bottom?"}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the sky color blue?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the color of the text off-white?'}
 {'answer': 'yes', 'category': 'color', 'question': 'Is the aircraft red?'}
 {'answer': 'yes', 'category': 'position', 'question': "Is the airplane's wing on the right side of the image?"}
 {'answer': 'yes', 'category': 'relative position', 'question': "Is the text 'Alaska' to the left of the airplane's wing?"}
 {'answer': 'yes', 'category': 'entity size', 'question': 'Is the airplane large?'}
 {'answer': 'yes', 'category': 'general', 'question': 'Does the image show daylight?'}
 {'answer': 'yes', 'category': 'image type', 'question': 'Is the image a photograph?'}
 {'answer': 'yes', 'category': 'color grading', 'question': 'Does the image have high contrast?'}]

openai_answers: 1. **Answer Each Question:**

   - "Does the image contain the text 'Alaska'?"  
     - yes

   - "Is the text 'HORIZON' on the bottom?"  
     - yes

   - "Is the sky color blue?"  
     - yes

   - "Is the color of the text off-white?"  
     - n/a

   - "Is the aircraft red?"  
     - yes

   - "Is the airplane's wing on the right side of the image?"  
     - yes

   - "Is the text 'Alaska' to the left of the airplane's wing?"  
     - yes

   - "Is the airplane large?"  
     - n/a

   - "Does the image show daylight?"  
     - yes

   - "Is the image a photograph?"  
     - yes

   - "Does the image have high contrast?"  
     - yes

2. **Calculate Score:**

   - Number of Correct Answers: 10
   - Total Number of Questions: 11

   Score = (10/11) × 100 = 90.91

score: 90.91

reasons: The score is calculated based on the number of correct answers provided in relation to the total number of questions. Out of 11 questions, 10 were answered correctly, resulting in a score of 90.91%.

token_count: 347

caption_vocabulary_size: 221

score_bin: 90-100

evaluated_by: gpt-4o-2024-08-06

