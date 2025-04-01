import importlib
import sys
import maya.cmds as cmds
import os
import dat
importlib.reload(dat)
from os import path as ospath
from sys import path as syspath
from sys import platform
from dat import ROOT_DIR
from dat import MAIN_PATH
from dat import MAYA_VERSION
from dat import dnaPath
from dat import body_type

ROOT_LIB_DIR = f"{ROOT_DIR}/lib/Maya{MAYA_VERSION}"
if platform == "win32":
    LIB_DIR = f"{ROOT_LIB_DIR}/windows"
elif platform == "linux":
    LIB_DIR = f"{ROOT_LIB_DIR}/linux"
else:
    raise OSError(
        "OS not supported, please compile dependencies and add value to LIB_DIR"
    )

# Adds directories to path
syspath.insert(0, ROOT_DIR)
sys.path.append(f"{ROOT_DIR}/examples")
syspath.insert(0, LIB_DIR)
sys.path.append(MAIN_PATH)
import MetaPipeFree
import BatchImport
import BuildBody_drv
import Export_FBX
import MetaTrans
import Prepare
importlib.reload(MetaPipeFree)

def studio_load_dna():
    if not cmds.objExists('wpGRP'):
        MetaPipeFree.loadimport(ROOT_DIR)
        def repExtra(repBase, tartar):
            # Define the base mesh and target mesh
            base_mesh = cmds.duplicate(repBase)
            cmds.rename(base_mesh, repBase + "_CS")
            target_mesh = tartar
            cmds.select([repBase + "_CS", target_mesh], r=True)
            cmds.CreateWrap() 

        repExtra('cartilage_lod0_mesh', 'head_lod0_mesh')
        repExtra('saliva_lod0_mesh', 'teeth_lod0_mesh')

        head_mesh = 'head_lod0_mesh'
        eye_meshes = ['eyeRight_lod0_mesh', 'eyeLeft_lod0_mesh']  # Replace with actual eye mesh names

        # Create a group
        group_name = 'wpGRP'
        if not cmds.objExists(group_name):
            cmds.group(em=True, name=group_name)

        # Parent the head mesh and eye meshes to the group
        cmds.parent(head_mesh, eye_meshes, group_name)
        cmds.parent(group_name, "head_lod0_grp")

        repExtra('eyeshell_lod0_mesh', 'wpGRP')
        repExtra('eyeEdge_lod0_mesh', 'head_lod0_mesh')
        repExtra('eyelashes_lod0_mesh', 'head_lod0_mesh')
        cmds.warning("Loaded Succesfully!")
    else:
        cmds.warning("Already Loaded!")
def studio_save_dna(body_type):
    BuildBody_drv.LODS(body_type)
    MetaPipeFree.saveimport(ROOT_DIR)

#DNA Calib File Path
dnaCalibPath=ROOT_DIR
CHARACTER_NAME = os.path.basename(dnaPath).split(".")[0]
MetaPipeFree.codeblock (dnaPath, ROOT_DIR, CHARACTER_NAME)
def show_dna_edit_window():
    studio_window_name = "MetaPipe Studio 2023 1.3.0"
    if cmds.window(studio_window_name, exists = True):
        cmds.deleteUI(studio_window_name)
    cmds.window(studio_window_name, title=studio_window_name, width=350, height=550, sizeable=False, resizeToFitChildren=True)
    
    color = (0.164, 0.384, 0) # RGB Values
    colorbuttons = (.2, .2, .2)
    layout = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1,150)], columnSpacing=[(1,100)], backgroundColor=(0.1,0.1,0.1))
    
    cmds.text(label="", height = 25)
    cmds.text(label="METAPIPE STUDIO 1.3.0", height = 40, font="boldLabelFont")
    cmds.text(label="", height = 15)
    cmds.text(label="Metahuman DNA", height = 20)
    text_dna = cmds.textField(text=dnaPath)
    cmds.text(label="", height = 5)
    cmds.button(label="Update", command=lambda x: MetaPipeFree.update_dna_dir(text_dna, ROOT_DIR), backgroundColor=color, height= 20)
    cmds.text(label="", height = 20)
    cmds.button(label="Open DNA Viewer", command=lambda x: MetaPipeFree.OpenDNA(ROOT_DIR), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Load DNA", command=lambda x: studio_load_dna(), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Batch Import", command=lambda x: BatchImport.FileBatchImport(), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Joint Trns", command=lambda x: MetaTrans.joint_transformation(), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Save Dna", command=lambda x: studio_save_dna(body_type), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Prepare To Export", command=lambda x: MetaPipeFree.prepare_export(), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Build Body", command=lambda x: BuildBody_drv.build_body(ROOT_DIR, body_type), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Material Assign", command=lambda x: Prepare.matSet(), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)
    cmds.button(label="Export", command=lambda x: Export_FBX.export_fbx(dnaCalibPath), backgroundColor=colorbuttons, height= 40)
    cmds.text(label="", height = 5)   
    cmds.text(label="ARTS AND SPELLS", height = 40, font="boldLabelFont")
    
    cmds.showWindow()
    
#show_dna_edit_window()
