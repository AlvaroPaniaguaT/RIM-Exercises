from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

tokenizer = RegexpTokenizer(r'\w+')

def main():
    # Remove commas from input text file
    file = input('Path to the file to use  ->  ')
    with open(file, 'r', encoding="utf-8") as f:
        f = f.read()
        words = f.split()
        print("Top 5 repeated words without remove commas --> ", word_frecuency(words))
        
        words = tokenizer.tokenize(f)
        print("Top 5 repeated words after remove commas --> ", word_frecuency(words))

def word_frecuency(words):
    fdist = FreqDist(words)
    return fdist.most_common(5)


main()