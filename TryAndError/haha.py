import speech_recognition as sr
import json


# Create a dictionary to store new words
with open("new_words.json", "a") as f:
    new_words = {f}

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
        except sr.UnknownValueError:
            print("I didn't understand that.")
            continue

        # Check if the user's input is a new word
        if text not in new_words:
            # Add the new word to the dictionary
            new_words[text] = 1

            # Print a message to the user
            print("I learned a new word: {}.".format(text))

            # Save the dictionary to a JSON file
            with open("new_words.json", "a") as f:
                json.dump(new_words, f, indent=4)
        else:
            new_words[text] += 1


        # Check if the user wants to exit the program
        if text == "exit":
            break
        else:
            if text=="close":
                break
            else:
                if text == "shutdown":
                    break
                else:
                    continue
    
# Print the dictionary of new words
print("Here are the new words I learned:")
for word in new_words:
    print(word)
