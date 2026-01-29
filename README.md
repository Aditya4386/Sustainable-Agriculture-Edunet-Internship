# 🌾 Advanced Crop & Fertilizer Recommendation System  
**Final Project | Edunet Foundation & Shell Internship**

This repository contains a complete **machine learning–based decision support system** for agriculture.  
The system predicts the **most suitable crop** based on soil, climate, and location data, and then recommends the **optimal fertilizer** for that crop.  
The project is deployed as a fully interactive **Streamlit web application**.

---

## 🚀 Live Demo (Deployed App)

👉 **Test the project here:**  
🔗 https://sustainable-agriculture-crop-fertilizer-recommendation.streamlit.app/

---

## 📌 Project Overview

Traditional farming decisions often rely on experience and intuition, which can result in inefficient fertilizer usage, higher costs, and environmental impact.  
This project addresses that challenge by introducing a **two-step, data-driven recommendation system**.

### How it works:
1. **Crop Recommendation**  
   Predicts the most suitable crop using:
   - Soil nutrients (N, P, K)
   - Soil pH
   - Rainfall and temperature
   - District and soil type

2. **Fertilizer Recommendation**  
   Uses the same inputs **plus the selected crop** to recommend the best fertilizer.

This approach transforms agricultural decision-making into a **precise and scientific process**.

---

## ✨ Key Features

- **Dual-Model Architecture**  
  Two Decision Tree models:
  - Crop prediction model
  - Fertilizer recommendation model

- **Interactive Streamlit UI**  
  Clean, user-friendly interface with sliders, dropdowns, and buttons.

- **Manual Crop Override**  
  Users can override the predicted crop before fertilizer recommendation.

- **High Accuracy Models**  
  - Crop model accuracy ≈ 99%  
  - Fertilizer model accuracy ≈ 97%

- **Educational Resource Links**  
  Provides YouTube planting guides for the recommended crop.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical computation |
| Pandas | Data manipulation |
| Scikit-learn | Machine learning models & encoders |
| Joblib | Model and encoder serialization |
| Jupyter Notebook | Data analysis & training |
| Streamlit | Web application & deployment |

---

## 🧠 Project Development Journey

### Week 1 – Data Preparation & Exploration
- Loaded and analyzed the crop & fertilizer dataset
- Verified data quality (no missing values or duplicates)
- Encoded categorical features using `LabelEncoder`

### Week 2 – Model Building & Evaluation
- Trained **Decision Tree Classifier** for crop prediction
- Trained **Decision Tree Classifier** for fertilizer prediction
- Evaluated models and achieved high accuracy
- Saved trained models and encoders as `.pkl` files

### Week 3 – Deployment & Finalization
- Built a two-step Streamlit interface
- Implemented session-based workflow for predictions
- Added planting guide links
- Deployed the app on **Streamlit Community Cloud**

---
### 1️⃣ Clone the repository

    git clone https://github.com/Aditya4386/Sustainable-Agriculture-Edunet-Internship.git
    cd Sustainable-Agriculture-Edunet-Internship

### 2️⃣ Install dependencies

    pip install -r requirements.txt

### 3️⃣ Run the Streamlit app

    streamlit run app.py

### 4️⃣ (Optional) View model training notebook

    jupyter notebook

Open `Fertilizer_Recommendation_System.ipynb`

---

## 🔭 Future Scope

- Integrate **real-time weather data** using APIs
- Experiment with **ensemble models** (Random Forest, Gradient Boosting)
- Add fertilizer dosage recommendations
- Expand dataset for broader regional coverage

---

## 👤 Author

**Aditya Pawar**  
Machine Learning Intern – Edunet Foundation & Shell  
GitHub: https://github.com/Aditya4386
