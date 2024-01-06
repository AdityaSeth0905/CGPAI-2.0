import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
import json
from PIL import Image, ImageTk

# Create the Tkinter window
window = ctk.CTk()
window.title("NebulaSource")

# Variable to track whether the "Database" button has been clicked
database_button_clicked = False
navigation_bar = None  # Store the navigation bar frame
data = None

# Function to handle login
def login():
    global navigation_bar
    username = username_entry.get()
    password = password_entry.get()

    # Load user data from the JSON file
    with open('users.json', 'r') as file:
        users = json.load(file)

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login Successful")
        messagebox.showinfo("Login Successful!", "Welcome " + username + " to the NebulaSource Server")
        clear_login_screen()
        create_navigation_bar()
    else:
        messagebox.showerror("Login", "Login Failed")

# Function to create the navigation bar
def create_navigation_bar():
    global navigation_bar
    # Create a navigation bar
    nav_frame = tk.Frame(window, bg="black")
    nav_frame.pack(side="top", fill="x")

    profile_button = tk.Button(nav_frame, text="Profile", font=("Helvetica", 15))
    profile_button.pack(side="left", padx=10)

    database_button = tk.Button(nav_frame, text="Database", font=("Helvetica", 15), command=handle_database_button)
    database_button.pack(side="left", padx=10)

    navigation_bar = nav_frame  # Store the navigation bar frame

# Function to connect to the database and retrieve data
def connect_to_database():
    try:
        # Connect to your MySQL database
        db_connection = mysql.connector.connect(
            host="localhost", 
            user="root",  
            passwd="8882187203",
            database="CIIE"
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        # Execute an SQL query to retrieve data
        cursor.execute("SELECT * FROM users")

        # Fetch all the data from the query result
        data = cursor.fetchall()

        # Close the cursor and the database connection
        cursor.close()
        db_connection.close()

        return data

    except mysql.connector.Error as e:
        print("Error:", e)

# Function to handle the "Database" button click
def handle_database_button():
    global database_button_clicked
    if not database_button_clicked:
        database_button_clicked = True
        show_database_viewer()

# Function to switch to the database viewer
def show_database_viewer():
    global data
    clear_login_screen()
    data = connect_to_database()

    # Create a Treeview widget to display the data
    tree = ttk.Treeview(window, columns=list(range(len(data[0]))), show="headings")
    tree.pack()

    # Add column headings
    for i, col in enumerate(data[0]):
        tree.heading(i, text=col)
        tree.column(i, width=100)

    # Add data rows
    for row in data[1:]:
        tree.insert("", "end", values=row)
    
    # Calculate the size of the window based on data size
    window.geometry(f"{len(data[0]) * 100}x{len(data) * 20}")

# Function to clear the login screen
def clear_login_screen():
    image_label.pack_forget()
    username_label.pack_forget()
    username_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()

# Load and resize the image using BILINEAR filter
image = Image.open("CIIELOGOWhite.png")
image = image.resize((400, 300), Image.BILINEAR)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=photo, bg="black")
image_label.pack(pady=20)

# Create labels and entry widgets for username and password with a black background
username_label = tk.Label(window, text="Username:", bg="black", fg="white", font=("Helvetica", 20))
username_label.pack(pady=10)

username_entry = tk.Entry(window, font=("Helvetica", 20), bg="black", fg="white")
username_entry.pack(pady=10)

password_label = tk.Label(window, text="Password:", bg="black", fg="white", font=("Helvetica", 20))
password_label.pack(pady=10)

password_entry = tk.Entry(window, show="*", font=("Helvetica", 20), bg="black", fg="white")
password_entry.pack(pady=10)

# Create a login button with the custom font
login_button = tk.Button(window, text="Login", command=login, font=("Helvetica", 20))
login_button.pack(pady=10)

# Start the main event loop
window.mainloop()
