# Words Finder
On a board, find words that can be formed by a sequence of adjacent (top, bottom, left, right, diagonal) letters.
Words must be 3 or more letters.
You may move to any of 8 adjacent letters, however, a word should not have multiple instances of the same cell.

## Logic
For each index in the grid, find all matching words that start with the character at that index in all 8 directions (i.e N, S, E, W, NE, NW, SE & SW).

## Design
- Read letters/grid from a file `input.py`.
- Initialize Compass object (compass will give the curent direction of search e.g right, left, top-right diagonal, etc.).
- Initialize Matcher object to generate matching words for a given sequence of letters.
- For each letter, obtain a list of all letters in each direction and pass each list to the matcher to generate matching words.
- Add the words returned from matcher each time to a result list which is then printed to `output.py`

## Modules
### `dictionary` 
A list of valid words that can be matched.

### `compass.py`
Defines a Compass class that returns the change in row and column indexes at any given time given the current direction. This allows to easily navigate all 8 directions 
using only one loop. The compass is implemented using a array of length 8 where each index (0-7)represents the direction from North to Northwest and contains
a tuple (ROWn, COLn) representing the changes in i and j for each direction. When initialized, the compass starts from 0 by default which indicates the North direction and
moves in a clockwise direction. 

### `matcher.py`
Defines a Matcher class that finds matching words given a sequence of characters. First, the matcher obtains a set of words starting with the first character. The set is then filtered using the following logic:
- Each word in the set is checked at a current index i.
- if the current letter in the word does not match the current letter in the search sequence, that word is removed from the set.
- if the current letter is a match and i is at the last index of the word, that word is also removed from the set but added to a result list.
- the above steps are repeated till we reach the end of the sequence.
