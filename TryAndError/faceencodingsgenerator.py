#All the Imported Libraries
import PIL.Image
import PIL.ImageDraw
import requests
from io import BytesIO
import json
import face_recognition
from IPython.display import display


#Path of images
aditya_seth=r"C:\Users\gnkit\Downloads\me.jpg"
ronak_raval=r"C:\Users\gnkit\Downloads\ronakraval.jpeg"
shreshth_pandey=r"C:\Users\gnkit\Downloads\shryesthpandey.jpg"

#Loading of files
image_of_aditya_seth=face_recognition.load_image_file(aditya_seth)
image_of_ronak_raval=face_recognition.load_image_file(ronak_raval)
image_of_shreshth_pandey=face_recognition.load_image_file(shreshth_pandey)

#Getting face locations of every image
face_locations = face_recognition.face_locations(image_of_aditya_seth)
face_locations = face_recognition.face_locations(image_of_aditya_seth)
face_locations = face_recognition.face_locations(image_of_aditya_seth)

# Using all the encodings
aditya_seth_face_encoding = face_recognition.face_encodings(image_of_aditya_seth, known_face_locations=face_locations)[0]
ronak_raval_face_encoding = face_recognition.face_encodings(image_of_ronak_raval, known_face_locations=face_locations)[0]
shreshth_pandey_face_encoding = face_recognition.face_encodings(image_of_shreshth_pandey, known_face_locations=face_locations)[0]

person_1_face_encoding = aditya_seth_face_encoding.tolist()
person_2_face_encoding = ronak_raval_face_encoding.tolist()
person_3_face_encoding = shreshth_pandey_face_encoding.tolist()

# Create a dictionary to store the face encodings with corresponding names as keys
face_encodings_dict = {
    "Aditya_Seth": person_1_face_encoding,
    "Ronak_Raval": person_2_face_encoding,
    "Shreshth_Pandey": person_3_face_encoding
}

# Write the dictionary to a JSON file
file_path = "GPAICIIEENC.json"
with open(file_path, "w") as json_file:
    json.dump(face_encodings_dict, json_file)
