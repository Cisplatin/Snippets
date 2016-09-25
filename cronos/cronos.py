from struct import pack
from pickle import dump

class Cronos:
    """
    Cronos is a compression function that is designed specifically for use on
    text files containing only the English language.

    We use the following collection of the most common English words:
    https://github.com/first20hours/google-10000-english
    """

    # The words, in order of frequency, appear in WORDS_TXT delimited by \n.
    # Words with their mapped n-byte output are placed into MAPPED_WORDS_TXT.
    WORDS_TXT = 'WORDS.txt'
    MAPPED_WORDS_P = 'MAPPED_WORDS.p'

    # This indicates that we store keys as little-endian unsigned ints
    PACK_FORMATTING = ">I"

    # Re-maps all words in WORDS_TXT to MAPPED_WORDS_TXT
    @staticmethod
    def __map():
        translation, current_byte = {}, 0
        with open(Cronos.WORDS_TXT, 'r') as words:
            for word in words.read().split('\n')[:-1]:
                translation[word] = pack(">I", current_byte)
                current_byte += 1
        dump(translation, open(Cronos.MAPPED_WORDS_P, "wb"))

Cronos._Cronos__map()
