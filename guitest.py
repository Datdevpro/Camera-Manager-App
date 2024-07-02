import tkinter as tk
from tkinter import ttk
import requests

def fetch_data():
    try:
        response = requests.get("http://127.0.0.1:8000/data")
        response.raise_for_status()
        data = response.json()
        label.config(text=data["message"])
        print(data["message"])
    except requests.exceptions.RequestException as e:
        label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Tkinter and FastAPI Integration")
root.geometry("400x200")

label = ttk.Label(root, text="Fetching data...")
label.pack(pady=20)

button = ttk.Button(root, text="Fetch Data", command=fetch_data)
button.pack(pady=20)

root.mainloop()
