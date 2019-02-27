import re, pprint, os, numpy
import nltk
import spacy
import collections
import en_core_web_sm
from bs4 import BeautifulSoup
from sklearn.metrics.cluster import *
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score
from TikaReader import TikaReader
from tikapp import TikaApp
from ProcessText import TextProcessor

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
                                      linkage="average", affinity=distance)
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

def parse_all_docs(list_files, folder):
    Tika_Objects_List = list()

    for filename in list_files:
        print('Parsing', filename)
        path_to_file = folder + '/' + filename
        Tika_Objects_List.append(TikaReader(path_to_file, value=True))

    return Tika_Objects_List

def parse_texts_spaCy(Tika_objects_list):
    # Traducir a inglés todos los textos
    nlp_dict = {
        'es': (spacy.load('es'), spacy.lang.es.stop_words.STOP_WORDS),
        'en': (spacy.load('en'), spacy.lang.en.stop_words.STOP_WORDS),
        'de': (spacy.load('en'), spacy.lang.en.stop_words.STOP_WORDS)
    }
    texts = list()
    for tika_obj in Tika_objects_list:
        text = tika_obj.get_title()
        lang = tika_obj.get_language()
        tuple_nlp = nlp_dict[lang]

        t_processor = TextProcessor(text, tuple_nlp[1])
        texts.append(t_processor.filter_stopwords())
        
        #nlp = nlp_dict[tika_obj.get_language()]
        #doc = nlp(tika_obj.get_title())
        #for ent in doc.ents:
        #    print(ent.text, ent.label_)
    test = cluster_texts(texts,6,'cosine')
    print("test: ", test)
    # Gold Standard
    reference =[0, 4, 2, 2, 2, 3, 2, 2, 2, 1, 0, 0, 3, 3, 1, 2, 3, 0, 1, 1, 1, 1]
    print("reference: ", reference)

    # Evaluation
    print("rand_score: ", adjusted_rand_score(reference,test))


        
    #article = nlp(document)

if __name__ == "__main__":
    folder = "./CorpusHTMLNoticiasPractica1819"

    listing = os.listdir(folder) # List all files in 'folder' directory
    list_of_Tika_objs = parse_all_docs(listing, folder) # Parse with Tika all files and return list of objects

################ spaCy ###################
    parse_texts_spaCy(list_of_Tika_objs)
    raise Exception()
    # Python: The dir() function returns all properties and methods of the specified object, without the values.
    print(dir(article))
    print("***********************")
    print(article)
    print("***********************")
    print('Entities number: ', len(article.ents))


    def print_entities(entities):
        for entity in entities:
            print(entity)


    labels = [x.label_ for x in article.ents]
    # Python: A Counter is a dict subclass for counting hashable objects
    number = collections.Counter(labels)
    print('Entity labels: ', number)

    entities_map = {}
    for key in number.keys():
        entities_map[key] = []

    for entity in article.ents:
        list = entities_map.get(entity.label_)
        list.append(entity)
        entities_map[key] = list

    for key in entities_map.keys():
        print(key, ' ------------------------ ENTITIES ')
        for entity in entities_map.get(key):
            print(entity)
        print()

    print("*******************************")
    # Five most common entities
    print('Five most common entities')
    items = [x.text for x in article.ents]
    print(collections.Counter(items).most_common(5))



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