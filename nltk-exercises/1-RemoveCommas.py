from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

def main():
    # Remove commas from input text file
    file = input('Path to the file to use  ->  ')
    with open(file, 'r', encoding="utf-8") as f:
        f = f.read()
        print(tokenizer.tokenize(f))

main()