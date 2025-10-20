♻️ Waste Classifier Streamlit App

An AI-powered web application that classifies waste images into categories such as cardboard, glass, metal, paper, plastic, or trash.
The app is built using TensorFlow/Keras for deep learning and Streamlit for an interactive web interface, and it is deployed on Render for public access.

🔗 Live Demo:https://waste-classifier-streamlit.onrender.com/

🚀 Features

AI-Powered Waste Classification: Uses a trained CNN model to predict the waste type.

User-Friendly Interface: Built with Streamlit for simplicity and speed.

Cloud Deployment on Render: Accessible from anywhere with a browser.

Instant Image Predictions: Upload a photo and get the classification result instantly.

Modular and Extensible: The structure allows easy updates and improvements.

📁 Project Structure

waste-classifier/
│
├── app.py                     # Main Streamlit app script
├── model/
│   └── waste_classifier.h5     # Pre-trained CNN model
├── requirements.txt            # Required dependencies
├── README.md                   # Documentation
└── assets/
    └── sample_images/          # Example waste images (optional)


🧩 Supported Waste Categories

Cardboard – Boxes, cartons

Glass – Bottles, jars

Metal – Cans, tins

Paper – Sheets, newspapers

Plastic – Bottles, containers

Trash – Non-recyclable waste

🧠 Model Overview

The underlying model is a Convolutional Neural Network (CNN) trained using TensorFlow and Keras.
It learns to differentiate between various waste types based on image patterns, colors, and textures.
The model can be stored locally or downloaded from a cloud source during runtime for flexibility.

⚙️ Requirements

The application is built using:

Python 3.7 or higher

Streamlit

TensorFlow and Keras

NumPy

Pillow

(Optional) gdown or requests for cloud model download

🌍 Deployment on Render

The application is hosted on Render, allowing users to access the app online without local installation.
Render automatically installs dependencies, sets up the environment, and runs the Streamlit app using a specified start command.
This makes deployment quick and scalable for public use.

🙏 Acknowledgments

This project is motivated by the need for sustainable waste management and AI-driven recycling solutions.
It combines open-source tools and public datasets to make waste classification accessible and educational.

Developed using Streamlit for the web interface

Trained using TensorFlow/Keras for image classification

Deployed on Render for cloud accessibility

Inspired by community efforts in environmental sustainability and machine learning for good

## 🧪 Sample Images
### cardboard/
 ![cardboard9 jpg](https://github.com/user-attachments/assets/8ecb2b6a-9814-44ab-8bd7-9104829cf6c4)
 
 ![cardboard246](https://github.com/user-attachments/assets/452ce418-e60d-4c7d-99ed-41e291714a00)

### glass/
 ![glass97](https://github.com/user-attachments/assets/615d7c8b-93ef-4820-984a-13859542f984)
 
 ![glass325](https://github.com/user-attachments/assets/9ce09f04-98bd-44c2-b743-75b0922f866e)


### metal/
 ![metal9](https://github.com/user-attachments/assets/3570a6d8-3759-4421-8dc2-28f0889628b1)

 ![metal141](https://github.com/user-attachments/assets/41835dd2-75bb-4eb8-8f62-59089b4e7e77)


### paper/
 ![paper9](https://github.com/user-attachments/assets/b79357da-3e28-4ac6-b7f7-26a1ebc659f0)
  
 ![paper461](https://github.com/user-attachments/assets/0ab32825-0226-4aad-9358-b056c9e5707b)
`

### plastic/
 ![plastic50](https://github.com/user-attachments/assets/fc755112-0c65-4ba0-9fa9-3070d108dbc1)

 ![plastic327](https://github.com/user-attachments/assets/8ea58e3a-aa0b-45ff-a98e-ae33a229e0cd)



### trash/
 ![trash64](https://github.com/user-attachments/assets/97d5de03-e582-4a07-8910-e0741e683449)

 ![trash137](https://github.com/user-attachments/assets/cc15672e-92e8-464b-9cce-bbf2346a3252)





