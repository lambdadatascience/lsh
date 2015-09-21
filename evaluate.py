import scipy.spatial.distance as distance

def distance_metric(vector1, vector2):
    """ Returns a score value using Jaccard distance

    Args:
        vector1 (np.array): first vector with minHash values
        vector2 (np.array): second vector with minHash values

    Returns:
        float: Jaccard similarity
    """
    return distance.pdist(np.array([vector1,vector2]), 'jaccard').sum()

#TODO: test large sets of text files and return their similarity scores
def runTest():
    # TODO: generate a vector of minhash values for each document
    # TODO: score documents based on their similarity matrix, e.g.
    #  given a document A find 20 sorted documents with highest scores,
    #  i.e. being most similar content-wise
    pass
