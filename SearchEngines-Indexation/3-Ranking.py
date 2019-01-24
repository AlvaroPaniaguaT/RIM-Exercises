from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



class RankingIndex():
    def __init__(self, files):
        self.filenames = files
        self.files_content = [ open(filename, 'r').read() for filename in filenames] # Read content of each file
        self.tfidf = TfidfVectorizer(analyzer='word', strip_accents="unicode")
    
    def process_files(self, query):
        self.files_content.append(query)
        tfidf_matrix = self.tfidf.fit_transform(self.files_content)
        similarity = cosine_similarity(tfidf_matrix) # Calculates distance between documents
        return similarity

class RankingQuery():
    def __init__(self, query, ranking_index):
        self.ranking_index = ranking_index
        self.query = query
        self.similarity = self.ranking_index.process_files(query)

    def get_most_similar_texts(self):
        # Se obtiene la fila completa.
        sim_rows = self.similarity[0:, -1]
        index_ordering = {}
        for i in range(0, len(sim_rows)):
            # Se guarda cada valor para no perderlo al ordenar
            index_ordering[sim_rows[i]] = i
        # Se ordena la lista
        sim_cols_ordered = sorted(sim_rows, reverse=True)
        files = []
        for col in sim_cols_ordered:
            # Se recuperan los nombres de los ficheros originales salvo el propio (tiene similaridad 1 consigo mismo).
            if col < 1:
                files.append(self.ranking_index.filenames[index_ordering[col]])
        return files

if __name__  == "__main__":
    terminate = False
    while not terminate:
        print("Enter 'exit()' if you want to terminate.")
        query = input("Enter your query --> ")
        if(query != "exit()"):
            filenames = ['../corpus/pg135.txt', '../corpus/pg76.txt', '../corpus/pg5200.txt'] # File list
            ranking = RankingIndex(filenames)
            r_query = RankingQuery(query, ranking)
            print(r_query.get_most_similar_texts())
        else:
            terminate = True