from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



class RankingIndex():
    def __init__(self, files, files_content):
        self.filenames = files
        self.files_content = files_content
        self.process_files()
    
    def process_files(self):
        tfidf = TfidfVectorizer(analyzer='word', strip_accents="unicode")
        tfidf_matrix = tfidf.fit_transform(self.files_content)
        similarity = cosine_similarity(tfidf_matrix) # Calculates distance between documents
        self.ranking = self.order_texts(similarity)
    
    def order_texts(self, similarity):
        # Se obtiene la fila completa.
        sim_rows = similarity[0:, -1]
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
                files.append(self.filenames[index_ordering[col]])
        return files

    def get_ranking(self):
        return self.ranking

if __name__  == "__main__":
    terminate = False
    while not terminate:
        print("Enter 'exit()' if you want to terminate.")
        query = input("Enter your query --> ")
        if(query != "exit()"):
            filenames = ['../corpus/pg135.txt', '../corpus/pg76.txt', '../corpus/pg5200.txt'] # File list
            files_content = [ open(filename, 'r').read() for filename in filenames] # Read content of each file
            files_content.append(query) # Add query to the file content list

            ranking = RankingIndex(filenames, files_content)
            print(ranking.get_ranking())
        else:
            terminate = True