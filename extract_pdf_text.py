from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.pdfparser import PDFParser

def extract_text_from_pdf(file_path):
    # Abrir el archivo PDF
    with open(file_path, 'rb') as f:
        # Crear un objeto PDFParser utilizando el objeto BufferedReader
        parser = PDFParser(f)
        # Crear un documento PDF utilizando el objeto PDFParser
        document = PDFDocument(parser)
        # Obtener una lista de páginas
        pages = PDFPage.get_pages(f)

        # Crear un PDFResourceManager para gestionar los recursos
        resource_manager = PDFResourceManager()
        # Crear un PDFPageAggregator para procesar el layout del documento
        laparams = LAParams()
        device = PDFPageAggregator(resource_manager, laparams=laparams)

        # Crear un PDFPageInterpreter para procesar cada página
        interpreter = PDFPageInterpreter(resource_manager, device)

        # Inicializar una variable para almacenar el texto extraído
        text = ''

        # Procesar cada página del documento
        for page in pages:
            interpreter.process_page(page)
            # Obtener el layout de la página
            layout = device.get_result()
            # Procesar el layout de la página
            page_text = process_page_layout(layout)
            # Añadir el texto a la variable
            text += page_text

        # Devolver el texto extraído
        return text

def process_page_layout(layout):
    text = ''
    for element in layout:
        # Verificar si el elemento es una caja de texto o una línea de texto
        if isinstance(element, LTTextBox) or isinstance(element, LTTextLine):
            # Extraer el texto del elemento y agregarlo a la variable
            text += element.get_text()
    return text
