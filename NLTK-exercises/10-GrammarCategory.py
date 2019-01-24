from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

def main():
    file_path = input("Path to the file to use --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        words = tokenizer.tokenize(f)
        print(pos_tag(words, 'universal'))
        print("\n"*3, "-"*100)
        print(pos_tag(words))

main()