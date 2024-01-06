import speech_recognition as sr
import json
import os

def speech_recognition(responses_file):
    # Load the responses from the JSON file
    with open(responses_file, "r") as file:
        responses = json.load(file)

    # Create a speech recognition object
    recognizer = sr.Recognizer()

    # Start listening for speech
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            # Get the user's input
            audio = recognizer.listen(source)

            # Try to recognize the user's input
            try:
                text = recognizer.recognize_google(audio)
                print("Recognized:", text)

                # Check if any word group matches the recognized text
                for word_group, response in responses.items():
                    if any(word.lower() in text.lower() for word in word_group.split()):
                        return response
                else:
                    print("I didn't understand that.")
            except sr.UnknownValueError:
                print("I didn't understand that.")
            except sr.RequestError as e:
                print("An error occurred:", str(e))
