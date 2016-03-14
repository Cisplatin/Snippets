from random import randint

class Markov:
    """
    An implementation of a second order Markov chain. Represents the directed
    acyclic graph as an adjacency list.
    """

    EOF = [".", "\n"]
    SPECIAL_CHARS = [",", "(", ")"]

    def __init__(self):
        """
        Creates a new Markov chain.
        """
        # We represent the graph has a dictionary of dictionaries. The entry
        # "." is used as both the end and the beginning of a sentence.
        self.graph = {}

    @staticmethod
    def clean(word):
        """
        Returns a cleaned version of the given word.
        """
        # Remove any "special" characters that we don't want
        for char in Markov.SPECIAL_CHARS:
            word = word.replace(char, "")
        return word.strip()

    def addWord(self, recent_word, last_word, word):
        """
        Adds the new word into the known dictionary.
        """
        if not (recent_word, last_word) in self.graph:
            self.graph[(recent_word, last_word)] = {}
        if not word in self.graph[(recent_word, last_word)]:
            self.graph[(recent_word, last_word)][word] = 0
        self.graph[(recent_word, last_word)][word] += 1

    def learn(self, filename):
        """ 
        Learns the given data for later generation.
        """
        last_word, recent_word = Markov.EOF[0], Markov.EOF[0]
        with open(filename) as data:
            for entry in data:
                # Take each entry line by line and enter it into our graph
                words = [Markov.clean(word) for word in entry.split(" ")]
                for word in words:
                    # Take note if its an end of line
                    EOF_found = False
                    if word[-1] in Markov.EOF:
                        word = word[:-1]
                        EOF_found = True

                    # Learn the new word
                    self.addWord(recent_word, last_word, word)
                    if EOF_found:
                        self.addWord(last_word, word, Markov.EOF[0])
                        recent_word, last_word = Markov.EOF[0], Markov.EOF[0]
                    else:
                        recent_word, last_word = last_word, word

    def generate_word(self, recent_word, last_word):
        """
        Generates a word based on the two given preceding words.
        """
        current_graph = self.graph[(recent_word, last_word)]
        total_weight = sum(current_graph[next_word] for next_word in current_graph.keys())
        selected = randint(0, total_weight)
        for next_word in current_graph.keys():
            if selected <= current_graph[next_word]:
                return next_word
            selected -= current_graph[next_word]

    def generate_sentence(self):
        """
        Generates a sentence based on what has been learned thus far.
        """
        recent_word, last_word = Markov.EOF[0], Markov.EOF[0]
        next_word = self.generate_word(recent_word, last_word)
        sentence = ""
        while next_word != ".":
            next_word = self.generate_word(recent_word, last_word)
            sentence += next_word + " "
            recent_word, last_word = last_word, next_word
        return sentence[:-2].strip() + Markov.EOF[0]

if __name__ == '__main__':
    markov = Markov()
    markov.learn("testfile.txt")
    print markov.generate_sentence()
