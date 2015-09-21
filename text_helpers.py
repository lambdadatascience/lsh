#TODO: use text corpora to transform document, e.g. from plural to singular form
#TODO: remove other document signs/symbols that do not add relevance to meaning

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
