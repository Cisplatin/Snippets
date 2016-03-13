from random import choice, randint
from collections import defaultdict

class Markov:
    """
    An implementation of a markov graph. Current implementation is first order,
    using an adjacency list to represent the directed acyclic graph.
    """

    def __init__(self):
        self.graph = defaultdict(lambda : defaultdict(int))
        # We add a \n character as part of the graph to indicate the end
        self.graph["\n"] = {}
        
    @staticmethod
    def clean_word(word):
        """
        Removes punctuation from the given word, and removes capital letters
        """
        PUNCTUATION = [".", ",", "\"", "\'", ")", "(", "\\", ";"]
        for element in PUNCTUATION:
            word = word.replace(element, "")
        return word.lower()

    def learn(self, filename):
        """
        Given a file, learns the text inside of it and adds it to the graph.
        """
        with open(filename) as text_file:
            for line in text_file:
                # Generate the list of words, without the newline character.
                # We remove all commas and periods.
                words = [Markov.clean_word(word) for word in line[:-1].split(" ")]

                # Add a unit of weight to an edge if we find a connection
                for number, word in enumerate(words):
                    if number == len(words) - 1:
                        self.graph[word]["\n"] += 1
                    else:
                        self.graph[word][words[number + 1]] += 1

    def generate_sentence(self):
        """
        Generates a sentence based on what self has learned so far.
        """
        # Currently chooses a random word as a starting word
        current = choice(self.graph.keys())
        sentence = current

        # Keep generating words until an end-of-sentence is come across
        while not current == "\n":
            total_weight = sum(self.graph[current][key] for key in self.graph[current].keys())
            next_word = randint(0, total_weight)
            for key in self.graph.keys():
                if next_word < self.graph[current][key]:
                    current = key
                    sentence += " " + current
                    break
                else:
                    next_word -= self.graph[current][key]
    
        # A new line is found, so we return the sentence
        return sentence

markov = Markov()
markov.learn("apple.txt")
print markov.generate_sentence()
                    
