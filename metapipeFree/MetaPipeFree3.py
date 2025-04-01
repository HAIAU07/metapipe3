#ALL RIGHTS BELONGS TO UZAY CALISKAN.
#PLEASE CHECK THE FULL LICENSE INSIDE PRODUCT FOLDER (Part of the agreement is below)
#You will not:

# make any copy of the Product except for archival or backup purposes;

# circumvent or disable any access control technology, security device, procedure, protocol, or technological protection mechanism that may be included or established in or as part of the Product;

# hack, reverse engineer, decompile, disassemble, modify or create derivative works of the Product or any part of the Product;

# publish, sell distribute or otherwise make the Product available to others to use, download or copy;

#transfer or sub-license the Product or any rights under this Agreement to any third party, whether voluntarily or by operation of law;

# use the Product for any purpose that may be defamatory, threatening, abusive, harmful or invasive of anyone's privacy, or that may otherwise violate any law or give rise to civil or other liability;

# misrepresent yourself as the creator or owner of the Property;

# remove or modify any proprietary notice, symbol or label in or on the Product;

# directly or indirectly assist, facilitate or encourage any third party to carry on any activity prohibited by this Agreement.

import importlib
import sys
import maya.cmds as cmds
import os
from os import path as ospath
from sys import path as syspath
from sys import platform
maya_version = int(cmds.about(version=True))
#MAYAPLUGINPATH
maya_plugin_path = os.environ.get('MAYA_PLUG_IN_PATH')
new_path = ""
if maya_version == 2022:
    new_path = 'c:/dna_calibration/lib/Maya2022/windows'
if maya_version == 2023:
    new_path = 'c:/dna_calibration/lib/Maya2023/windows'
if maya_version == 2024:
    new_path = 'c:/dna_calibration/lib/Maya2024/windows'
if maya_plugin_path:
    updated_path = maya_plugin_path + os.pathsep + new_path
else:
    updated_path = new_path
os.environ['MAYA_PLUG_IN_PATH'] = updated_path
if maya_version < 2022 or maya_version > 2024:
    raise ValueError("Metapipe only works with MAYA 2022/2023/2024")
ROOT_DIR = "c:/dna_calibration"  
MAIN_PATH = "c:/Arts and Spells/Metapipe Free 3.0.0"
iconPath = MAIN_PATH + "/Icons/"
MAYA_VERSION =  maya_version  
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
syspath.insert(0, LIB_DIR)
sys.path.append(MAIN_PATH)
sys.path.append("c:/Arts and Spells/Scripts")
sys.path.append(ROOT_DIR + "/examples")

#Dna Path
dnaPath= "C:/Users/MONSTER/Documents/Megascans Library/Downloaded/DHI/h344NMUV_asset/1k/asset_source/MetaHumans/CustomDNA/SourceAssets/CustomDNA.dna"  
body_type= "m_med_nrw"
sceneLodN = str(0)
scenebodyLodN = str(0)

CHARACTER_NAME = os.path.basename(dnaPath).split(".")[0]

import time 

import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets, QtGui, QtCore

from os import environ
import logging
import maya.OpenMaya as om
from os import environ, makedirs
#import dna_viewer
cmds.select(clear=True)

if maya_version == 2024:
    if sys.version_info < (3, 10, 8):
        cmds.confirmDialog(title="ERROR", message="Python 3.11.0 or above is required. Please download correct Python Version!")
        raise ValueError("Python 3.11.0 or above is required. Please download correct Python Version!")
if maya_version == 2023:
    if sys.version_info < (3, 9, 7):
        raise ValueError("Python 3.9.7 or above is required. Please download correct Python Version!")
if maya_version == 2022:
    if sys.version_info < (3, 7, 0):
        raise ValueError("Python 3.9.7 or above is required. Please download correct Python Version!")

auto_keyframe_toggle = cmds.autoKeyframe(q=True, state=True)

if auto_keyframe_toggle:
    raise ValueError("Auto Keyframe Toggle is On! Turn it of and try again.")

global selChack
selCheck=0
worldCheck=0
file_path = "c:/Arts and Spells/Scripts/dat.py"
if os.path.exists(file_path):
    import dat
    importlib.reload(dat)
    ROOT_DIR = dat.ROOT_DIR
    MAIN_PATH = dat.MAIN_PATH
    dnaPath = dat.dnaPath
    body_type = dat.body_type

def newScene():
    if cmds.file(query=True, modified=True):
        result = cmds.confirmDialog(
            title="Save Changes?",
            message="Do you want to save changes to the current scene?",
            button=["Save", "Don't Save", "Cancel"],
            defaultButton="Save",
            cancelButton="Cancel",
            dismissString="Cancel")
    
        if result == "Save":
            # Save the current scene
            cmds.file(save=True, force=True)
        elif result == "Don't Save":
            # Discard changes and create a new scene
            cmds.file(new=True, force=True)
    else:
        # No unsaved changes, create a new scene directly
        cmds.file(new=True, force=True)
    if not cmds.objExists("metapipefreewindow"):
        cmds.createNode("transform", name="metapipefreewindow")
    leftPanelButtonV(0) 

def saveScene():
    if cmds.objExists("LoadedDNAInfoNode") or cmds.objExists("rl4Embedded_Archetype") or cmds.objExists ("rl4Embedded_Archtype"):
        saveFileName = "Checkpoint"
    else:
        saveFileName = "Custom Head"
    # Define the file path for the .mb file
    file_path = f"{ROOT_DIR}/data/" + saveFileName + ".mb"

    # Save the current scene as an .mb file
    cmds.file(rename=file_path)
    cmds.file(save=True, type="mayaBinary")

    print(f"Saved as {file_path}")

def loadScene(saveFileName):
    # Define the file path for the .mb file
    file_path = f"{ROOT_DIR}/data/" + saveFileName + ".mb"
    if os.path.isfile(file_path):
        if cmds.file(query=True, modified=True):
            result = cmds.confirmDialog(
                title="Save Changes?",
                message="Do you want to save changes to the current scene?",
                button=["Save", "Don't Save", "Cancel"],
                defaultButton="Save",
                cancelButton="Cancel",
                dismissString="Cancel")
        
            if result == "Save":
                # Save the current scene
                cmds.file(save=True, force=True)
                cmds.file(file_path, force=True, open=True)
            elif result == "Don't Save":
                # Discard changes and create a new scene
                cmds.file(file_path, force=True, open=True)
        else:
            # No unsaved changes, create a new scene directly
            cmds.file(file_path, force=True, open=True)
        
    else:
        cmds.confirmDialog(title="ERROR", message="Couldnt find any [Saved Scene]. You need to Save the scene to use this button.")
        raise ValueError("Couldnt find any [Saved Scene]. You need to Save the scene to use this button.")
    if not cmds.objExists("metapipefreewindow"):
        cmds.createNode("transform", name="metapipefreewindow")
    leftPanelButtonV(0)

def openDNAViewer():

    """calib_check = f"{ROOT_DIR}/dna_calibration.mod"
    if not os.path.isfile(calib_check):
        cmds.confirmDialog(title="ERROR", message="Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")
        raise ValueError("Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")
    calib_check = f"{ROOT_DIR}/data/mh4/additional_assemble_script.py"
    if os.path.isfile(calib_check):
        cmds.confirmDialog(title="ERROR", message="Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")
        raise ValueError("Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")"""
    metapipe_vcheck = f"{ROOT_DIR}/Metapipe_Free.py"
    if os.path.isfile(metapipe_vcheck):
        cmds.confirmDialog(title="ERROR", message="Old Version file found. Please delete Metapipe_Free.py file in your dna_calibration path!")
        raise ValueError("Old Version file found. Please delete Metapipe_Free.py file in your dna_calibration path!")
    root_check = f"{ROOT_DIR}/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py"
    if not os.path.isfile(root_check):
        cmds.confirmDialog(title="ERROR", message="Please check ROOT_DIR path for the dna_calibration files! Files are not in ROOT_DIR")
        raise ValueError("Please check ROOT_DIR path for the dna_calibration files! Files are not in ROOT_DIR")
    dna_datas = f"{ROOT_DIR}/examples/datas_dna.py"

    if not os.path.isfile(dna_datas):
        cmds.confirmDialog(title="ERROR", message="Please save your preferences and try again")
        raise ValueError("Please save your preferences and try again")
    dna_viewer.show() 
    cmds.createNode("transform", name="OpenedDNAInfoNode")  
        
    leftPanelButtonV(1)

def datasBuild(mod):
    from dna_viewer import DNA, RigConfig, build_rig
    file_path = "c:/Arts and Spells/Scripts/dat.py"
    if os.path.exists(file_path):
        import dat
        importlib.reload(dat)
        ROOT_DIR = dat.ROOT_DIR
        MAIN_PATH = dat.MAIN_PATH
        dnaPath = dat.dnaPath
        body_type = dat.body_type
    if mod == "gen":
        DATA_DIR = f"{ROOT_DIR}/data" 
        dna = DNA(dnaPath)
        config = RigConfig(
            gui_path=f"{DATA_DIR}/gui.ma",
            analog_gui_path=f"{DATA_DIR}/analog_gui.ma",
            aas_path=f"{DATA_DIR}/additional_assemble_script.py")
        build_rig(dna=dna, config=config)
        if cmds.objExists("rl4Embedded_Archetype"):
            cmds.delete("rl4Embedded_Archetype")
        if cmds.objExists("rl4Embedded_Archtype"):
            cmds.delete("rl4Embedded_Archtype")
    elif mod=="rigged":
        DATA_DIR = f"{ROOT_DIR}/data" 
        dna = DNA(dnaPath)
        config = RigConfig(
            gui_path=f"{DATA_DIR}/gui.ma",
            analog_gui_path=f"{DATA_DIR}/analog_gui.ma",
            aas_path=f"{DATA_DIR}/additional_assemble_script.py")
        build_rig(dna=dna, config=config)
    elif mod=="":
        #datas_dna.assemble_maya_scene()
        result = cmds.confirmDialog(
                title="Build DNA",
                message="Please choose Build DNA Option.",
                button=["Editable", "Rigged", "Cancel"],
                defaultButton="Editable",
                cancelButton="Cancel",
                dismissString="Cancel")
        
        if result == "Editable":
            DATA_DIR = f"{ROOT_DIR}/data" 
            dna = DNA(dnaPath)
            config = RigConfig(
                gui_path=f"{DATA_DIR}/gui.ma",
                analog_gui_path=f"{DATA_DIR}/analog_gui.ma",
                aas_path=f"{DATA_DIR}/additional_assemble_script.py")
            build_rig(dna=dna, config=config)
            if cmds.objExists("rl4Embedded_Archetype"):
                cmds.delete("rl4Embedded_Archetype")
            if cmds.objExists("rl4Embedded_Archtype"):
                cmds.delete("rl4Embedded_Archtype")
        elif result == "Rigged":
            DATA_DIR = f"{ROOT_DIR}/data" 
            dna = DNA(dnaPath)
            config = RigConfig(
                gui_path=f"{DATA_DIR}/gui.ma",
                analog_gui_path=f"{DATA_DIR}/analog_gui.ma",
                aas_path=f"{DATA_DIR}/additional_assemble_script.py")
            build_rig(dna=dna, config=config)
        
