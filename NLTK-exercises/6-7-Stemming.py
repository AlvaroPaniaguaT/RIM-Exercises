from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')


def main():
    file_path = input("Path to the file to use --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        
        words = tokenizer.tokenize(f)
        stemmer = PorterStemmer()
        [print(stemmer.stem(word)) for word in words]
        

main()