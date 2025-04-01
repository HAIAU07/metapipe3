#All Rights Belongs to Uzay CALISKAN
#Artstation Marketplace Standart License 

import maya.cmds as cmds
import sys


def body_transformation(gender_mesh):
    
    
    
    
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
    all_joints = list(set(all_joints) - set(exclude_joints))
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
    
    j_name = []
    j_delta_x = []
    j_delta_y = []
    j_delta_z = []
    # DELTA X CALCULATE
    for joint_name in end_joints:
        mesh_name = gender_mesh
    
        # 1. Get the world-space position of the joint
        joint_pos = cmds.xform(joint_name, query=True, worldSpace=True, translation=True)
    
        # 2. Find the nearest vertex named "NVertex" on the mesh to the joint's position
        closest_point_node = cmds.createNode("closestPointOnMesh")
        cmds.connectAttr(mesh_name + ".worldMesh", closest_point_node + ".inMesh")
        cmds.setAttr(closest_point_node + ".inPosition", joint_pos[0], joint_pos[1], joint_pos[2])
    
        nearest_vertex_index = cmds.getAttr(closest_point_node + ".closestVertexIndex")
        cmds.delete(closest_point_node)
        vertex = mesh_name + ".vtx[{}]".format(nearest_vertex_index)
        cmds.select(vertex, replace=True)
        
        # Grow selection
        
        for i in range(1):
        
            # Get the currently selected vertices
            vertices = cmds.ls(selection=True, flatten=True)
            
            # Convert the vertices to edges
            edges = []
            for vertex in vertices:
                edges.extend(cmds.polyListComponentConversion(vertex, fromVertex=True, toEdge=True))
            
            # Select the edges
            cmds.select(edges)
            
            # Get the currently selected edges
            edges = cmds.ls(selection=True, flatten=True)
            
            # Convert the edges to vertices
            vertices = []
            for edge in edges:
                vertices.extend(cmds.polyListComponentConversion(edge, fromEdge=True, toVertex=True))
            
            # Select the vertices
            cmds.select(vertices)
            
            vertices = cmds.ls(selection=True, flatten=True)
        # Add the vertices to a list
        vertex_position_before = []
        for vertex in vertices:
            position = cmds.pointPosition(vertex, world=True)
            vertex_position_before.append(position)
        
    
        # 3 Set the target blendshape node to a weight of 1
        cmds.setAttr("BodyShape.B2", 1)
    
        # 4. Get the new position of NVertex and find the new position
        vertex_position_after = []
        for vertex in vertices:
            position = cmds.pointPosition(vertex, world=True)
            vertex_position_after.append(position)
        
        delta_vertex = [] 
    
        for i in range(len(vertex_position_after)):
            sub_delta = []
            for j in range(3):
                sub_delta.append(vertex_position_after[i][j] - vertex_position_before[i][j])
            delta_vertex.append(sub_delta)
        
        average_vertex = [sum(x) / len(x) for x in zip(*delta_vertex)]
    
        # 5. Move the joint with the distance that NVertex moved
        delta_x = average_vertex[0]
        delta_y = average_vertex[1]
        delta_z = average_vertex[2]
        
        if not cmds.attributeQuery("delta_x", node=joint_name, exists=True):
            cmds.addAttr(joint_name, ln="delta_x", at="double")
        if not cmds.attributeQuery("delta_y", node=joint_name, exists=True):
            cmds.addAttr(joint_name, ln="delta_y", at="double")
        if not cmds.attributeQuery("delta_z", node=joint_name, exists=True):
            cmds.addAttr(joint_name, ln="delta_z", at="double")
        
        cmds.setAttr(joint_name + ".delta_x", delta_x)
        cmds.setAttr(joint_name + ".delta_y", delta_y)
        cmds.setAttr(joint_name + ".delta_z", delta_z)
    
        # 6 Reset
        cmds.setAttr("BodyShape.B2", 0)
        j_name.append(joint_name)
        j_delta_x.append(delta_x)
        j_delta_y.append(delta_y)
        j_delta_z.append(delta_z)
        #cmds.move(delta_x, delta_y, delta_z, joint_name, relative=True)
    for i in range(len(j_name)):
        cmds.move(j_delta_x[i], j_delta_y[i], j_delta_z[i], j_name[i], relative=True)  
    
        
    
    #Fix the body parts
    moving_joint = []
    target_joint = []       
    def fix_body(moving_joint, target_joint):
        m_pos = cmds.xform(moving_joint, query=True, worldSpace=True, rotatePivot=True)
        ta_pos = cmds.xform(target_joint, query=True, worldSpace=True, rotatePivot=True)
        child_joints = cmds.listRelatives(moving_joint, c=True, type="joint")
        child_positions = []
        if child_joints:
            for child_joint in child_joints:
                child_positions.append(cmds.xform(child_joint, q=True, ws=True, t=True))
        # Set the translate and rotate pivot attributes of the "FACIAL_C_LowerLipRotation" joint to match those of "FACIAL_C_MouthUpper"
        cmds.xform(moving_joint, translation=ta_pos, rotatePivot=m_pos, worldSpace=True)
        if child_joints:
            for i, child_joint in enumerate(child_joints):
                cmds.xform(child_joint, ws=True, t=child_positions[i])
        m_pos = cmds.xform(moving_joint, query=True, worldSpace=True, rotatePivot=True)
        ta_pos = cmds.xform(target_joint, query=True, worldSpace=True, rotatePivot=True)
        cmds.xform(target_joint, translation=m_pos, rotatePivot=ta_pos, worldSpace=True)
    
    # Filter joints with a chainDepth value of 0
    CD = 1
    lower_CD = 0
    maxCD = 15
    while CD <= maxCD:
        joint_CD = [joint for joint in all_joints if cmds.getAttr(joint + ".chainDepth") == CD]
        lower_joints = [joint for joint in all_joints if cmds.getAttr(joint + ".chainDepth") == lower_CD]
        for joint_name in joint_CD:
           
           first_place = cmds.xform(joint_name, q=True, ws=True, translation=True)
           child_joints = cmds.listRelatives(joint_name, children=True, type="joint")
           average_point = []
     
           if child_joints:
            
               target_points = []
               for child_joint in child_joints:
                   if child_joint in lower_joints:
                       delta_x = cmds.getAttr(child_joint + '.delta_x')
                       delta_y = cmds.getAttr(child_joint + '.delta_y')
                       delta_z = cmds.getAttr(child_joint + '.delta_z')
                       target_points.append([delta_x, delta_y, delta_z])
                   if child_joint in end_joints:
                       delta_x = cmds.getAttr(child_joint + '.delta_x')
                       delta_y = cmds.getAttr(child_joint + '.delta_y')
                       delta_z = cmds.getAttr(child_joint + '.delta_z')
                       #print(cmds.getAttr(child_joint + ".chainDepth"))
                       target_points.append([delta_x, delta_y, delta_z])
                       target_points.append([delta_x, delta_y, delta_z])
                       target_points.append([delta_x, delta_y, delta_z])
                       target_points.append([delta_x, delta_y, delta_z])
                       target_points.append([delta_x, delta_y, delta_z])
               average_point = [sum(x) / len(x) for x in zip(*target_points)]
               if not average_point:
                   average_point = [0, 0, 0]
               avg_x = average_point[0]
               avg_y = average_point[1]
               avg_z = average_point[2]
               cmds.move(avg_x, avg_y, avg_z, joint_name, relative=True)
               for child_joint in child_joints:
                   cmds.move(-avg_x, -avg_y, -avg_z, child_joint, relative=True)
               pureJoint = joint_name[:-2]
               last_letter = joint_name[-2:]
               joint_name_corrective = pureJoint+"_correctiveRoot"+last_letter
               joint_name_half = pureJoint+"_half"+last_letter
               if joint_name_corrective in all_joints:
                   fix_body(joint_name, joint_name_corrective)
                   #print(joint_name + " fixed to the " + joint_name_corrective)
               if joint_name_half in all_joints:
                   fix_body(joint_name, joint_name_half)
                   #print(joint_name + " fixed to the " + joint_name_half)
               end_place = cmds.xform(joint_name, q=True, ws=True, translation=True)
               delta_x = end_place[0] - first_place[0]
               delta_y = end_place[1] - first_place[1]
               delta_z = end_place[2] - first_place[2]
               if not cmds.attributeQuery("delta_x", node=joint_name, exists=True):
                   cmds.addAttr(joint_name, ln="delta_x", at="double")
               if not cmds.attributeQuery("delta_y", node=joint_name, exists=True):
                   cmds.addAttr(joint_name, ln="delta_y", at="double")
               if not cmds.attributeQuery("delta_z", node=joint_name, exists=True):
                   cmds.addAttr(joint_name, ln="delta_z", at="double")
                
               cmds.setAttr(joint_name + ".delta_x", delta_x)
               cmds.setAttr(joint_name + ".delta_y", delta_y)
               cmds.setAttr(joint_name + ".delta_z", delta_z)           
    
        lower_CD += 1         
        CD += 1

    #
    #
    # Transfer Body original skeleton to the new head Skeleton
    CD = 15
    lower_CD = -1
    minCD = 0
        
    # Define the joint names and namespaces
    head_joint = "DHIhead:spine_04"
    body_joint = "DHIbody:spine_04"
    
    # Split the joint names into their respective namespaces and joint names
    head_namespace, head_joint_name = head_joint.split(":")
    body_namespace, body_joint_name = body_joint.split(":")
    
    # Get the list of child joints for the head joint
    head_child_joints = cmds.listRelatives(head_joint, children=True, allDescendents=True,type="joint")
    body_child_joints = cmds.listRelatives(body_joint, children=True, allDescendents=True, type="joint")
    
    while CD >= minCD:
            joint_CD = [joint for joint in body_child_joints if cmds.getAttr(joint + ".chainDepth") == CD]
            for joint_name in joint_CD:
                body_namespace, body_joint_name = joint_name.split(":")
                # Build the joint names for the current joint
                head_current_joint = "{}:{}".format(head_namespace, body_joint_name)
                body_current_joint = "{}:{}".format(body_namespace, body_joint_name)
                if cmds.objExists(head_current_joint): 
                    moving_joint = body_current_joint
                    target_joint = head_current_joint
                    def move2target_joint():
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
                        
                move2target_joint()
                                
        
            lower_CD -= 1         
            CD -= 1   
            
    fix_body("DHIbody:spine_04", "DHIhead:spine_04")    
    
