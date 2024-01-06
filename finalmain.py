import tkinter as tk
from tkinter import messagebox
import bcrypt
import numpy as np
import mysql.connector
from PIL import Image, ImageTk
import face_recognition
import cv2

# Create the main application window
root = tk.Tk()
root.title("NebulaSource")
root.configure(background="black")

# Function to establish a connection to your MySQL database
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            #host="Nebula Source Server",
            user="root",
            password="8882187203",
            database="CIIE"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

# Function to hash a password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Function to verify a password using bcrypt
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Function to serialize a face encoding to a string
def serialize_face_encoding(face_encoding):
    return ",".join(map(str, face_encoding.tolist()))

# Function to deserialize a face encoding from a string
def deserialize_face_encoding(encoded_face):
    return np.array(list(map(float, encoded_face.split(","))))

# Function to register a new user
def register_user():
    username = username_entry.get()
    password = "Adityaseth@09052002"  # Set a default password (you can change this)

    # Capture and serialize the user's face encoding
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        if face_locations:
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            serialized_face_encoding = serialize_face_encoding(face_encoding)
            break
        cv2.imshow('Capture Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

    # Hash the password
    hashed_password = hash_password(password)

    # Connect to MySQL database
    conn = connect_to_mysql()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        
        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            messagebox.showerror("Registration", "Username already exists")
            return

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password, face_encoding) VALUES (%s, %s, %s)",
                       (username, hashed_password, serialized_face_encoding))
        conn.commit()
        messagebox.showinfo("Registration", "User registered successfully")

    except mysql.connector.Error as err:
        print("Error:", err)
        messagebox.showerror("Registration", "An error occurred during registration")

    finally:
        cursor.close()
        conn.close()


# Start the main event loop
root.mainloop()
