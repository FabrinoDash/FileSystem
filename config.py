from pathlib import Path
import termcolor
path = Path('.')

# SHOWING ALL DIRECTORIES IN CURRENT FOLDER
print(termcolor.colored("SHOWING ALL DIRECTORIES IN CURRENT FOLDER",color="blue"))
for instance in path.iterdir():
    if instance.is_dir():
        print(termcolor.colored(instance,color="green"))

# LISTING PYTHON SOURCE FILES THAT END WITH .py
print(termcolor.colored("\nLISTING PYTHON SOURCE FILES THAT END WITH .py",color="blue"))
pythonFiles = list(path.glob('**/*.py'))
for pythonFile in pythonFiles:
    print(termcolor.colored(pythonFile,color="green"))

# NAVIGATING INSIDE DIRECTORY
print(termcolor.colored("\nNAVIGATING INSIDE DIRECTORY",color="blue"))
newPath = Path('./projects/')
combined = newPath / 'inside' / 'test.txt'

print(termcolor.colored(f"Only folder: {newPath}",color="green"))
print(termcolor.colored(f"File Inside: {combined}",color="green"))

# DISPLAYING ABSOLUTE POSITION
print(termcolor.colored("\nDISPLAYING ABSOLUTE PATH #uncommentLineBelow",color="blue"))
# print(termcolor.colored(f"{combined.resolve()}",color="green")) #uncomment this to get absolute path
# print(termcolor.colored(f"{combined.absolute()}",color="green")) #uncomment this to get absolute path

# QUERYING PATH PROPERTIES
print(termcolor.colored("\nQUERYING PATH PROPERTIES",color="blue"))
print(termcolor.colored(f"./projects Exists: {newPath.exists()}",color="green"))
print(termcolor.colored(f"./projects is_file: {newPath.is_file()}",color="green"))
print(termcolor.colored(f"./projects is folder: {newPath.is_dir()}",color="green"))

# opening files
print(termcolor.colored("\nOPENING FILES",color="blue"))
f = combined.open()
fileContent = f.readlines()
for line in fileContent:
    print(termcolor.colored(line,color="green",on_color="on_grey"))
