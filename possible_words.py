# Specify any green letters in KNOWN_LETTERS array
# Leave blank strings in KNOWN_LETTERS array for non-greens
# Specify any gray/excluded letters in EXCLUDED_LETTERS array

KNOWN_LETTERS = ["","","e","a","d"]
EXCLUDED_LETTERS = ["t", "k", "r", "n"]
INPUT_FILE = "shuffled_wordle_words.txt"

with open(INPUT_FILE) as f:
    lines = f.read()
f.close()

word_list = lines.split("\n")

def filter_words_by_known_letters(known_letters, word_list):
    filtered_word_list = []
    for word in word_list:
        word_letters = list(word)
        for i in range(5):
            if known_letters[i] != "" and word_letters[i] != known_letters[i]:
                break
        else:
            filtered_word_list.append(word)
    return filtered_word_list

def filter_words_by_excluded_letters(excluded_letters, word_list):
    filtered_word_list = []
    for word in word_list:
        skip = False
        for letter in excluded_letters:
            if letter in word:
                skip = True
                break
        if skip:
            continue
        else:
            filtered_word_list.append(word)
    return filtered_word_list


filtered_words = filter_words_by_known_letters(KNOWN_LETTERS, word_list)
print("\nFILTERED BY KNOWN GREEN LETTERS:")
print(filtered_words)
filtered_words = filter_words_by_excluded_letters(EXCLUDED_LETTERS, filtered_words)
print("\nFILTERED BY KNOWN GRAY LETTERS:")
print(filtered_words)
print("\n")
