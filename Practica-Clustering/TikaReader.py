# Librería de Tika para Python.
from tikapp import TikaApp

class TikaReader:
    # Iniciador de la clase.
    def __init__(self,file_process, value=False):
        # Cliente Tika que utiliza que carga el fichero jar cliente.
        self.tika_client = TikaApp(file_jar="tika-app-1.20.jar")
        self.file_process = file_process
        self.parsed_file = self.tika_client.extract_all_content(self.file_process,convert_to_obj=value)[0]
        self.language = self.tika_client.detect_language(self.file_process)
    
    # Detector del tipo de contenido MIME.
    def get_document_type(self):
        return self.parsed_file['Content-Type']

    # Detector de lenguaje utilizado en el documento.
    def get_language(self):
        return self.language

    # Extractor del contenido completo del documento.
    def get_complete_info(self):
        return self.parsed_file

    # Extractor de solo el contenido del documento.
    def get_content(self):
        return self.parsed_file['X-TIKA:content']

    def get_title(self):
        return self.parsed_file['title']

    def get_description(self):
        return self.parsed_file['og:description']
    
    def get_keywords(self):
        return self.parsed_file['keywords']