from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer, SnowballStemmer

class TextProcessor():
    # Se obtienen las stopwords del inglés y se crea un lematizador.
    def __init__(self, text, lang):
        self.text = text  # Remove commas and not alphanumeric characters
        self.lang = lang
        self.stop = self.load_stopwords()
        self.lemmatizer = WordNetLemmatizer()

    def load_stopwords(self):
        if self.lang == 'es':
            stop = set(stopwords.words('spanish'))
        else:
            stop = set(stopwords.words('english'))
        return stop

    def tokenize(self, text):
        tokens = RegexpTokenizer(r'\w+').tokenize(text)
        return tokens

    # Filter non meaningful words
    def filter_stopwords(self, tokens):
        clean_tokens = []
        for token in tokens:
            if (token not in self.stop) and (token != '“'):
                clean_tokens.append(token)

        #freq = nltk.FreqDist(clean_tokens)
        #freq.plot(40, cumulative=False)
        return clean_tokens

    def stem(self, words):
        if self.lang == 'es':
            sball_stemmer = SnowballStemmer(language='spanish')
            tokens = [sball_stemmer.stem(word) for word in words]
        else:
            stemmer = PorterStemmer()
            tokens = [stemmer.stem(word) for word in words]
        return tokens

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
                pos = self.wordnet_value(token)
                if pos != '':
                    result.append(self.lemmatizer.lemmatize(str(token), pos=pos))
        return result

    # Se procesa un texto completo, eliminando stopwords, símbolos de puntuación, y retornando una lista de tokens
    # lematizados en minúsculas.
    def process_text(self):
        tokens = self.tokenize(self.text)
        #tokens = self.stem(tokens)
        tokens = self.filter_stopwords(tokens)
        #tokens = self.lemmatize(tokens)
        return list(set(tokens))