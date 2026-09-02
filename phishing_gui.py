import tkinter as tk
from tkinter import messagebox
import joblib


# Load trained model
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")


def detect_email():
    email_text = email_box.get("1.0", tk.END).strip()

    if not email_text:
        messagebox.showwarning("Warning", "Please enter an email.")
        return

    email_vectorized = vectorizer.transform([email_text])
    prediction = model.predict(email_vectorized)[0]

    if prediction == 1:
        result_label.config(
            text="⚠️ PHISHING EMAIL DETECTED",
            fg="red"
        )
    else:
        result_label.config(
            text="✅ SAFE EMAIL",
            fg="green"
        )


def clear_email():
    email_box.delete("1.0", tk.END)
    result_label.config(text="")


# Create window
window = tk.Tk()
window.title("Phishing Email Detector")
window.geometry("800x650")
window.configure(bg="#0F172A")


# Title
title_label = tk.Label(
    window,
    text="🛡️ PHISHING EMAIL DETECTOR",
    font=("Arial", 24, "bold"),
    fg="#38BDF8",
    bg="#0F172A"
)
title_label.pack(pady=25)


# Instruction
instruction_label = tk.Label(
    window,
    text="Enter the email text below:",
    font=("Arial", 14, "bold"),
    fg="#CBD5E1",
    bg="#0F172A"
)
instruction_label.pack(pady=5)


# Email input box
email_box = tk.Text(
    window,
    height=12,
    width=75,
    font=("Arial", 11)
)
email_box.pack(pady=15)


# Detect button
detect_button = tk.Button(
    window,
    text="CHECK EMAIL",
    command=detect_email,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8
)
detect_button.pack(pady=5)


# Clear button
clear_button = tk.Button(
    window,
    text="CLEAR",
    command=clear_email,
    font=("Arial", 11),
    padx=25,
    pady=5
)
clear_button.pack(pady=5)


# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)


# Start GUI
window.mainloop()