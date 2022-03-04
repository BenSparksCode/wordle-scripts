# Imports ordered words
# Shuffles them 3 times
# Saves the shuffled words in shuffled_wordle_words.txt
import random

INPUT_FILE = "ordered_words.txt"
OUTPUT_FILE = "shuffled_wordle_words.txt"

with open(INPUT_FILE) as f:
    lines = f.read()
f.close()

word_list = lines.split("\n")
random.shuffle(word_list)
random.shuffle(word_list)
random.shuffle(word_list)

final_write_string = "\n".join(word_list)

with open(OUTPUT_FILE, 'w') as f:
    f.write(final_write_string)
f.close()