def buildDNA(mod):
    file_path = "c:/Arts and Spells/Scripts/dat.py"
    if os.path.exists(file_path):
        import dat
        importlib.reload(dat)
        ROOT_DIR = dat.ROOT_DIR
        MAIN_PATH = dat.MAIN_PATH
        dnaPath = dat.dnaPath
        body_type = dat.body_type
    """calib_check = f"{ROOT_DIR}/dna_calibration.mod"
    if not os.path.isfile(calib_check):
        cmds.confirmDialog(title="ERROR", message="Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")
        raise ValueError("Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")
    calib_check = f"{ROOT_DIR}/UnrealFest.zip"
    if os.path.isfile(calib_check):
        cmds.confirmDialog(title="ERROR", message="Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")
        raise ValueError("Please download Epic Games Dna Calibration 1.1.0 Version. Version is not matching or files are not found!")"""
    metapipe_vcheck = f"{ROOT_DIR}/Metapipe_Free.py"
    if os.path.isfile(metapipe_vcheck):
        cmds.confirmDialog(title="ERROR", message="Old Version file found. Please delete Metapipe_Free.py file in your dna_calibration path!")
        raise ValueError("Old Version file found. Please delete Metapipe_Free.py file in your dna_calibration path!")
    root_check = f"{ROOT_DIR}/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py"
    if not os.path.isfile(root_check):
        cmds.confirmDialog(title="ERROR", message="Please check ROOT_DIR path for the dna_calibration files! Files are not in ROOT_DIR")
        raise ValueError("Please check ROOT_DIR path for the dna_calibration files! Files are not in ROOT_DIR")
    dna_datas = f"{ROOT_DIR}/examples/datas_dna.py"
    if not os.path.isfile(dna_datas):
        cmds.confirmDialog(title="ERROR", message="Please save your preferences and try again")
        raise ValueError("Please save your preferences and try again")
    if not os.path.isfile(dnaPath):
        cmds.confirmDialog(title="ERROR", message="DNA not found. Please check your preferences and correct the DNA path.")
        raise ValueError("DNA not found. Please check your preferences and correct the DNA path.")
    # Create a progress window
    datasBuild(mod)
    cmds.createNode("transform", name="OpenedDNAInfoNode") 
    if not cmds.objExists("metapipefreewindow"):
        cmds.createNode("transform", name="metapipefreewindow")
    leftPanelButtonV(1)

def datasLoad():
    file_path = "c:/Arts and Spells/Scripts/dat.py"
    if os.path.exists(file_path):
        import dat
        importlib.reload(dat)
        ROOT_DIR = dat.ROOT_DIR
        MAIN_PATH = dat.MAIN_PATH
        dnaPath = dat.dnaPath
        body_type = dat.body_type
    import datas_dna
    importlib.reload(datas_dna)
    datas_dna.load_dna_data()
def loadDNA():
    file_path = "c:/Arts and Spells/Scripts/dat.py"
    if os.path.exists(file_path):
        import dat
        importlib.reload(dat)
        ROOT_DIR = dat.ROOT_DIR
        MAIN_PATH = dat.MAIN_PATH
        dnaPath = dat.dnaPath
        body_type = dat.body_type
    dna_datas = f"{ROOT_DIR}/examples/datas_dna.py"

    #if not os.path.isfile(dna_datas):
        #raise ValueError("Please press Update button first")
    sys.path.append(f"{ROOT_DIR}/examples")
    if not os.path.isfile(dna_datas):
            cmds.confirmDialog(title="ERROR", message="Please save [Metapipe Preferences] again")
            raise ValueError("Please save [Metapipe Preferences] again")
    datasLoad()
    if not cmds.objExists("LoadedDNAInfoNode"):
        cmds.createNode("transform", name="LoadedDNAInfoNode")
        cmds.warning("Loaded Succesfully!")
    cmds.warning("Already Loaded!")
    leftPanelButtonV(2)
    unlock()

def datasSave():
    import datas_dna
    datas_dna.save_dna_data()
def datasSaveRaw():
    import datas_dna
    datas_dna.save_dna_data_raw()
def saveDNA():
    sys.path.append(f"{ROOT_DIR}/examples")
    datasSave()
    if not cmds.objExists("metapipefreewindow"):
        cmds.createNode("transform", name="metapipefreewindow")
    leftPanelButtonV(3) 
    
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
    
    leftPanelButtonV(4)
    print("Ready")   


def fixbody():
    #
    #
    # Transfer Body original skeleton to the new head Skeleton
    CD = 15
    lower_CD = -1
    minCD = 0
        
    # Define the joint names and namespaces
    head_joint = "DHIhead:spine_04"
    body_joint = "spine_04_drv"
    
    # Split the joint names into their respective namespaces and joint names
    head_namespace, head_joint_name = head_joint.split(":")
    
    # Get the list of child joints for the head joint
    head_child_joints = cmds.listRelatives(head_joint, children=True, allDescendents=True,type="joint")
    body_child_joints = cmds.listRelatives(body_joint, children=True, allDescendents=True, type="joint")
    
    def move2target_joint(moving_joint, target_joint):
        lower_lip_rotation_pos = cmds.xform(moving_joint, query=True, worldSpace=True, rotatePivot=True)
        jaw_pos = cmds.xform(target_joint, query=True, worldSpace=True, rotatePivot=True)
        # Get the child joints
        child_joints = cmds.listRelatives(moving_joint, c=True, type="joint")
        # Store the initial positions of the child joints
        child_positions = []
        if child_joints:
            for child_joint in child_joints:                          
                child_positions.append(cmds.xform(child_joint, q=True, ws=True, t=True))
        
        # Set the translate and rotate pivot attributes of the "FACIAL_C_LowerLipRotation" joint to match those of "FACIAL_C_MouthUpper"
        cmds.xform(moving_joint, translation=jaw_pos, rotatePivot=lower_lip_rotation_pos, worldSpace=True)
        if child_joints:
            
            # Move each child joint back to its original position
            for i, child_joint in enumerate(child_joints):
                cmds.xform(child_joint, ws=True, t=child_positions[i])
    moving_joint = body_joint
    target_joint = head_joint      
    move2target_joint(moving_joint, target_joint)
    while CD >= minCD:
            joint_CD = [joint for joint in body_child_joints if cmds.getAttr(joint + ".chainDepth") == CD]
            for joint_name in joint_CD:
                
                drvname = joint_name.replace("_drv", "")
                # Build the joint names for the current joint
                
                
                head_current_joint = "{}:{}".format(head_namespace, drvname)
                if cmds.objExists(head_current_joint):
                    if joint_name[-5] == "r":
                        offnamer = joint_name.replace("_r_drv", "Off_r_drv")
                        if cmds.objExists(offnamer):
                            joint_name = offnamer
                    if joint_name[-5] == "l":
                        offnamel = joint_name.replace("_l_drv", "Off_l_drv")
                        if cmds.objExists(offnamel):
                            joint_name = offnamel
                    moving_joint = joint_name
                    target_joint = head_current_joint       
                    move2target_joint(moving_joint, target_joint)
                                
        
            lower_CD -= 1         
            CD -= 1   
    cmds.createNode("transform", name="FixBodyInfoNode")
    leftPanelButtonV(6)        

    
def bind_skin(gender_mesh):

    # Body
    mesh_obj = cmds.ls(gender_mesh)[0]
    
    # Duplicate the mesh
    duplicated_mesh_obj = cmds.duplicate(mesh_obj)[0]
    
    cmds.select([duplicated_mesh_obj, "DHIbody:root"])
    
    # Bind skin to the mesh
    skin_cluster = cmds.skinCluster("DHIbody:root", duplicated_mesh_obj)[0]
    
    cmds.select([mesh_obj, duplicated_mesh_obj])
    
    cmds.copySkinWeights(noMirror=True, surfaceAssociation="closestPoint", influenceAssociation=["name", "oneToOne"])
    
    cmds.delete(mesh_obj)
    cmds.rename(duplicated_mesh_obj, gender_mesh)
gender=0
gender_mesh = body_type +  "_body_lod0_mesh"
 
def build_body():
    cmds.createNode("transform", name="body_gen_node")
    leftPanelButtonV(5)
    Body_DRV = f"{ROOT_DIR}/data/Body_Drv.mb"
    if not os.path.isfile(Body_DRV):
        raise ValueError("Please prepare the body file first. Body_Drv file is not found")
    skeleton_file_path = f"{ROOT_DIR}/data/Body_Drv.mb"  
    # Import the FBX file
    cmds.file(skeleton_file_path, i=True, ignoreVersion=True, mergeNamespacesOnClash=False)
    def add_chain_depth_attribute(joints):
        for joint in joints:
            if not cmds.attributeQuery('chainDepth', node=joint, exists=True):
                cmds.addAttr(joint, longName='chainDepth', attributeType='long', defaultValue=0)
                cmds.setAttr(joint + '.chainDepth', keyable=True)
    
    def set_chain_depth_value(joints, value):
        for joint in joints:
            cmds.setAttr(joint + '.chainDepth', value)
  
    # Get all joints in the scene
    all_joints = cmds.ls(type="joint")
    
    # Remove joints in the "DHIhead:spine_04" hierarchy (Avoid HEAD)
    exclude_joints = cmds.ls("DHIhead:spine_04", dag=True, type="joint")
    all_joints = cmds.ls("root_drv", dag=True, type="joint")
    add_chain_depth_attribute(all_joints)
    
    # Filter end joints (joints with no child joints)
    end_joints = [joint for joint in all_joints if not cmds.listRelatives(joint, children=True, type='joint')]

    
    # Set chainDepth attribute to 0 for all end joints
    set_chain_depth_value(all_joints, 100)
    set_chain_depth_value(end_joints, 0)
    
    parents1 = []
    
    for joint_name in end_joints:
        p_joint = cmds.listRelatives(joint_name, parent=True, type="joint")
        if p_joint:
            children = cmds.listRelatives(p_joint, children=True, type="joint") or []
            if all(cmds.getAttr(child + ".chainDepth") == 0 for child in children):
               
               parents1.append(p_joint[0])
               
    set_chain_depth_value(parents1, 1)
    #Chaindepth add Attr Loop
    chainDepth = 1
    while parents1:
        chainDepth += 1
        new_parents = []
        for joint_name in parents1:
            p_joint = cmds.listRelatives(joint_name, parent=True, type="joint")
            if p_joint:
                children = cmds.listRelatives(p_joint, children=True, type="joint") or []
                if all(cmds.getAttr(child + ".chainDepth") < chainDepth for child in children):
                    new_parents.append(p_joint[0])
        if new_parents:
            set_chain_depth_value(new_parents, chainDepth)
            parents1 = new_parents
        else:
            break
    DHIBODY_name = 'DHIbody:root'
    bind_skin(gender_mesh)
    unlock()
    
def connect_body():
    bodyNS = "DHIbody:"
    headNS = "DHIhead:"
    
    for i in cmds.ls(type="joint"):
        if headNS in i:
            if i.replace(headNS,bodyNS) in cmds.ls(type="joint"):
                cmds.parentConstraint(i.replace(headNS,bodyNS),i,mo=True)
                cmds.scaleConstraint(i.replace(headNS,bodyNS),i,mo=True)

def bindSkinC():
    selected_objects = cmds.ls(selection=True)
    sel = selected_objects[0]
    cmds.select('DHIbody:root', add=True)
    cmds.skinCluster()
    cmds.rename(sel, body_type +  "_binded_body_lod0_mesh")
    cmds.hide(body_type +  "_body_lod0_mesh")
def copySkin():
    selected_objects = cmds.ls(selection=True)
    sel = selected_objects[0]
    cmds.select(clear=True)
    cmds.select(body_type +  "_body_lod0_mesh", add=True)
    cmds.select(sel, add=True)
    cmds.copySkinWeights(noMirror=True, surfaceAssociation="closestPoint", influenceAssociation=["name", "oneToOne"])
    cmds.delete(body_type +  "_body_lod0_mesh")
    cmds.rename(sel, body_type +  "_body_lod0_mesh")
    
def shapeEdit():
    import maya.mel as mel
    mel.eval("ShapeEditor")

