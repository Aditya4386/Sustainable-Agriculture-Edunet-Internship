# Fertilizer Recommendation System using Machine Learning

### Final Project Submission | Edunet Foundation & Shell Internship

This repository contains the final submission for the Machine Learning internship project focused on developing a smart fertilizer recommendation system. The model analyzes soil and environmental data to suggest the optimal fertilizer, aiming to improve agricultural efficiency and sustainability.

![Project Banner](https://i.imgur.com/your-banner-image.png) 
---

## 📋 Project Overview

[cite_start]Traditional farming often relies on historical practices for fertilization, which can lead to inefficient nutrient use, increased costs, and environmental damage[cite: 31, 32]. [cite_start]This project tackles that challenge by building a **Smart Recommendation Engine**[cite: 55]. [cite_start]Using a dataset of soil health metrics, climate data, and crop types, this machine learning model predicts the most suitable fertilizer, shifting the paradigm from guesswork to data-driven precision[cite: 52, 53].

## ✨ Key Results

[cite_start]The final model successfully predicts the optimal fertilizer with an overall **accuracy of 98%** on unseen test data[cite: 60]. [cite_start]The detailed classification report shows high precision and recall, confirming that the model is reliable across all fertilizer types[cite: 61].

![Classification Report](https://i.imgur.com/your-screenshot.png)
---

## 🛠️ Tech Stack & Tools

[cite_start]This project was developed using a standard, powerful stack for data science and machine learning[cite: 39, 40].

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%23007ACC.svg?style=for-the-badge&logo=Seaborn&logoColor=white)


---

## 🚀 Project Journey & Weekly Progress

This project was completed over three weeks, following a structured machine learning workflow.

### Week 1: Foundations & Data Preprocessing (30% Complete)
**Objective:** To understand, clean, and prepare the dataset for modeling.

* [cite_start]**Data Loading & Inspection:** Loaded the `Crop and fertilizer dataset.csv` file using Pandas and performed initial inspections with `.info()`, `.describe()`, and `.shape()` to understand its structure[cite: 2].
* [cite_start]**Exploratory Data Analysis (EDA):** Analyzed the data to check for missing values (`.isna().sum()`) and duplicates (`.duplicated().sum()`), both of which were zero, indicating a clean dataset[cite: 2]. [cite_start]The distribution of various features was also explored[cite: 2].
* [cite_start]**Feature Engineering:** Separated the dataset into features (X) and the target variable (y), which is `Fertilizer`[cite: 2].
* [cite_start]**Data Transformation:** Converted categorical features like `Soil_color`, `Crop`, and `District_Name` into numerical format using `sklearn.preprocessing.LabelEncoder` to make them machine-readable[cite: 2].

### Week 2: Model Building & Initial Evaluation (60% Complete)
**Objective:** To build a baseline predictive model and assess its initial performance.

* [cite_start]**Model Selection:** Chose the **Decision Tree Classifier** as the initial model, as it is highly effective for tabular classification tasks and is easily interpretable[cite: 2].
* [cite_start]**Data Splitting:** Divided the processed data into training (80%) and testing (20%) sets using `train_test_split` to ensure the model could be evaluated on unseen data[cite: 2].
* [cite_start]**Model Training:** Trained the Decision Tree model on the training dataset using the `.fit()` method[cite: 2].
* [cite_start]**Baseline Evaluation:** Performed an initial performance check using the `.score()` method, which revealed a very high training accuracy (~99.9%) and testing accuracy (~97.8%)[cite: 2].

### Week 3: Advanced Evaluation & Finalization (100% Complete)
**Objective:** To conduct a deep-dive analysis of the model's performance and prepare the final project deliverables.

* **In-Depth Performance Analysis:** Went beyond simple accuracy to evaluate the model using more robust metrics.
    * [cite_start]Generated a **Classification Report** to analyze precision, recall, and F1-score for each fertilizer type[cite: 2, 58].
    * [cite_start]Created a **Confusion Matrix** to visualize where the model was making correct and incorrect predictions[cite: 2].
* [cite_start]**Result Interpretation:** The detailed analysis confirmed the model's excellent performance, achieving a final weighted average precision, recall, and F1-score of **98%**[cite: 59, 60, 61].
* [cite_start]**Project Documentation:** Created a comprehensive PowerPoint presentation summarizing the project's journey, methodology, and key findings[cite: 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61].

---

## ⚙️ How to Run This Project

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install dependencies:**
    It is recommended to create a virtual environment first. All required libraries are listed in the notebook.
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```

3.  **Run the Jupyter Notebook:**
    Launch Jupyter Notebook and open the `Fertilizer_Recommendation_System.ipynb` file.
    ```bash
    jupyter notebook
    ```

---

## 🔭 Future Scope

While the current model is highly accurate, there are several avenues for future improvement:

* **Hyperparameter Tuning:** Use techniques like `GridSearchCV` to find the absolute optimal parameters for the Decision Tree model.
* **Explore Advanced Models:** Experiment with ensemble models like Random Forest or Gradient Boosting (XGBoost) to potentially achieve even higher accuracy.
* **Deployment:** The ultimate goal would be to deploy this model as a simple web application using a framework like **Streamlit** or **Flask**, making it easily accessible to farmers.
