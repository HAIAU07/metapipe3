#All Rights Belongs to Uzay CALISKAN
#Artstation Marketplace Standart License 

import sys
import os
import maya.cmds as cmds

def export_fbx(ROOT_DIR):

    
    
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
    

