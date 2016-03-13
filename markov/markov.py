from random import choice, randint
from collections import defaultdict

class Markov:
    """
    An implementation of a markov graph. Current implementation is first order,
    using an adjacency list to represent the directed acyclic graph.
    Intended for ASCII text (i.e. won't filter characters like \xe2)
    """

    punctuation = [".", ",", "'", "\"", "(", ")", ";", " "]

    def __init__(self):
        self.graph = defaultdict(lambda : defaultdict(int))
        # We add a \n character as part of the graph to indicate the end
        self.graph["\n"] = {}
        
    @staticmethod
    def clean_word(word):
        """
        Removes punctuation from the given word, and removes capital letters
        """
        for element in Markov.punctuation:
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

    def generate_next_word(self, word):
        """
        Returns a randomly selected next-word based on the given word.
        """
        # Keep generating words until an end-of-sentence is come across
        total_weight = sum(self.graph[word][key] for key in self.graph[word].keys())
        next_word = randint(0, total_weight)
        for key in self.graph.keys():
            if next_word <= self.graph[word][key]:
                return "" if key == "\n" else key
            else:
               next_word -= self.graph[word][key]

    def generate_sentence(self):
        """
        Generates a sentence based on what self has learned so far.
        """
        # Currently chooses a random word as a starting word
        current = choice(self.graph.keys())
        sentence = current.capitalize() + " "
        while current:
            current = self.generate_next_word(current)
            sentence += current + " "
        return sentence

markov = Markov()
markov.learn("apple.txt")
print markov.generate_sentence()
                    
