from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import nltk
import string
from nltk.tokenize import RegexpTokenizer


class TextProcessor():
    # Se obtienen las stopwords del inglés y se crea un lematizador.
    def __init__(self, text, stopwords):
        self.tokens = RegexpTokenizer(r'\w+').tokenize(text)
        self.stop = stopwords
        self.lemmatizer = WordNetLemmatizer()

    # Se filtran las stopwords del texto.
    def filter_stopwords(self):
        clean_tokens = []
        for token in self.tokens:
            if token not in self.stop:
                clean_tokens.append(token)
        return clean_tokens

    # Se eliminan los símbolos de puntuación.
    def remove_punctuation(self,token_list):
        result = []
        for token in token_list:
            punct_removed = ''.join([letter for letter in token[0] if letter in string.ascii_letters])
            if punct_removed != '':
                result.append((punct_removed,token[1]))
        return result

    # Se genera la equivalencia para que el lematizador entienda los tags de la NLTK.
    def wordnet_value(self,value):
        result = ''
        if value.startswith('J'):
            return wordnet.ADJ
        elif value.startswith('V'):
            return wordnet.VERB
        elif value.startswith('N'):
            return wordnet.NOUN
        elif value.startswith('R'):
            return wordnet.ADV
        return result

    # Se realiza la lematización de los tokens conforme a su tag modificado.
    def lemmatize(self,token_list):
        result = []
        for token in token_list:
            if len(token) > 0:
                pos = self.wordnet_value(token[1])
                if pos != '':
                    result.append(self.lemmatizer.lemmatize(str(token[0]).lower(), pos=pos))
        return result

    # Se procesa un texto completo, eliminando stopwords, símbolos de puntuación, y retornando una lista de tokens
    # lematizados en minúsculas.
    def process_text(self,text):
        tokens = nltk.word_tokenize(text)

        tokens = self.filter_stopwords(tokens)
        tokens = self.remove_punctuation(tokens)
        tokens = self.lemmatize(tokens)
        return tokens