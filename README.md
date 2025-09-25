# Advanced Crop & Fertilizer Recommendation System
### Final Project Submission | Edunet Foundation & Shell Internship

This repository contains the final submission for the Machine Learning internship project. This advanced system first predicts the optimal crop for given soil and environmental conditions, and then recommends the most suitable fertilizer for that predicted crop. The project culminates in a fully interactive web application built with Streamlit.

---

### 📋 Project Overview
[cite_start][cite: 11, 12, 13] Traditional farming often relies on intuition for fertilization, which can lead to inefficient nutrient use, increased costs for farmers, and environmental damage. This project tackles that challenge by building a **two-step Smart Recommendation Engine**.

The system moves beyond a simple fertilizer prediction and provides a complete agricultural recommendation:
1.  **Crop Recommendation**: Based on soil data (N, P, K, pH), climate data (rainfall, temperature), and location, the first model predicts the most suitable crop to cultivate.
2.  **Fertilizer Recommendation**: Using the initial data **plus the predicted crop**, the second model recommends the optimal fertilizer to maximize yield and efficiency.

This turns agricultural guesswork into a precise, data-driven science.

---

### ✨ Key Features
* **Dual-Model System**: Utilizes two distinct Decision Tree models for a comprehensive crop-then-fertilizer recommendation.
* **Interactive Web App**: A user-friendly interface built with Streamlit allows for easy input and clear, actionable results.
* **Manual Override**: After receiving the crop recommendation, the user can manually select a different crop before getting a fertilizer prediction, adding practical flexibility.
* **High Accuracy**: Both the crop and fertilizer prediction models achieve high accuracy, ensuring reliable recommendations.
* **Informative Links**: Provides a direct YouTube link for a planting guide for the recommended crop.

---

### 🛠️ Tech Stack & Tools
[cite_start][cite: 19, 20, 21, 22, 23, 24, 25, 26, 27, 28] This project was developed using a standard, powerful stack for data science and web application development.

| Tool | Description |
| :--- | :--- |
| **Python** | The primary programming language used. |
| **Pandas & NumPy** | For efficient data manipulation, analysis, and numerical operations. |
| **Scikit-learn** | The core library for building and evaluating machine learning models. |
| **Matplotlib & Seaborn** | For data visualization and exploratory data analysis. |
| **Jupyter Notebook**| Interactive environment for coding, experimentation, and documentation. |
| **Streamlit** | For building and deploying the interactive web application. |

---

### 🚀 Project Journey & Weekly Progress
This project was completed over three weeks, following a structured machine learning workflow that evolved from a single model to a complete, interactive system.

#### Week 1: Foundations & Data Exploration (30% Complete)
**Objective**: To understand, clean, and prepare the dataset for modeling.
* **Data Loading & Inspection**: Loaded the `Crop and fertilizer dataset.csv` file using Pandas and performed initial analysis to understand its structure.
* **Exploratory Data Analysis (EDA)**: Analyzed the data to check for missing values and duplicates, confirming the dataset was clean.
* **Data Transformation**: Converted all categorical features (`Soil_color`, `Crop`, `District_Name`, `Fertilizer`) into numerical format using `LabelEncoder` to make them machine-readable.

#### Week 2: Dual-Model Building & Evaluation (70% Complete)
**Objective**: To build and evaluate two distinct predictive models for the core recommendation logic.
* **Model 1 (Crop Prediction)**: Trained a Decision Tree Classifier to predict the optimal **Crop** based on soil and climate features. This model achieved **~99.7% accuracy** on the test set.
* **Model 2 (Fertilizer Prediction)**: Trained a second Decision Tree Classifier to predict the best **Fertilizer**. The key difference is that its features included the soil/climate data **plus the crop type**. This model achieved **~97.8% accuracy**.
* **Model Saving**: Saved both trained models (`dt_crop` and `dt_fertilizer`) and all the fitted encoders as `.pkl` files using `joblib` for use in the web app.

#### Week 3: Interactive UI & Finalization (100% Complete)
**Objective**: To build a user-friendly interface and finalize the project deliverables.
* **Streamlit UI Development**: Developed an interactive web application (`app.py`) where a user can input their field's data through sliders, number inputs, and dropdowns.
* **Two-Step Logic Implementation**: Implemented the core two-button workflow:
    1.  The first button triggers the **crop prediction**.
    2.  The app then displays the result and a **new dropdown**, pre-filled with the recommended crop.
    3.  The user can accept this or choose another crop.
    4.  The second button triggers the **fertilizer prediction** based on the final crop choice.
* [cite_start]**Project Documentation**: [cite: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42] Created a comprehensive PowerPoint presentation summarizing the project's journey, methodology, and key findings.

---

### ⚙️ How to Run This Project
To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Aditya4386/Sustainable-Agriculture-Edunet-Internship.git](https://github.com/Aditya4386/Sustainable-Agriculture-Edunet-Internship.git)
    cd Sustainable-Agriculture-Edunet-Internship
    ```

2.  **Install dependencies:**
    It is recommended to create a virtual environment first.
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn joblib streamlit
    ```

3.  **Run the Interactive Web App:**
    To see the final project in action, run the Streamlit app from your terminal:
    ```bash
    streamlit run app.py
    ```

4.  **(Optional) Run the Jupyter Notebook:**
    To see the data processing and model training steps, launch Jupyter Notebook and open the `Fertilizer_Recommendation_System.ipynb` file.
    ```bash
    jupyter notebook
    ```

---

### 🔭 Future Scope
While the current system is a robust proof-of-concept, there are several avenues for future improvement:

* **Cloud Deployment**: Deploy the Streamlit application on a cloud service like Streamlit Community Cloud or Heroku to make it publicly accessible.
* **Explore Advanced Models**: Experiment with ensemble models like Random Forest or Gradient Boosting (XGBoost) to potentially improve accuracy even further.
* **Integrate Real-Time Data**: Connect the app to a weather API to pull in real-time temperature and rainfall data for a user's location, making recommendations more dynamic.
