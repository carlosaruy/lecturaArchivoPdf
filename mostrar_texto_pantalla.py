import sys
import extract_pdf_text

def main():
    # Obtener el nombre del archivo del primer argumento del script
    file_name = sys.argv[1]

    # Invocar la función extract_text_from_pdf con el nombre del archivo
    text = extract_text.extract_text_from_pdf(file_name)

    # Imprimir el texto por pantalla
    print(text)

if __name__ == '__main__':
    main()
