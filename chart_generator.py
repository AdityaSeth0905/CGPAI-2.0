import json
import os
import matplotlib.pyplot as plt

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
    plt.pie(frequencies, labels=words, autopct="%1.1f%%")
    plt.title("Word Frequencies")

    # Display the chart
    plt.show()
