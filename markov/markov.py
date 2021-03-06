from pickle import load, dump
from random import randint

class Markov:
    """
    An implementation of a second order Markov chain. Represents the directed
    acyclic graph as an adjacency list.
    """

    EOF = [".", "\n"]
    SPECIAL_CHARS = [",", "(", ")"]
    ORDER = 2
    SAVE_FILE = "markov_save.dat"

    def __init__(self):
        """
        Creates a new Markov chain.
        """
        # We represent the graph has a dictionary of dictionaries. The entry
        # "." is used as both the end and the beginning of a sentence.
        self.graph = {}

        # Try to load the default .json file. If it doesn't exist, we ignore
        try:
            self.load(Markov.SAVE_FILE)
        except IOError:
            pass

    @staticmethod
    def empty_list():
        """
        Returns a recent object that assumes nothing has been read.
        """
        return tuple([Markov.EOF[0] for i in xrange(Markov.ORDER)])

    @staticmethod
    def clean(word):
        """
        Returns a cleaned version of the given word.
        """
        # Remove any "special" characters that we don't want
        for char in Markov.SPECIAL_CHARS:
            word = word.replace(char, "")
        return word.strip()

    def load(self, load_file=None):
        """
        Loads a given .json file into the graph. Throws an IOError if the file
        does not exist.
        """
        if not load_file:
            load_file = Markov.SAVE_FILE
        with open(load_file) as data:
            # We use pickle to save/load the data as JSON doesn't have
            # native tuple support
            self.graph = load(data)

    def save(self, save_file=None):
        """
        Stores the graph so far into a .json file.
        """
        if not save_file:
            save_file = Markov.SAVE_FILE
        with open(save_file, "w") as data:
            dump(self.graph, data)

    def addWord(self, recent, word):
        """
        Adds the new word into the known dictionary.
        """
        if not recent in self.graph:
            self.graph[recent] = {}
        if not word in self.graph[recent]:
            self.graph[recent][word] = 1
        else:
            self.graph[recent][word] += 1

    def learn(self, filename):
        """
        Learns the given data for later generation.
        """
        recent = Markov.empty_list()
        with open(filename) as data:
            for entry in data:
                # Take each entry line by line and enter it into our graph
                words = tuple(Markov.clean(word) for word in entry.split(" "))
                words = filter(lambda x: x, words)
                for word in words:
                    # Take note if its an end of line
                    EOF_found = False
                    if word[-1] in Markov.EOF:
                        word = word[:-1]
                        EOF_found = True

                    # Learn the new word
                    self.addWord(recent, word)
                    if EOF_found:
                        self.addWord(recent[1:] + (word,), Markov.EOF[0])
                        recent = Markov.empty_list()
                    else:
                        recent = recent[1:] + (word,)

    def generate_word(self, recent):
        """
        Generates a word based on the two given preceding words.
        """
        try:
            current_graph = self.graph[recent]
        except:
            # We haven't learned anything yet!
            raise Exception("No data has been learned yet.")
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
        recent, sentence = Markov.empty_list(), ""
        next_word = self.generate_word(recent)
        while next_word != ".":
            next_word = self.generate_word(recent)
            sentence += next_word + " "
            recent = recent[1:] + (next_word,)
        return sentence[:-2].strip() + Markov.EOF[0]
