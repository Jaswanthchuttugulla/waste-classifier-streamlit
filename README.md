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

