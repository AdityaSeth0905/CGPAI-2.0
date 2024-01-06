import speech_recognition as sr
import requests
from gtts import gTTS
import os
import pygame
from pygame.locals import *

def save_response_as_audio(response, filename):
    tts = gTTS(text=response, lang='en')
    tts.save(filename)

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def speech_recognition():
    bot_message = ""
    message = ""
    while bot_message != "Bye":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                message = r.recognize_google(audio)
                print("You said: {}".format(message))
            except:
                print("Sorry, could not recognize your voice")

        if len(message) == 0:
            continue

        print("Sending message now")
        r = requests.post("http://localhost:5002/webhooks/rest/webhook", json={'message': message})
        print("Bot says:")
        for i in r.json():
            bot_message = i['text']
            print(bot_message)
            filename = "Sounds/response{}.mp3".format(len(os.listdir("Sounds")))
            save_response_as_audio(bot_message, filename)

    print("End of conversation")

# Main program
pygame.init()
speech_recognition()

# Wait for a key press to play the audio responses
while True:
    event = pygame.event.wait()
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            for response_file in os.listdir("Sounds"):
                play_audio("Sounds/" + response_file)
            break
