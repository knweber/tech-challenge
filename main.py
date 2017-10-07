import sys
import re

# PSEUDOCODE:
# 1. Open file
# 2. Read file
# 3. Save contents of file as a string
# 4. Split string into individual words in a list (make them lowercase in list)
# 5. Go through each word letter-by-letter, filtering out punctuation
# 6. Add characters to a dictionary with their respective counts within the word
#     - If the document is blank, break out of loop and return
# 7. Take the character counts for each word and find the most-repeated character in each
# 8. Take the max repeat numbers for each word and find the highest number out of those (i.e., the word that contains the most repeats of a particular letter)
# 9. Return the corresponding word
#     - Return word with original punctuation and capitalization, which is still accessible in the original list of words
#     - If there is a tie, the first word should be returned
#         - Since this will happen in a for loop, the number of repeats for a word will be evaluated chronologically and the first one should be returned

def cli():
    filename = sys.argv[1]
    specific_file = open(filename,"U")
    file_text = specific_file.read()
    specific_file.close()
    most_repeats(file_text)

# Remove any newline characters
def remove_new_lines(sentence):
    sentence = " ".join([line.rstrip() for line in sentence.rstrip().splitlines()])
    return(sentence)

# Remove any punctuation or numbers
def remove_non_letters(letter_list,char,count_table):
    if char.isalpha():
        count_table[char] = int(letter_list.count(char))
        return(count_table[char])

# Check to see if the highest number of repeats in current word is higher than the current highest number
def is_max_value(existing_max,new_val):
    if new_val > existing_max:
        return(True)

# Find word with the highest number of repeats of a single letter
def most_repeats(sentence):
    if len(sentence) == 0: # If file is blank, return
        return

    if "\n" in sentence: # If there are any newline characters, remove them
        sentence = remove_new_lines(sentence)

    curr_max = 0 # The highest count of character repeats out of all the words
    ans = ""
    words = sentence.split(" ")

    for word in words:
        char_counts = dict() # Create dictionary to hold character counts for current word
        letters = list(word.lower()) # Letters in word are made lowercase and added to a list
        for l in letters:
            remove_non_letters(letters,l,char_counts) # Only keep the letters

        counts_per_word = char_counts.values() # Make list of just the letter counts for current word

        if len(counts_per_word) == 0: # If no characters are letters (e.g. all punctuation), move onto next word
            continue

        word_max = max(counts_per_word) # Find highest value in list (most repeated character)

        if is_max_value(curr_max,word_max):
            curr_max = word_max # If the current word has a character with more repeats than the previous leading word, reassign the number of repeats to correspond to the number of repeats in the current word
            ans = word # Answer is set as the current word

    print ans


if __name__ == '__main__':
    cli()
