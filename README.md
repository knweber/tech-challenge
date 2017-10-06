# tech-challenge
A Python app that returns a word with the most repeated characters from a given file

## Instructions:
1. Clone down repo
2. Navigate into repo: 
``cd tech-challenge``
3. Run any of the included test files: 
``python main.py <FILE_NAME_HERE>``

## My notes:
- Punctuation:
- Blank documents:
- Test files:
  - test1: returns "wherefore" (3 "e" repeats, most repeats of any word)
  - test2: returns "people" (2 "p"/"e" repeats, first instance of a tie)
  - test3: returns "bananas" (has the most repeats of a character -- the question marks are excluded because they are punctuation marks)
  - test4: returns "aaa" (the first instance of a tie)
  - test5: returns "blue-collar" (the first instance of a tie between words with different punctuation)
  - test6: nothing (file is blank) 
  - test7: returns "ApPle" (the first instance of a tie between words with different cases)
  - test8: nothing (file only consists of punctuation marks)
