# %%

from os     import system as cmd
from json   import loads

# %%

Dir = input('''
Enter directory to save files to (Example: D:/Folder1/Folder2/)
To use current directory, leave blank:
'''
)
if (Dir == ''): Dir = './'
elif (Dir[-1] != '/'): Dir += '/'
File = 'winget_packages.json'   # JSON export of all packages
Exec = 'package_installer.bat'  # Batch output

# %%

print('Exporting list of installed programs as a JSON file')
cmd(f'winget export \"{Dir + File}\"')
print()

# %%

print('Loading JSON file to Python and creating a list of packages')
with open(Dir + File, 'r') as hdlFile:
    dctFile = loads(hdlFile.read())

lstPackages = [ package['PackageIdentifier'] for package in dctFile['Sources'][0]['Packages'] ]
print()

# %%

# Building the Batch script
print('Exported programs available through winget')
with open(Dir + Exec, 'w') as hdlExec:
    for package in lstPackages:
        hdlExec.write(f'winget install -s winget -e --id --force {package}\n')
        print(f'Package id: {package}')
print()

input(f'Task completed succesfully. To install the packages in the new PC/OS, transfer and run "{Exec}"\nPress ENTER to finish')
