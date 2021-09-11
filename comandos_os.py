import os

def tree_dir_files(ruta, ruta_salida_txt):
    '''
    Esta funcion saca en texto los files de un directorio en formato txt
    '''
    #cambiamos la ruta
    os.chdir(ruta)
    #generamos un txt con el tree_completo
    os.system(f'tree /F > {ruta_salida_txt}\\files_dir.txt')

if __name__ == '__main__':
    tree_dir_files('C:\\Users\\pgome\\Documents\\files_dir_excel\\SGS_SCC- Ensayos Geomecánicos Montonero','C:\\Users\\pgome\\Documents\\files_dir_excel')