def findCustom():
    
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        poly_Match = 0
        poly_count = cmds.polyEvaluate(obj, vertex=True)
        if poly_count == 24049:
            cmds.rename(obj, "custom_head_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_head",edit=True,enable=True)
            continue
        elif poly_count == 4246:
            cmds.rename(obj, "custom_teeth_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_teeth",edit=True,enable=True)
            continue
        elif poly_count == 660:
            cmds.rename(obj, "custom_saliva_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_saliva",edit=True,enable=True)
            continue
        elif poly_count == 770:
            if not cmds.objExists("custom_eyeLeft_lod0_mesh1"):
                cmds.rename(obj, "custom_eyeLeft_lod0_mesh0")
                poly_count = 1
        elif poly_count == 552:
            cmds.rename(obj, "custom_eyeshell_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_eyeshell",edit=True,enable=True)
            continue
        elif poly_count == 2144:
            cmds.rename(obj, "custom_eyelashes_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_eyelashes",edit=True,enable=True)
            continue
        elif poly_count == 268: 
            cmds.rename(obj, "custom_eyeEdge_lod0_mesh")
            poly_Match = 1 
            cmds.symbolButton("gcustom_eyeEdge",edit=True,enable=True)
            continue  
        elif poly_count == 386:
            cmds.rename(obj, "_custom_cartilage_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_cartilage",edit=True,enable=True)
            continue
        elif poly_count == 30455:
            cmds.rename(obj, body_type + "_custom_body_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_body",edit=True,enable=True)
            continue
        elif poly_count == 54412:
            cmds.rename(obj, body_type + "_custom_combined_lod0_mesh")
            poly_Match = 1
            cmds.symbolButton("gcustom_combined",edit=True,enable=True)
            continue
  
    if cmds.objExists("custom_eyeLeft_lod0_mesh0") and cmds.objExists("custom_eyeLeft_lod0_mesh1"):
        cmds.symbolButton("gcustom_eyeLeft",edit=True,enable=True)
        cmds.symbolButton("gcustom_eyeRight",edit=True,enable=True)
        cmds.xform("custom_eyeLeft_lod0_mesh0", centerPivots=True)
        cmds.xform("custom_eyeLeft_lod0_mesh1", centerPivots=True)
        pos1 = cmds.xform("custom_eyeLeft_lod0_mesh0", query=True, worldSpace=True, rotatePivot=True)
        pos2 = cmds.xform("custom_eyeLeft_lod0_mesh1", query=True, worldSpace=True, rotatePivot=True)      
        # Check the model is in rigth or left
        if pos1[0] > 0 and pos2[0] > 0:
            print("Both eyes are on the positive X side of the origin")
        elif pos1[0] < 0 and pos2[0] < 0:
            print("Both eyes are on the negative X side of the origin")
        elif pos1[0] < 0 and pos2[0] > 0:
            if cmds.objExists("eyeRight") or cmds.objExists("eyeLeft"):
                print("Eye names already exist, Delete or rename them")
            else:
                cmds.rename("custom_eyeLeft_lod0_mesh0", "custom_eyeRight_lod0_mesh")
                cmds.rename("custom_eyeLeft_lod0_mesh1", "custom_eyeLeft_lod0_mesh")
        elif pos1[0] > 0 and pos2[0] < 0:
            if cmds.objExists("eyeRight") or cmds.objExists("eyeLeft"):
                print("Eye names already exist, Delete or rename them")
            else:
                cmds.rename("custom_eyeLeft_lod0_mesh0", "custom_eyeLeft_lod0_mesh")
                cmds.rename("custom_eyeLeft_lod0_mesh1", "eyeRight_lod0_mesh")
        elif pos1[0] == 0 or pos2[0] == 0:
            print("Eye is in the middle")  
def jointSelectionC(butName):
    print(butName)
    if cmds.objExists(butName):
        butNameS=butName

    if cmds.objExists("DHIhead:"+butName):
        butNameS="DHIhead:"+butName 

    if cmds.objExists(butName+"_drv"):
        butNameS=butName+"_drv"
        
    global selCheck
    selected_objects = cmds.ls(selection=True)
    if butNameS not in selected_objects:
        cmds.symbolButton(butName, edit=True, image=iconPath + "JointButtonSelected.png")
        cmds.select(butNameS, add=True)
        selCheck=1
    else:
        cmds.symbolButton(butName, edit=True, image=iconPath + "JointButton.png")
        cmds.select(butNameS, deselect=True)
        selCheck=0

def meshSelC(mesh, toggleN):
    if toggleN == 0:
        meshN = mesh + "_lod" + sceneLodN + "_mesh"
    
        selected_objects = cmds.ls(selection=True)
        if meshN not in selected_objects:
            cmds.symbolButton("g" + mesh,edit=True,image=iconPath + "UIGeo" + mesh + "Pressed.png")
            cmds.select(meshN, add=True)
            selCheck=1
        else:
            cmds.symbolButton("g" + mesh,edit=True,image=iconPath + "UIGeo" + mesh + ".png")
            cmds.select(meshN, deselect=True)
            selCheck=0
    if toggleN == 1:
        meshN = body_type + "_" + mesh + "_lod" + scenebodyLodN + "_mesh"
    
        selected_objects = cmds.ls(selection=True)
        if meshN not in selected_objects:
            cmds.symbolButton("g" + mesh,edit=True,image=iconPath + "UIGeo" + mesh + "Pressed.png")
            cmds.select(meshN, add=True)
            selCheck=1
        else:
            cmds.symbolButton("g" + mesh,edit=True,image=iconPath + "UIGeo" + mesh + ".png")
            cmds.select(meshN, deselect=True)
            selCheck=0
    if toggleN == 2:
        meshN = mesh + "_drv"
    
        selected_objects = cmds.ls(selection=True)
        if meshN not in selected_objects:
            cmds.symbolButton(mesh,edit=True,image=iconPath + "JointButtonHPressed.png")
            cmds.select(meshN, add=True)
            selCheck=1
        else:
            cmds.symbolButton(mesh,edit=True,image=iconPath + "JointButtonH.png")
            cmds.select(meshN, deselect=True)
            selCheck=0

def selectAllGeo(toggleN):
    if toggleN==0:
        gheadMesh = ['head_lod' + sceneLodN + '_mesh', 'teeth_lod' + sceneLodN + '_mesh', 'saliva_lod' + sceneLodN + '_mesh', 'eyeLeft_lod' + sceneLodN + '_mesh', 'eyeshell_lod' + sceneLodN + '_mesh', 'eyelashes_lod' + sceneLodN + '_mesh', 'eyeEdge_lod' + sceneLodN + '_mesh', 'cartilage_lod' + sceneLodN + '_mesh', 'eyeRight_lod' + sceneLodN + '_mesh']
        for obj in gheadMesh:
            if cmds.objExists(obj):
                cmds.select(obj, add=True)
    if toggleN==1:
        gheadMesh = ['head_lod' + sceneLodN + '_mesh', 'teeth_lod' + sceneLodN + '_mesh', 'saliva_lod' + sceneLodN + '_mesh', 'eyeLeft_lod' + sceneLodN + '_mesh', 'eyeshell_lod' + sceneLodN + '_mesh', 'eyelashes_lod' + sceneLodN + '_mesh', 'eyeEdge_lod' + sceneLodN + '_mesh', 'cartilage_lod' + sceneLodN + '_mesh', 'eyeRight_lod' + sceneLodN + '_mesh']
        for obj in gheadMesh:
            if cmds.objExists("custom_" + obj):
                cmds.select("custom_" + obj, add=True)
    if toggleN==2:
        gbodyMesh = [body_type + "_body_lod" + scenebodyLodN + '_mesh',body_type + "_combined_lod" + scenebodyLodN + '_mesh',body_type + "_flipflops_lod" + scenebodyLodN + '_mesh']
        for obj in gbodyMesh:
            if cmds.objExists(obj):
                cmds.select(obj, add=True)
    if toggleN==3:
        gbodyMesh = [body_type + "_custom_body_lod" + scenebodyLodN + '_mesh',body_type + "_custom_combined_lod" + scenebodyLodN + '_mesh',body_type + "_custom_flipflops_lod" + scenebodyLodN + '_mesh']
        for obj in gbodyMesh:
            if cmds.objExists(obj):
                cmds.select(obj, add=True)
def checkSceneSel():
    if cmds.objExists("metapipefreewindow"):
        global toggleCheck
        selected_objects = cmds.ls(selection=True)
        gheadMesh = ['head_lod' + sceneLodN + '_mesh', 'teeth_lod' + sceneLodN + '_mesh', 'saliva_lod' + sceneLodN + '_mesh', 'eyeLeft_lod' + sceneLodN + '_mesh', 'eyeshell_lod' + sceneLodN + '_mesh', 'eyelashes_lod' + sceneLodN + '_mesh', 'eyeEdge_lod' + sceneLodN + '_mesh', 'cartilage_lod' + sceneLodN + '_mesh', 'eyeRight_lod' + sceneLodN + '_mesh']
        gbodyMesh = [body_type + "_body_lod" + scenebodyLodN + '_mesh',body_type + "_combined_lod" + scenebodyLodN + '_mesh',body_type + "_flipflops_lod" + scenebodyLodN + '_mesh']
        gcustomheadMesh = ['custom_head_lod0_mesh', 'custom_teeth_lod0_mesh', 'custom_saliva_lod0_mesh', 'custom_eyeLeft_lod0_mesh', 'custom_eyeshell_lod0_mesh', 'custom_eyelashes_lod0_mesh', 'custom_eyeEdge_lod0_mesh', 'custom_cartilage_lod0_mesh', 'custom_eyeRight_lod0_mesh']
        gcustombodyMesh = [body_type + "_custom_body_lod0_mesh", body_type + "_custom_combined_lod0_mesh"]
        jointButs=["pelvis", "spine_01", "spine_02", "spine_03", "spine_04", "spine_05", "neck_02", "head", "clavicle_r", "clavicle_l", "thigh_r", "thigh_l", "calf_r", "calf_l", "foot_r", "foot_l", "upperarm_r", "upperarm_l", "lowerarm_r", "lowerarm_l", "hand_r", "hand_l", "FACIAL_C_Jaw", "FACIAL_C_TeethUpper", "FACIAL_C_TeethLower", "root",
                    'FACIAL_R_EyelidUpperB1', 'FACIAL_R_EyelidUpperA1', 'FACIAL_R_EyelidLowerA1', 'FACIAL_R_EyelidLowerB1', 'FACIAL_R_Eye', 'FACIAL_R_LipUpperOuter', 'FACIAL_R_LipUpper', 'FACIAL_R_LipLower', 'FACIAL_L_EyelidUpperB1', 'FACIAL_L_EyelidUpperA1', 'FACIAL_L_EyelidLowerA1', 'FACIAL_L_EyelidLowerB1', 'FACIAL_L_Eye', 'FACIAL_L_LipUpperOuter', 'FACIAL_R_LipUpper', 'FACIAL_R_LipLower', 'FACIAL_R_EyelidUpperB2', 'FACIAL_R_EyelidUpperA2', 'FACIAL_R_EyelidLowerA2', 'FACIAL_R_EyelidLowerB2', 'FACIAL_R_EyeCornerOuter', 'FACIAL_R_LipCorner', 'FACIAL_L_LipUpper', 'FACIAL_L_LipLower', 'FACIAL_L_EyelidUpperB2', 'FACIAL_L_EyelidUpperA2', 'FACIAL_L_EyelidLowerA2', 'FACIAL_L_EyelidLowerB2', 'FACIAL_L_EyeCornerOuter', 'FACIAL_L_LipCorner', 'FACIAL_L_LipUpper', 'FACIAL_L_LipLower', 'FACIAL_R_EyelidUpperB3', 'FACIAL_R_EyelidUpperA3', 'FACIAL_R_EyelidLowerA3', 'FACIAL_R_EyelidLowerB3', 'FACIAL_R_EyeCornerInner', 'FACIAL_R_LipLowerOuter', 'FACIAL_C_LipUpper', 'FACIAL_C_LipLower', 'FACIAL_L_EyelidUpperB3', 'FACIAL_L_EyelidUpperA3', 'FACIAL_L_EyelidLowerA3', 'FACIAL_L_EyelidLowerB3', 'FACIAL_L_EyeCornerInner', 'FACIAL_L_LipLowerOuter', 'FACIAL_C_LipUpper', 'FACIAL_C_LipLower']
        handButs = ['index_01_r_drv', 'index_01_l_drv', 'index_02_r_drv', 'index_02_l_drv', 'index_03_r_drv', 'index_03_l_drv', 'middle_01_r_drv', 'middle_01_l_drv', 'middle_02_r_drv', 'middle_02_l_drv', 'middle_03_r_drv', 'middle_03_l_drv', 'ring_01_r_drv', 'ring_01_l_drv', 'ring_02_r_drv', 'ring_02_l_drv', 'ring_03_r_drv', 'ring_03_l_drv', 'pinky_01_r_drv', 'pinky_01_l_drv', 'pinky_02_r_drv', 'pinky_02_l_drv', 'pinky_03_r_drv', 'pinky_03_l_drv', 'thumb_01_r_drv', 'thumb_01_l_drv', 'thumb_02_r_drv', 'thumb_02_l_drv', 'thumb_03_r_drv', 'thumb_03_l_drv']
        for obj in jointButs:
                cmds.symbolButton(obj, edit=True, image=iconPath + "JointButton.png")
        for obj in handButs:
                obj = obj.split("_drv")
                cmds.symbolButton(obj[0], edit=True, image=iconPath + "JointButtonH.png")
        for obj in gheadMesh:
                obj = obj.split('_lod' + sceneLodN + '_mesh')
                if not cmds.objExists(obj[0] + '_lod' + sceneLodN + '_mesh'):
                    cmds.symbolButton("g" + obj[0],edit=True,image=iconPath + "UIGeo" + obj[0] + ".png", enable = False)
                else:
                    cmds.symbolButton("g" + obj[0],edit=True,image=iconPath + "UIGeo" + obj[0] + ".png", enable = True)
        for obj in gbodyMesh:
                obj = obj.split('_lod' + scenebodyLodN + '_mesh')
                obj = obj[0].split(body_type + "_")
                if not cmds.objExists(body_type + "_" + obj[1] + '_lod' + scenebodyLodN + '_mesh'):
                    cmds.symbolButton("g" + obj[1],edit=True,image=iconPath + "UIGeo" + obj[1] + ".png", enable = False)
                else:
                    cmds.symbolButton("g" + obj[1],edit=True,image=iconPath + "UIGeo" + obj[1] + ".png", enable = True)
        for obj in gcustomheadMesh: 
                objCheck=obj.replace("0",sceneLodN)
                if not cmds.objExists(objCheck):
                    obj = obj.split('_lod0_mesh')
                    cmds.symbolButton("g" + obj[0],edit=True,image=iconPath + "UIGeoC.png", enable = False)
                else:
                    obj = obj.split('_lod0_mesh')
                    cmds.symbolButton("g" + obj[0],edit=True,image=iconPath + "UIGeoC.png", enable = True)
                    if toggleCheck == 0:
                        cmds.symbolButton("gcustom_all",edit=True,enable=True, visible=True)
        for obj in gcustombodyMesh: 
                objCheck=obj.replace("0",scenebodyLodN)
                if not cmds.objExists(objCheck):
                    obj = obj.split('_lod0_mesh')
                    obj = obj[0].split(body_type + "_")
                    cmds.symbolButton("g" + obj[1],edit=True,image=iconPath + "UIGeoC.png", enable = False)
                else:
                    obj = obj.split('_lod0_mesh')
                    obj = obj[0].split(body_type + "_")
                    cmds.symbolButton("g" + obj[1],edit=True,image=iconPath + "UIGeoC.png", enable = True)
                    if toggleCheck == 1:
                        cmds.symbolButton("gcustom_all",edit=True,enable=True, visible=True)
                    
        for obj in selected_objects:
            
            if "DHIhead:" in obj: 
                headObj = obj.split("DHIhead:")
                if headObj[1] in jointButs:       
                    cmds.symbolButton(headObj[1], edit=True, image=iconPath + "JointButtonSelected.png")
            if "_drv" in obj: 
                bodyObj = obj.split("_drv")
                if bodyObj[0] in jointButs:       
                    cmds.symbolButton(bodyObj[0], edit=True, image=iconPath + "JointButtonSelected.png")
            if obj in jointButs:                
                cmds.symbolButton(obj, edit=True, image=iconPath + "JointButtonSelected.png")
            if obj in handButs:
                obj = obj.split("_drv")
                cmds.symbolButton(obj[0], edit=True, image=iconPath + "JointButtonHPressed.png")
            if obj in gheadMesh:
                obj = obj.split('_lod' + sceneLodN + '_mesh')
                cmds.symbolButton("g" + obj[0],edit=True,image=iconPath + "UIGeo" + obj[0] + "Pressed.png")
            if obj in gcustomheadMesh:
                obj = obj.split('_lod' + sceneLodN + '_mesh')    
                cmds.symbolButton("g" + obj[0],edit=True,image=iconPath + "UIGeoCPressed.png")
            if obj in gbodyMesh:
                obj = obj.split('_lod' + scenebodyLodN + '_mesh')
                obj = obj[0].split(body_type + "_")
                cmds.symbolButton("g" + obj[1],edit=True,image=iconPath + "UIGeo" + obj[1] + "Pressed.png")
            if obj in gcustombodyMesh:
                obj = obj.split('_lod' + scenebodyLodN + '_mesh')
                obj = obj[0].split(body_type + "_")    
                cmds.symbolButton("g" + obj[1],edit=True,image=iconPath + "UIGeoCPressed.png")

