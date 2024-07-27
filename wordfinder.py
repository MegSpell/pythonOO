"""Word Finder: A tool for retrieving random words from a dictionary file."""

import random


class WordFinder:
    """
    A class that reads words from a dictionary file and provides random word selection.

    This class reads words from a file where each line represents a word, and allows for retrieving a random word from the file.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """
        Initializes the WordFinder instance by reading words from the specified file.

        Opens the file at `path`, parses the words, and stores them in the instance.

        Prints the total number of words read from the file.

        Parameters:
        - path (str): The file path to the dictionary file containing words.
        """

        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """
        Parses the given file object to extract a list of words.

        Reads each line from the file, strips any leading or trailing whitespace,
        and returns a list of words.

        Parameters:
        - dict_file (file object): The file object containing lines of words.

        Returns:
        - list of str: A list where each item is a word extracted from the file.
        """

        return [w.strip() for w in dict_file]

    def random(self):
        """
        Selects and returns a random word from the list of words.

        Uses the `random.choice` method to pick and return a word randomly from the list of words read from the file.

        Returns:
        - str: A random word from the list.
        """

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    A specialized version of WordFinder that excludes blank lines and comments.

    This subclass extends WordFinder to handle files that may contain blank lines
    or comments (lines starting with '#'). It parses the file to include only valid words.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """
        Parses the given file object to extract a list of words, ignoring blank lines and comments.

        Reads each line from the file, strips any leading or trailing whitespace, and includes
        the line in the list only if it is not empty and does not start with a '#' character.

        Parameters:
        - dict_file (file object): The file object containing lines of words with potential comments.

        Returns:
        - list of str: A list of words, excluding any blank lines and comments.
        """

        return [w.strip() for w in dict_file
            if w.strip() and not w.startswith("#")]
    