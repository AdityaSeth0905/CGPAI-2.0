import cv2
import json
import face_recognition
import os
import time

# Open the webcam
video_capture = cv2.VideoCapture(0)

# Initialize variables to track if a person is found
person_found = False

# Specify the directory to save the captured images
image_directory = r"C:\Users\gnkit\OneDrive\Desktop\GeneralAIModelForCIIE\GPAI\WebFrameFeedPics"

# Generate a new name for the image using a timestamp
timestamp = str(int(time.time()))  # Get current timestamp
image_name = f"frame_{timestamp}.jpg"

# Create the full path for the captured image
image_path = os.path.join(image_directory, image_name)

# Global variables
name = ""
registration_number = ""
department = ""
year = ""

# Save the captured image if a person is found
def capture_verification_picture():
    global person_found, image_path
    
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) > 0:
        # Save the captured image
        cv2.imwrite(image_path, frame)
        person_found = True

    # Release the webcam if a person is found
    if person_found:
        video_capture.release()

# Capture a new picture from the webcam and take inputs from the user
def capture_verification_picture_from_user():
    global name, registration_number, department, year
    
    capture_verification_picture()
    
    if person_found:
        # Prompt the user to enter name, registration number, department, and year
        name = input("Enter the name: ")
        registration_number = input("Enter the registration number: ")
        department = input("Enter the department: ")
        year = input("Enter the year: ")

        # Edit the picture name based on the inputs
        file_name = os.path.splitext(image_name)[0]  # Remove file extension
        new_file_name = f"{name}_{registration_number}_{department}_{year}"
        new_image_path = os.path.join(image_directory, f"{new_file_name}.jpg")

        # Rename the captured image
        os.rename(image_path, new_image_path)

        # Update the image path
        image_path = new_image_path

# Ask if the user already has a verification picture
def ask_verification_picture():
    choice = input("Do you already have a verification picture? (y/n): ")

    if choice.lower() == "y":
        # Take values from the picture name
        name, registration_number, department, year = image_name.split("_")[:4]
    else:
        # Take a new picture and inputs from the user
        capture_verification_picture_from_user()

    # Load the captured image and generate the face encoding
    if person_found:
        captured_image = face_recognition.load_image_file(image_path)
        captured_image_encoding = face_recognition.face_encodings(captured_image)[0]

        # Load the existing unknown encodings from the JSON file
        json_file_path = "unknown.json"
        try:
            with open(json_file_path, "r") as json_file:
                unknown_encodings = json.load(json_file)
        except FileNotFoundError:
            unknown_encodings = []

        # Store the encoding with the generated name, registration number, department, and year in a dictionary
        unknown_encoding = {
            "name": name,
            "registration_number": registration_number,
            "department": department,
            "year": year,
            "encoding": captured_image_encoding.tolist()
        }

        # Append the new encoding to the list of unknown encodings
        unknown_encodings.append(unknown_encoding)

        # Save the updated unknown encodings to the JSON file
        with open(json_file_path, "w") as json_file:
            json.dump(unknown_encodings, json_file)

    # Now you can use the captured image encoding for comparison with other face encodings

def main():
    ask_verification_picture()

if __name__ == "__main__":
    main()

