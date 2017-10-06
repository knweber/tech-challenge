import sys

# PSEUDOCODE:
# 1. Open file
# 2. Read file
# 3. Save contents of file as a string
# 4. Split string into individual words in a list (make them lowercase in list)
# 5. Go through each word letter-by-letter, filtering out punctuation
# 6. Add characters to a dictionary with their respective counts within the word
#     - If the document is blank, break out of loop and return an empty string
# 7. Take the character counts for each word and find the most-repeated character in each
# 8. Take the max repeat numbers for each word and find the highest number out of those (i.e., the word that contains the most repeats of a particular letter)
# 9. Return the corresponding word
#     - Return word with original punctuation and capitalization, which is still accessible in the original list of words
#     - If there is a tie, the first word should be returned
#         - Since this will happen in a for loop, the number of repeats for a word will be evaluated chronologically and the first one should be returned

def main():
    filename = sys.argv[1]
    specificFile = open(filename,"r")
    text = specificFile.read()
    repeats(text)
    specificFile.close()


def repeats(sentence):
    print(sentence)

if __name__ == '__main__':
    main()
