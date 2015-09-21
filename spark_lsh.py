import argparse
import os.path
import functools
import numpy as np
from pyspark.mllib.linalg import SparseVector
from pyspark import SparkContext, SparkConf

import text_helpers

#TODO: implement
def getHashFunctions(n=200):
    """ generates n number of hash functions
    """
    pass

#TODO: implement
def getStopWords():
    """ returns a list of stop words
    """
    #TODO: use NLTK to get a list of stopwords
    pass

#TODO: implement
def minHash(text, hash):
    """ Returns min hash value of all hashes for a given text

    Args:
        data (RDD)
        hash (function)

    Returns:
        int: min hash value for entire data set
    """
    pass

def run(fileName, n_hashes, n_buckets):
    """ Starts the main LSH process.

    Args:
        data (RDD): RDD of lines of text
        hashes (list): a list of hash values
        n_buckets (int): number of buckets to use

    Returns:
        Vector: buckets of minhash values
    """
    sc = SparkContext(conf = SparkConf())
    hashes = sc.broacast(getHashFunctions(n_hashes))
    stopWords = sc.broadcast(getStopWords())

    text = sc.textFile(fileName)
    stopWords = sc.parallelize(stopWords)
    cleanData = text.map(removePunctuation).subtract(stopWords).cache()

    #TODO: convert to n-grams
    #TODO: get min-hash values -> total of n_hashes runs. Implement using a
    #       partial function from functools
    #TODO: return a vector representing buckets of minhash values

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Spark LSH',
        epilog = 'LSH', add_help = 'How to use',
        prog = 'python spark-driver.py <arguments>')
    parser.add_argument("-i", "--input", required = True,
        help = "Input directory of text files.")

    # Optional parameters.
    parser.add_argument("-h", "--hashes", type = int, default = 200,
        help = "Number of hash functions to use. [DEFAULT: 200]")
    parser.add_argument("-b", "--buckets", type = int, default = 1000,
        help = "Number of buckets to use. [DEFAULT: 1000]")

    args = vars(parser.parse_args())
    n_hashes,n_buckets = args['hashes'], args['buckets']

    baseDir = os.path.join(args['input'])
    inputPath = os.path.join('<path/to/document>')
    fileName = os.path.join(baseDir, inputPath)

    lsh.run(fileName, n_hashes, n_buckets)
