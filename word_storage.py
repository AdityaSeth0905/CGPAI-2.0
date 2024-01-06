import json
from collections import defaultdict
import os

def store_new_words(new_words, file_name):
    # Load existing words and frequencies from the JSON file
    if os.path.exists(file_name) and os.stat(file_name).st_size > 0:
        with open(file_name, "r") as file:
            data = json.load(file)
    else:
        data = defaultdict(int)

    # Update the frequencies of new words
    for word in new_words:
        data[word] += 1

    # Save the updated data to the JSON file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
