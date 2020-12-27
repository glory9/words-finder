# scan the dictionary to obtain a set of words 
# starting with a specified character
def getWordsList(char):
    words_list = set()
    with open("dictionary.txt") as reader:
        for line in reader.readlines():
            word=line.strip().lower()
            if word[0] == char:
                words_list.add(word)

    return words_list

class Matcher:
    def __init__(self, char):
        self.potential_matches = getWordsList(char)

        # for every processed sequence for any given character, we need
        # self.potential_matches to hold a complete list of all potentially 
        # matching words. But since self.potential_matches gets altered after
        # processing each sequence/direction, we can use a cache to quickly 
        # re-compute the original list of matching words.
        self.cache = set(self.words)

    def process_sequence(self, letters):
        curr_idx = 0
        correct_matches = []

        while curr_idx < len(letters) and len(self.potential_matches) > 0:
            match_char = letters[curr_idx]
            # we need to delete some items during the iteration, so we keep a copy
            # of self.potential_matches instead, then delete the respective items
            # from the copy and finally update self.words after the iteration.
            updated_potential_matches = set(self.potential_matches)

            for word in self.potential_matches:
                if word[curr_idx] != match_char:
                    updated_potential_matches.remove(word)
                elif curr_idx == len(word) - 1:
                    # we only add words of length 3 or more (i.e, curr_idx 2 and above)
                    if curr_idx > 1:
                        correct_matches.append(word)
                    updated_potential_matches.remove(word)

            self.potential_matches = updated_potential_matches
            curr_idx += 1
        # update self.words to its original state after processing each sequence
        self.potential_matches = set(self.cache)

        return correct_matches
