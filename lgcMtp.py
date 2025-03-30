import re
import os

from maya2023 import studioInstaller23
from metapipeFree import freeInstaller

studioInstaller23.run()
freeInstaller.run()

file_path = "c:/Arts and Spells/Scripts/dat.py"
MAIN = "C:/Arts and Spells/Metapipe Studio 2.3.0"
# Open the file in read mode
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use a regular expression to replace MAIN_PATH assignment
    pattern = re.compile(r'MAIN_PATH\s*=\s*"[^"]+"')
    content = pattern.sub('MAIN_PATH = "' + MAIN + '"', content)

    # Open the file in write mode and save the modified content
    with open(file_path, 'w') as file:
        file.write(content)

    print("Variable MAIN_PATH updated successfully.")