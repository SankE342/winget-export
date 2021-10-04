# %%

from os     import system as cmd
from json   import loads

# %%

Dir = input('''
Enter directory to save files to (Example: D:/Folder1/Folder2/)
To use current directory, leave blank
'''
)
if (Dir == ''): Dir = './'
File = 'winget_packages.json'   # JSON export of all packages
Exec = 'package_installer.bat' # Batch output

# %%

cmd(f'winget export {Dir + File}') # Exporting packages to a JSON file
print()

# %%

# Loading JSON file to Python and creating a list of packages
with open(Dir + File, 'r') as hdlFile:
    dctFile = loads(hdlFile.read())

lstPackages = [ package['PackageIdentifier'] for package in dctFile['Sources'][0]['Packages'] ]

# %%

# Building the Batch script
with open(Dir + Exec, 'w') as hdlExec:
    for package in lstPackages:
        hdlExec.write(f'winget install -s winget -e --id --force {package}\n')
        print(f'Package id: {package}')

input(f'\nTask completed succesfully. To install the packages in the new PC/OS, run "{Exec}"\nPress any key to finish')
