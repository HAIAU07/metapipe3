import maya.cmds as cmds
import os
import os.path as ospathe
from os import environ
from sys import path as syspath
from sys import platform
import sys

import logging
import maya.OpenMaya as om
from maya import cmds
    
from os import environ, makedirs
from os import path as ospath

import BuildBodyFree
import dna_viewer

maya_version = int(cmds.about(version=True))
if maya_version == 2023:
    if sys.version_info < (3, 9, 7):
        raise ValueError("Python 3.9.7 or above is required. Please download correct Python Version!")
if maya_version == 2022:
    if sys.version_info < (3, 7, 0):
        raise ValueError("Python 3.9.7 or above is required. Please download correct Python Version!")

auto_keyframe_toggle = cmds.autoKeyframe(q=True, state=True)

if auto_keyframe_toggle:
    raise ValueError("Auto Keyframe Toggle is On! Turn it of and try again.")

def OpenDNA(ROOT_DIR):
    calib_check = f"{ROOT_DIR}/dna_calibration.mod"
    if not os.path.isfile(calib_check):
        raise ValueError("Please download Epic Games Dna Calibration 1.1.0 Version. Files not found!")
    metapipe_vcheck = f"{ROOT_DIR}/Metapipe_Free.py"
    if os.path.isfile(metapipe_vcheck):
        raise ValueError("Old Version file found. Please delete Metapipe_Free.py file in your dna_calibration path!")
    root_check = f"{ROOT_DIR}/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py"
    if not os.path.isfile(root_check):
        raise ValueError("Please check ROOT_DIR path for the dna_calibration files! Files are not in ROOT_DIR")
    dna_datas = f"{ROOT_DIR}/examples/datas_dna.py"

    if not os.path.isfile(dna_datas):
        raise ValueError("Please press Update button first")
    import dna_viewer_run_in_maya
    dna_viewer_run_in_maya.dna_viewer.show()  

def codeblock (dnaPath, ROOT_DIR, CHARACTER_NAME):
    output_file_path = os.path.join(f"{ROOT_DIR}/examples", "datas_dna.py")
    # Open the Python file and read the lines
    with open(f"{ROOT_DIR}/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py") as file:
        lines_all = file.readlines()
        lines = lines_all[43:204]
        lineslists = lines_all[211:214]
        linesload = lines_all[214:220] 
        lines2 = lines_all[226:242]   
        defload = ["def load_dna_data():\n"]
        defsave = ["def save_dna_data():\n"]
        lines = [line.replace('f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\\\", "/")','"'+ROOT_DIR+'"') for line in lines]
        lines = [line.replace('f"{DNA_DIR}/{CHARACTER_NAME}.dna"', '"'+dnaPath+'"') for line in lines]
        lines = [line.replace('"Ada"','"'+CHARACTER_NAME+'"') for line in lines]
        linesload = ["    " + line for line in linesload]
        lines2 = ["    " + line for line in lines2]

    code_block = ''.join(lines + lineslists + defload + linesload + defsave + lines2)

    with open(output_file_path, "w") as output_file:
        output_file.write(code_block)

    dnaCalibPath=ROOT_DIR

def update_dna_dir(text_dna, ROOT_DIR):
    character_dna = cmds.textField(text_dna, q=True, text=True)
    CHARACTER_DNA = ospathe.abspath(character_dna)
    CHARACTER_DNA = CHARACTER_DNA.replace("\\", "/")
    CHARACTER_NAME = os.path.basename(CHARACTER_DNA).split(".")[0]
    print(f"New DNA_DIR: {CHARACTER_DNA}")
    print(f"New DNA_Name: {CHARACTER_NAME}")
    codeblock (CHARACTER_DNA, ROOT_DIR, CHARACTER_NAME)
    return CHARACTER_DNA, CHARACTER_NAME

# Create a function that will be called when the button is clicked
def button_callback(text_field, *args):
    path = cmds.textField(text_field, query=True, text=True)
    run_dna_viewer(path, text_field)
    cmds.scriptEditorInfo(suppressWarnings=True, echoAllCommands=False)

def prepare_export():
    
    # Detach spine_04 from head_grp and move it to the top level of the Outliner
    cmds.parent('spine_04', w=True, r=True)
    
    if not cmds.namespace(exists="DHIhead"):
        cmds.namespace(add="DHIhead", parent=":")
        cmds.namespace(set="DHIhead")
        cmds.namespace(set=":")
    
    # Get a list of all the joints in the scene
    joints = cmds.ls(type="joint")
    
    # Add every joint to the "DHIhead" namespace and print a message if it already has the "DHIhead" prefix
    for joint in joints:
        if joint.startswith("DHIhead:"):
            print(joint + " is already in the DHIhead namespace")
        else:
            cmds.rename(joint, "DHIhead:" + joint)
    
    
    print("Ready")

def loadimport(ROOT_DIR):
    dna_datas = f"{ROOT_DIR}/examples/datas_dna.py"

    if not os.path.isfile(dna_datas):
        raise ValueError("Please press Update button first")
    sys.path.append(f"{ROOT_DIR}/examples")
    import datas_dna
    datas_dna.load_dna_data()
    cmds.warning("Loaded Succesfully!")
def saveimport(ROOT_DIR):
    sys.path.append(f"{ROOT_DIR}/examples")
    import datas_dna
    datas_dna.save_dna_data()

dnaPath=""
dnaCalibPath=""
def show_dna_edit_window(dnaPath, ROOT_DIR):
    # Create window
    window_name = "MetaPipe"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name, title=window_name, width=300, height=380, sizeable=False, resizeToFitChildren=True)

    # Create layout
    
    color = (0.164, 0.384, 0) # RGB values for #0077c2
    colorbuttons = (.2, 0.2, 0.2) # RGB values for #0077c2
    layout = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 150)], columnSpacing=[(1,75)], backgroundColor=(0.1, 0.1, 0.1))
    
    cmds.text(label="", height=15)    
    cmds.text(label="METAPIPE DNA CALIB UI 1.2.0", height=20, font="boldLabelFont")
    cmds.text(label="(Free Edition)", height=20, font="boldLabelFont")
    cmds.text(label="", height=15)
    cmds.text(label="Metahuman DNA:",height=20)
    text_dna = cmds.textField(text=dnaPath)
    cmds.text(label="", height=5)
    cmds.button(label="Update", command=lambda x: update_dna_dir(text_dna, ROOT_DIR), backgroundColor=color, height=20)
    cmds.text(label="", height=20)
    cmds.button(label="Open DNA Viewer", command=lambda x: dna_viewer.show(), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)
    cmds.button(label="Load Dna", command=lambda x: loadimport(ROOT_DIR), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)
    cmds.button(label="Save Dna", command=lambda x: saveimport(ROOT_DIR), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)
    cmds.button(label="Prepare to Export", command=lambda x: prepare_export(), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)
    cmds.button(label="Load Body", command=lambda x: BuildBodyFree.build_body(ROOT_DIR), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)
    cmds.button(label="Fix Body", command=lambda x: BuildBodyFree.fixbody(), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)
    cmds.button(label="Connect Body", command=lambda x: BuildBodyFree.connect_body(), backgroundColor=colorbuttons, height=40)
    cmds.text(label="", height=5)

    #cmds.image(image='C:/Arts and Spells/pps.png', w=64, h=64)
    cmds.text(label="ARTS AND SPELLS",height=40, font="boldLabelFont")



    # Show window
    cmds.showWindow()

# Show window
#show_dna_edit_window(dnaPath)
