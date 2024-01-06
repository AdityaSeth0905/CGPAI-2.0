import json
import face_recognition

# Load the face encodings from the JSON file
file_path = "GPAICIIEENC.json"
with open(file_path, "r") as json_file:
    face_encodings_dict = json.load(json_file)

# Assuming you have obtained the face encoding for another person, named "unknown_person"
unknown_person_face_encoding = 
# Obtain the face encoding for the unknown person

# Compare the unknown person's face encoding with each stored face encoding
for name, stored_face_encoding in face_encodings_dict.items():
    similarity = face_recognition.compare_faces([stored_face_encoding], unknown_person_face_encoding, tolerance=0.08)
    if similarity[0]:
        print("Match found! The unknown person is:", name)
        break
else:
    print("No match found for the unknown person.")