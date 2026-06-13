# 🚦 Traffic Sign Classification

This repository contains a Deep Learning project that classifies images of traffic signs into 43 distinct categories. It was trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset. 

The project includes both the data exploration/training notebooks, a local desktop interface, and a modern web application for testing the model.

## 🎥 Demo

*(Insert your video recording or GIF of the working Streamlit website here!)*

> **Tip:** You can literally drag and drop a `.mp4` video file or a `.gif` file right here into the GitHub text editor to upload your video!

## 🚀 Project Structure

- **`traffic_signs.ipynb`**: The research notebook containing the data loading, preprocessing, and Convolutional Neural Network (CNN) training process.
- **`app.py`**: A clean, interactive web application built with Streamlit.
- **`gui.ipynb`**: A local desktop application built with Tkinter.
- **`traffic_classifier.h5`**: The trained Keras neural network model weights.

## 💻 How to Run Locally

If you want to run the web application on your own computer, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/traffic-sign-classification.git
   cd traffic-sign-classification
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
* **Frontend UI:** Streamlit, Tkinter