def sceneRT(*args):
    checkSceneSel()

selection_change_callback = cmds.scriptJob(event=["SelectionChanged", sceneRT])
def newScene():
    if cmds.file(query=True, modified=True):
        result = cmds.confirmDialog(
            title="Save Changes?",
            message="Do you want to save changes to the current scene?",
            button=["Save", "Don't Save", "Cancel"],
            defaultButton="Save",
            cancelButton="Cancel",
            dismissString="Cancel"
        )
    
        if result == "Save":
            # Save the current scene
            cmds.file(save=True, force=True)
        elif result == "Don't Save":
            # Discard changes and create a new scene
            cmds.file(new=True, force=True)
    else:
        # No unsaved changes, create a new scene directly
        cmds.file(new=True, force=True)
    leftPanelButtonV(0) 


def import_obj():
    # Open the import dialog with a filter set to OBJ files
    file_path = cmds.fileDialog2(fileFilter="Obj (*.obj)", dialogStyle=2, fileMode=1)

    # Check if the user selected a file
    if file_path:
        # Import the selected OBJ file into Maya
        try:
            cmds.file(file_path[0], i=True, type="OBJ", rpr="auto")
            print("OBJ file imported successfully:", file_path[0])
        except Exception as e:
            print("Error importing OBJ file:", str(e))

def export_fbx():

    if cmds.objExists("DHIbody:root"):
    
        # Set the path and filename for the FBX file
        path = f"{ROOT_DIR}/output"
        filename = "body.fbx"
        filepath = path + "/" + filename
        cmds.select(clear=True)
        cmds.select("body_rig", add=True)
        cmds.select("DHIbody:root", add=True)
        # Export the selected objects as FBX
        cmds.file(filepath, force=True, options="groups=0;ptgroups=0;materials=0;smoothing=1;normals=1", type='FBX export', exportSelected=True)
    
        filename = "head.fbx"
        filepath = path + "/" + filename
        cmds.select("DHIbody:spine_04", hi=True)  # Select "DHIbody:spine_04" and its children
        cmds.delete()  # Delete the selected objects
        cmds.select("DHIbody:thigh_r", hi=True)  # Select "DHIbody:spine_04" and its children
        cmds.delete()  # Delete the selected objects
        cmds.select("DHIbody:thigh_l", hi=True)  # Select "DHIbody:spine_04" and its children
        cmds.delete()  # Delete the selected objects
        
        # Parent "DHIhead:spine_04" under "DHIbody:spine_03"
        cmds.parent("DHIhead:spine_04", "DHIbody:spine_03")
        
        # Print the new parent of "DHIhead:spine_04"
        print(cmds.listRelatives("DHIhead:spine_04", parent=True))
        
        cmds.select(clear=True)
        cmds.select("head_grp", add=True)
        cmds.select("DHIbody:root", add=True)
        # Export the selected objects as FBX
        cmds.file(filepath, force=True, options="groups=0;ptgroups=0;materials=0;smoothing=1;normals=1", type='FBX export', exportSelected=True)
        
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
        cmds.undo()
    else:
        raise ValueError("Process is not finished! Body is missing")

def unlock():

    if cmds.objExists("body_gen_node") or cmds.objExists("root_drv"):
        gbodyMesh = [body_type + "_body_lod" + scenebodyLodN + '_mesh',body_type + "_combined_lod" + scenebodyLodN + '_mesh',body_type + "_flipflops_lod" + scenebodyLodN + '_mesh']
        for obj in gbodyMesh:
            if cmds.objExists(obj):
                for attr in ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]:
                    cmds.setAttr(obj + "." + attr, lock=False)

    else:
        cmds.select("spine_04", hierarchy=True)
        selected_objects = cmds.ls(selection=True)
        gheadMesh = ['head_lod' + sceneLodN + '_mesh', 'teeth_lod' + sceneLodN + '_mesh', 'saliva_lod' + sceneLodN + '_mesh', 'eyeLeft_lod' + sceneLodN + '_mesh', 'eyeshell_lod' + sceneLodN + '_mesh', 'eyelashes_lod' + sceneLodN + '_mesh', 'eyeEdge_lod' + sceneLodN + '_mesh', 'cartilage_lod' + sceneLodN + '_mesh', 'eyeRight_lod' + sceneLodN + '_mesh']
        for obj in selected_objects:
            if cmds.attributeQuery("radius", node=obj, exists=True):
                cmds.setAttr(obj + ".radius", 0.1)
        for obj in gheadMesh:
            if cmds.objExists(obj):
                for attr in ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]:
                    cmds.setAttr(obj + "." + attr, lock=False)
            
    cmds.select(clear=True)

