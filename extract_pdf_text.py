import PyPDF2

def extract_text_from_pdf(file_path):
    # Abrir el archivo PDF
    with open(file_path, 'rb') as f:
        # Crear un objeto PDFReader para leer el archivo
        # Utiliza PdfReader en lugar de PdfFileReader
        pdf_reader = PyPDF2.PdfReader(f)

        # Inicializar una variable para almacenar el texto extraído
        text = ''

        # Recorrer todas las páginas del archivo PDF
        # utiliza len(pdf_reader.pages), ya que  reader.numPages está deprecado.
        for page in range(len(pdf_reader.pages)):
            # Extraer el texto de la página actual
            # Utiliza reader.pages[page_number] en lugar de reader.getPage(pageNumber)
            page_text = pdf_reader.pages[page].extract_text()
            # Añadir el texto a la variable
            text += page_text

        # Devolver el texto extraído
        return text
