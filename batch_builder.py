from os     import system
from json   import loads


path = input('''
Enter directory to save files to (Example: D:/Folder1/Folder2/)
To use current directory, leave blank:
'''
)

if      path == ''      : path = './'
elif    path[-1] != '/' : path += '/'

file_name = 'winget_packages.json'   # JSON export of all packages
exec_name = 'package_installer.bat'  # Batch output


print('Exporting list of installed programs as a JSON file\n')
system(f'winget export \"{path + file_name}\"')
print()


print('Loading JSON file to Python and creating a list of packages')
with open(path + file_name, 'r') as file_hdl:
    file_dct = loads(file_hdl.read())

packages_lst = [
    package['PackageIdentifier']
    for package in file_dct['Sources'][0]['Packages']
]
print()


# Building the Batch script
print('Exported programs available through winget')
with open(path + exec_name, 'w') as exec_hdl:
    for package in packages_lst:
        exec_hdl.write(f'winget install -s winget -e --id --force {package}\n')
        print(f'Package id: {package}')
print()

input(f'''
Task completed succesfully
To install the packages in the new PC/OS, transfer and run "{exec_name}"
Press ENTER to finish
''')

