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

# Remove any punctuation
def removePunctuation(letterList,char,countTable):
    if re.match("\w",char):
        countTable[char] = int(letterList.count(char))
        return countTable[char]

def isMaxValue(existingMax,newVal):
    if newVal > existingMax:
        return(True)

def repeats(sentence):

    # If file is blank, return
    if len(sentence) == 0:
        return

    # If there are any newline characters
    if "\n" in sentence:
        sentence = removeNewLines(sentence)

    currMax = 0 # the highest count of character repeats out of all the words
    ans = ""
    words = sentence.split(" ")

    for word in words:
        charCounts = dict() # create dictionary to hold character counts for current word
        letters = list(word.lower()) # add lowercase letters of word into list
        for l in letters:
            # Remove punctuation marks, if any
            removePunctuation(letters,l,charCounts)

        # Make list of letter counts for current word
        countsPerWord = charCounts.values()

        # If no characters are letters, return
        if len(countsPerWord) == 0:
            return

        # Find highest value in list (most repeated character)
        wordMax = max(countsPerWord)

        # if wordMax > currMax:
        #     currMax = wordMax
        #     ans = word

        if isMaxValue(currMax,wordMax):
            currMax = wordMax
            ans = word


    print ans


if __name__ == '__main__':
    cli()
