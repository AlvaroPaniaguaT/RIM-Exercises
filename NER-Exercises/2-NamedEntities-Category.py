import nltk

def main():
    file_path = input("Path to the file to use --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        tokenized_sentence = nltk.word_tokenize(f.read())
        tagged_sentence = nltk.pos_tag(tokenized_sentence)
        named_entity = nltk.ne_chunk(tagged_sentence)
        print(named_entity)
        

main()