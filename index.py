import tkinter as tk
from tkinter import scrolledtext, messagebox
from model import predict


def predict_spam():
    email_text = email_body_input.get("1.0", tk.END).strip()
    email_address = email_address_input.get("1.0", tk.END).strip()
    print(email_address)
    print(email_text)
    
    if not email_text or not email_address:
        messagebox.showwarning("Input Error", "Please enter email text and address.")
        return
    
    prediction = predict(email_text,email_address)
    
    result_label.config(text=f"Prediction: {prediction}",background=prediction == "spam" and "red" or "green")
def clear_text():
    email_body_input.delete("1.0", tk.END)
    result_label.config(text="Prediction: ",background="#d9d9d9")
    email_address_input.delete("1.0", tk.END)

# Initialize the main window
window = tk.Tk()
window.title("Email Spam Detector")
window.geometry("800x600")
window.resizable(False, False)


email_address_label = tk.Label(window, text="Email Address:", font=("Arial", 12))
email_address_label.pack(pady=10)
email_address_input = tk.Text(window,height=1,width=60, font=("Arial", 12))
email_address_input.pack(pady=10)

# Email input label
input_label = tk.Label(window, text="Enter Email Text:", font=("Arial", 12))
input_label.pack(pady=10)
# Email input text area
email_body_input = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, font=("Arial", 10))
email_body_input.pack(pady=5)

# Predict button
predict_button = tk.Button(window, text="Predict", command=predict_spam, font=("Arial", 12), bg="#4CAF50", fg="white")
predict_button.pack(pady=10)


clear_button = tk.Button(window, text="Clear", command=clear_text, font=("Arial", 12))
clear_button.pack(pady=10)


# Result label
result_label = tk.Label(window, text="Prediction: ", font=("Arial", 14))
result_label.pack(pady=20)


# Start the GUI event loop
window.mainloop()


