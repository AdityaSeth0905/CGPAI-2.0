from custom_speech_recognition import speech_recognition
from response_processing import process_response, load_audio_responses
from chart_generator import generate_chart
from word_storage import store_new_words
import os
import pygame

def main():
    responses_file = "responses.json"
    new_words_file = "new_words.json"
    audio_responses_dir = "audio_responses"

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load audio responses
    load_audio_responses(responses_file, audio_responses_dir)

    while True:
        response = speech_recognition(responses_file)
        process_response(response)
        store_new_words(response, new_words_file)

        # Check if there is an audio response for the given response
        audio_file = os.path.join(audio_responses_dir, response.lower() + ".mp3")
        if os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

if __name__ == "__main__":
    main()
