import os

ruta = input("seleccione ruta: ")

#cambiamos la ruta
os.chdir(ruta)
#generamos un txt con el tree_completo
os.system("tree /F > files_dir.txt")