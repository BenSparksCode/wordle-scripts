# Fill in known letters

GREEN_LETTERS = ["","","","",""]
YELLOW_LETTERS = [["s", "c"],[],["o"],[],[]]
EXCLUDED_LETTERS = ["a", "l", "e", "t", "r", "w", "d"]
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


def find_most_common_unknown_letters(known_letters, word_list):
    unknown_letters = []
    unknown_letters_scores = {} # {letter: score}
    for word in word_list:
        for letter in word:
            if letter in known_letters:
                continue
            elif letter in unknown_letters:
                unknown_letters_scores[letter] += 1
            else:
                unknown_letters.append(letter)
                unknown_letters_scores[letter] = 1
    return sorted(unknown_letters_scores.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True)

def find_best_words_to_guess(common_letters_dict, word_list):
    word_scores = {} # {word: score}
    for word in word_list:
        score = 0
        for letter in word:
            # TODO refine to not reward words with repeated letters
            if letter in common_letters_dict:
                score += common_letters_dict[letter]
        word_scores[word] = score
    return sorted(word_scores.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True)

def filter_words_by_yellow_letters(yellow_letters, word_list):
    filtered_word_list = []
    for word in word_list:
        word_has_potential = True
        for slot in range(5):
            if not word_has_potential: break
            for letter in yellow_letters[slot]:
                if letter not in word:
                    word_has_potential = False
                    break
                elif word[slot] == letter:
                    word_has_potential = False
                    break
        if word_has_potential:
            filtered_word_list.append(word)         
    return filtered_word_list



# Words with GREEN letters
filtered_words = filter_words_by_known_letters(GREEN_LETTERS, word_list)
print("\nFILTERED BY KNOWN GREEN LETTERS:")
print(filtered_words)

# Words NOT with GRAY letters
filtered_words = filter_words_by_excluded_letters(EXCLUDED_LETTERS, filtered_words)
print("\nFILTERED BY KNOWN GRAY LETTERS:")
print(filtered_words)

# Words with YELLOW letters
filtered_words = filter_words_by_yellow_letters(YELLOW_LETTERS, filtered_words)
print("\nFILTERED BY KNOWN YELLOW LETTERS:")
print(filtered_words)

# Sort remaining words by most common unknown letters
common_letters = find_most_common_unknown_letters(GREEN_LETTERS, filtered_words)
print_output = "\n".join(["{}: {}".format(letter, score) for letter, score in common_letters])
print("\nMOST COMMON UNKNOWN LETTERS:")
print(print_output)

best_words = find_best_words_to_guess(dict(common_letters), filtered_words)
print_output = "\n".join(["{}: {}".format(word, score) for word, score in best_words])
print("\nBEST WORDS TO GUESS NEXT:")
print(print_output)
print("\n")
