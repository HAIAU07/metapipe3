#All Rights Belongs to Uzay CALISKAN
#Artstation Marketplace Standart License 
import os
import maya.cmds as cmds
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
gender_mesh = "m_med_nrw_body_lod0_mesh"  
 
def build_body(ROOT_DIR):
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

def connect_body():
    bodyNS = "DHIbody:"
    headNS = "DHIhead:"
    
    for i in cmds.ls(type="joint"):
        if headNS in i:
            if i.replace(headNS,bodyNS) in cmds.ls(type="joint"):
                cmds.parentConstraint(i.replace(headNS,bodyNS),i,mo=True)
                cmds.scaleConstraint(i.replace(headNS,bodyNS),i,mo=True)
    
#build_body()