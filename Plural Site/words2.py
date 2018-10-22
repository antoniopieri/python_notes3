
"""Retrieve and print words from a URL.
Usage:
    Python3 words.py <URL>
"""

import sys
from urllib.request import urlopen
def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:  # this binds the response to avariabled named story
        story_words = []  # emptry list which will hold all words of text
        for line in story:  # the response for http gives list so we must iterate for each list
            line_words = line.decode('utf-8').split()  # this decodes each line and also splits line into list of words
            for word in line_words:  # nested for loop, this loops over each word in the line
                story_words.append(word)  # The append() method appends a passed obj into the existing list.
    return story_words


def print_items(items):
    """Prints items one per line.

    Args: An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL
    Args"
        url:The URL of a UTF-8 text document
    """
    words=fetch_words(url)
    print_items(words)


if __name__ =='__main__':
    main(sys.argv[1])#this accepts the input as a command line argument
#the 0th arg is the module filename
#print(__name__)#evaluates to '__main__' or the actual module name depending on how the enclosing module is being used
#to make a file that run as a script AND is able to be imported we must do the above.
#This enables us to import the module without unduly executing the function.
