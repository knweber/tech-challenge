# tech-challenge
A Python app that returns a word with the most repeated characters from a given file

## Instructions:
1. Clone down repo
2. Navigate into repo:
``cd tech-challenge``
3. Run any of the included test files:
``python main.py <FILE_NAME_HERE>``

## My notes:
- Blank files: I decided to return nothing if a file is blank.
- Punctuation:
  - If a file consists only of punctuation marks, they are eventually filtered out through the ``removePunctuation()`` function, leaving a blank file. As a result, nothing is returned.
  - According to the instructions, when the correct word is returned, all original punctuation should be included. I made the choice to include trailing punctuation marks following the word as well (e.g., "Romeo, Romeo!" would return "Romeo," and "Cat's apples!" would return "apples!").

- Test files:
  - test1: returns "wherefore" (3 "e" repeats, most repeats of any word)
  - test2: returns "people" (2 "p"/"e" repeats, first instance of a tie)
  - test3: returns "bananas" (has the most repeats of a character -- the question marks are excluded because they are punctuation marks)
  - test4: returns "aaa" (the first instance of a tie)
  - test5: returns "blue-collar" (the first instance of a tie between words with different punctuation)
  - test6: nothing (file is blank)
  - test7: returns "ApPle" (the first instance of a tie between words with different cases)
  - test8: nothing (file only consists of punctuation marks)
