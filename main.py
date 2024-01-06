import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk  # Import PIL modules
from customtkinter import *
# Create the main application window
root = CTk()
root.title("NebulaSource")

# Changing the background color of the Interface window to dark gray
#root.configure(background="black")
CTk.colorchooser= "dark blue"

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Load user data from the JSON file
    with open('users.json', 'r') as file:
        users = json.load(file)

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login Successful")
        messagebox.showinfo("Login Successful!", "Welcome " + username + " to the NebulaSource Server")
    else:
        messagebox.showerror("Login", "Login Failed")

# Load and resize the image using BILINEAR filter
image = Image.open("CIIELOGOWhite.png")
image = image.resize((400, 300), Image.BILINEAR)  # Resize to 300x200 with BILINEAR filter
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo, bg="black")
image_label.pack(pady=20)

# Create labels and entry widgets for username and password with a black background
username_label = tk.Label(root, text="Username:", bg="black", fg="white", font=("Helvetica", 20))
username_label.pack(pady=10)

username_entry = tk.Entry(root, font=("Helvetica", 20), bg="black", fg="white")
username_entry.pack(pady=10)

password_label = tk.Label(root, text="Password:", bg="black", fg="white", font=("Helvetica", 20))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Helvetica", 20), bg="black", fg="white")  # Use 'show' to hide password
password_entry.pack(pady=10)

# Create a login button with the custom font
login_button = tk.Button(root, text="Login", command=login, font=("Helvetica", 20))
login_button.pack(pady=10)

# Start the main event loop
root.mainloop()

