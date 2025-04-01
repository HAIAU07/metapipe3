import os
import shutil
import sys
import tkinter as tk
import webbrowser

if getattr(sys, 'frozen', False):
    # Running in a bundle (PyInstaller)
    source_folder = os.path.dirname(sys.executable)
    source_folder = os.path.join(source_folder, "maya2024")
else:
    # Running in a normal Python environment
    source_folder = os.path.dirname(os.path.abspath(__file__))
source_folder_data = os.path.join(source_folder, "data")
source_folder_icons = os.path.join(source_folder, "Icons")
source_folder_scripts = os.path.join(source_folder, "scripts")
destination_folder = "C:/Arts and Spells/Metapipe Studio 3.0.0"
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

        if file_name == "MetapipeLIC.py":
            if os.path.isfile(destination_folder + "/" + file_name):
                continue
            if os.path.isfile("C:/Arts and Spells/Metapipe Studio 2.4.0/" + file_name):
                source = os.path.join("C:/Arts and Spells/Metapipe Studio 2.4.0", file_name)
            else:
                if os.path.isfile("C:/Arts and Spells/Metapipe Studio 2.3.0/" + file_name):
                    source = os.path.join("C:/Arts and Spells/Metapipe Studio 2.3.0", file_name)
                else:
                    if os.path.isfile("C:/Arts and Spells/Metapipe Studio 2.2.0/" + file_name):
                        source = os.path.join("C:/Arts and Spells/Metapipe Studio 2.2.0", file_name)
                    else:
                        if os.path.isfile("C:/Arts and Spells/Metapipe Studio 2.1.0/" + file_name):
                            source = os.path.join("C:/Arts and Spells/Metapipe Studio 2.1.0", file_name)
                        else:
                            if os.path.isfile("C:/Arts and Spells/Metapipe Studio 2.0.0/" + file_name):
                                source = os.path.join("C:/Arts and Spells/Metapipe Studio 2.0.0", file_name)

        if os.path.isfile(source):  # Check if the item is a file
            try:
                shutil.copy(source, destination)
            except PermissionError as e:
                print(f"Permission error: {e}")
                # Handle the permission error as needed

def open_tutorial(tutLink):
    webbrowser.open(tutLink)  # Replace with your desired YouTube link

def shelfSel():
    from tkinter.filedialog import askdirectory
    import ctypes
    result = ctypes.windll.user32.MessageBoxW(0, "Select 'MAYA SHELF FOLDER' path.", "MAYA SHELF", 1)
    if result == 1:
        shelves_folder = askdirectory(title="Please select 'MAYA SHELF FOLDER' path.")
        if "shelves" in shelves_folder:
            if os.path.exists(shelves_folder):
                shutil.copy(os.path.join(source_folder, "shelf_Metapipe3.mel"), shelves_folder)
        else:
            print("ERROR: Maya folder is not in Default Place. Please find shelf folder of Maya and copy and paste 'shelf_Metapipe3' file manually.")
            sys.exit()
    else:
        print("ERROR: Maya folder is not in Default Place. Please find shelf folder of Maya and copy and paste 'shelf_Metapipe3' file manually.")

def checkShelf():
    file_name = destination_folder + "/MetapipeLic.py"
    mtpLic = ""
    try:
        with open(file_name, 'r') as file:
            mtpLic = file.read()
            if "CBB5B5-34A5DD-4B33BE-6643B7-67E0B3-98227E" in mtpLic:
                show_lic_messagebox()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def show_custom_messagebox():
    custom_messagebox = tk.Toplevel()
    custom_messagebox.title("Message")
    custom_messagebox.resizable(False, False)
    custom_messagebox.configure(bg="#1e1e1e")

    message = tk.Label(custom_messagebox, text="Maya Shelf Folder not found. Please check the tutorial.", padx=20, pady=20,bg="#1e1e1e", fg = "white")
    message.pack()

    button_frame = tk.Frame(custom_messagebox,bg="#1e1e1e")
    button_frame.pack(pady=10)

    ok_button = tk.Button(button_frame, text="Continue", command=shelfSel, width=12,bg="#1e1e1e", fg = "white")
    ok_button.pack(side=tk.LEFT, padx=5)

    tutorial_button = tk.Button(button_frame, text="Watch Tutorial", command=lambda: open_tutorial("https://youtu.be/KbpJCKy1pRg"), width=12, bg="green", fg = "white")
    tutorial_button.pack(side=tk.LEFT, padx=5)

def show_lic_messagebox():
    custom_messagebox = tk.Toplevel()
    custom_messagebox.title("Message")
    custom_messagebox.resizable(False, False)
    custom_messagebox.configure(bg="#1e1e1e")

    message = tk.Label(custom_messagebox, text="Personal License not found. Please replace your license.", padx=20, pady=20,bg="#1e1e1e", fg = "white")
    message.pack()

    button_frame = tk.Frame(custom_messagebox,bg="#1e1e1e")
    button_frame.pack(pady=10)

    ok_button = tk.Button(button_frame, text="Continue", command=lambda: custom_messagebox.destroy(), width=12,bg="#1e1e1e", fg = "white")
    ok_button.pack(side=tk.LEFT, padx=5)

    tutorial_button = tk.Button(button_frame, text="Watch Tutorial", command=lambda: open_tutorial("https://youtu.be/A8a0DcdduEQ"), width=12, bg="green", fg = "white")
    tutorial_button.pack(side=tk.LEFT, padx=5)

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

    shelfCH = 0
    shelves_folder = os.path.expanduser("~/Documents/maya/2024/prefs/shelves")
    if os.path.exists(shelves_folder):
        shutil.copy(os.path.join(source_folder, "shelf_Metapipe3.mel"), shelves_folder)
        shelfCH = 1

    shelves_folder = os.path.expanduser("~/Documents/maya/2024/zh_CN/prefs/shelves")
    if os.path.exists(shelves_folder):
        shutil.copy(os.path.join(source_folder, "shelf_Metapipe3.mel"), shelves_folder)
        shelfCH = 1
    
    shelves_folder = os.path.expanduser("~/Documents/maya/2024/ja_JP/prefs/shelves")
    if os.path.exists(shelves_folder):
        shutil.copy(os.path.join(source_folder, "shelf_Metapipe3.mel"), shelves_folder)
        shelfCH = 1

    shelves_folder = os.path.expanduser("~/Documents/maya/2024/en_US/prefs/shelves")
    if os.path.exists(shelves_folder):
        shutil.copy(os.path.join(source_folder, "shelf_Metapipe3.mel"), shelves_folder)
        shelfCH = 1

    if shelfCH == 0:
        show_custom_messagebox()
    else:
        checkShelf()
        