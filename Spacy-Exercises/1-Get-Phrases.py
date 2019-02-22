import spacy

# # load the model
nlp = spacy.load('es')

with open('../Textos/NoticiaRobo.txt', 'r', encoding="utf8") as f:
    document = f.read()
f.close()

# Ahora document forma parte de la clase de modelos de spacy y tiene una serie de propiedades como tokens, vocabulario...
document = nlp(document)
print(dir(document))

for sent in document.sents:
     print(sent)