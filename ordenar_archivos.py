import os
import shutil

# Variables:
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.py','.ipynb')

# Función que crea las carpetas si no existen
def crear_carpetas():
    '''
    Crea las carpetas Imagenes, Documentos y Programas en el directorio actual si no existen.
    '''
    try:
        os.mkdir("Imagenes")
    except:
        print('Ya existe la carpeta Imagenes.')
    try:
        os.mkdir("Documentos")
    except:
        print('Ya existe la carpeta Documentos.')
    try:
        os.mkdir("Programas")
    except:
        print('Ya existe la carpeta Programas.')

# Función que mueve los archivos
def separador_archivos(doc_types:tuple, img_types:tuple, software_types:tuple, carpeta:str):
    '''
    Función que separa archivos en una carpeta en función de la extensión de los archivos
    
    doc_types (tuple): Tupla de extensiones de documentos
    img_types (tuple): Tupla de extensiones de imágenes
    software_types (tuple): Tupla de extensiones de programas
    carpeta (str): Carpeta donde se encuentran los archivos

    Crea tres carpetas y mueve los archivos a la carpeta Documentos, Imagenes o Programas según la extensión.

    '''
    # En este bloque el programa comprueba que el parámetro carpeta es correcto. Debe ser el nombre de la carpeta existente en el mismo lugar que el script.
    # Si hay un error, se sale de la función devolviendo un False.
    carpeta_actual = os.getcwd()
    try:
        os.chdir(carpeta_actual + carpeta)
    except:
        print('La carpeta no es correcta')
        return False

    # Si el nombre de la carpeta es correcto, se crean las carpetas
    crear_carpetas()

    # Se intentan mover los documentos a las carpetas correspondientes. Si hay algún error, como que el documento ya exista dentro de la carpeta de destino, el programa
    # avisa y pasa al siguiente archivo.
    for i in os.listdir(os.getcwd()):
        if i.endswith(doc_types):
            print("Es un documento")
            try:
                shutil.move(i, "Documentos")
            except:
                print('No se ha podido mover el documento.')
        elif i.endswith(img_types):
            print("Es una imagen")
            try:
                shutil.move(i, "Imagenes")
            except:
                print('No se ha podido mover el documento.')
        elif i.endswith(software_types):
            print("Es un programa")
            try:
                shutil.move(i, "Programas")
            except:
                print('No se ha podido mover el documento.')
        else:
            print('Es otra cosa y paso, míralo tú.')

    # Volvemos a la carpeta previa. Esto es sobre todo para hacer pruebas y no tener que reiniciar todo el rato
    os.chdir(carpeta_actual)
    
    return True

if __name__ == '__main__':
    separador_archivos(doc_types, img_types, software_types, "/carpeta_practica/")