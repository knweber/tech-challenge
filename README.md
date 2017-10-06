# tech-challenge
A Python app that returns a word with the most repeated characters from a given file

## Instructions:
1. Clone down repo
2. Navigate into repo:
``cd tech-challenge``
3. Run any of the included test files:
``python main.py <FILE_NAME_HERE>``

## Notes:
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

## Original challenge:
In some English words, there is a letter that appears more than once. Search through a
sample of text to find the word with a letter that is repeated more times than any other
letter is repeated in any other word. When there is a tie between two words, choose the
word that appeared first in the sample.

The text sample will contain only english letters (a-z and A-Z) — separated by any type
and any amount of whitespace — and punctuation marks. A letter is considered to be
the same letter regardless of whether it appears in uppercase or lowercase. Any
punctuation marks should be ignored. So, in particular, contractions, possessives, and
hyphenated words count as a single word.

Write either a PHP, Ruby, or Python program, to be executed from the CLI. The
program should accept a file path as an argument and return the original text of the
winning word — meaning the same capitalization and punctuation marks. So for
example, “Blue-collar worker” should return “Blue-collar” and not “blue-collar”,
“Bluecollar”, “bluecollar”, or “Blue collar”. The program should be able to handle any
character for input, and merely ignore any character that is not a letter. Lastly, the
program should not return exceptions or warnings.


**Example:**

Input: “O Romeo, Romeo, wherefore art thou Romeo?”

Output: “wherefore”

Explanation: The letter “e” is repeated three times in the word “wherefore”—and this is
more than any other letter is repeated in any other word!


**Example:**

Input: “Some people feel the rain, while others just get wet.”

Output: “people”

Explanation: Both “people” and “feel” have a letter that is repeated twice within the
word. This is a tie—and the first word wins!
