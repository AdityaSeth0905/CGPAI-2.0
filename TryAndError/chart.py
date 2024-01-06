import os
import matplotlib.pyplot as plt
import json

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

generate_chart()
