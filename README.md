# 🛡️ Phishing Email Detector

A machine learning-based system that detects whether an email is **Phishing** or **Safe** using Natural Language Processing (NLP) and Scikit-learn.

## 📌 Project Overview

Phishing emails are designed to trick users into revealing sensitive information such as passwords, banking details, and personal data.

This project uses **TF-IDF text vectorization** and **Logistic Regression** to analyze email content and classify it as either:

- ✅ Safe Email
- ⚠️ Phishing Email

The project also includes a graphical user interface (GUI) built using **Tkinter**.

## 🚀 Features

- 📧 Email text analysis
- 🤖 Machine learning classification
- 🔤 TF-IDF text vectorization
- 📊 Logistic Regression model
- 📈 Accuracy evaluation
- 📋 Classification report
- 🔲 Confusion matrix
- 🖥️ Professional graphical interface
- 💾 Trained model saved using Joblib

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Matplotlib
- Seaborn
- Tkinter
- Joblib

## 📊 Model Performance

The trained model achieved approximately:

**Accuracy: 98.15%**

### Confusion Matrix

| Actual / Predicted | Safe | Phishing |
|---|---:|---:|
| Safe | 7747 | 172 |
| Phishing | 133 | 8446 |

## 📂 Project Structure

```text
Phishing-Email-Detector/
│
├── dataset/
│   └── phishing_gui.py
│
├── model/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── phishing_detector.py
└── README.md
