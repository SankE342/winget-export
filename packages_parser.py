# INSTRUCCIONES:
# Abrir el archivo "package_export.bat"

# %%

from os     import system as cmd
from json   import loads

# %%

# Dir = input('''
# Escribe el directorio donde guardarás la lista de paquetes (terminado con un /)
# Ejemplo: D:/Varios/Archivos/
# Si quieres guardar en este mismo directorio, solo presiona ENTER
# '''
# )
# if (Dir == ''):

Dir = './'
File = 'winget_packages.json' # Nombre del archivo
Exec = 'packages_installer.bat' # Nombre del ejecutable

# %%

cmd(f'winget export {Dir + File}') # Exportando los packetes instalados a un archivo JSON
print()

# %%

with open(Dir + File, 'r') as hdlFile:
    dctFile = loads(hdlFile.read())

lstPackages = [ package['PackageIdentifier'] for package in dctFile['Sources'][0]['Packages'] ]
print(lstPackages, end='\n\n') # Muestra la lista de paquetes según su id

# %%

# Construye la lista de comandos en un archivo bat ejecutable desde el cmd
with open(Dir + Exec, 'w') as hdlExec:
    for package in lstPackages:
        hdlExec.write(f'winget install -s winget -e --force {package}\n')

input(f'Exportación exitosa. Para instalar los paquetes en el nuevo OS, abrir "{Exec}"\nPresione cualquier tecla para finalizar')
