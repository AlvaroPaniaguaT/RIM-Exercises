from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')

def main():
    # Remove commas from input text file
    file = input('Path to the file to use  ->  ')
    stop_words = read_input_language()

    with open(file, 'r', encoding="utf-8") as f:
        f = f.read()
        phrases = f.split('.')

        for phrase in phrases:
            remove_stop_words(phrase, stop_words)

def remove_stop_words(phrase, stop_words):
    filtered_words = [word for word in phrase.split() if word not in stop_words]
    print(filtered_words)

def read_input_language():
    language = input("Enter the language of the file ->  ")
    try:
        stop_words = set(stopwords.words(language))
    except Exception as e:
        print("Language doesn't supported, try again.")
        stop_words = read_input_language()
    
    return stop_words

main()