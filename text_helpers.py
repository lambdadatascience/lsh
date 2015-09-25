#TODO: lemmatize words (i.e. return to base or dictionary form of word)
#TODO: remove other document signs/symbols that do not add relevance to meaning
#  Could use: str.translate(table[, deletechars])
#  Returns a copy of the string where all characters occurring in the optional
#  argument deletechars are removed.


import re

def removePunctuation(text):
    """ Removes punctuation and quatoation marks,
    changes to lower case, and strips leading and trailing spaces.

    Args:
        text (str): A string.

    Returns:
        str: The cleaned up string.
    """
    text = re.sub(r'[\'\"]+', '', text)   # remove apostrophes & quatoation marks
    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text) # remove underscore
    text = text.lower().strip()

    return text
