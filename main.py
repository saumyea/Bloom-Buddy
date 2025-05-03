import streamlit as st
import tensorflow as tf
import numpy as np
import sqlite3
import random
from tensorflow.keras.preprocessing import image

# Function to fetch class names and descriptions from the database
def fetch_class_info():
    conn = sqlite3.connect('plant_diseases.db')
    c = conn.cursor()
    c.execute("SELECT class_name, description FROM PlantDiseases")
    result = c.fetchall()
    
    conn.close()
    return result

# Tensorflow Model Prediction
def model_prediction(test_image):
    # Your model prediction code here
    model = tf.keras.models.load_model('plant_disease_model.h5')

    # Load and preprocess the new image
    img = image.load_img(test_image, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values

    # Make a prediction
    predictions = model.predict(img_array)

    # Get the top 5 predicted classes and their corresponding probabilities
    top5_indices = np.argsort(predictions[0])[-5:][::-1]
    top5_probs = predictions[0][top5_indices]

    # Define the class indices and labels 
    class_indices = {
        0: 'Apple__black_rot',
        1: 'Apple__healthy',
        2: 'Apple__rust',
        3: 'Apple__scab',
        4: 'Cherry__healthy',
        5: 'Cherry__powdery_mildew',
        6: 'Chili__healthy',
        7: 'Chili__leaf curl',
        8: 'Chili__leaf spot',
        9: 'Chili__whitefly',
        10: 'Chili__yellowish',
        11: 'Coffee__cercospora_leaf_spot',
        12: 'Coffee__healthy',
        13: 'Coffee__red_spider_mite',
        14: 'Coffee__rust',
        15: 'Cucumber__diseased',
        16: 'Cucumber__healthy',
        17: 'Gauva__diseased',
        18: 'Gauva__healthy',
        19: 'Lemon__diseased',
        20: 'Lemon__healthy',
        21: 'Mango__diseased',
        22: 'Mango__healthy',
        23: 'Peach__bacterial_spot',
        24: 'Peach__healthy',
        25: 'Pepper_bell__bacterial_spot',
        26: 'Pepper_bell__healthy',
        27: 'Pomegranate__diseased',
        28: 'Pomegranate__healthy',
        29: 'Potato__early_blight',
        30: 'Potato__healthy',
        31: 'Potato__late_blight',
        32: 'Strawberry___leaf_scorch',
        33: 'Strawberry__healthy',
        34: 'Tea__algal_leaf',
        35: 'Tea__anthracnose',
        36: 'Tea__bird_eye_spot',
        37: 'Tea__brown_blight',
        38: 'Tea__healthy',
        39: 'Tea__red_leaf_spot',
        40: 'Tomato__bacterial_spot',
        41: 'Tomato__early_blight',
        42: 'Tomato__healthy',
        43: 'Tomato__late_blight',
        44: 'Tomato__leaf_mold',
        45: 'Tomato__mosaic_virus',
        46: 'Tomato__septoria_leaf_spot',
        47: 'Tomato_spider_mites(two_spotted_spider_mite)',
        48: 'Tomato__target_spot',
        49: 'Tomato__yellow_leaf_curl_virus'
    }
    class_labels = list(class_indices.values())

    # Print the top 5 predictions and their probabilities
    for i in range(5):
        print(f"Prediction {i+1}: {class_labels[top5_indices[i]]} - Probability: {top5_probs[i]}")

    if top5_probs[0] < 0.8:
        return None

    # Return the predicted class index
    return top5_indices[0]

# Function to check if the user is registered
def is_user_registered(username):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to fetch user's test history
def fetch_user_test_history(username):
    conn = sqlite3.connect('user_test_history.db')
    c = conn.cursor()
    c.execute("SELECT test_image, predicted_class FROM UserTestHistory WHERE username = ?", (username,))
    history = c.fetchall()
    conn.close()
    return history

# Sidebar
def sidebar():
    st.sidebar.title("Dashboard")
    app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition", "Login", "Register", "Test History"])

    # Main Page
    if app_mode == "Home":
        st.header("PLANT DISEASE RECOGNITION SYSTEM")
        image_path = "home_page.jpeg"
        st.image(image_path, use_column_width=True)
        st.markdown("""
        Welcome to the Plant Disease Recognition System! 🌿🔍
        
        Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

        ### How It Works
        1. *Upload Image:* Go to the *Disease Recognition* page and upload an image of a plant with suspected diseases.
        2. *Analysis:* Our system will process the image using advanced algorithms to identify potential diseases.
        3. *Results:* View the results and recommendations for further action.

        ### Why Choose Us?
        - *Accuracy:* Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
        - *User-Friendly:* Simple and intuitive interface for seamless user experience.
        - *Fast and Efficient:* Receive results in seconds, allowing for quick decision-making.

        ### Get Started
        Click on the *Disease Recognition* page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

        ### About Us
        Learn more about the project, our team, and our goals on the *About* page.
        """)

    # About Project
    elif app_mode == "About":
        st.header("About")
        st.markdown("""
### About Dataset:
 This experiment utilized a substantial dataset comprising 36,406 images, with 29,106 images allocated for training and 7,300 images for testing, divided into a ratio of 80:20. Each image was categorized into one of 50 classes. Data preprocessing played a pivotal role in preparing the dataset for model training, ensuring robustness and generalization.

### Content:

- train: This directory contains 29,106 images utilized for training the model.
- test: A set of 7,300 images for testing the trained model's performance.

The dataset was meticulously curated to ensure diversity and representativeness across different classes, facilitating effective model learning and inference.

### CNN Model:

A Convolutional Neural Network (CNN) is a deep learning architecture specifically designed for image classification tasks. It comprises multiple layers, including convolutional layers, pooling layers, and fully connected layers. 

- Convolutional layers: These layers apply convolutional filters to extract features from the input image. Each filter detects specific patterns or features, such as edges or textures.
  
- Pooling layers: Pooling layers reduce the dimensionality of the feature maps generated by convolutional layers, helping to retain the most important information while reducing computational complexity.
  
- Fully connected layers: These layers connect every neuron in one layer to every neuron in the next layer, enabling the network to learn complex patterns and relationships in the data.

CNNs are well-suited for image recognition tasks due to their ability to automatically learn hierarchical representations of features directly from raw pixel data, making them highly effective for tasks such as image classification, object detection, and image segmentation.
                    """)

    # Prediction Page
    elif app_mode == "Disease Recognition":
        if st.session_state.get("logged_in", False):  # Check if user is logged in
            st.header("Disease Recognition")
            test_image = st.file_uploader("Choose an Image:")
            if st.button("Show Image"):
                st.image(test_image, width=4, use_column_width=True)

            # Predict button
            if st.button("Predict"):
                st.write("Our Prediction")
                if test_image:
                    result_index = model_prediction(test_image)
                    if result_index is not None:
                        class_data = fetch_class_info()
                        class_name, description = class_data[result_index]
                        st.success(f"Model is predicting it's a {class_name}\n\nDescription: {description}")

                        # Log the user's test
                        # custom_class_name = st.text_input("Enter custom class name (optional):")
                        # print(custom_class_name)
    
                        # if custom_class_name:
                        #     class_name = custom_class_name
                        # take_input()
                      
                        log_user_test(st.session_state['username'], test_image, class_name)
                    else:
                        st.error("Sorry, the model is not confident enough to make a prediction.")
                else:
                    st.warning("Please upload an image for prediction.")
        else:
            st.warning("Please login to access disease recognition functionality.")

    # Login Page
    elif app_mode == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            result = login_user(username, password)
            if result:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"Welcome back, {username}! You are now logged in. You can now access the disease recognition facility.")
               
            else:
                if is_user_registered(username):
                    st.error("Invalid username or password")
                else:
                    st.error("Invalid username or password. If you haven't registered yet, please do so.")
            

    # Register Page
    elif app_mode == "Register":
        st.title("Register")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        if st.button("Register"):
            add_user(new_username, new_password)
            st.success(f"Registered successfully {new_username}! Please login.")

        

    # Test History Page
    elif app_mode == "Test History":
        if st.session_state.get("logged_in", False):  # Check if user is logged in
            st.title("Test History")
            
            username = st.session_state['username']
            st.header(f"Welcome {username}!")
            history = fetch_user_test_history(username)
            if history:
                st.write("Your Test History:")
                for test in history:
                    st.write(f"Test Image: {test[0]}, Predicted Class: {test[1]}")
            else:
                st.info("No test history available.")
        else:
            st.warning("Please login to view your test history.")
    if st.session_state.get("logged_in", False):  # Check if user is logged in
        st.sidebar.button("Logout", on_click=logout_user)

# Function to create user table in the database
def take_input():
    user_input = st.text_input("Enter something:")
    print(user_input)

                        # Print the input
    if user_input:
        st.write("You entered:", user_input)

def create_user_table():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Function to login user
def login_user(username, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

# Function to logout user
def logout_user():
    # Reset session state or clear any stored session information
    st.session_state.pop('username', None)
    st.session_state.pop('logged_in', False)
    st.success("You have been logged out.")

# Function to log user's test
def log_user_test(username, test_image, predicted_class):
    
    conn = sqlite3.connect('user_test_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO UserTestHistory (username, test_image, predicted_class) VALUES (?, ?, ?)", (username, test_image.name, predicted_class))
    conn.commit()
    conn.close()

# Function to create user test history table in the database
def create_user_test_history_table():
    conn = sqlite3.connect('user_test_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS UserTestHistory
                 (username TEXT, test_image TEXT, predicted_class TEXT)''')
    conn.commit()
    conn.close()

# Main function
def main():
    create_user_table()
    create_user_test_history_table()
    sidebar()

if __name__ == "__main__":
    main()