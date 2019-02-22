import spacy
import os

path = "../Textos/"
list_files = os.listdir(path)

def main():
    for index, filename in enumerate(list_files):
        print(index, filename)
    fileindex = input("Selecciona el numero del fichero de entrada: ")
    filepath = list_files[int(fileindex)]
    lang = input("Introduce el idioma (Español -> es // Ingles -> en) --> ")
    nlp = spacy.load(lang)
    text = open(path+filepath, 'r', encoding="utf-8")
    doc = nlp(text.read())
    print("\nEntidad nombrada --> Tipo de la entidad nombrada")
    dict_types = {"Num": 0}
    dict_ne = {}
    for ent in doc.ents:
        if (ent.label_ != ""):
            dict_types['Num'] += 1
            print("%s --> %s" % (ent, ent.label_))
            if ent.label_ in dict_types:
                dict_types[ent.label_] += 1
                dict_ne[ent.text] = (dict_ne[ent.text] + 1) if (ent.text in dict_ne.keys()) else 1
            else:
                dict_types[ent.label_] = 1

    print(dict_ne)
    print(dict_types)
main()