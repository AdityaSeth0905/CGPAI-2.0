import cv2
import json
import face_recognition
import os
import time

# Open the webcam
video_capture = cv2.VideoCapture(0)


def capture_verification_picture(frame):
    # Generate a new name for the image using a timestamp
    timestamp = str(int(time.time()))  # Get current timestamp
    image_name = f"frame_{timestamp}.jpg"

    # Specify the directory to save the captured images
    image_directory = r"C:\Users\gnkit\OneDrive\Desktop\GeneralAIModelForCIIE\GPAI\WebFrameFeedPics"

    # Create the full path for the captured image
    image_path = os.path.join(image_directory, image_name)

    # Save the captured image
    cv2.imwrite(image_path, frame)

    return image_path


def capture_verification_picture_from_user():
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Capture verification picture from user
    image_path = capture_verification_picture(frame)

    # Load the captured image and generate the face encoding
    captured_image = face_recognition.load_image_file(image_path)
    captured_image_encoding = face_recognition.face_encodings(captured_image)[0]

    # Prompt the user to enter name, registration number, department, and year
    name = input("Enter the name: ")
    registration_number = input("Enter the registration number: ")
    department = input("Enter the department: ")
    year = input("Enter the year: ")

    # Generate the name for the new encoding
    new_encoding_name = name

    # Store the encoding with the generated name, registration number, department, and year in a dictionary
    unknown_encoding = {
        "name": new_encoding_name,
        "registration_number": registration_number,
        "department": department,
        "year": year,
        "encoding": captured_image_encoding.tolist()
    }

    # Save the updated unknown encodings to the JSON file
    json_file_path = "unknown.json"
    try:
        with open(json_file_path, "r") as json_file:
            unknown_encodings = json.load(json_file)
    except FileNotFoundError:
        unknown_encodings = []

    # Append the new encoding to the list of unknown encodings
    unknown_encodings.append(unknown_encoding)

    with open(json_file_path, "w") as json_file:
        json.dump(unknown_encodings, json_file)

    print("Verification picture captured and saved.")


def ask_verification_picture():
    choice = input("Do you already have a verification picture? (y/n): ")
    if choice.lower() == "y":
        # Take values from picture name
        print("Taking values from picture name...")
        # TODO: Implement the code to extract values from the picture name
        print("Values extracted from picture name.")
    elif choice.lower() == "n":
        # Capture a new verification picture and take inputs from the user
        print("Taking a new verification picture...")
        capture_verification_picture_from_user()
    else:
        print("Invalid choice.")


def main():
    ask_verification_picture()


if __name__ == "__main__":
    main()
