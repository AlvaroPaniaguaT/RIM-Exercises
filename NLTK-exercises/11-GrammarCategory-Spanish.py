from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.tag import StanfordPOSTagger

tokenizer = RegexpTokenizer(r'\w+')

jar = './stanford-postagger-full-2018-10-16/stanford-postagger.jar'
model = './stanford-postagger-full-2018-10-16/models/spanish-distsim.tagger'

def main():
    file_path = input("Path to the file to use --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        words = tokenizer.tokenize(f)
        st = StanfordPOSTagger(model, path_to_jar=jar, encoding='utf-8')
        print(st.tag(words))
        print("\n"*3, "-"*100)

main()