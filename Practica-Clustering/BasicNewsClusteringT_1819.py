import re, os, numpy
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
from lxml import html
from newspaper import Article
from textblob import TextBlob

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

def parse_texts_spaCy(list_articles):
    # Traducir a inglés todos los textos
    nlp_dict = {
        'es': spacy.load('es_core_news_md'),
        'en': spacy.load('en_core_web_md'),
        'de': spacy.load('en_core_web_md')
    }

    texts = list()
    for article_item in list_articles:
        title = article_item['article'].text
        text = article_item['article'].text.replace('\n', ' ')
        # Translate all texts to english
        translated = translate_to('en', text)
        lang = article_item['lang']

        # Process text = tokenize text removing punctuaction and remove stopwords
        t_processor = TextProcessor(translated, 'en')
        tokens = t_processor.process_text()

        nlp = nlp_dict['en']
        doc = nlp(text)


        ents = filter_ner(doc)
        tokens.extend(ents)
        tokens.extend(ents)

        texts.append(nltk.Text(tokens))

    get_evaluation(texts)

def translate_to(lang, text):
    text_blob = TextBlob(text)
    detected_lang = text_blob.detect_language()
    if detected_lang != lang:
        translated_text = text_blob.translate(to=lang)
        return str(translated_text)
    else:
        return text

def filter_ner(article):
    # Filter named entities to only the one in the list
    mantain_ners = ['LOC', 'ORG', 'PER']
    ents = list()
    for ent in article.ents:
        if ent.label_ in mantain_ners:
            ents.append(ent.text)

    return list(set(ents))

def get_entities(article):
    # Get all entities in a list
    labels = [x.text for x in article.ents]

    return labels

def get_evaluation(texts):

    test = cluster_texts(texts, 6, 'cosine')
    print("test: ", test)

    # Gold Standard reference
    reference =[0, 4, 2, 2, 2, 3, 2, 2, 2, 1, 0, 0, 3, 3, 1, 2, 3, 0, 1, 1, 5, 6]
    r = '[0 4 2 2 2 3 2 2 2 1 0 0 3 3 1 2 3 0 1 1 5 6]'
    print("ref : ", r)

    # Evaluation
    print("rand_score: ", adjusted_rand_score(reference,test))


def extract_content(html_string):
    xpaths = ['//article//p//text()', '//section//p//text()']
    tree = html.fromstring(html_string)
    text = ""
    for xp in xpaths:
        for item in tree.xpath(xp):
            text += ' ' + item
        if len(text) > 0:
            break
    
    return text
        

def read_file(filepath):
    try:
        f =  open(filepath, encoding="utf-8").read()
    except Exception as e:
        f =  open(filepath, encoding='latin-1').read()
    
    return f


def read_news_content(list_files, folder):
    list_of_articles = list()
    for item_file in list_files:
        print("Parsing file --> " + item_file)
        full_path = folder + '/' + item_file
        tika_obj = TikaReader(full_path)
        new_article = Article(full_path)
        content = read_file(full_path)
        new_article.set_html(content)
        new_article.parse()

        # If text not parsed automatically test with two XPATHS selectors
        if len(new_article.text) == 0:
            content = extract_content(new_article.html)
            new_article.set_text(content)
            
        list_of_articles.append({
            'article': new_article,
            'lang': tika_obj.get_language()
        })
    
    return list_of_articles



if __name__ == "__main__":
    folder = "./CorpusHTMLNoticiasPractica1819"

    # List all files in 'folder' directory
    listing = os.listdir(folder)
    listing.sort()
    # Parse all news and return a list of <Article> objects with methods like 'title' , 'content' , etc.
    articles_list = read_news_content(listing, folder)

    parse_texts_spaCy(articles_list)