import os
import shutil

source_folder = os.path.dirname(os.path.abspath(__file__))
source_folder_data = os.path.join(source_folder, "data")
source_folder_icons = os.path.join(source_folder, "Icons")
source_folder_scripts = os.path.join(source_folder, "scripts")
destination_folder = "C:/Arts and Spells/Metapipe Free 3.0.0"
destination_folder_data = destination_folder + "/data"
destination_folder_icons = destination_folder + "/Icons"
destination_folder_scripts = "C:/Arts and Spells/Scripts"
def move_files(source_folder, destination_folder):
    files = os.listdir(source_folder)
    os.makedirs(destination_folder, exist_ok=True)
    os.makedirs(destination_folder_scripts, exist_ok=True)

    for file_name in files:
        source = os.path.join(source_folder, file_name)
        destination = os.path.join(destination_folder, file_name)

        if os.path.isfile(source):  # Check if the item is a file
            try:
                shutil.copy(source, destination)
            except PermissionError as e:
                print(f"Permission error: {e}")
                # Handle the permission error as needed

def run():
    if not source_folder == destination_folder:
        try:
            os.makedirs(destination_folder, exist_ok=True)
            move_files(source_folder, destination_folder)
            move_files(source_folder_data, destination_folder_data)
            move_files(source_folder_icons, destination_folder_icons)
            move_files(source_folder_scripts, destination_folder_scripts)
            print("Installation completed successfully.")
        except Exception as e:
            print(f"An Error occurred: {e}")
    else:
        print("Installation already completed.")

    shelves_folder = os.path.expanduser("~/Documents/maya/2024/prefs/shelves")
    if os.path.exists(shelves_folder):
        shutil.copy(os.path.join(source_folder, "shelf_MetapipeFree.mel"), shelves_folder)
    else:
        print("ERROR: Maya folder is not in Default Place. Please copy and paste 'shelf_Metapipe2' file manually.")