def headPanel(State):
    imagepath=iconPath + "JointButton.png"
    #LEFT BUTTONS                 
    cmds.image("im4",edit=True,visible=State)
    ebutTop = 325
    ebutL = 157
    ebutR = 50
    ebutSpace=12
    ebutWSpa=12
    
    mbutTop = ebutTop + 105
    mbutR = 92
    mbutSpace=12
    mbutWSpa=12
    eyeList = ["", "CornerOuter", "CornerInner"]
    mouthList = ["R", "L", "C"]
    mouthSymList = ["UpperOuter", "Corner", "LowerOuter"]
    propers = ["Upper","Lower", "A", "B"]
    for i in range(3):

        for y in range(2):
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[0] + propers[3] + str(i+1), edit=True, image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[0] + propers[2] + str(i+1), edit=True, image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[1] + propers[2] + str(i+1), edit=True, image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[1] + propers[3] + str(i+1), edit=True, image=imagepath,visible=State)

            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eye" + eyeList[i], edit=True, image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Lip" + mouthSymList[i], edit=True, image=imagepath,visible=State)
        
        cmds.symbolButton("FACIAL_" + mouthList[i] + "_LipUpper", edit=True, image=imagepath,visible=State)
        cmds.symbolButton("FACIAL_" + mouthList[i] + "_LipLower", edit=True, image=imagepath,visible=State)

    bodyParent =0
    headSelJ = ["FACIAL_C_Jaw", "FACIAL_C_TeethUpper", "FACIAL_C_TeethLower", "neck_02", "head"]
    for i in range(len(headSelJ)):
        cmds.symbolButton(headSelJ[i], edit=True,visible=State)
    
    titleName = ["RIGHT EYE", "LEFT EYE", "MOUTH"]
    for i in range(3):
        cmds.text("title" + str(i+1), label= titleName[i], edit=True, p="formLay2",visible=State)

    
    cmds.formLayout( "formLay2", edit=True, attachForm=[("FACIAL_R_EyelidUpperB3", 'top', ebutTop), ("FACIAL_R_EyelidUpperB3", 'left', ebutR),("FACIAL_R_EyelidUpperB2", 'top', ebutTop), ("FACIAL_R_EyelidUpperB2", 'left', ebutR+ebutSpace),("FACIAL_R_EyelidUpperB1", 'top', ebutTop), ("FACIAL_R_EyelidUpperB1", 'left',ebutR+2*ebutSpace),("FACIAL_R_EyelidUpperA3", 'top', ebutTop+ebutWSpa), ("FACIAL_R_EyelidUpperA3", 'left', ebutR),("FACIAL_R_EyelidUpperA2", 'top', ebutTop+ebutWSpa), ("FACIAL_R_EyelidUpperA2", 'left', ebutR+ebutSpace),("FACIAL_R_EyelidUpperA1", 'top', ebutTop+ebutWSpa), ("FACIAL_R_EyelidUpperA1", 'left',ebutR+2*ebutSpace),
                                                ("FACIAL_R_EyelidLowerA3", 'top', ebutTop+4*ebutWSpa), ("FACIAL_R_EyelidLowerA3", 'left', ebutR),("FACIAL_R_EyelidLowerA2", 'top', ebutTop+4*ebutWSpa), ("FACIAL_R_EyelidLowerA2", 'left', ebutR+ebutSpace),("FACIAL_R_EyelidLowerA1", 'top', ebutTop+4*ebutWSpa), ("FACIAL_R_EyelidLowerA1", 'left',ebutR+2*ebutSpace),("FACIAL_R_EyelidLowerB3", 'top', ebutTop+5*ebutWSpa), ("FACIAL_R_EyelidLowerB3", 'left', ebutR),("FACIAL_R_EyelidLowerB2", 'top', ebutTop+5*ebutWSpa), ("FACIAL_R_EyelidLowerB2", 'left', ebutR+ebutSpace),("FACIAL_R_EyelidLowerB1", 'top', ebutTop+5*ebutWSpa), ("FACIAL_R_EyelidLowerB1", 'left',ebutR+2*ebutSpace),
                                                
                                                ("FACIAL_L_EyelidUpperB1", 'top', ebutTop), ("FACIAL_L_EyelidUpperB1", 'left', ebutL),("FACIAL_L_EyelidUpperB2", 'top', ebutTop), ("FACIAL_L_EyelidUpperB2", 'left', ebutL+ebutSpace),("FACIAL_L_EyelidUpperB3", 'top', ebutTop), ("FACIAL_L_EyelidUpperB3", 'left',ebutL+2*ebutSpace),("FACIAL_L_EyelidUpperA1", 'top', ebutTop+ebutWSpa), ("FACIAL_L_EyelidUpperA1", 'left', ebutL),("FACIAL_L_EyelidUpperA2", 'top', ebutTop+ebutWSpa), ("FACIAL_L_EyelidUpperA2", 'left', ebutL+ebutSpace),("FACIAL_L_EyelidUpperA3", 'top', ebutTop+ebutWSpa), ("FACIAL_L_EyelidUpperA3", 'left',ebutL+2*ebutSpace),
                                                ("FACIAL_L_EyelidLowerA1", 'top', ebutTop+4*ebutWSpa), ("FACIAL_L_EyelidLowerA1", 'left', ebutL),("FACIAL_L_EyelidLowerA2", 'top', ebutTop+4*ebutWSpa), ("FACIAL_L_EyelidLowerA2", 'left', ebutL+ebutSpace),("FACIAL_L_EyelidLowerA3", 'top', ebutTop+4*ebutWSpa), ("FACIAL_L_EyelidLowerA3", 'left',ebutL+2*ebutSpace),("FACIAL_L_EyelidLowerB1", 'top', ebutTop+5*ebutWSpa), ("FACIAL_L_EyelidLowerB1", 'left', ebutL),("FACIAL_L_EyelidLowerB2", 'top', ebutTop+5*ebutWSpa), ("FACIAL_L_EyelidLowerB2", 'left', ebutL+ebutSpace),("FACIAL_L_EyelidLowerB3", 'top', ebutTop+5*ebutWSpa), ("FACIAL_L_EyelidLowerB3", 'left',ebutL+2*ebutSpace),
                                                
                                                ("FACIAL_R_EyeCornerOuter", 'top', ebutTop+2.5*ebutWSpa), ("FACIAL_R_EyeCornerOuter", 'left', ebutR-ebutSpace),("FACIAL_R_Eye", 'top', ebutTop+2.5*ebutWSpa), ("FACIAL_R_Eye", 'left', ebutR+ebutSpace),("FACIAL_R_EyeCornerInner", 'top', ebutTop+2.5*ebutWSpa), ("FACIAL_R_EyeCornerInner", 'left', ebutR+3*ebutSpace),
                                                ("FACIAL_L_EyeCornerInner", 'top', ebutTop+2.5*ebutWSpa), ("FACIAL_L_EyeCornerInner", 'left', ebutL-ebutSpace),("FACIAL_L_Eye", 'top', ebutTop+2.5*ebutWSpa), ("FACIAL_L_Eye", 'left', ebutL+ebutSpace),("FACIAL_L_EyeCornerOuter", 'top', ebutTop+2.5*ebutWSpa), ("FACIAL_L_EyeCornerOuter", 'left', ebutL+3*ebutSpace),
                                                
                                                ("FACIAL_R_LipUpperOuter", 'top', mbutTop), ("FACIAL_R_LipUpperOuter", 'left', mbutR),("FACIAL_R_LipUpper", 'top', mbutTop), ("FACIAL_R_LipUpper", 'left', mbutR+ebutSpace),("FACIAL_C_LipUpper", 'top', mbutTop), ("FACIAL_C_LipUpper", 'left',mbutR+2*mbutSpace),("FACIAL_L_LipUpper", 'top', mbutTop), ("FACIAL_L_LipUpper", 'left', mbutR+3*mbutSpace),("FACIAL_L_LipUpperOuter", 'top', mbutTop), ("FACIAL_L_LipUpperOuter", 'left', mbutR+4*mbutSpace),("FACIAL_R_LipCorner", 'top', mbutTop+0.5*mbutWSpa), ("FACIAL_R_LipCorner", 'left',mbutR-mbutSpace),
                                                ("FACIAL_R_LipLowerOuter", 'top', mbutTop+mbutWSpa), ("FACIAL_R_LipLowerOuter", 'left', mbutR),("FACIAL_R_LipLower", 'top', mbutTop+mbutWSpa), ("FACIAL_R_LipLower", 'left', mbutR+ebutSpace),("FACIAL_C_LipLower", 'top', mbutTop+mbutWSpa), ("FACIAL_C_LipLower", 'left',mbutR+2*mbutSpace),("FACIAL_L_LipLower", 'top', mbutTop+mbutWSpa), ("FACIAL_L_LipLower", 'left', mbutR+3*mbutSpace),("FACIAL_L_LipLowerOuter", 'top', mbutTop+mbutWSpa), ("FACIAL_L_LipLowerOuter", 'left', mbutR+4*mbutSpace),("FACIAL_L_LipCorner", 'top', mbutTop+0.5*mbutWSpa), ("FACIAL_L_LipCorner", 'left',mbutR+5*mbutSpace),
                                                
                                                ("FACIAL_C_Jaw", 'top', bodyParent+117),("FACIAL_C_Jaw", 'left', 97),("FACIAL_C_TeethUpper", 'top', bodyParent+122), ("FACIAL_C_TeethUpper", 'left', 62),("FACIAL_C_TeethLower", 'top', bodyParent+138), ("FACIAL_C_TeethLower", 'left', 67),
                                                ("neck_02", 'top', bodyParent+167), ("neck_02", 'left', 127),("head", 'top', bodyParent+67),("head", 'left', bodyParent+127),
                                                
                                                ("title1", 'top', ebutTop-35), ("title1", 'left', 41),("title2", 'top', ebutTop-35), ("title2", 'left', 153),("title3", 'top', mbutTop-35), ("title3", 'left', 100)])
                    
    bodyParent=0       
    geoTop=515
    geoLeft=20
    geoSpace=20
    geoLSpace=109
    cgeoLeft=10
    gheadMesh = ["head","teeth","saliva","eyeLeft","eyeshell","eyelashes","eyeEdge","cartilage","eyeRight", "all"]
    for i in range(len(gheadMesh)):

            cmds.symbolButton("g" + gheadMesh[i],edit=True,command=lambda x, i=i:meshSelC(gheadMesh[i],0),visible=State)
            cmds.symbolButton("g" + "custom_" + gheadMesh[i],edit=True,command=lambda x, i=i:meshSelC("custom_" + gheadMesh[i],0), visible=State)
            
    cmds.symbolButton("gall",edit=True,command=lambda x: selectAllGeo(0))
    cmds.symbolButton("gcustom_all",edit=True,command=lambda x: selectAllGeo(1))
    lodTop=675
    lodLeft=20
    lodSpace=25
    for i in range(8):

        cmds.text("t" + str(i),edit=True, visible=State)
        if i == 0:
            cmds.symbolButton("lod" + str(i),edit=True, image=iconPath + "UIButtonEmptySRT.png", visible=State)
        else:
            cmds.symbolButton("lod" + str(i),edit=True, image=iconPath + "UIButtonEmptySRTPressed.png", visible=State)

        
    lodtL=10
    lodtT=-20
    
    
    cmds.canvas("c1", edit=True, visible=State)
    cmds.canvas("c2", edit=True, visible=State)

    cmds.formLayout( "formLay2", edit=True,visible=True, attachForm=[("c1", 'top',bodyParent+483), ("c1", 'left', 20),("c2", 'top',bodyParent+690), ("c2", 'left', 20),
                                                ("ghead", 'top', geoTop), ("ghead", 'left', geoLeft),("gteeth", 'top', geoTop+geoSpace), ("gteeth", 'left', geoLeft),("gsaliva", 'top', geoTop+2*geoSpace), ("gsaliva", 'left', geoLeft),("geyeLeft", 'top', geoTop+3*geoSpace), ("geyeLeft", 'left', geoLeft),
                                                ("geyeshell", 'top', geoTop), ("geyeshell", 'left', geoLeft+geoLSpace),("geyelashes", 'top', geoTop+geoSpace), ("geyelashes", 'left', geoLeft+geoLSpace),("geyeEdge", 'top', geoTop+2*geoSpace), ("geyeEdge", 'left', geoLeft+geoLSpace),("gcartilage", 'top', geoTop+3*geoSpace), ("gcartilage", 'left', geoLeft+geoLSpace),
                                                ("geyeRight", 'top', geoTop+4*geoSpace), ("geyeRight", 'left', geoLeft), ("gall", 'top', geoTop+4*geoSpace), ("gall", 'left', geoLeft +geoLSpace),
                                                ("gcustom_head", 'top', geoTop), ("gcustom_head", 'left', cgeoLeft),("gcustom_teeth", 'top', geoTop+geoSpace), ("gcustom_teeth", 'left', cgeoLeft),("gcustom_saliva", 'top', geoTop+2*geoSpace), ("gcustom_saliva", 'left', cgeoLeft),("gcustom_eyeLeft", 'top', geoTop+3*geoSpace), ("gcustom_eyeLeft", 'left', cgeoLeft),
                                                ("gcustom_eyeshell", 'top', geoTop), ("gcustom_eyeshell", 'left', cgeoLeft+geoLSpace),("gcustom_eyelashes", 'top', geoTop+geoSpace), ("gcustom_eyelashes", 'left', cgeoLeft+geoLSpace),("gcustom_eyeEdge", 'top', geoTop+2*geoSpace), ("gcustom_eyeEdge", 'left', cgeoLeft+geoLSpace),("gcustom_cartilage", 'top', geoTop+3*geoSpace), ("gcustom_cartilage", 'left', cgeoLeft+geoLSpace),
                                                ("gcustom_eyeRight", 'top', geoTop+4*geoSpace), ("gcustom_eyeRight", 'left', cgeoLeft), ("gcustom_all", 'top', geoTop+4*geoSpace), ("gcustom_all", 'left', cgeoLeft +geoLSpace)])

