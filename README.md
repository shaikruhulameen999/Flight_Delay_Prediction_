# ✈️ Flight Delay Prediction Using Machine Learning

## 📌 Project Overview

Flight delays can cause inconvenience to passengers and increase operational costs for airlines. This project uses **Machine Learning** to predict whether a flight is likely to be delayed based on historical flight data and flight-related features.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and is deployed on **Hugging Face Spaces** with an interactive web interface.

---

## 🎯 Problem Statement

Airline delays are influenced by several factors, including airline operations, airport traffic, flight distance, and scheduling. Predicting delays in advance helps airlines optimize operations and enables passengers to plan their journeys more effectively.

This project develops a Machine Learning classification model that predicts whether a flight will be delayed based on flight information.

---

## 📂 Dataset

* **Dataset:** Flight Delays Dataset
* **Source:** Kaggle
* **Link:** https://www.kaggle.com/datasets/umeradnaan/flight-delays-dataset

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📊 Features Used

The model uses the following features:

* Distance
* Scheduled Departure Hour
* Actual Departure Hour
* Scheduled Arrival Hour
* Actual Arrival Hour
* Cancelled
* Diverted
* Airline
* Origin Airport
* Destination Airport
* Delay Reason
* Aircraft Type

---

## 🤖 Machine Learning Model

**Algorithm Used:**

* Decision Tree Classifier

The model is trained using historical flight data to classify flights into:

* ✅ Delayed
* ✅ Not Delayed

---

## ⚙️ Project Workflow

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Feature Engineering
5. Encoding Categorical Variables
6. Model Training using Decision Tree
7. Model Evaluation
8. Model Serialization using Joblib
9. Streamlit Web Application
10. Deployment on Hugging Face Spaces

---

## 📈 Project Structure

```text
Flight-Delay-Prediction/
│
├── app.py
├── Decision_Tree.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## ▶️ Run Locally

### Clone the repository

```bash
git clone https://github.com/your-username/Flight-Delay-Prediction.git
```

### Navigate to the project

```bash
cd Flight-Delay-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots of your Streamlit application here.

Example:

* Home Page
* Prediction Result

---

## 🎯 Future Enhancements

* Improve prediction accuracy using ensemble models.
* Include weather and real-time flight information.
* Deploy using Docker and cloud services.
* Add visualization dashboards for delay analysis.

---

## 🙏 Acknowledgements

* Innomatics Research Labs
* Upender Muthyala
* Sonam Pawar
* Kaggle Flight Delays Dataset

---

## 👨‍💻 Author

**Shaik Ruhulameen**
---


If you found this project useful, consider giving it a ⭐ on GitHub!
