import sys
import argparse
import extract_pdf_text

def main():
    #parser para recibir para indicar como se utiliza el script, y solicitar el parámetro: nombre arcchivo
    parser = argparse.ArgumentParser(description='Extrae el texto de un archivo PDF')
    parser.add_argument('file', help='Ruta al archivo PDF a leer')
    args = parser.parse_args()


    # Obtener el nombre del archivo del primer argumento del script
    file_name = args.file

    # Invocar la función extract_text_from_pdf con el nombre del archivo
    text = extract_pdf_text.extract_text_from_pdf(file_name)

    # Imprimir el texto por pantalla
    print(text)

if __name__ == '__main__':
    main()
