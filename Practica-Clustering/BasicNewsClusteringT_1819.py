import re, pprint, os, numpy
import nltk
from bs4 import BeautifulSoup
from sklearn.metrics.cluster import *
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score
from TikaReader import TikaReader
from pprint import pprint

def cluster_texts(texts, clustersNumber, distance):
    #Load the list of texts into a TextCollection object.
    collection = nltk.TextCollection(texts)
    print("Created a collection of", len(collection), "terms.")

    #get a list of unique terms
    unique_terms = list(set(collection))
    print("Unique terms found: ", len(unique_terms))

    ### And here we actually call the function and create our array of vectors.
    vectors = [numpy.array(TF(f,unique_terms, collection)) for f in texts]
    print("Vectors created.")

    # initialize the clusterer
    clusterer = AgglomerativeClustering(n_clusters=clustersNumber,
                                      linkage="average", affinity=distanceFunction)
    clusters = clusterer.fit_predict(vectors)

    return clusters

# Function to create a TF vector for one document. For each of
# our unique words, we have a feature which is the tf for that word
# in the current document
def TF(document, unique_terms, collection):
    word_tf = []
    for word in unique_terms:
        word_tf.append(collection.tf(word, document))
    return word_tf


if __name__ == "__main__":
    folder = "./CorpusHTMLNoticiasPractica1819"
    # Empty list to hold text documents.
    texts = []

    listing = os.listdir(folder)
    
    tika_reader = TikaReader(folder + '/' + listing[0])

    pprint(tika_reader.extract_complete_info(True)[0])
    
    #print("Prepared ", len(texts), " documents...")
    #print("They can be accessed using texts[0] - texts[" + str(len(texts)-1) + "]")
#
    #distanceFunction ="cosine"
    ##distanceFunction = "euclidean"
    #test = cluster_texts(texts,4,distanceFunction)
    #print("test: ", test)
    ## Gold Standard
    #reference =[0, 4, 2, 2, 2, 3, 2, 2, 2, 1, 0, 0, 3, 3, 1, 2, 3, 0, 1, 1, 1, 1]
    #print("reference: ", reference)
#
    ## Evaluation
    #print("rand_score: ", adjusted_rand_score(reference,test))