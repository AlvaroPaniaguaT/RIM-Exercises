import nltk
from nltk.tag import StanfordPOSTagger, StanfordNERTagger


jar = './stanford-ner-2018-10-16/stanford-ner.jar'
model_1 = './spanish.ancora.distsim.s512.prop' # No funciona
model_2 = './spanish.ancora.distsim.s512.crf.ser.gz' # Funciona pero el output no parece correcto.

english_model = './stanford-ner-2018-10-16/classifiers/english.muc.7class.distsim.crf.ser.gz'
def main():
    file_path = input("Path to the file to use --> ")
    lang = input("Language for the tagger (spanish and english supported) --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()
        words = f.split()
        if lang == "spanish":
            st = StanfordNERTagger(model_2, path_to_jar=jar, encoding='utf-8')
            st.java_options='-mx4096m'
        elif lang == 'english':
            st = StanfordNERTagger(english_model, path_to_jar=jar, encoding='utf-8')
            st.java_options='-mx4096m'

        for tags in st.tag(words):
            print(tags)

main()