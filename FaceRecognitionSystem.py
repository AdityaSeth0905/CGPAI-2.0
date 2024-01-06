import cv2
import json
import face_recognition
import os
import time
#"Aditya Seth_11022210076_Btech CSE DSAI_1st"
def capture_verification_picture_from_filename():
    image_file = input("Enter the path of the verification picture: ")

    # Extract information from the file name
    file_name = os.path.basename(image_file)
    name, registration_number, department, year = file_name.split("_")[:4]

    # Load the verification picture and generate the face encoding
    verification_image = face_recognition.load_image_file(image_file)
    verification_encoding = face_recognition.face_encodings(verification_image)[0]

    # Load the existing unknown encodings from the JSON file
    json_file_path = "unknown.json"
    try:
        with open(json_file_path, "r") as json_file:
            unknown_encodings = json.load(json_file)
    except FileNotFoundError:
        unknown_encodings = []

    # Store the encoding with the extracted name, registration number, department, and year in a dictionary
    unknown_encoding = {
        "name": name,
        "registration_number": registration_number,
        "department": department,
        "year": year,
        "encoding": verification_encoding.tolist()
    }

    # Append the new encoding to the list of unknown encodings
    unknown_encodings.append(unknown_encoding)

    # Save the updated unknown encodings to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(unknown_encodings, json_file)

    print("Verification picture information extracted and saved successfully.")


def capture_verification_picture_from_user():
    # Open the webcam
    video_capture = cv2.VideoCapture(0)

    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Initialize variables to track if a person is found
    person_found = False

    # Specify the directory to save the captured images
    image_directory = r"C:\Users\gnkit\OneDrive\Desktop\GeneralAIModelForCIIE\GPAI\WebFrameFeedPics"

    # Generate a new name for the image using a timestamp
    timestamp = str(int(time.time()))  # Get current timestamp
    image_name = f"frame_{timestamp}.jpg"

    # Create the full path for the captured image
    image_path = os.path.join(image_directory, image_name)

    # Save the captured image if a person is found
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) > 0:
        # Save the captured image
        cv2.imwrite(image_path, frame)
        person_found = True

    # Release the webcam if a person is found
    if person_found:
        video_capture.release()

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

        # Append the new encoding to the list of unknown encodings
        unknown_encodings.append(unknown_encoding)

        # Save the updated unknown encodings to the JSON file
        with open(json_file_path, "w") as json_file:
            json.dump(unknown_encodings, json_file)

        print("Verification picture captured and information saved successfully.")


def ask_verification_picture():
    choice = input("Do you already have a verification picture? (y/n): ")

    if choice.lower() == "y":
        capture_verification_picture_from_filename()
    elif choice.lower() == "n":
        edit_choice = input("Do you want to edit the picture name? (y/n): ")

        if edit_choice.lower() == "n":
            capture_verification_picture_from_user()
        elif edit_choice.lower() == "y":
            # Prompt the user to enter name, registration number, department, and year
            name = input("Enter the name: ")
            registration_number = input("Enter the registration number: ")
            department = input("Enter the department: ")
            year = input("Enter the year: ")

            # Load the existing unknown encodings from the JSON file
            json_file_path = "unknown.json"
            try:
                with open(json_file_path, "r") as json_file:
                    unknown_encodings = json.load(json_file)
            except FileNotFoundError:
                unknown_encodings = []

            # Generate the name for the new encoding
            new_encoding_name = name

            # Store the encoding with the generated name, registration number, department, and year in a dictionary
            unknown_encoding = {
                "name": new_encoding_name,
                "registration_number": registration_number,
                "department": department,
                "year": year,
                "encoding": None  # Set to None as no picture is captured
            }

            # Append the new encoding to the list of unknown encodings
            unknown_encodings.append(unknown_encoding)

            # Save the updated unknown encodings to the JSON file
            with open(json_file_path, "w") as json_file:
                json.dump(unknown_encodings, json_file)

            print("Verification picture information saved successfully.")

        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")


def main():
    ask_verification_picture()


if __name__ == "__main__":
    main()
