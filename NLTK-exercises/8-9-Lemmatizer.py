import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def main():
    file_path = input("Path to the file to use --> ")
    stop_words, language = read_input_language()
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        if language == "english":
            lemmatize_english(f, stop_words)
        else:
            lemmatize_spanish(f, stop_words)


def lemmatize_english(content, stop_words):
    words = tokenizer.tokenize(content)
    [print(lemmatizer.lemmatize(word, get_wordnet_pos(word))) for word in words]


def lemmatize_spanish(content, stop_words):
    spanish_dict = create_spanish_dict()
    words = tokenizer.tokenize(content)
    words = remove_stop_words(words, stop_words)
    for word in words:
        if(word in spanish_dict.keys()):
            print(spanish_dict[word])
        else:
            print(word)

def remove_stop_words(words, stop_words):
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

def read_input_language():
    language = input("Enter the language of the file ->  ")
    try:
        stop_words = set(stopwords.words(language))
    except Exception as e:
        print("Language doesn't supported, try again.")
        stop_words = read_input_language()
    
    return stop_words, language

def create_spanish_dict():
    spanish_dict = {}
    spanish_lem = open("../Lemmatizer/lemmatization-es.txt", 'r').read()
    spanish_lem = spanish_lem.split("\n")
    for values in spanish_lem:
        array_vals = values.split("\t")
        spanish_dict[array_vals[1].lower()] = array_vals[0].lower()
    return spanish_dict

main()