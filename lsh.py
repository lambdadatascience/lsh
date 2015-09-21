##############################################################################
# This is a proof of concept implementation of an lsh function in python.
# Although performance is slow, similarity scoring works well even with dirty
#  data. Next step is to implement this in pySpark.
#
# TODO: Use regex to cleanup text on input; remove non-alphanumeric symbols etc.
# TODO: Subtract stop words. Start with stop words from NLTK library
# TODO: Implement in pySpark
# TODO:  - generate n hash functions instead of using crc32
# TODO:  - distribute/broadcast hash functions to all worker nodes
# TODO: test on full data set of 20K docs.
##############################################################################

import os.path
import binascii
from collections import deque
import numpy as np
import scipy.spatial.distance as distance

def windowText(doc_text = "", window_size = 2):
    """Parses original document text and returns windowed results

    Args:
        doc_text (str): document text to analyze (default: "")
        window_size (int): size of the sliding window (default: 2)

    Returns:
        List[str]: list of word pairs of length window_size.
    """
    window = deque(maxlen=window_size)
    window_list = []

    for word in doc_text.split():   # splits on whitespaces (extra ignored)
    	window.append(word)
    	if (len(window) == window_size):
    		window_list.append(' '.join(w for w in window))

    return window_list

def txtCRC(text="", crc=0):
    """Generates a crc32 for a given text input.

    Args:
        text (str): text to process (default: "")
        crc (int): crc to offset/init value

    """
    return binascii.crc32(text, crc)

def getMinHashList(text="", maxGen=1):
    """Return "minhash" value.

    Note: not using an actual hash function, but a shortcut using crc32
           with crc offset.

    Args:
        text (str):  text to process (default: "")
        maxGen (int): maximum number of min hashes to generate (default: 1)

    Returns:
        List(int): list of minhash values
    """
    # Note: using two-word pairs; briefly tested with three-word pairs and got better results;
    #  greater than three does not produce significantly better results tho further testing required
    unique_list_of_word_sets = set(windowText(text.lower(), 2))

    return (min(txtCRC(w,i) for w in unique_list_of_word_sets) for i in xrange(maxGen))

def getScore(list_1, list_2):
    """ Returns a score value using Jaccard distance

    Args:
        list1 (list): first list representing minHash values of a document
        list2 (list): second list representing minHash values of another document

    Returns:
        float: Jaccard similarity score
    """
    return distance.pdist(np.array([list_1,list_2]), 'jaccard').sum()

# Quick test
if __name__ == '__main__':

    num_hashes = 200
    num_buckets = 20

    with open('<path1>', 'r') as f: doc1 = f.read()
    with open('<path2>', 'r') as f: doc2 = f.read()
    with open('<path3>', 'r') as f: doc3 = f.read()

    doc_list = ((doc1, "id1"), (doc2, "id2"), (doc3, "id3"))

    signatures = ((id_,(g % 2 for g in getMinHashList(doc, num_hashes))\
                    for doc, id_ in doc_list)

    bucket_dict = {}
    band = num_hashes/num_buckets
    for (id_, sig) in signatures:
        sig_list = list(sig)
        for i in xrange(num_buckets):
            bin_str = ''.join([str(bit) for bit in sig_list[i*band:i*band+band]])
            bucket_id = int(bin_str,2)
            print "bucket ",i,":", bucket_id," doc_id",id_

            #TODO: create hash table with key=bucket_id, val=id_
            #  bucket_dict[bucket_id] ... append another value
