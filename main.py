from compass import Compass
from matcher import Matcher


def isWithinRange(x, y, rows, cols):
    if (x < 0 or y < 0 or x >= rows or y >= cols):
        return False
    return True
    
# to filter out single characters obtained from the dictionry
def invalidSingleCharater(string):
    return len(string) == 1 and string[0] not in ['a','i']

def findValidWords(grid, rows, cols):
    valid_words = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            compass = Compass()
            sequence_matcher =  Matcher(grid[i][j])

            # for each index in character grid, obtain all the valid words
            # starting at that index in all 8 directions - left, right, top, down,
            # and all four diagonals.
            for TURN in range(8):
                x, y = i, j

                # obtain current change in rows(i) and change in columns(j) from 
                # compass (compass automatically updates to the next direction)
                iChange, jChange = compass.get_curr_index_changes()

                # compute character sequence in current direction
                char_sequence = []
                while isWithinRange(x, y, rows, cols):
                    char_sequence.append(grid[x][y])
                    x += iChange
                    y += jChange
                # compute correct matches
                correct_matches = sequence_matcher.process_sequence(char_sequence)
                valid_words.extend(correct_matches)

    return valid_words

with open("input.txt") as reader:
    rows, cols = list(map(int, reader.readline().strip().split(" ")))
    if not rows or not cols:
        raise Exception("[INVALID INPUT] Empty Grid")
    grid = []

    for R in range(rows):
        line = reader.readline().strip()
        row = [C.lower() for C in line.split(" ")]
        grid.append(row)

    valid_words = set(findValidWords(grid, rows, cols))

    # clean up results to remove single characters pulled from dictionary except
    # 'a' and 'i'.
    result = [W for W in valid_words if not invalidSingleCharater(W)]
    # sort words by length
    result.sort(key= lambda w: len(w))


with open("output.txt", 'w') as writer:
    for word in result:
        writer.write(word + "\n")
    
print("Code Executed Successfully.\nCheck results in output.py")
print("You can modify the input in input.py")
