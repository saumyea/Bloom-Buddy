import sqlite3

# Create a SQLite database and connect to it
conn = sqlite3.connect('plant_diseases.db')
c = conn.cursor()

# Create a table to store class names and descriptions
c.execute('''CREATE TABLE IF NOT EXISTS PlantDiseases
             (class_name TEXT PRIMARY KEY, description TEXT)''')

# Insert class names and descriptions into the table
class_data = [
    ('Apple__black_rot', 'Denotes apple plants affected by black rot disease, characterized by black, circular lesions on fruit, leaves, and twigs, leading to fruit decay and defoliation.'),
    ('Apple__healthy', 'Represents healthy apple plants with vibrant green foliage, vigorous growth, and high-quality fruit production, devoid of any visible signs of diseases or pest infestations.'),
    ('Apple__rust', 'Indicates apple plants exhibiting symptoms of rust disease, showing orange to rusty brown spots or pustules on leaves and fruit, leading to premature defoliation and reduced fruit yield.'),
    ('Apple__scab', 'Denotes apple plants afflicted by apple scab disease, characterized by olive-green to black lesions with a velvety texture on leaves and fruit, leading to defoliation and fruit blemishes.'),
    ('Cherry__healthy', 'Represents healthy cherry plants with lush green foliage, vigorous growth, and high-quality fruit production, free from any visible signs of diseases or pest infestations.'),
    ('Cherry__powdery_mildew', 'Indicates cherry plants affected by powdery mildew disease, showing white powdery patches on leaves and shoots, leading to reduced photosynthesis and fruit quality.'),
    ('Chili__healthy', 'Represents healthy chili plants with vibrant green foliage, robust growth, and high fruit production, devoid of any visible signs of diseases or pest infestations.'),
    ('Chili__leaf curl', 'Denotes chili plants exhibiting symptoms of leaf curl disease, characterized by upward curling and distortion of leaves, leading to reduced photosynthesis and fruit yield.'),
    ('Chili__leaf spot', 'Indicates chili plants affected by leaf spot disease, showing dark, irregular lesions on leaves, leading to defoliation and reduced fruit quality.'),
    ('Chili__whitefly', 'Represents chili plants infested with whiteflies, showing symptoms such as yellowing of leaves, sticky honeydew secretions, and reduced vigor, leading to poor fruit development and yield.'),
    ('Chili__yellowish', 'Indicates chili plants displaying yellowing of leaves, which could be due to various factors such as nutrient deficiencies, water stress, or diseases, potentially leading to reduced growth and yield.'),
    ('Coffee__cercospora_leaf_spot', 'Denotes coffee plants exhibiting symptoms of cercospora leaf spot disease, characterized by small, dark lesions with yellow halos on leaves, leading to defoliation and reduced yield.'),
    ('Coffee__healthy', 'Represents healthy coffee plants with lush green foliage, vigorous growth, and high-quality bean production, free from any visible signs of diseases or pest infestations.'),
    ('Coffee__red_spider_mite', 'Indicates coffee plants infested with red spider mites, showing symptoms such as stippling, webbing, and leaf discoloration, leading to reduced photosynthesis and yield.'),
    ('Coffee__rust', 'Denotes coffee plants affected by coffee rust disease, showing orange to rusty brown powdery spots on leaves and stems, leading to defoliation and reduced bean quality and yield.'),
    ('Cucumber__diseased', 'Indicates cucumber plants exhibiting symptoms of various diseases, such as wilting, yellowing of leaves, lesions, or rotting, leading to reduced growth and fruit quality.'),
    ('Cucumber__healthy', 'Represents healthy cucumber plants with lush green foliage, vigorous growth, and high-quality fruit production, free from any visible signs of diseases or pest infestations.'),
    ('Gauva__diseased', 'Denotes guava plants displaying symptoms of various diseases, such as wilting, leaf spots, yellowing, or fruit rotting, leading to reduced vigor and fruit yield.'),
    ('Gauva__healthy', 'Represents healthy guava plants with vibrant green foliage, robust growth, and high fruit production, devoid of any visible signs of diseases or pest infestations.'),
    ('Lemon__diseased', 'Indicates lemon plants exhibiting symptoms of various diseases, such as leaf yellowing, leaf spots, wilting, or fruit rotting, leading to reduced vigor and fruit yield.'),
    ('Lemon__healthy', 'Represents healthy lemon plants with lush green foliage, vigorous growth, and high-quality fruit production, free from any visible signs of diseases or pest infestations.'),
    ('Mango__diseased', 'Denotes mango plants displaying symptoms of various diseases, such as wilting, leaf spots, yellowing, or fruit rotting, leading to reduced vigor and fruit yield.'),
    ('Mango__healthy', 'Represents healthy mango plants with vibrant green foliage, robust growth, and high fruit production, devoid of any visible signs of diseases or pest infestations.'),
    ('Peach__bacterial_spot', 'Indicates peach plants affected by bacterial spot disease, showing dark, water-soaked lesions on leaves and fruit, leading to defoliation and reduced fruit quality and yield.'),
    ('Peach__healthy', 'Represents healthy peach plants with lush green foliage, vigorous growth, and high-quality fruit production, free from any visible signs of diseases or pest infestations.'),
    ('Pepper_bell__bacterial_spot', 'Denotes bell pepper plants exhibiting symptoms of bacterial spot disease, characterized by dark, water-soaked lesions on leaves and fruit, leading to defoliation and reduced fruit yield.'),
    ('Pepper_bell__healthy', 'Represents healthy bell pepper plants with vibrant green foliage, robust growth, and high-quality fruit production, devoid of any visible signs of diseases or pest infestations.'),
    ('Pomegranate__diseased', 'Indicates pomegranate plants displaying symptoms of various diseases, such as wilting, leaf spots, yellowing, or fruit rotting, leading to reduced vigor and fruit yield.'),
    ('Pomegranate__healthy', 'Represents healthy pomegranate plants with lush green foliage, vigorous growth, and high fruit production, free from any visible signs of diseases or pest infestations.'),
    ('Potato__early_blight', 'Denotes potato plants exhibiting symptoms of early blight disease, characterized by dark, concentric rings or lesions with a yellow halo on leaves, leading to defoliation and reduced tuber yield.'),
    ('Potato__healthy', 'Represents healthy potato plants with lush green foliage, vigorous growth, and high-quality tuber production, free from any visible signs of diseases or pest infestations.'),
    ('Potato__late_blight', 'Indicates potato plants affected by late blight disease, showing symptoms such as dark lesions with a water-soaked appearance on leaves, leading to rapid defoliation and reduced tuber yield.'),
    ('Strawberry___leaf_scorch', 'Denotes strawberry plants exhibiting symptoms of leaf scorch disease, characterized by browning and necrosis of leaf margins, leading to reduced photosynthesis and yield.'),
    ('Strawberry__healthy', 'Represents healthy strawberry plants with lush green foliage, vigorous growth, and high-quality fruit production, free from any visible signs of diseases or pest infestations.'),
    ('Tea__algal_leaf', 'Indicates tea plants affected by algal leaf spot disease, showing dark, water-soaked lesions or spots on leaves, leading to reduced photosynthesis and yield.'),
    ('Tea__anthracnose', 'Denotes tea plants exhibiting symptoms of anthracnose disease, characterized by dark lesions with concentric rings on leaves and stems, leading to defoliation and reduced yield.'),
    ('Tea__bird_eye_spot', 'Indicates tea plants affected by bird\'s eye spot disease, showing small, dark lesions with a light center on leaves, leading to defoliation and reduced yield.'),
    ('Tea__brown_blight', 'Denotes tea plants exhibiting symptoms of brown blight disease, characterized by brown lesions on leaves and stems, leading to defoliation and reduced yield.'),
    ('Tea__healthy', 'Represents healthy tea plants with lush green foliage, vigorous growth, and high-quality leaf production, free from any visible signs of diseases or pest infestations.'),
    ('Tea__red_leaf_spot', 'Indicates tea plants displaying symptoms of red leaf spot disease, showing reddish-brown lesions on leaves, leading to defoliation and reduced yield.'),
    ('Tomato__bacterial_spot', 'Denotes tomato plants affected by bacterial spot disease, showing dark, water-soaked lesions on leaves and fruit, leading to defoliation and reduced fruit yield.'),
    ('Tomato__early_blight', 'Indicates tomato plants exhibiting symptoms of early blight disease, characterized by dark, concentric rings or lesions with a yellow halo on leaves, leading to defoliation and reduced fruit yield.'),
    ('Tomato__healthy', 'Represents healthy tomato plants with vibrant green foliage, robust growth, and high-quality fruit production, devoid of any visible signs of diseases or pest infestations.'),
    ('Tomato__late_blight', 'Denotes tomato plants affected by late blight disease, showing symptoms such as dark lesions with a water-soaked appearance on leaves, leading to rapid defoliation and reduced fruit yield.'),
    ('Tomato__leaf_mold', 'Indicates tomato plants afflicted by leaf mold disease, displaying symptoms such as fuzzy white or gray patches on the undersides of leaves, caused by fungal infections and high humidity.'),
    ('Tomato__mosaic_virus', 'Represents tomato plants exhibiting symptoms of mosaic virus infection, characterized by mottled or streaked patterns on leaves, stunted growth, and reduced fruit yield.'),
    ('Tomato__septoria_leaf_spot', 'Denotes tomato plants affected by septoria leaf spot disease, showing symptoms such as small dark lesions with a light center on leaves, leading to defoliation and reduced yield.'),
    ('Tomato_spider_mites(two_spotted_spider_mite)', 'Indicates tomato plants infested with two-spotted spider mites, displaying symptoms such as stippling, webbing, and yellowing of leaves, leading to reduced vigor and yield.'),
    ('Tomato__target_spot', 'Represents tomato plants exhibiting symptoms of target spot disease, characterized by concentric rings or bullseye-like lesions on leaves, caused by fungal infections and high humidity.'),
    ('Tomato__yellow_leaf_curl_virus', 'Denotes tomato plants infected with yellow leaf curl virus, showing symptoms such as upward curling and yellowing of leaves, stunted growth, and reduced fruit yield due to viral infection.')
]

c.executemany('INSERT INTO PlantDiseases VALUES (?, ?)', class_data)

# Commit changes and close connection
conn.commit()
conn.close()