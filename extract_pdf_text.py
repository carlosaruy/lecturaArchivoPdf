import PyPDF2

def extract_text_from_pdf(file_path):
    # Abrir el archivo PDF
    with open(file_path, 'rb') as f:
        # Crear un objeto PDFReader para leer el archivo
        pdf_reader = PyPDF2.PdfFileReader(f)

        # Inicializar una variable para almacenar el texto extraído
        text = ''

        # Recorrer todas las páginas del archivo PDF
        for page in range(pdf_reader.numPages):
            # Extraer el texto de la página actual
            page_text = pdf_reader.getPage(page).extractText()
            # Añadir el texto a la variable
            text += page_text

        # Devolver el texto extraído
        return text
