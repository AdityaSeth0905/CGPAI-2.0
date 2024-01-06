import cv2
import face_recognition
import json
import openpyxl
import numpy as np

# Load the face encodings from the "unknown.json" file
with open("unknown.json") as file:
    unknown_data = json.load(file)

# Extract the face encodings and corresponding details
unknown_encodings = [np.array(unknown['encoding']) for unknown in unknown_data]
unknown_names = [unknown['name'] for unknown in unknown_data]
unknown_reg_nums = [unknown['registration_number'] for unknown in unknown_data]
unknown_departments = [unknown['department'] for unknown in unknown_data]
unknown_years = [unknown['year'] for unknown in unknown_data]

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# List to store the encodings of already processed faces
processed_encodings = []

# Loop to capture frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through the face encodings in the current frame
    for face_encoding in face_encodings:
        # Compare the face encoding with the known encodings
        matches = face_recognition.compare_faces(unknown_encodings, face_encoding)

        # Check if there is a match
        if True in matches:
            # Find the index of the matched encoding
            match_index = matches.index(True)

            # Get the details of the matched person
            name = unknown_names[match_index]
            reg_num = unknown_reg_nums[match_index]
            department = unknown_departments[match_index]
            year = unknown_years[match_index]

            # Check if the encoding has already been processed
            if face_encoding.tolist() not in processed_encodings:
                # Add the details to the "StudentODList.xlsx" file
                workbook = openpyxl.load_workbook("StudentODList.xlsx")
                worksheet = workbook.active
                new_row = [name, reg_num, department, year]
                worksheet.append(new_row)
                workbook.save("StudentODList.xlsx")

                # Add the encoding to the processed encodings list
                processed_encodings.append(face_encoding.tolist())

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the windows
video_capture.release()
cv2.destroyAllWindows()
