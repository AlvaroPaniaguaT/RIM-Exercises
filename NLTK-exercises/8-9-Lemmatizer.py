from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()


def main():
    file_path = input("Path to the file to use --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        words = tokenizer.tokenize(f)
        [print(lemmatizer.lemmatize(word)) for word in words]

main()