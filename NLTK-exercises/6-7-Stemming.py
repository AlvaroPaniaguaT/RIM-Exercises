from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')


def main():
    file_path = input("Path to the file to use --> ")
    lang = input("Language --> ")

    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        words = tokenizer.tokenize(f)

        if lang == "english":
            process_english(words)
        elif lang == 'spanish':
            process_spanish(words)

def process_spanish(words):
    sball_stemmer = SnowballStemmer(language='spanish')
    [print(word, sball_stemmer.stem(word)) for word in words]

def process_english(words):
    stemmer = PorterStemmer()
    [print(word, stemmer.stem(word)) for word in words]

main()