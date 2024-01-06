import PIL.Image
import PIL.ImageDraw
import requests
from io import BytesIO

from IPython.display import display

import face_recognition

#response = requests.get("C:\Users\gnkit\Downloads\me.jpg")
#fr_image = face_recognition.load_image_file(BytesIO(response.content))

response = r"C:\Users\gnkit\Downloads\me.jpg"  
fr_image = face_recognition.load_image_file(response)

face_locations = face_recognition.face_locations(fr_image)

number_of_faces = len(face_locations)
print("I found {} face(s) in this photograph.".format(number_of_faces))

pil_image = PIL.Image.fromarray(fr_image)

for face_location in face_locations:
    # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    # Let's draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="black")


display(pil_image)

face_encodings = face_recognition.face_encodings(fr_image)
face_encodings[0]

response1 = r"C:\Users\gnkit\Downloads\me.jpg"
image_of_person_1 = face_recognition.load_image_file(response1)
face_locations = face_recognition.face_locations(image_of_person_1)
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1, known_face_locations=face_locations)

response2 = r"C:\Users\gnkit\Downloads\me2.jpg"
image_of_person_2 = face_recognition.load_image_file(response2)
face_locations = face_recognition.face_locations(image_of_person_2)
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2, known_face_locations=face_locations)

response3 = r"C:\Users\gnkit\Downloads\ronakraval.jpeg"
image_of_person_3 = face_recognition.load_image_file(response3)
face_locations = face_recognition.face_locations(image_of_person_3)
person_3_face_encoding = face_recognition.face_encodings(image_of_person_3, known_face_locations=face_locations)

person_1_face_encoding=person_1_face_encoding[0]
person_2_face_encoding=person_2_face_encoding[0]
person_3_face_encoding=person_3_face_encoding[0]
tolerance=0.08

similarity=face_recognition.compare_faces([person_1_face_encoding], person_3_face_encoding, tolerance)
print(similarity)

#face_landmarks_list = face_recognition.face_landmarks(fr_image)
#print(face_landmarks_list)

