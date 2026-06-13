# 🚦 Traffic Sign Classification

**[🔴 Try the Live Web App Here!](https://trafficsignclassification-27.streamlit.app/)**

## 🎥 Demo

https://github.com/user-attachments/assets/streamlit-app-demo.webm

This is a Deep Learning project I built to classify images of traffic signs into 43 distinct categories using a Convolutional Neural Network (CNN).

The model was trained on the German Traffic Sign Recognition Benchmark (GTSRB) [Dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) and is integrated into a web application for easy testing and predictions.

## 🚀 Project Structure

- **`traffic_signs.ipynb`**: My research notebook containing the data loading, preprocessing, and model training code.
- **`app.py`**: The interactive web application built with Streamlit.
- **`traffic_classifier.h5`**: The trained Keras neural network model weights.

## 💻 How to Run Locally

To run the web application on your own computer, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rkstylecode/traffic_sign_classification.git
   cd traffic_sign_classification
   ```

2. **Install the requirements:**
   Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the web application:**
   ```bash
   streamlit run app.py
   ```
   This will automatically open the web application in your default browser!

## 🧠 Technologies Used
* **Deep Learning:** TensorFlow, Keras
* **Computer Vision:** PIL (Pillow), NumPy
* **Frontend UI:** Streamlit