def bodyPanel(State):
    #LEFT BUTTONS
    bodyParent=0
    cmds.image("im2",edit=True,image=iconPath + "UIBODY.png",visible=State) 
    cmds.image("im3",edit=True,image=iconPath + "UIHAND.png",visible=State) 
    jointButs=["pelvis", "spine_01", "spine_02", "spine_03", "spine_04", "spine_05", "neck_02", "head", "clavicle_r", "clavicle_l", "thigh_r", "thigh_l", "calf_r", "calf_l", "foot_r", "foot_l", "upperarm_r", "upperarm_l", "lowerarm_r", "lowerarm_l", "hand_r", "hand_l", "root"]
    for i in range(len(jointButs)):
        cmds.symbolButton(jointButs[i], edit=True,visible=State)
    cmds.canvas("c1", edit=True, visible=State)
    cmds.canvas("c2", edit=True, visible=State)
    
    
    geoTop=532
    geoLeft=20
    geoSpace=20
    geoLSpace=109
    cgeoLeft=10
    gheadMesh = ["body","combined","flipflops", "all"]
    for i in range(len(gheadMesh)):
        cmds.symbolButton("g" + gheadMesh[i],edit=True,command=lambda x, i=i:meshSelC(gheadMesh[i],1),visible=State)
        cmds.symbolButton("g" + "custom_" + gheadMesh[i],edit=True,command=lambda x, i=i:meshSelC("custom_" + gheadMesh[i],1),visible=State)
    
    cmds.symbolButton("gall",edit=True,command=lambda x: selectAllGeo(2))
    cmds.symbolButton("gcustom_all",edit=True,command=lambda x: selectAllGeo(3))
    lodTop=675
    lodLeft=20
    lodSpace=25
    for i in range(8):
        
        cmds.text("t" + str(i),edit=True, visible=State)
        if i == 0:
            cmds.symbolButton("lod" + str(i),edit=True, image=iconPath + "UIButtonEmptySRT.png", visible=State)
        else:
            cmds.symbolButton("lod" + str(i),edit=True, image=iconPath + "UIButtonEmptySRTPressed.png", visible=State)
    
    
    lodtL=10
    lodtT=-20

        
    cmds.formLayout( "formLay2", edit=True,visible=True, attachForm=[("im2", 'top', bodyParent+20), ("im2", 'left', 9),("im3", 'top', bodyParent+385), ("im3", 'left', 25),
                                                ("pelvis", 'top', bodyParent+187), ("pelvis", 'left', 117),("spine_01", 'top', bodyParent+167), ("spine_01", 'left', 117),("spine_02", 'top', bodyParent+147), ("spine_02", 'left', 117),("spine_03", 'top', bodyParent+127), ("spine_03", 'left', 117),("spine_04", 'top', bodyParent+107), ("spine_04", 'left', 117),("spine_05", 'top', bodyParent+87), ("spine_05", 'left', 117),
                                                ("neck_02", 'top', bodyParent+67), ("neck_02", 'left', 117),("head", 'top', bodyParent+47), ("head", 'left', 117),("clavicle_r", 'top', bodyParent+117), ("clavicle_r", 'left', 100),("clavicle_l", 'top', bodyParent+117), ("clavicle_l", 'left', 134), ("thigh_r", 'top', bodyParent+202), ("thigh_r", 'left', 100),("thigh_l", 'top', bodyParent+202), ("thigh_l", 'left', 134),
                                                ("calf_r", 'top', bodyParent+257), ("calf_r", 'left', 97),("calf_l", 'top', bodyParent+257), ("calf_l", 'left', 137),("foot_r", 'top', bodyParent+332), ("foot_r", 'left', 92),("foot_l", 'top', bodyParent+332), ("foot_l", 'left', 142),("upperarm_r", 'top', bodyParent+107), ("upperarm_r", 'left', 79),("upperarm_l", 'top', bodyParent+107), ("upperarm_l", 'left', 155),
                                                ("lowerarm_r", 'top', bodyParent+142), ("lowerarm_r", 'left', 54),("lowerarm_l", 'top', bodyParent+142), ("lowerarm_l", 'left', 180),("hand_r", 'top', bodyParent+172), ("hand_r", 'left', 35),("hand_l", 'top', bodyParent+172), ("hand_l", 'left', 200), ("root", 'top', bodyParent+347), ("root", 'left', 117),
                                                ("c1", 'top',bodyParent+510), ("c1", 'left', 20),("c2", 'top',bodyParent+690), ("c2", 'left', 20),
                                                ("gbody", 'top', geoTop), ("gbody", 'left', geoLeft),("gcombined", 'top', geoTop+geoSpace), ("gcombined", 'left', geoLeft),("gflipflops", 'top', geoTop+2*geoSpace), ("gflipflops", 'left', geoLeft), ("gall", 'top', geoTop+3*geoSpace), ("gall", 'left', geoLeft),
                                                ("gcustom_body", 'top', geoTop), ("gcustom_body", 'left', cgeoLeft),("gcustom_combined", 'top', geoTop+geoSpace), ("gcustom_combined", 'left', cgeoLeft),("gcustom_flipflops", 'top', geoTop+2*geoSpace), ("gcustom_flipflops", 'left', cgeoLeft), ("gcustom_all", 'top', geoTop+3*geoSpace), ("gcustom_all", 'left', cgeoLeft),])
    hrIndexPos =[450,72]
    hlIndexPos =[450,167]
    hrjointButs=["index_0", "middle_0", "ring_0", "pinky_0", "thumb_0"]
    direx = ["r", "l"]
    for i in range(len(hrjointButs)):
        for y in range(3):
            for z in range(2):
                cmds.symbolButton(hrjointButs[i] + str(y+1) + "_" + direx[z], edit=True, command=lambda x, i=i,y=y,z=z:meshSelC(hrjointButs[i] + str(y+1) + "_" + direx[z],2), image=iconPath + "JointButtonH.png", visible=State)
        
    
    cmds.formLayout( "formLay2", edit=True, attachForm=[("index_01_r", 'top', hrIndexPos[0]), ("index_01_r", 'left', hrIndexPos[1]+2),("middle_01_r", 'top', hrIndexPos[0]+5), ("middle_01_r", 'left', hrIndexPos[1]-12),("ring_01_r", 'top', hrIndexPos[0]), ("ring_01_r", 'left', hrIndexPos[1]-22),("pinky_01_r", 'top', hrIndexPos[0]-8), ("pinky_01_r", 'left', hrIndexPos[1]-30),("thumb_01_r", 'top', hrIndexPos[0]-22), ("thumb_01_r", 'left', hrIndexPos[1]+12),
                    ("index_02_r", 'top', hrIndexPos[0]+20), ("index_02_r", 'left', hrIndexPos[1]+5),("middle_02_r", 'top', hrIndexPos[0]+25), ("middle_02_r", 'left', hrIndexPos[1]-15),("ring_02_r", 'top', hrIndexPos[0]+18), ("ring_02_r", 'left', hrIndexPos[1]-30),("pinky_02_r", 'top', hrIndexPos[0]+2), ("pinky_02_r", 'left', hrIndexPos[1]-40),("thumb_02_r", 'top', hrIndexPos[0]-12), ("thumb_02_r", 'left', hrIndexPos[1]+26),
                    ("index_03_r", 'top', hrIndexPos[0]+40), ("index_03_r", 'left', hrIndexPos[1]+10),("middle_03_r", 'top', hrIndexPos[0]+42), ("middle_03_r", 'left', hrIndexPos[1]-20),("ring_03_r", 'top', hrIndexPos[0]+32), ("ring_03_r", 'left', hrIndexPos[1]-36),("pinky_03_r", 'top', hrIndexPos[0]+12), ("pinky_03_r", 'left', hrIndexPos[1]-49),("thumb_03_r", 'top', hrIndexPos[0]-8), ("thumb_03_r", 'left', hrIndexPos[1]+39)])
    
    cmds.formLayout( "formLay2", edit=True, attachForm=[("index_01_l", 'top', hlIndexPos[0]), ("index_01_l", 'left', hlIndexPos[1]-2),("middle_01_l", 'top', hlIndexPos[0]+5), ("middle_01_l", 'left', hlIndexPos[1]+12),("ring_01_l", 'top', hlIndexPos[0]), ("ring_01_l", 'left', hlIndexPos[1]+22),("pinky_01_l", 'top', hlIndexPos[0]-8), ("pinky_01_l", 'left', hlIndexPos[1]+30),("thumb_01_l", 'top', hlIndexPos[0]-22), ("thumb_01_l", 'left', hlIndexPos[1]-12),
                    ("index_02_l", 'top', hlIndexPos[0]+20), ("index_02_l", 'left', hlIndexPos[1]-5),("middle_02_l", 'top', hlIndexPos[0]+25), ("middle_02_l", 'left', hlIndexPos[1]+15),("ring_02_l", 'top', hlIndexPos[0]+18), ("ring_02_l", 'left', hlIndexPos[1]+30),("pinky_02_l", 'top', hlIndexPos[0]+2), ("pinky_02_l", 'left', hlIndexPos[1]+40),("thumb_02_l", 'top', hlIndexPos[0]-12), ("thumb_02_l", 'left', hlIndexPos[1]-26),
                    ("index_03_l", 'top', hlIndexPos[0]+40), ("index_03_l", 'left', hlIndexPos[1]-10),("middle_03_l", 'top', hlIndexPos[0]+42), ("middle_03_l", 'left', hlIndexPos[1]+20),("ring_03_l", 'top', hlIndexPos[0]+32), ("ring_03_l", 'left', hlIndexPos[1]+36),("pinky_03_l", 'top', hlIndexPos[0]+12), ("pinky_03_l", 'left', hlIndexPos[1]+49),("thumb_03_l", 'top', hlIndexPos[0]-8), ("thumb_03_l", 'left', hlIndexPos[1]-39)])
 
    
    

toggleCheck = 2
def togglePanel():
    global toggleCheck
    if toggleCheck == 0:
        bodyPanel(False)
        headPanel(True)
        toggleCheck = 1
        cmds.symbolButton("gcustom_all",edit=True, command=lambda x: selectAllGeo(1))
    else:
        headPanel(False)
        bodyPanel(True)
        toggleCheck = 0
        cmds.symbolButton("gcustom_all",edit=True, command=lambda x: selectAllGeo(3))
        
       
