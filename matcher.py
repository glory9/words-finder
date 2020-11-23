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
        self.words = getWordsList(char)

        # for every processed sequence for any given character, we need
        # self.words to hold a complete list of all potential matching words.
        # but since self.words gets altered during each sequence, we can use a 
        # cache to quickly obtain the list of matching words
        self.cache = set(self.words)

    def process_sequence(self, letters):
        curr_idx = 0
        correct_matches = []

        while curr_idx < len(letters):
            match_char = letters[curr_idx]
            # we need to delete some items during the iteration, so we keep
            # a copy of self.words instead, then delete the respective items
            # from it and finally update self.words after the iteration
            matching_words = set(self.words)

            for word in self.words:
                if word[curr_idx] != match_char:
                    matching_words.remove(word)
                elif curr_idx == len(word) - 1:
                    correct_matches.append(word)
                    matching_words.remove(word)

            self.words = matching_words
            curr_idx += 1

        self.words = set(self.cache)

        return correct_matches