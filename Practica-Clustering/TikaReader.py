# Librería de Tika para Python.
from tikapp import TikaApp

class TikaReader:
    # Iniciador de la clase.
    def __init__(self,file_process):
        # Cliente Tika que utiliza que carga el fichero jar cliente.
        self.tika_client = TikaApp(file_jar="tika-app-1.20.jar")
        self.file_process = file_process

    # Detector del tipo de contenido MIME.
    def detect_document_type(self):
        return self.tika_client.detect_content_type(self.file_process)

    # Detector de lenguaje utilizado en el documento.
    def detect_language(self):
        return self.tika_client.detect_language(self.file_process)

    # Extractor del contenido completo del documento.
    def extract_complete_info(self,value=False):
        return self.tika_client.extract_all_content(self.file_process,convert_to_obj=value)

    # Extractor de solo el contenido del documento.
    def extract_content_info(self):
        return self.tika_client.extract_only_content(self.file_process)