#LEFTPANELBUTTON
def leftPanelButtonV(worldCheck):
    global toggleCheck
    imagepath=iconPath + "JointButton.png"
        
    worldCheck = 0
    if cmds.objExists("spine_04") or cmds.objExists("OpenedDNAInfoNode"):
        worldCheck = 1
    if cmds.objExists("LoadedDNAInfoNode"):
        worldCheck = 2
    if cmds.objExists ("rl4Embedded_Archetype") or cmds.objExists ("rl4Embedded_Archtype"):
        worldCheck = 3 
    if cmds.objExists ("DHIhead:spine_04"):
        worldCheck = 4
    if cmds.objExists("body_gen_node") or cmds.objExists("root_drv"):
        worldCheck = 5
    if cmds.objExists("FixBodyInfoNode"):
        worldCheck = 6 

    
    #OPEN DNA
    if worldCheck==0:
        toggleCheck = 2
        headPanel(False)
        bodyPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=80
        for i in range(10):
            if i == 0:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [1,2,9]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [3,4,5,6,7,8]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
        
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout( "formLay", edit=True, attachForm=[("b10", 'top', butTop + 3*butH+offsetTop), ("b10", 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=False)
        cmds.symbolButton("Toggle", edit=True, enable=False)
    
    
    #LOAD DNA
    if worldCheck==1:
        toggleCheck = 2
        headPanel(False)
        bodyPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=80
        for i in range(10):
            if i in [0,1]:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [2,9]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [3,4,5,6,7,8]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout( "formLay", edit=True, attachForm=[("b10", 'top', butTop + 3*butH+offsetTop), ("b10", 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=False)
        cmds.symbolButton("Toggle", edit=True, enable=False)


    #MODIFICATIONS
    if worldCheck==2:
        toggleCheck = 0
        bodyPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=80
        for i in range(10):
            if i in [2,9]:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [0,1]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [3,4,5,6,7,8]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout( "formLay", edit=True, attachForm=[("b10", 'top', butTop + 3*butH+offsetTop), ("b10", 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=True)
        headPanel(True)  
        #cmds.symbolButton("Toggle", edit=True, enable=False)
    
    
    #PREPARE TO EXPORT
    if worldCheck==3:
        toggleCheck = 2
        headPanel(False)
        bodyPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=-80
        for i in range(10):
            if i in [3,9]:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [4,5,6,7,8]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [0,1,2]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=False)
        cmds.symbolButton("Toggle", edit=True, enable=False)


    #LOAD BODY
    if worldCheck==4:
        toggleCheck = 2
        headPanel(False)
        bodyPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=-80
        for i in range(10):
            if i in [4,9]:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [3,5,6,7,8]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [0,1,2]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=False)
        cmds.symbolButton("Toggle", edit=True, enable=False)


    #BODY MODIFICATIONS
    if worldCheck==5:
        toggleCheck = 1
        headPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=-80
        for i in range(10):
            if i in [5,7,8,9]:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [3,4,6]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [0,1,2]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=True)
        bodyPanel(True)
        cmds.symbolButton("Toggle", edit=True, enable=True)
        
    
    #FIXED BODY END                      
    if worldCheck==6:
        toggleCheck = 1
        headPanel(False)
        #RIGHT BUTTONS
        butTop = 250
        butH = 41
        butW=44
        offsetTop=-80
        for i in range(10):
            if i in [5,6,7,8,9]:
                StateVis = True
                StateEnab = True
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [3,4]:
                StateVis = True
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            if i in [0,1,2]:
                StateVis = False
                StateEnab = False
                cmds.symbolButton("b" + str(i+1), edit=True, image=iconPath + "UIButton" + str(i+1) + ".png", visible=StateVis ,enable=StateEnab)
            cmds.formLayout( "formLay", edit=True, attachForm=[("b" + str(i+1), 'top', butTop+i*butH+offsetTop), ("b" + str(i+1), 'left', butW)])
        cmds.formLayout("formLay2", edit=True,visible=True)
        
        bodyPanel(True)
        cmds.symbolButton("Toggle", edit=True, enable=True)
        
        
        
        
        
        

def yzUP():
    # Get the current up axis from the preferences
    up_axis = cmds.upAxis(q=True, axis=True)
    
    # Toggle the up axis based on the current value
    if up_axis == 'y':
        cmds.upAxis(axis='z')
        final_up_axis = 'z'
        cmds.symbolButton("yUP", edit=True,image=iconPath + "Zup.png")
    else:
        cmds.upAxis(axis='y')
        final_up_axis = 'y'
        cmds.symbolButton("yUP",edit=True,image=iconPath + "Yup.png")
    
    # Print the final up axis
    print("Final up axis:", final_up_axis)


 
def centerF():
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        if cmds.objExists(obj):
            cmds.xform(obj, translation=[0, 0, 0], worldSpace=True)
def freezeF():
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        if cmds.objExists(obj):
            cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1)
def unlockF():
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        if cmds.objExists(obj):
            for attr in ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]:
                cmds.setAttr(obj + "." + attr, lock=False)   



def lodLayerC(lodN):
    for i in range(8):
        cmds.symbolButton("lod"+str(i), edit=True, image=iconPath + "UIButtonEmptySRTPressed.png")
        cmds.setAttr("head_lod"+str(i)+"_layer" + ".visibility", False)
        if cmds.objExists("root_drv"):
            cmds.setAttr("body_lod"+str(i//2)+"_layer" + ".visibility", False)
    cmds.symbolButton("lod"+str(lodN), edit=True, image=iconPath + "UIButtonEmptySRT.png")
    cmds.setAttr("head_lod"+str(lodN)+"_layer" + ".visibility", True)
    if cmds.objExists("root_drv"):
        cmds.setAttr("body_lod"+str(lodN//2)+"_layer" + ".visibility", True)
    global sceneLodN
    sceneLodN = str(lodN)
    global scenebodyLodN
    scenebodyLodN = str(lodN//2)
    cmds.symbolButton("gcustom_all",edit=True,enable=False, visible=True)
    checkSceneSel()













def codeblock (dnaPath, ROOT_DIR, CHARACTER_NAME, MAIN_PATH, body_type):
    
    #DATAS DNA
    output_file_path = os.path.join(f"{ROOT_DIR}/examples", "datas_dna.py")
    with open(f"{ROOT_DIR}/examples/dna_viewer_grab_changes_from_scene_and_propagate_to_dna.py") as file:
        lines_all = file.readlines()
        lines = lines_all[43:204]
        lineslists = lines_all[217:220]
        linesload = lines_all[220:226] 
        lines2 = lines_all[232:247]  
        lines3 =  lines_all[232:246]  
        defload = ["def load_dna_data():\n"]
        defsave = ["def save_dna_data():\n"]
        defsaveraw = ["def save_dna_data_raw():\n"]
        lines = [line.replace('f"{ospath.dirname(ospath.abspath(__file__))}/..".replace("\\\\", "/")','"'+ROOT_DIR+'"') for line in lines]
        lines = [line.replace('f"{DNA_DIR}/{CHARACTER_NAME}.dna"', '"'+dnaPath+'"') for line in lines]
        lines = [line.replace('"Ada"','"'+CHARACTER_NAME+'"') for line in lines]
        linesload = ["    " + line for line in linesload]
        lines2 = ["    " + line for line in lines2]
        lines3 = ["    " + line for line in lines3]
    code_block = ''.join(lines + lineslists + defload + linesload + defsave + lines2 + defsaveraw + lines3)
    with open(output_file_path, "w") as output_file:
        output_file.write(code_block)
        
        
    #DAT FILE
    file_path = os.path.join("c:/Arts and Spells/Scripts", "dat.py")    
    tRoot = ["ROOT_DIR = " + '"' +ROOT_DIR+ '"' + "\n"]
    tMain = ["MAIN_PATH = " + '"' +MAIN_PATH+ '"' + "\n"]
    tDNA = ["dnaPath= " + '"' +dnaPath+ '"' + "\n"]
    tBody = ["body_type = " + '"' +body_type+ '"' + "\n"]
    tVer = ["MAYA_VERSION = " + '"' + str(MAYA_VERSION) + '"' + "\n"]
    dat_code_block = ''.join(tRoot + tMain + tDNA + tBody + tVer) 
    directory = 'c:/Arts and Spells/Scripts'
    if not os.path.exists(directory):
        os.makedirs(directory)   
    with open(file_path, "w") as datfile:
        datfile.write(dat_code_block)


def savePref(textdnaPath, textROOT_DIR, textMAIN_PATH, textbody_type):
    global body_type
    global ROOT_DIR
    global MAIN_PATH
    global dnaPath
    character_dna = cmds.textField(textdnaPath, q=True, text=True)
    ROOT_DIR = cmds.textField(textROOT_DIR, q=True, text=True)
    MAIN_PATH = cmds.textField(textMAIN_PATH, q=True, text=True)
    body_type = cmds.textField(textbody_type, q=True, text=True)
    CHARACTER_DNA = ospath.abspath(character_dna)
    CHARACTER_DNA = CHARACTER_DNA.replace("\\", "/")
    CHARACTER_NAME = os.path.basename(CHARACTER_DNA).split(".")[0]
    
    chX=2
    file_path = os.path.join("c:/Arts and Spells/Scripts", "dat.py")
    if os.path.exists(file_path):
        chX=0
    else:
        chX=1
        
    print(f"New DNA_DIR: {CHARACTER_DNA}")
    print(f"New DNA_Name: {CHARACTER_NAME}")
    print(f"New Body_Type: {body_type}")
    codeblock (CHARACTER_DNA, ROOT_DIR, CHARACTER_NAME, MAIN_PATH, body_type)
    if os.path.exists(file_path):
        import dat
        importlib.reload(dat)
        ROOT_DIR = dat.ROOT_DIR
        MAIN_PATH = dat.MAIN_PATH
        dnaPath = dat.dnaPath
        body_type = dat.body_type
    if chX==1:
        if cmds.window("prefWindow", exists=True):
            cmds.deleteUI("prefWindow", window=True)
        mFree_window()
    else:
        if cmds.window("prefWindow", exists=True):
            cmds.deleteUI("prefWindow", window=True)
    
def prefUI(dnaPath, ROOT_DIR, MAIN_PATH, body_type):
    heightSpa=20
    heightField=25
    file_path = "c:/Arts and Spells/Scripts" + "/dat.py"
    if os.path.exists(file_path):
        import dat
        importlib.reload(dat)
        ROOT_DIR = dat.ROOT_DIR
        MAIN_PATH = dat.MAIN_PATH
        dnaPath = dat.dnaPath
        body_type = dat.body_type
    if cmds.window("prefWindow", exists=True):
        cmds.deleteUI("prefWindow", window=True)
    
    cmds.window("prefWindow", title="Metapipe Preferences", widthHeight=(200, 100), bgc=(0.3,0.3,0.3),resizeToFitChildren=True,sizeable=False)
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="",height=25)
    cmds.text(label="DNA CALIBRATION PATH:",height=30, font="boldLabelFont")
    textROOT_DIR = cmds.textField(text=ROOT_DIR, bgc=(0.2,0.2,0.2), height=heightField)
    cmds.text(label="",height=heightSpa)
    cmds.text(label="METAPIPE FILES PATH:",height=30, font="boldLabelFont")
    textMAIN_PATH = cmds.textField(text=MAIN_PATH, bgc=(0.2,0.2,0.2),height=heightField)
    cmds.text(label="",height=heightSpa)
    cmds.text(label="METAHUMAN DNA FILE PATH:",height=30, font="boldLabelFont")
    textdnaPath = cmds.textField(text=dnaPath, bgc=(0.2,0.2,0.2),height=heightField)
    cmds.text(label="",height=heightSpa)
    cmds.text(label="METAHUMAN BODY TYPE:",height=30, font="boldLabelFont")
    textbody_type = cmds.textField(text=body_type, bgc=(0.2,0.2,0.2),height=heightField)
    cmds.text(label="",height=heightSpa)
    cmds.rowLayout(numberOfColumns=2, columnWidth2=(250, 200))
    cmds.button(label="SAVE", command=lambda x: savePref(textdnaPath, textROOT_DIR, textMAIN_PATH, textbody_type))
    cmds.button(label="Cancel", command=lambda x: cmds.deleteUI("prefWindow", window=True))
    
    cmds.showWindow("prefWindow")


def mFree_window():
    # Create window
    window_name = "MetaPipe"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name, title=window_name, width=1360, height=768, sizeable=True, resizeToFitChildren=True, menuBar=False, tlc=(0, 0), tb=False, tbm=False)
    layout = cmds.formLayout(bgc=(0,0,0))
    cmds.image(image=iconPath + "UICover.png", p=layout)
    
    cmds.showWindow()

mFree_window()
time.sleep (1)
def mFree_window():
    
    #WINDOW
    window_name = "MetaPipe"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name, title=window_name, wh=(1368, 768), sizeable=True, resizeToFitChildren=True, menuBar=False, tlc=(0, 0))
    
    color = (0.135135, 0.360326, 0.715)  
    backGr = (0.08, 0.08, 0.08)
    buttonColor = (0.25, 0.25, 0.25) 
    
    layout = cmds.paneLayout(bgc=backGr, cn="quad", ps=[[1, 83,95], [2, 17, 95], [3, 1,5]], st=5)
    layout2 = cmds.paneLayout(bgc=backGr, cn="vertical2", ps=[[1, 20, 1], [2, 80, 1]], st=5, p=layout)
    formLay = cmds.formLayout("formLay", w=240, p=layout2)
    
    
    #LEFT PANEL
    
    

    #SETTINGS
    settings=cmds.symbolButton("settings",image=iconPath + "UISettings.png")
    cmds.popupMenu(parent="settings", button=1, mm=1)
    cmds.menuItem(label="New", command=lambda x:newScene())
    cmds.menuItem(label="Starter Scene", command=lambda x:loadScene("Custom Head"))
    cmds.menuItem(label="Recent Scene", command=lambda x:loadScene("Checkpoint"))
    cmds.menuItem(label="Save Scene", command=lambda x:saveScene())
    cmds.menuItem(label="Import...", command=lambda x:import_obj())
    cmds.menuItem(label="Export", command=lambda x:export_fbx())
    cmds.menuItem(label="Shape Editor", command=lambda x:shapeEdit())
    cmds.menuItem(label="Selection Panel", command=lambda x:cmds.formLayout( formLay2, edit=True,visible = True))
    cmds.menuItem(label="Preferences", command=lambda x:prefUI(dnaPath, ROOT_DIR, MAIN_PATH, body_type))
    

    im1 = cmds.image(image=iconPath + "UI LOGO.png")
    #TOP
    yUP=cmds.symbolButton("yUP", command=lambda x: yzUP(),image=iconPath + "yUP.png")
    center0=cmds.symbolButton("center0", command=lambda x: centerF(),image=iconPath + "center.png")
    freeze0=cmds.symbolButton("freeze0", command=lambda x: freezeF(),image=iconPath + "freeze.png")
    unlock0=cmds.symbolButton("unlock0", command=lambda x: unlockF(),image=iconPath + "unlock.png")
    
    
    
    
    #BUTTONS
    butTop = 250
    butH = 41
    butW=44
    offsetTop=0
    
    b1=cmds.symbolButton("b1", command=lambda x: buildDNA("free"),image=iconPath + "UIButton1Pressed.png",enable=False)
    b2=cmds.symbolButton("b2",command=lambda x: loadDNA(), image=iconPath + "UIButton2Pressed.png", enable=False)
    b3=cmds.symbolButton("b3",command=lambda x: saveDNA(), image=iconPath + "UIButton3Pressed.png", enable=False)
    b4=cmds.symbolButton("b4",command=lambda x: prepare_export(), image=iconPath + "UIButton4Pressed.png", enable=False)
    b5=cmds.symbolButton("b5",command=lambda x: build_body(), image=iconPath + "UIButton5Pressed.png", enable=False)
    b8=cmds.symbolButton("b6",command=lambda x: fixbody(), image=iconPath + "UIButton6Pressed.png", enable=False)
    b9=cmds.symbolButton("b7",command=lambda x: connect_body(), image=iconPath + "UIButton7Pressed.png", enable=False)
    b6=cmds.symbolButton("b8",command=lambda x: bindSkinC(), image=iconPath + "UIButton8Pressed.png", enable=False)
    b7=cmds.symbolButton("b9",command=lambda x: copySkin(), image=iconPath + "UIButton9Pressed.png", enable=False)
    b10=cmds.symbolButton("b10",command=lambda x:findCustom(), image=iconPath + "UIButton10Pressed.png", enable=False)
    
    #MODIFY PANEL
    t1=cmds.text(label="MODIFY PANEL", height=30, font="boldLabelFont", p=formLay)
    
    
    #FORMLAY
    cmds.formLayout(formLay, edit=True, attachForm=[(t1, 'top', 695), (t1, 'left', 83), 
                                    
                    (im1, 'top', 20), (im1, 'left', 14),
                    (settings, 'top', 15), (settings, 'left', 5),(yUP, 'top', 7), (yUP, 'left', 210),
                    (center0, "top", 7), (center0, "left", 150), (freeze0, "top", 7), (freeze0, "left", 170), (unlock0, "top", 7), (unlock0, "left", 190)])
    
    
    
    
    #MID PANEL 3D VIEWER
    panel_name = cmds.modelPanel(p=layout2)
    cmds.control(panel_name, edit=True)
    cmds.modelEditor(panel_name, edit=True, da="smoothShaded")
    cmds.grid(toggle=False)
    cmds.viewFit()
    
    
    
    #RIGHT PANEL
    bodyParent=0
    formLay2 = cmds.formLayout("formLay2", w=240, p=layout) 
    im2 = cmds.image("im2", image=iconPath + "UIBODY.png",visible=False) 
    im3 = cmds.image("im3", image=iconPath + "UIHAND.png",visible=False) 
    im4 = cmds.image("im4", image=iconPath + "UIHEAD.png",visible=False) 
    
    cmds.symbolButton("Toggle", command=lambda x: togglePanel(), image=iconPath + "Toggle.png",visible=True)
    cmds.symbolButton("Close", command=lambda x: cmds.formLayout( formLay2, edit=True,visible = False), image=iconPath + "Close.png",visible=True)
    cmds.formLayout( formLay2, edit=True, attachForm=[("Toggle", 'top', 10), ("Toggle", 'left', 10),("Close", 'top', 10), ("Close", 'left', 210)])
    
    #SKELETON HIERARCHY
    imagepath=iconPath + "JointButton.png"
    jointButs=["pelvis", "spine_01", "spine_02", "spine_03", "spine_04", "spine_05", "neck_02", "head", "clavicle_r", "clavicle_l", "thigh_r", "thigh_l", "calf_r", "calf_l", "foot_r", "foot_l", "upperarm_r", "upperarm_l", "lowerarm_r", "lowerarm_l", "hand_r", "hand_l", "FACIAL_C_Jaw", "FACIAL_C_TeethUpper", "FACIAL_C_TeethLower", "root"]
    for i in range(len(jointButs)):
        State=False
        cmds.symbolButton(jointButs[i], command=lambda x, i=i: jointSelectionC(jointButs[i]), image=imagepath,visible=State)
    
    #HANDS
    hrIndexPos =[450,72]
    hlIndexPos =[450,167]
    hrjointButs=["index_0", "middle_0", "ring_0", "pinky_0", "thumb_0"]
    direx = ["r", "l"]
    for i in range(len(hrjointButs)):
        for y in range(3):
            for z in range(2):
                cmds.symbolButton(hrjointButs[i] + str(y+1) + "_" + direx[z],  visible=False)
    

    titleName = ["RIGHT EYE", "LEFT EYE", "MOUTH"]
    for i in range(3):
        cmds.text("title" + str(i+1), label= titleName[i],visible=State)
        
    #FACIAL / EYES / MOUTH
    ebutTop = 410
    ebutL = 157
    ebutR = 50
    ebutSpace=12
    ebutWSpa=12
    
    mbutTop = 515
    mbutR = 92
    mbutSpace=12
    mbutWSpa=12
    eyeList = ["", "CornerOuter", "CornerInner"]
    mouthList = ["R", "L", "C"]
    mouthSymList = ["UpperOuter", "Corner", "LowerOuter"]
    propers = ["Upper","Lower", "A", "B"]
    for i in range(3):
        State=False

        for y in range(2):
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[0] + propers[3] + str(i+1), command=lambda x, y=y, i=i: jointSelectionC("FACIAL_" + mouthList[y] + "_Eyelid" + propers[0] + propers[3] + str(i+1)), image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[0] + propers[2] + str(i+1), command=lambda x, y=y, i=i: jointSelectionC("FACIAL_" + mouthList[y] + "_Eyelid" + propers[0] + propers[2] + str(i+1)), image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[1] + propers[2] + str(i+1), command=lambda x, y=y, i=i: jointSelectionC("FACIAL_" + mouthList[y] + "_Eyelid" + propers[1] + propers[2] + str(i+1)), image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eyelid" + propers[1] + propers[3] + str(i+1), command=lambda x, y=y, i=i: jointSelectionC("FACIAL_" + mouthList[y] + "_Eyelid" + propers[1] + propers[3] + str(i+1)), image=imagepath,visible=State)

            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Eye" + eyeList[i], command=lambda x, y=y, i=i: jointSelectionC("FACIAL_" + mouthList[y] + "_Eye" + eyeList[i]), image=imagepath,visible=State)
            cmds.symbolButton("FACIAL_" + mouthList[y] + "_Lip" + mouthSymList[i], command=lambda x, y=y, i=i: jointSelectionC("FACIAL_" + mouthList[y] + "_Lip" + mouthSymList[i]), image=imagepath,visible=State)
        
        cmds.symbolButton("FACIAL_" + mouthList[i] + "_LipUpper", command=lambda x, i=i: jointSelectionC("FACIAL_" + mouthList[i] + "_LipUpper"), image=imagepath,visible=State)
        cmds.symbolButton("FACIAL_" + mouthList[i] + "_LipLower", command=lambda x, i=i: jointSelectionC("FACIAL_" + mouthList[i] + "_LipLower"), image=imagepath,visible=State)
        

    #MESH SELECTION
    geoTop=562
    geoLeft=20
    geoSpace=20
    geoLSpace=109
    gheadMesh = ["head","teeth","saliva","eyeLeft","eyeshell","eyelashes","eyeEdge","cartilage","eyeRight", "all"]
    for i in range(len(gheadMesh)):
        State=False
        cmds.symbolButton("g" + gheadMesh[i],command=lambda x, i=i:meshSelC(gheadMesh[i],0),image=iconPath + "UIGeo" + gheadMesh[i] + ".png",visible=State)
        cmds.symbolButton("g" + "custom_" + gheadMesh[i],command=lambda x, i=i:meshSelC("custom_" + gheadMesh[i],0),image=iconPath + "UIGeoC.png",enable=False, visible=State)
    gheadMesh = ["body","combined","flipflops"]
    for i in range(len(gheadMesh)):
        State=False
        cmds.symbolButton("g" + gheadMesh[i],command=lambda x, i=i:meshSelC(gheadMesh[i],1),image=iconPath + "UIGeo" + gheadMesh[i] + ".png",visible=State)
        cmds.symbolButton("g" + "custom_" + gheadMesh[i],command=lambda x, i=i:meshSelC("custom_" + gheadMesh[i],1),image=iconPath + "UIGeoC.png",enable=False, visible=State)
        
        
    
    
    #LOD SELECTION
    lodTop=655
    lodLeft=20
    lodSpace=25
    for i in range(8):
        cmds.symbolButton("lod" + str(i), command=lambda x, i=i: lodLayerC(i), image=iconPath + "UIButtonEmptyPressed.png",visible=False)
        cmds.text("t" + str(i), label=str(i), height=30, font="boldLabelFont", p=formLay2,visible=False)
    lodtL=10
    lodtT=-20
    
    
    #SEPERATION LINES
    cBGC=(0.4, 0.4, 0.4)
    c1=cmds.canvas("c1", height=1, width=200, bgc=cBGC, p=formLay2,visible=False)
    c2=cmds.canvas("c2", height=1, width=200, bgc=cBGC, p=formLay2,visible=False)
    
    
    #SELECTION PANEL
    t2=cmds.text("tSELECTION PANEL",label="SELECTION PANEL", height=30, font="boldLabelFont", p=formLay2)

    
    

    
    #FORMLAY2
    cmds.formLayout( formLay2, edit=True, attachForm=[(im2, 'top', bodyParent+20), (im2, 'left', 9),(im3, 'top', bodyParent+20), (im3, 'left', 9),(im4, 'top', bodyParent+20), (im4, 'left', 49),

                                                    ("lod0", 'top', lodTop), ("lod0", 'left', lodLeft),("lod1", 'top', lodTop), ("lod1", 'left', lodLeft+lodSpace),("lod2", 'top', lodTop), ("lod2", 'left', lodLeft+2*lodSpace),("lod3", 'top', lodTop), ("lod3", 'left', lodLeft+3*lodSpace),
                                                    ("lod4", 'top', lodTop), ("lod4", 'left', lodLeft+4*lodSpace),("lod5", 'top', lodTop), ("lod5", 'left', lodLeft+5*lodSpace),("lod6", 'top', lodTop), ("lod6", 'left', lodLeft+6*lodSpace),("lod7", 'top', lodTop), ("lod7", 'left', lodLeft+7*lodSpace),
                                                    
                                                    ("t0", 'top', lodTop+lodtT), ("t0", 'left', lodLeft+lodtL),("t1", 'top', lodTop+lodtT), ("t1", 'left', lodLeft+lodSpace+lodtL),("t2", 'top', lodTop+lodtT), ("t2", 'left', lodLeft+2*lodSpace+lodtL),("t3", 'top', lodTop+lodtT), ("t3", 'left', lodLeft+3*lodSpace+lodtL),
                                                    ("t4", 'top', lodTop+lodtT), ("t4", 'left', lodLeft+4*lodSpace+lodtL),("t5", 'top', lodTop+lodtT), ("t5", 'left', lodLeft+5*lodSpace+lodtL),("t6", 'top', lodTop+lodtT), ("t6", 'left', lodLeft+6*lodSpace+lodtL),("t7", 'top', lodTop+lodtT), ("t7", 'left', lodLeft+7*lodSpace+lodtL),
                                                    
                                                    (c1, 'top', 370), (c1, 'left', 20),(c2, 'top', 550), (c2, 'left', 20),
                                                    
                                                    (t2, 'top', 695), (t2, 'left', 76)])

    cmds.formLayout("formLay2", edit=True,visible=False)
    
    
    
    #WINDOW CHECK
    if cmds.objExists ("spine_04"):
        if cmds.objExists ("rl4Embedded_Archetype"):
            leftPanelButtonV(3)
        else:
            leftPanelButtonV(1)
    else:
        leftPanelButtonV(0)
        
    file_path = "c:/Arts and Spells/Scripts/dat.py"
    if os.path.exists(file_path):
        cmds.showWindow()
    else:
        prefUI(dnaPath, ROOT_DIR, MAIN_PATH, body_type)
    checkSceneSel()
    if not cmds.objExists("metapipefreewindow"):
        cmds.createNode("transform", name="metapipefreewindow")
    
def get_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
#mFree_window()