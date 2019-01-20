from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

d_tokenizer = RegexpTokenizer(r'\bd\w+')
s_tokenizer = RegexpTokenizer(r'\bs\w*[^s\W]')
e_tokenizer = RegexpTokenizer(r'[^e\W]\w*e\b')

def main():
    # Remove commas from input text file
    file = input('Path to the file to use  ->  ')
    with open(file, 'r', encoding="utf-8") as f:
        f = f.read()
        d_words = d_tokenizer.tokenize(f)
        print("List of words that starts with 'd': ", d_words)
        s_words = ' '.join(s_tokenizer.tokenize(f))
        output = e_tokenizer.tokenize(s_words)
        print("List of words starting with 's' character and ending with 'e': ", output)

main()