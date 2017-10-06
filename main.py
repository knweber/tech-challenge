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
    specificFile = open(filename,"U")
    text = specificFile.read()
    repeats(text)
    specificFile.close()

# Remove any newline characters
def removeNewLines(sentence):
    sentence = " ".join([line.rstrip() for line in sentence.rstrip().splitlines()])
    return(sentence)

# Remove numbers
def isNum(word):
    if re.match("\d",char):
        char = ""
        return(char)

# Remove any punctuation or numbers
def removeNonLetters(letterList,char,countTable):
    if char.isalpha():
        countTable[char] = int(letterList.count(char))
        return(countTable[char])

# Check to see if the highest number of repeats in current word is higher than the current highest number
def isMaxValue(existingMax,newVal):
    if newVal > existingMax:
        return(True)

def repeats(sentence):
    if len(sentence) == 0: # If file is blank, return
        return

    if "\n" in sentence: # If there are any newline characters
        sentence = removeNewLines(sentence)

    currMax = 0 # The highest count of character repeats out of all the words
    ans = ""
    words = sentence.split(" ")

    for word in words:
        charCounts = dict() # Create dictionary to hold character counts for current word
        letters = list(word.lower()) # Add lowercase letters of word into list
        for l in letters:
            removeNonLetters(letters,l,charCounts) # Only keep letters

        countsPerWord = charCounts.values() # Make list of letter counts for current word

        if len(countsPerWord) == 0: # If no characters are letters
            continue

        wordMax = max(countsPerWord) # Find highest value in list (most repeated character)

        if isMaxValue(currMax,wordMax):
            currMax = wordMax
            ans = word

    print ans


if __name__ == '__main__':
    cli()
