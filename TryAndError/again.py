import speech_recognition as sr
import json
from collections import defaultdict
import os
import matplotlib.pyplot as plt
import sys

def store_new_words(new_words):
    # Load existing words and frequencies from the JSON file
    if os.path.exists("new_words.json") and os.stat("new_words.json").st_size > 0:
        with open("new_words.json", "r") as file:
            data = json.load(file)
    else:
        data = defaultdict(int)

    # Update the frequencies of new words
    for word in new_words:
        data[word] += 1

    # Save the updated data to the JSON file
    with open("new_words.json", "w") as file:
        json.dump(data, file, indent=4)

def process_response(response):
    # Perform actions based on the response
    # Example actions: print, play music, open a file, etc.
    print("Response:", response)
    if response.lower() == "exit":
        exit()
    elif "hell" in response.lower():
        generate_chart()

def generate_chart():
    # Load the word frequencies from the JSON file
    if os.path.exists("new_words.json") and os.stat("new_words.json").st_size > 0:
        with open("new_words.json", "r") as file:
            data = json.load(file)
    else:
        print("No data available.")
        return

    # Extract the words and frequencies
    words = list(data.keys())
    frequencies = list(data.values())

    # Plot the chart
    plt.bar(words, frequencies)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Word Frequencies")
    plt.xticks(rotation=45)

    # Display the chart
    plt.show()

def speech_recognition():
    # Load the responses from the JSON file
    with open("responses.json", "r") as file:
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
                        process_response(response)
                        break
                else:
                    print("I didn't understand that.")
            except sr.UnknownValueError:
                print("I didn't understand that.")
            except sr.RequestError as e:
                print("An error occurred:", str(e))

speech_recognition()
