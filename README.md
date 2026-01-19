# 🏥 HealthGuard AI: Risk Prediction System

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)

**HealthGuard AI** is a specialized diagnostic support tool that leverages Machine Learning to assess the risk of chronic diseases (such as Diabetes) based on key medical metrics. 

By providing an intuitive interface for health data entry, this application demonstrates how AI can empower proactive healthcare monitoring and early-stage risk detection.

---

## 🚀 Live Demo
### 🔗 [Click Here to Access the Live Application](MASUKKAN_LINK_DEMO_KAMU)

---

## ✨ Features
- **User-Centric Medical Form**: Easy-to-use interface for entering glucose, BMI, insulin, and age metrics.
- **Instant Risk Assessment**: Real-time classification using the **Random Forest** algorithm.
- **Probability Confidence**: Provides a percentage-based confidence score for every prediction.
- **Health Recommendations**: Context-aware suggestions based on the analysis results (Low Risk vs. High Risk).

## 🛠️ Technical Implementation
- **Classification Engine**: Built with **Scikit-Learn's Random Forest Classifier** for high reliability in categorical outcomes.
- **Data Handling**: Efficient array processing using **NumPy** and **Pandas**.
- **Responsive UI**: Interactive dashboard built entirely with **Streamlit**.



---

## 🔧 Installation & Usage
1.  **Clone this repository**:
    ```bash
    git clone [https://github.com/nisfu/health-risk-prediction.git](https://github.com/nisfu/health-risk-prediction.git)
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app**:
    ```bash
    streamlit run app_health.py
    ```

---

## 📂 Project Structure
```text
📁 health-risk-prediction
├── 📄 app_health.py      # Main Application Script
├── 📄 requirements.txt    # Library Dependencies
└── 📄 README.md           # Documentation

## 💡 Why This Project?
In modern healthcare, early detection is critical. This project serves as a Proof of Concept (PoC) for:
- Predictive Analytics: Using historical medical data to forecast individual health risks.
- Domain Expertise: Applying Data Science techniques to the healthcare sector (HealthTech).
- UI/UX for Data: Translating complex model outputs into simple, actionable insights for end-users.

##📫 Connect with Me
Email: nisfurohmatul@outlook.com
Disclaimer: This application is for educational and portfolio purposes only. It is not a substitute for professional medical advice.
