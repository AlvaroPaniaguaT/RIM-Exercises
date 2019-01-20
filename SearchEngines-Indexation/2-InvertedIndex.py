class BuildIndex:
    # Se crea el índice conteniendo los ficheros a procesar y el contenido ya procesado.
    def __init__(self, files):
        self.filenames = files
        self.terms_per_file = self.process_files()

    # Se procesa el contenido de los ficheros y se almacenan las palabras procesadas para cada texto.
    def process_files(self):
        terms_to_file = {}
        for file in self.filenames:
            text = open(file, encoding='utf8',mode='r').read()

            for word in text.split():
                if word in terms_to_file.keys():
                    if not file in terms_to_file[word]:
                        terms_to_file[word].append(file)
                else:
                    terms_to_file[word] = []
                    terms_to_file[word].append(file)
        return terms_to_file

class BasicQuery:
    # Se crea la consulta conteniendo el índice
    def __init__(self, index):
        self.index = index
        self.basicIndex = self.index.terms_per_file

    # Se consulta por una palabra en el índice.
    def one_word_query_basic_index(self, word):
        result = []
        for filename in self.basicIndex.keys():
            if word in self.basicIndex[filename]:
                result.append(filename)
        return result

    # Se consulta un texto completo en el índice.
    def free_text_query_basic_index(self, text):
        result = {}
        tokens = text.split()
        for token in tokens:
            # Para cada token se busca en cuales textos aparece.
            result[token] = self.basicIndex[token]
        return result

if __name__  == "__main__":
    filenames = ['./corpus/pg135.txt', './corpus/pg76.txt', './corpus/pg5200.txt'] # Lista de archivos dentro del
    index = BuildIndex(filenames)
    q = BasicQuery(index)
    print(q.free_text_query_basic_index('house'))
    print(q.free_text_query_basic_index("The house was in England"))