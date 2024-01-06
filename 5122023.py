import cv2 as cv
import face_recognition
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

class FaceRecognitionApp:
    def __init__(self, root, faces_directory):
        self.root = root
        self.root.title("Face Recognition")

        # Load stored facial encodings
        self.known_faces = self.load_known_faces(faces_directory)

        # Create OpenCV video capture object
        self.cap = cv.VideoCapture(0)

        # Create Tkinter label for displaying the video feed
        self.label = tk.Label(root)
        self.label.pack(padx=10, pady=10)

        # Create recognition button
        self.recognize_button = tk.Button(root, text="Recognize", command=self.recognize)
        self.recognize_button.pack(pady=10)

        # Set up the GUI update loop
        self.update()

    def load_known_faces(self, faces_directory):
        known_faces = {}
        for filename in os.listdir(faces_directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                name = os.path.splitext(filename)[0]
                image_path = os.path.join(faces_directory, filename)
                face_image = face_recognition.load_image_file(image_path)
                face_encoding = face_recognition.face_encodings(face_image)[0]
                known_faces[name] = face_encoding
        return known_faces

    def recognize(self):
        # Capture a frame from the webcam
        ret, frame = self.cap.read()

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches any known faces
            for name, known_encoding in self.known_faces.items():
                matches = face_recognition.compare_faces([known_encoding], face_encoding)
                if True in matches:
                    messagebox.showinfo("Recognition", f"Recognized: {name}")
                    return

        # If no match is found
        messagebox.showwarning("Recognition", "No match found.")

    def update(self):
        # Capture a frame from the webcam
        ret, frame = self.cap.read()

        # Convert the frame to RGB for displaying in Tkinter
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Convert the frame to a Tkinter-compatible photo image
        img = Image.fromarray(rgb_frame)
        img = ImageTk.PhotoImage(image=img)

        # Update the Tkinter label with the new frame
        self.label.img = img
        self.label.config(image=img)

        # Call the update method recursively to continuously update the GUI
        self.root.after(10, self.update)

    def run(self):
        self.root.mainloop()

    def __del__(self):
        # Release the video capture object when the application is closed
        self.cap.release()

# Replace 'path/to/faces_directory' with the actual path to the directory containing facial encodings
faces_directory = 'C:/Users/adity/OneDrive/Desktop/work/GPAI/faces'

# Create the Tkinter root window
root = tk.Tk()

# Create an instance of the FaceRecognitionApp class
app = FaceRecognitionApp(root, faces_directory)

# Run the Tkinter application
app.run()

