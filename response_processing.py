import os
import json
import pyttsx3
from chart_generator import generate_chart

# Preload audio responses
audio_responses = {}

def load_audio_responses():
    responses_file = "responses.json"
    if os.path.exists(responses_file):
        with open(responses_file, "r") as file:
            responses = json.load(file)
            for key, value in responses.items():
                audio_file = f"audio_responses/{key.lower()}.mp3"
                audio_responses[key] = audio_file
    else:
        print("Responses file not found.")

def process_response(response):
    # Perform actions based on the response
    # Example actions: print, play music, open a file, etc.
    print("Response:", response)
    if response.lower() == "exit":
        exit()
    elif response in audio_responses:
        play_audio_response(response)
        if response.lower() == "diagram":
            generate_chart()
    else:
        print("Response not recognized.")

def play_audio_response(response_key):
    if response_key in audio_responses:
        audio_file = audio_responses[response_key]
        if os.path.exists(audio_file):
            engine = pyttsx3.init()
            engine.setProperty("rate", 150)  # Adjust the speech rate as needed
            engine.setProperty("volume", 1.0)  # Adjust the volume as needed
            engine.save_to_file(response_key, audio_file)
            engine.runAndWait()
        else:
            print("Audio response file not found.")
    else:
        print("Audio response not available for the given response key.")

# Load audio responses from responses.json
load_audio_responses()
