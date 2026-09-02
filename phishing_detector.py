import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


print("========================================")
print("       PHISHING EMAIL DETECTOR")
print("========================================")


# Load dataset
data = pd.read_csv("dataset/phishing_email.csv")

print("\nDataset loaded successfully!")
print("Total emails:", len(data))


# Select text and labels
X = data["text_combined"].fillna("")
y = data["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Training emails:", len(X_train))
print("Testing emails:", len(X_test))


# Convert text into numerical features
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Train machine learning model
model = LogisticRegression(max_iter=1000)

model.fit(X_train_vectorized, y_train)


# Test model
predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)


print("\n========================================")
print("MODEL TRAINING COMPLETED")
print("========================================")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Save model and vectorizer
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")


print("Model saved successfully!")
print("Files saved inside the model folder.")
# Email prediction
print("\n========================================")
print("       TEST AN EMAIL")
print("========================================")

email = input("\nEnter the email text: ")

email_vectorized = vectorizer.transform([email])

prediction = model.predict(email_vectorized)[0]

print("\nResult:")

if prediction == 1:
    print("⚠️ PHISHING EMAIL DETECTED")
else:
    print("✅ SAFE EMAIL")