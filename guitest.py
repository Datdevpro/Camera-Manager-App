# import tkinter as tk
# from tkinter import ttk
# import requests

# def fetch_data():
#     try:
#         response = requests.get("http://127.0.0.1:8000/data")
#         response.raise_for_status()
#         data = response.json()
#         label.config(text=data["message"])
#         print(data["message"])
#     except requests.exceptions.RequestException as e:
#         label.config(text=f"Error: {e}")

# root = tk.Tk()
# root.title("Tkinter and FastAPI Integration")
# root.geometry("400x200")

# label = ttk.Label(root, text="Fetching data...")
# label.pack(pady=20)

# button = ttk.Button(root, text="Fetch Data", command=fetch_data)
# button.pack(pady=20)

# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import requests

def send_data():
    # Get data from entry fields
    name = entry_name.get()
    description = entry_description.get()
    price = entry_price.get()
    tax = entry_tax.get()

    # Create payload
    payload = {
        "name": name,
        "description": description,
        "price": float(price),
        "tax": float(tax) if tax else None
    }

    # Send data to the API
    try:
        response = requests.post("http://127.0.0.1:8000/items/", json=payload)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Data sent successfully!")
        else:
            messagebox.showerror("Error", f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Send Data to API")

# Create and place labels and entry fields
tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Description").grid(row=1, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=1, column=1)

tk.Label(root, text="Price").grid(row=2, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1)

tk.Label(root, text="Tax").grid(row=3, column=0)
entry_tax = tk.Entry(root)
entry_tax.grid(row=3, column=1)

# Create and place the button
btn_send = tk.Button(root, text="Send Data", command=send_data)
btn_send.grid(row=4, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