def bind_skin(gender_mesh):

    # Body
    mesh_obj = cmds.ls(gender_mesh)[0]
    
    # Duplicate the mesh
    duplicated_mesh_obj = cmds.duplicate(mesh_obj)[0]
    new_name = gender_mesh + "_duplicate"
    cmds.rename(duplicated_mesh_obj, new_name)
    bind_obj = cmds.ls(new_name)[0]
    
    cmds.select([bind_obj, "DHIbody:root"])
    
    # Bind skin to the mesh
    skin_cluster = cmds.skinCluster("DHIbody:root", bind_obj)[0]
    
    # Set the skinning method to "classic linear"
    cmds.setAttr(skin_cluster + ".skinningMethod", 1)
    
    cmds.select([mesh_obj, bind_obj])
    
    cmds.copySkinWeights(noMirror=True, surfaceAssociation="closestPoint", influenceAssociation=["name", "oneToOne"])
    
    cmds.delete(mesh_obj)
    cmds.rename(bind_obj, gender_mesh)
ROOT_DIR = "c:/dna_calibration"
gender=0
gender_mesh = "f_tal_nrw_body_lod0_mesh"
skeleton_file_path = f"{ROOT_DIR}/data/Fem_Body_skeleton.fbx"   
def build_body(ROOT_DIR):
    #Toggle Gender
    if gender == 0:

        skeleton_file_path = f"{ROOT_DIR}/data/Fem_Body_skeleton.fbx"
        gender_mesh = "f_tal_nrw_body_lod0_mesh"
    elif gender == 1:

        skeleton_file_path = f"{ROOT_DIR}/data/Ma_Body_skeleton.fbx"
        gender_mesh = "m_med_nrw_body_lod0_mesh"
    #Rename Selected as B2    
    selected_object = cmds.ls(selection=True)
    cmds.rename(selected_object, "B2")
    
    # Import the FBX file
    cmds.file(skeleton_file_path, i=True, type="FBX", ignoreVersion=True, ra=True, mergeNamespacesOnClash=False, options="fbx")
    
    cmds.select("B2", replace=True)
    
    # Define the blendshape node and target shape names
    blendshape_node = "BodyShape"
    target_shape = "|body_rig|body_grp|body_geometry_grp|body_lod0_grp|"+gender_mesh+"|"+gender_mesh+"Shape"
    cmds.blendShape(gender_mesh, automatic=True)
    cmds.rename("blendShape1", "BodyShape")
    cmds.blendShape(blendshape_node, edit=True, target=[(target_shape, 0.0, "B2", 1.0)])
    cmds.setAttr("BodyShape.B2", 0)
    #cmds.setAttr("B2" + ".visibility", 0)
    cmds.delete('B2')
    
    body_transformation(gender_mesh)
    
    # Duplicate the head mesh
    body_mesh = gender_mesh
    new_mesh = cmds.duplicate(body_mesh)[0]
    
    # Unlock the translate attributes
    cmds.setAttr(new_mesh+'.translateX', lock=False)
    cmds.setAttr(new_mesh+'.translateY', lock=False)
    cmds.setAttr(new_mesh+'.translateZ', lock=False)
    
    # Translate the duplicated mesh along the X-axis by 75 units
    cmds.move(75, 0, 0, new_mesh, relative=True)
    
    # Add the duplicated mesh as a target blend shape to the existing blend shape node
    blend_shape_node = "BodyShape"
    cmds.blendShape(blend_shape_node, edit=True, target=(body_mesh, 1, new_mesh, 1.0))
    
    # Set the weight of the new_mesh target blend shape to -1
    cmds.setAttr("BodyShape."+new_mesh, -1)
    
    cmds.setAttr("BodyShape.B2", 1)
    
    cmds.delete(gender_mesh+"1")
    
    bind_skin(gender_mesh)
    
#build_body("c:/dna_calibration")