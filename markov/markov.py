from json import dump, load
from random import choice, randint
from collections import defaultdict

class Markov:
    """
    An implementation of a markov graph. Current implementation is first order,
    using an adjacency list to represent the directed acyclic graph.
    Intended for ASCII text (i.e. won't filter characters like \xe2)
    """

    # TODO Recognize proper nouns and capitalize appropriately
    # TODO Accept non-ASCII text

    punctuation = [".", ",", "'", "\"", "(", ")", ";", " "]
    minimum_sentence_length = 5
    save_file = "markov_save.json"

    def __init__(self):
        self.graph = defaultdict(lambda : defaultdict(int))

        # We add a \n character as part of the graph to indicate the end
        self.graph["\n"] = {}
        
        # We now load the previously learned data
        try:
            with open(Markov.save_file) as data_file:
                loaded_data = load(data_file)
                for word in loaded_data:
                    for next_word in loaded_data[word]:
                        self.graph[word][next_word] = loaded_data[word][next_word]
        except IOError:
        # No previous store was found. No worries, we just keep it empty
            pass        

    @staticmethod
    def clean_word(word):
        """
        Removes punctuation from the given word, and removes capital letters
        """
        for element in Markov.punctuation:
            word = word.replace(element, "")
        return word.lower()

    def convert_graph(self, ddict):
        """
        Converts the current graph to a normal dictionary for JSON's sake 
        """
        if isinstance(ddict, defaultdict):
            ddict = {key: self.convert_graph(value) for key, value in ddict.iteritems()}
        return ddict

    def save(self):
        """
        Saves the current data into a text file
        """
        converted = self.convert_graph(self.graph)
        dump(converted, open(self.save_file, "w"))

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
        sentence_length = 1
        while current:
            try:
                current = self.generate_next_word(current)
            except KeyError:
                raise Exception("No data has been learned yet.")
            while sentence_length < Markov.minimum_sentence_length and not current:
                current = choice(self.graph.keys())
            sentence += current + " "
            sentence_length += 1
        return sentence.strip() + "."
