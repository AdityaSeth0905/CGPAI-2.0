import cv2
import json
import face_recognition
import os
import time

class faceauth:
    # Open the webcam
    global video_capture 
    video_capture = cv2.VideoCapture(0)

    # Initialize variables to track if a person is found
    person_found = False

    # Specify the directory to save the captured images
    global image_directory 
    image_directory = r"C:\Users\adity\OneDrive\Desktop\work\GPAI\WebFrameFeedPics"

    def capture_verification_picture():
        # Capture a frame from the webcam
        ret, frame = video_capture.read()

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
            print("Verification picture captured successfully.")

        return person_found, image_name

    def capture_verification_picture_from_user():
        person_found, image_name = faceauth.capture_verification_picture()

        if person_found:
            # Load the captured image and generate the face encoding
            captured_image = face_recognition.load_image_file(os.path.join(image_directory, image_name))
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

            # Load the existing unknown encodings from the JSON file
            json_file_path = "unknown.json"
            try:
                with open(json_file_path, "r") as json_file:
                    unknown_encodings = json.load(json_file)
            except FileNotFoundError:
                unknown_encodings = []

            # Append the new encoding to the list of unknown encodings
            unknown_encodings.append(unknown_encoding)

            # Save the updated unknown encodings to the JSON file
            with open(json_file_path, "w") as json_file:
                json.dump(unknown_encodings, json_file)

            # Edit the file name with the user input
            edited_image_name = f"{name}_{registration_number}_{department}_{year}.jpg"
            edited_image_path = os.path.join(image_directory, edited_image_name)

            # Rename the captured image with the edited file name
            os.rename(os.path.join(image_directory, image_name), edited_image_path)
            print("Verification picture edited and saved successfully.")
        else:
            print("No person detected in the captured frame.")

        # Release the webcam
        video_capture.release()

    def ask_verification_picture():
        choice = input("Do you already have a verification picture? (y/n): ")
        if choice.lower() == "y":
            # TODO: Add code to use the verification picture
            print("Use the verification picture.")
        elif choice.lower() == "n":
            edit_choice = input("Do you want to edit the picture name? (y/n): ")
            if edit_choice.lower() == "y":
                faceauth.capture_verification_picture_from_user()
            else:
                person_found, image_name = faceauth.capture_verification_picture()

                if person_found:
                    # Load the captured image and generate the face encoding
                    captured_image = face_recognition.load_image_file(os.path.join(image_directory, image_name))
                    captured_image_encoding = face_recognition.face_encodings(captured_image)[0]

                    # Generate the name for the new encoding
                    name = image_name.split("_")[0]
                    registration_number = input("Enter the registration number: ")
                    department = input("Enter the department: ")
                    year = input("Enter the year: ")

                    # Store the encoding with the generated name, registration number, department, and year in a dictionary
                    unknown_encoding = {
                        "name": name,
                        "registration_number": registration_number,
                        "department": department,
                        "year": year,
                        "encoding": captured_image_encoding.tolist()
                    }

                    # Load the existing unknown encodings from the JSON file
                    json_file_path = "unknown.json"
                    try:
                        with open(json_file_path, "r") as json_file:
                            unknown_encodings = json.load(json_file)
                    except FileNotFoundError:
                        unknown_encodings = []

                    # Append the new encoding to the list of unknown encodings
                    unknown_encodings.append(unknown_encoding)

                    # Save the updated unknown encodings to the JSON file
                    with open(json_file_path, "w") as json_file:
                        json.dump(unknown_encodings, json_file)

                    # Edit the file name with the user input
                    edited_image_name = f"{name}_{registration_number}_{department}_{year}.jpg"
                    edited_image_path = os.path.join(image_directory, edited_image_name)

                    # Rename the captured image with the edited file name
                    os.rename(os.path.join(image_directory, image_name), edited_image_path)
                    print("Verification picture captured and saved successfully.")
                else:
                    print("No person detected in the captured frame.")

        # Release the webcam
        video_capture.release()

#def main():

if __name__ == "__main__":
    faceauth.ask_verification_picture()
    #main()
