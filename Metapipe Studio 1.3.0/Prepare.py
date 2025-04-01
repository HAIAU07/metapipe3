#All Rights Belongs to Uzay CALISKAN
#Artstation Marketplace Standart License 

import sys
import os
import maya.cmds as cmds
import random
def matSet():
    # Get the selection
    selection = cmds.ls(selection=True)



    # Assign the material to each selected object
    for obj in selection:
        # Create a new aiStandardSurface material
        ai_material = cmds.shadingNode('aiStandardSurface', asShader=True)
        
        # Generate a random base color
        base_color = [random.uniform(0, 1) for i in range(3)]
        
        # Set the material's base color
        cmds.setAttr(ai_material + '.baseColor', *base_color)
        
        # Assign the material to the object
        cmds.select(obj)
        cmds.hyperShade(assign=ai_material)

def prepare_export():
    
    import random   
    # Select the meshes under Head
    cmds.select("head_grp|geometry_grp", hierarchy=True)
    selection = cmds.ls(selection=True)

    # Assign the material to each selected object
    for obj in selection:
        # Create a new Lambert material
        material = cmds.shadingNode('lambert', asShader=True)
        base_color = [random.uniform(0, 1) for i in range(3)]
        
        # Set the material's base color
        cmds.setAttr(material + '.color', *base_color, type='double3')
        cmds.select(obj)
        cmds.hyperShade(assign=material)
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
