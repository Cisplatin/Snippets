class Cronos:
    """
    Cronos is a compression function that is designed specifically for use on
    text files containing only the English language.

    We use the following collection of the most common English words:
    https://github.com/first20hours/google-10000-english
    """

    # The words, in order of frequency, appear in WORDS_TXT delimited by \n
    WORDS_TXT = "WORDS.txt"
    MAPPED_WORDS_TXT = "MAPPED_WORDS.txt"

