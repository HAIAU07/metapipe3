#All Rights Belongs to Uzay CALISKAN
#Artstation Marketplace Standart License 

import maya.cmds as qqgdshfal2121

def qqgdshfbl2121(qqgdshfcl2121):
    qqgdshfdl2121 = ["upperarm_out_r", "upperarm_fwd_r", "upperarm_in_r", "upperarm_bck_r", "upperarm_out_l", "upperarm_fwd_l", "upperarm_in_l", "upperarm_bck_l", "clavicle_scap_r", "clavicle_scap_l", "clavicle_pec_r", "spine_04_latissimus_r", "clavicle_pec_l", "spine_04_latissimus_l"]
    qqgdskfl2121 = [7420, 15138, 13808, 15219, 3830, 22769, 3008, 7636, 15223, 7640, 3903, 7567, 135, 3784]
    qqgdshfel2121 = [[0.1699024408155907, -0.3332040870206754, -0.1930344920760314], [0.11690040570693228, 0.4939978561934879, -0.5805660764047733], [-0.2436459075293591, -0.03142811166006254, -0.3419563754727857], [0.04564125269769903, -0.2062310438095949, 0.6427715557300022], [-0.13804414820311095, -0.28261345695474915, -0.2134991563147417], [-0.7951241448210702, -0.7667491520491296, -0.5928049004566498], [-0.08825486525945436, -0.04778734136820617, -0.22201713310833826], [0.07160935714900063, -0.1496830381595089, 0.6151630903657406], [-0.17246398789486683, 0.5437517868399198, -1.6740717477777523], [0.27201854904233436, 0.5620542515761997, -1.6886435488079847], [0.550594227909599, 0.09054584226376505, 2.5818363397219883], [2.172409727224437, 0.6596836537776056, -8.546846179167737], [-0.23494616609070107, 0.13905025247231606, 2.794228629223454], [-2.1713319272131066, 0.6589998397599288, -8.546785529723104]]
    def qqgdshffl2121():
        qqgdshgfl2121 = qqgdshfcl2121
        if not qqgdshgfl2121:
            qqgdshfal2121.warning("No mesh selected.")
            return
        qqgdshhfl2121 = qqgdshfal2121.listRelatives(qqgdshgfl2121, shapes=True, type="mesh")
        if not qqgdshhfl2121:
            qqgdshfal2121.warning("Selected object is not a mesh.")
            return
        qqgdshhfl2121 = qqgdshhfl2121[0]
        for i in range(min(len(qqgdshfdl2121), len(qqgdskfl2121))):
            qqgdshifl2121 = qqgdshfdl2121[i]
            qqgdshjfl2121 = qqgdskfl2121[i]
            qqgdslfl2121 = "{}.vtx[{}]".format(qqgdshgfl2121, qqgdshjfl2121)
            qqgdshfal2121.select(qqgdslfl2121)
            qqgdsmlfl2121 = qqgdshfal2121.pointPosition(qqgdslfl2121, world=True)
            qqgdshfal2121.move(qqgdsmlfl2121[0], qqgdsmlfl2121[1], qqgdsmlfl2121[2], qqgdshifl2121, absolute=True, worldSpace=True)
            qqgdsnlfl2121x = qqgdshfel2121[i][0]
            qqgdsnlfl2121y = qqgdshfel2121[i][1] 
            qqgdsnlfl2121z = qqgdshfel2121[i][2]
            qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,qqgdshfdl2121[i], relative=True)
    qqgdshffl2121()
    qqgdsolfl2121 = qqgdshfal2121.xform("upperarm_out_r", query=True, translation=True, worldSpace=True)
    qqgdsolfl21212 = qqgdshfal2121.xform("upperarm_in_r", query=True, translation=True, worldSpace=True)
    t = 0.5
    qqgdsplfl2121 = [(qqgdsolfl2121[i] + t * (qqgdsolfl21212[i] - qqgdsolfl2121[i])) for i in range(3)] 
    qqgdsrlfl2121 = qqgdshfal2121.polyCube()[0]
    qqgdshfal2121.xform(qqgdsrlfl2121, translation=qqgdsplfl2121, rotatePivot=qqgdsplfl2121, worldSpace=True)
    qqjxeretsolfl21212 = qqgdshfal2121.xform("upperarm_r", query=True, translation=True, worldSpace=True)
    midqqgdsrlfl2121_position = qqgdshfal2121.xform(qqgdsrlfl2121, query=True, translation=True, worldSpace=True)
    qqgdsnlfl2121x = (midqqgdsrlfl2121_position[0] - qqjxeretsolfl21212[0])+2.34
    qqgdsnlfl2121y = (midqqgdsrlfl2121_position[1] - qqjxeretsolfl21212[1])+2.18 
    qqgdsnlfl2121z = (midqqgdsrlfl2121_position[2] - qqjxeretsolfl21212[2])-0.26
    qqgdshfal2121.delete(qqgdsrlfl2121)
    qqgdshfal2121.move(qqgdsnlfl2121x,qqgdsnlfl2121y,qqgdsnlfl2121z,"upperarm_r", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_out_r", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_fwd_r", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_in_r", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_bck_r", relative=True)
    qqgdsolfl2121 = qqgdshfal2121.xform("upperarm_out_l", query=True, translation=True, worldSpace=True)
    qqgdsolfl21212 = qqgdshfal2121.xform("upperarm_in_l", query=True, translation=True, worldSpace=True)
    t = 0.5
    qqgdsplfl2121 = [(qqgdsolfl2121[i] + t * (qqgdsolfl21212[i] - qqgdsolfl2121[i])) for i in range(3)] 
    qqgdsrlfl2121 = qqgdshfal2121.polyCube()[0]
    qqgdshfal2121.xform(qqgdsrlfl2121, translation=qqgdsplfl2121, rotatePivot=qqgdsplfl2121, worldSpace=True)
    qqjxeretsolfl21212 = qqgdshfal2121.xform("upperarm_l", query=True, translation=True, worldSpace=True)
    midqqgdsrlfl2121_position = qqgdshfal2121.xform(qqgdsrlfl2121, query=True, translation=True, worldSpace=True)
    qqgdsnlfl2121x = (midqqgdsrlfl2121_position[0] - qqjxeretsolfl21212[0])-2.34
    qqgdsnlfl2121y = (midqqgdsrlfl2121_position[1] - qqjxeretsolfl21212[1])+2.18 
    qqgdsnlfl2121z = (midqqgdsrlfl2121_position[2] - qqjxeretsolfl21212[2])-0.26
    qqgdshfal2121.delete(qqgdsrlfl2121)
    qqgdshfal2121.move(qqgdsnlfl2121x,qqgdsnlfl2121y,qqgdsnlfl2121z,"upperarm_l", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_out_l", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_fwd_l", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_in_l", relative=True)
    qqgdshfal2121.move(-qqgdsnlfl2121x,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"upperarm_bck_l", relative=True)
    qqjxerjolfl21212 = [55,63]
    qqgdslfl2121 = "{}.vtx[{}]".format(qqgdshfcl2121, qqjxerjolfl21212[0])
    qqgdslfl21212 = "{}.vtx[{}]".format(qqgdshfcl2121, qqjxerjolfl21212[1])
    qqgdsmlfl2121 = qqgdshfal2121.pointPosition(qqgdslfl2121, world=True)
    qqgdsmlfl21212 = qqgdshfal2121.pointPosition(qqgdslfl21212, world=True)
    qqgdsplfl2121 = [(qqgdsmlfl2121[i] + t * (qqgdsmlfl21212[i] - qqgdsmlfl2121[i])) for i in range(3)] 
    qqjxerjqwel21212 = qqgdshfal2121.xform("spine_04", query=True, translation=True, worldSpace=True)
    qqgdsnlfl2121x = (qqgdsplfl2121[0] - qqjxerjqwel21212[0])
    qqgdsnlfl2121y = (qqgdsplfl2121[1] - qqjxerjqwel21212[1])-0.28812594771619615
    qqgdsnlfl2121z = (qqgdsplfl2121[2] - qqjxerjqwel21212[2])+0.885471853421449
    qqgdshfal2121.move(0,qqgdsnlfl2121y,qqgdsnlfl2121z,"spine_04", relative=True)
    qqgdshfal2121.move(0,-qqgdsnlfl2121y,-qqgdsnlfl2121z,"spine_05", relative=True)
    qqgdssslfl2121 = qqgdshfal2121.xform("spine_04", query=True, translation=True, worldSpace=True)
    qqgdssslfl21212 = qqgdshfal2121.xform("neck_01", query=True, translation=True, worldSpace=True)
    t = 0.6
    qqgdsplfl2121 = [(qqgdssslfl2121[i] + t * (qqgdssslfl21212[i] - qqgdssslfl2121[i])) for i in range(3)] 
    qqgdstslfl2121 = qqgdshfal2121.listRelatives("spine_05", c=True, type="joint")  
    qqgdutslfl2121 = []
    for child_joint in qqgdstslfl2121:
        qqgdutslfl2121.append(qqgdshfal2121.xform(child_joint, q=True, ws=True, t=True))
    qqgdshfal2121.xform("spine_05", translation=qqgdsplfl2121, rotatePivot=qqgdsplfl2121, worldSpace=True) 
    for i, child_joint in enumerate(qqgdstslfl2121):
        qqgdshfal2121.xform(child_joint, ws=True, t=qqgdutslfl2121[i])
    # Get vertex position
    vertex_positionJaw = qqgdshfal2121.pointPosition("head_lod0_mesh.vtx[17640]", world=True)
    qqgdzqzqwersstslfl2121 = qqgdshfal2121.xform("clavicle_r", query=True, translation=True, worldSpace=True)
    qqgdzqaqwersstslfl2121 = qqgdshfal2121.listRelatives("clavicle_r", c=True, type="joint")
    qqgdzqbqwersstslfl2121 = []
    for child_joint in qqgdzqaqwersstslfl2121:
        qqgdzqbqwersstslfl2121.append(qqgdshfal2121.xform(child_joint, q=True, ws=True, t=True))
    # Set new joint position using vertex y-coordinate
    qqgdshfal2121.xform("clavicle_r", translation=(vertex_positionJaw[0], qqgdzqzqwersstslfl2121[1], qqgdzqzqwersstslfl2121[2]), worldSpace=True)
    
    for i, child_joint in enumerate(qqgdzqaqwersstslfl2121):
            qqgdshfal2121.xform(child_joint, ws=True, t=qqgdzqbqwersstslfl2121[i])
    # Get vertex position
    vertex_positionJaw = qqgdshfal2121.pointPosition("head_lod0_mesh.vtx[11591]", world=True)
    qqgdzqzqwersstslfl2121 = qqgdshfal2121.xform("clavicle_l", query=True, translation=True, worldSpace=True)
    qqgdzqaqwersstslfl2121 = qqgdshfal2121.listRelatives("clavicle_l", c=True, type="joint")
    qqgdzqbqwersstslfl2121 = []
    for child_joint in qqgdzqaqwersstslfl2121:
        qqgdzqbqwersstslfl2121.append(qqgdshfal2121.xform(child_joint, q=True, ws=True, t=True))
    # Set new joint position using vertex y-coordinate
    qqgdshfal2121.xform("clavicle_l", translation=(vertex_positionJaw[0], qqgdzqzqwersstslfl2121[1], qqgdzqzqwersstslfl2121[2]), worldSpace=True)
    
    for i, child_joint in enumerate(qqgdzqaqwersstslfl2121):
            qqgdshfal2121.xform(child_joint, ws=True, t=qqgdzqbqwersstslfl2121[i])
def qqgdutylfl2121():
    import maya.cmds as qqgdshfal2121
    def qqgdutzzzl2121(qqgduabgzl2121, target, qqgduacgzl2121):   
        import math
        qqgdutzazl2121 = qqgdshfal2121.exactWorldBoundingBox(qqgduacgzl2121)
        center = [
            (qqgdutzazl2121[0] + qqgdutzazl2121[3]) / 2.0,
            (qqgdutzazl2121[1] + qqgdutzazl2121[4]) / 2.0,
            (qqgdutzazl2121[2] + qqgdutzazl2121[5]) / 2.0
        ]
        qqgdutzbzl2121 = qqgdutzazl2121[2]
        qqgdutzczl2121 = qqgdutzazl2121[5]
        qqgdutzdzl2121 = qqgdshfal2121.xform(qqgduabgzl2121, query=True, worldSpace=True, rotatePivot=True)
        qqgdutzezl2121 = qqgdshfal2121.xform(target, query=True, worldSpace=True, rotatePivot=True)
        qqgdutzgzl2121 = qqgdutzdzl2121[2]
        positionRatio = (qqgdutzgzl2121 - qqgdutzbzl2121)/(qqgdutzczl2121 - qqgdutzbzl2121)
        qqgdutzazl2121 = qqgdshfal2121.exactWorldBoundingBox(target)
        center = [
            (qqgdutzazl2121[0] + qqgdutzazl2121[3]) / 2.0,
            (qqgdutzazl2121[1] + qqgdutzazl2121[4]) / 2.0,
            (qqgdutzazl2121[2] + qqgdutzazl2121[5]) / 2.0
        ]
        qqgdutzbzl2121 = qqgdutzazl2121[2]
        qqgdutzczl2121 = qqgdutzazl2121[5]
        qqgduaagzl2121 = (qqgdutzczl2121 - qqgdutzbzl2121) * (positionRatio - 0.5)
        qqgdshfal2121.xform(qqgduabgzl2121, translation=qqgdutzezl2121, worldSpace=True)
        qqgdshfal2121.move(0, 0, qqgduaagzl2121, qqgduabgzl2121, relative=True)
    qqgdutzzzl2121("FACIAL_R_Eye", "eyeRight", "eyeRight_lod0_mesh")
    qqgdutzzzl2121("FACIAL_L_Eye", "eyeLeft", "eyeLeft_lod0_mesh")
def joint_transformation ():
    import maya.cmds as qqgdshfal2121
    import sys
    qqgdshfcl2121 = qqgdshfal2121.ls(selection=True)
    tar = "head_lod0_mesh"
    for obj in qqgdshfcl2121:
        qqgdshfdsdual2991 = 0
        qqgdshfdsdual2891 = qqgdshfal2121.polyEvaluate(obj, vertex=True)
        if qqgdshfdsdual2891 == 24049:
            qqgdshfal2121.rename(obj, "CustomShape")
            qqgdshfdsdual2991 = 1
            continue
        elif qqgdshfdsdual2891 == 4246:
            qqgdshfal2121.rename(obj, "teeth_lod0_mesh_CS")
            qqgdshfdsdual2991 = 1
            continue
        elif qqgdshfdsdual2891 == 660:
            qqgdshfal2121.rename(obj, "saliva_lod0_mesh_CBS")
            qqgdshfdsdual2991 = 1
            continue
        elif qqgdshfdsdual2891 == 770:
            if not qqgdshfal2121.objExists("eyeLeft_lod0_mesh_CS1"):
                qqgdshfal2121.rename(obj, "eyeLeft_lod0_mesh_CS")
                qqgdshfdsdual2991 = 1
            else:
                qqgdshfal2121.error("1 or more of your Custom Mesh Topology not matching!")
            continue
        elif qqgdshfdsdual2891 == 552:
            qqgdshfal2121.rename(obj, "eyeshell_lod0_mesh_CBS")
            qqgdshfdsdual2991 = 1
            continue
        elif qqgdshfdsdual2891 == 2144:
            qqgdshfal2121.rename(obj, "eyelashes_lod0_mesh_CBS")
            qqgdshfdsdual2991 = 1
            continue
        elif qqgdshfdsdual2891 == 268: 
            qqgdshfal2121.rename(obj, "eyeEdge_lod0_mesh_CBS")
            qqgdshfdsdual2991 = 1 
            continue  
        elif qqgdshfdsdual2891 == 386:
            qqgdshfal2121.rename(obj, "cartilage_lod0_mesh_CBS")
            qqgdshfdsdual2991 = 1
            continue
        elif qqgdshfdsdual2891 == 30455:
            qqgdshfal2121.rename(obj, "body_mesh_CS")
            qqgdshfdsdual2991 = 1
            continue
        if qqgdshfdsdual2991 == 0:
            if not qqgdshfal2121.objExists("eyeLeft_lod0_mesh_CS1"):
                qqgdshfal2121.rename(obj, "eyeLeft_lod0_mesh_CS")
                qqgdshfdsdual2991 = 1
            else:
                qqgdshfal2121.error("1 or more of your Custom Mesh Topology not matching!")

    if not qqgdshfal2121.objExists("CustomShape"):
        qqgdshfal2121.error("Custom Head Mesh is missing or topology is not matching!")
    qqgdshfal2121.blendShape(tar, automatic=True)
    qqgdshfal2121.rename("blendShape1", "TargetBS")
    qqgduaegzl2121 = qqgdshfal2121.listRelatives(tar, shapes=True, fullPath=True)
    qqgdshfal2121.blendShape("TargetBS", edit=True, target=[(qqgduaegzl2121[0], 0.0, "CustomShape", 1.0)])
    qqgdshfcl2121 = qqgdshfal2121.ls(selection=True)
      
    is_hidden0 = qqgdshfal2121.getAttr("eyeLeft_lod0_mesh_CS" + ".visibility") == 0
    is_hidden1 = qqgdshfal2121.getAttr("eyeLeft_lod0_mesh_CS1" + ".visibility") == 0
    if is_hidden0 or is_hidden1:
        qqgdshfal2121.setAttr("eyeLeft_lod0_mesh_CS" + ".visibility", 1)
        qqgdshfal2121.setAttr("eyeLeft_lod0_mesh_CS1" + ".visibility", 1)
    qqgdshfal2121.xform("eyeLeft_lod0_mesh_CS", centerPivots=True)
    qqgdshfal2121.xform("eyeLeft_lod0_mesh_CS1", centerPivots=True)
    pos1 = qqgdshfal2121.xform("eyeLeft_lod0_mesh_CS", query=True, worldSpace=True, rotatePivot=True)
    pos2 = qqgdshfal2121.xform("eyeLeft_lod0_mesh_CS1", query=True, worldSpace=True, rotatePivot=True)
    if pos1[0] > 0 and pos2[0] > 0:
        print("Both eyes are on the positive X side of the origin")
    elif pos1[0] < 0 and pos2[0] < 0:
        print("Both eyes are on the negative X side of the origin")
    elif pos1[0] < 0 and pos2[0] > 0:
        if qqgdshfal2121.objExists("eyeRight") or qqgdshfal2121.objExists("eyeLeft"):
            print("Eye names already exist, Delete or rename them")
        else:
            qqgdshfal2121.rename("eyeLeft_lod0_mesh_CS", "eyeRight")
            qqgdshfal2121.rename("eyeLeft_lod0_mesh_CS1", "eyeLeft")
    elif pos1[0] > 0 and pos2[0] < 0:
        if qqgdshfal2121.objExists("eyeRight") or qqgdshfal2121.objExists("eyeLeft"):
            print("Eye names already exist, Delete or rename them")
        else:
            qqgdshfal2121.rename("eyeLeft_lod0_mesh_CS", "eyeLeft")
            qqgdshfal2121.rename("eyeLeft_lod0_mesh_CS1", "eyeRight")
    elif pos1[0] == 0 or pos2[0] == 0:
        print("Eye is in the middle")
    qqgdshfal2121.setAttr("eyeRight" + ".visibility", 0)
    qqgdshfal2121.setAttr("eyeLeft" + ".visibility", 0)
    qqgdutylfl2121()
    qqgduaggzl2121 = "body_mesh_CS"
    import maya.cmds as qqgdshfal2121
    #Adding the new chaind depth attribute
    def qqgduahgzl2121(joints):
        for joint in joints:
            if not qqgdshfal2121.attributeQuery('qqsgdsbzl2121', node=joint, exists=True):
                qqgdshfal2121.addAttr(joint, longName='qqsgdsbzl2121', attributeType='long', defaultValue=0)
                qqgdshfal2121.setAttr(joint + '.qqsgdsbzl2121', keyable=True)
    def qqgduajgzl2121(joints, value):
        for joint in joints:
            qqgdshfal2121.setAttr(joint + '.qqsgdsbzl2121', value)       
    qqgduajkzl2121 = qqgdshfal2121.ls(type="joint")
    qqgduahgzl2121(qqgduajkzl2121)
    qqgdlajkzl2121 = [joint for joint in qqgduajkzl2121 if not qqgdshfal2121.listRelatives(joint, children=True, type='joint')]
    qqgdlamkzl2121 = 'FACIAL_C_TeethLower'
    qqgdstslfl2121 = qqgdshfal2121.listRelatives(qqgdlamkzl2121, allDescendents=True, type='joint')
    qqtrewzxjuzztru2121 = [qqgdlamkzl2121] + qqgdstslfl2121 + ['FACIAL_R_Pupil', 'FACIAL_L_Pupil']             
    qqgdlannkzl2121 = [joint for joint in qqgduajkzl2121 if not qqgdshfal2121.listRelatives(joint, children=True, type='joint')
                  and joint not in qqtrewzxjuzztru2121]
    l1 = qqgdshfal2121.ls('FACIAL_L_EyelidUpperA1', type='joint')
    l2 = qqgdshfal2121.ls('FACIAL_L_EyelidUpperA2', type='joint')
    l3 = qqgdshfal2121.ls('FACIAL_L_EyelidUpperA3', type='joint')
    r1 = qqgdshfal2121.ls('FACIAL_L_EyelidUpperA1', type='joint')
    r2 = qqgdshfal2121.ls('FACIAL_L_EyelidUpperA2', type='joint')
    r3 = qqgdshfal2121.ls('FACIAL_L_EyelidUpperA3', type='joint')               
    qqsgdlannkzl2121 = [l1[0], l2[0], l3[0]]
    qqsgdlannkzl2121_r = [r1[0], r2[0], r3[0]]
    qqsgnnkzl2121 = []
    for joint in qqsgdlannkzl2121:
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqsgnnkzl2121.append(qqsgbbzl2121)
    qqrtjwfffhzl2121 = len(qqsgnnkzl2121)
    if qqrtjwfffhzl2121 > 0:
        qqsgjjkzl2121 = [sum(coord) / qqrtjwfffhzl2121 for coord in zip(*qqsgnnkzl2121)]
    else:
        qqsgjjkzl2121 = [0, 0, 0]
    for joint in qqsgdlannkzl2121:
        qqgdlamkzl2121=qqgdshfal2121.ls(joint)[0]
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqgdsnlfl2121_center_x= qqsgbbzl2121[0] - qqsgjjkzl2121[0]
        qqgdsnlfl2121_center_y= qqsgbbzl2121[1] - qqsgjjkzl2121[1]
        qqgdsnlfl2121_center_z= qqsgbbzl2121[2] - qqsgjjkzl2121[2]
        if not qqgdshfal2121.attributeQuery("dc_x", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="dc_x", at="double")
        if not qqgdshfal2121.attributeQuery("dc_y", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="dc_y", at="double")
        if not qqgdshfal2121.attributeQuery("dc_z", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="dc_z", at="double")
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".dc_x", qqgdsnlfl2121_center_x)
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".dc_y", qqgdsnlfl2121_center_y)
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".dc_z", qqgdsnlfl2121_center_z)
    qqsgnnkzl2121 = []
    for joint in qqsgdlannkzl2121_r:
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqsgnnkzl2121.append(qqsgbbzl2121)
    qqrtjwfffhzl2121 = len(qqsgnnkzl2121)
    if qqrtjwfffhzl2121 > 0:
        qqsgjjkzl2121 = [sum(coord) / qqrtjwfffhzl2121 for coord in zip(*qqsgnnkzl2121)]
    else:
        qqsgjjkzl2121 = [0, 0, 0]
    for joint in qqsgdlannkzl2121_r:
        qqgdlamkzl2121=qqgdshfal2121.ls(joint)[0]
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqgdsnlfl2121_center_x= qqsgbbzl2121[0] - qqsgjjkzl2121[0]
        qqgdsnlfl2121_center_y= qqsgbbzl2121[1] - qqsgjjkzl2121[1]
        qqgdsnlfl2121_center_z= qqsgbbzl2121[2] - qqsgjjkzl2121[2]
        if not qqgdshfal2121.attributeQuery("dc_x", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="dc_x", at="double")
        if not qqgdshfal2121.attributeQuery("dc_y", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="dc_y", at="double")
        if not qqgdshfal2121.attributeQuery("dc_z", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="dc_z", at="double")
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".dc_x", qqgdsnlfl2121_center_x)
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".dc_y", qqgdsnlfl2121_center_y)
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".dc_z", qqgdsnlfl2121_center_z)
    qqgduajgzl2121(qqgduajkzl2121, 100)
    qqgduajgzl2121(qqgdlajkzl2121, 0)
    qqsgcsbzl2121 = []
    for qqgdlamkzl2121 in qqgdlajkzl2121:
        qqsgdsczl2121 = qqgdshfal2121.listRelatives(qqgdlamkzl2121, parent=True, type="joint")
        if qqsgdsczl2121:
            children = qqgdshfal2121.listRelatives(qqsgdsczl2121, children=True, type="joint") or []
            if all(qqgdshfal2121.getAttr(child + ".qqsgdsbzl2121") == 0 for child in children):
               qqsgcsbzl2121.append(qqsgdsczl2121[0])
    qqgduajgzl2121(qqsgcsbzl2121, 1)
    qqsgdsbzl2121 = 1
    while qqsgcsbzl2121:
        qqsgdsbzl2121 += 1
        qqsgdsdzl2121 = []
        for qqgdlamkzl2121 in qqsgcsbzl2121:
            qqsgdsczl2121 = qqgdshfal2121.listRelatives(qqgdlamkzl2121, parent=True, type="joint")
            if qqsgdsczl2121:
                children = qqgdshfal2121.listRelatives(qqsgdsczl2121, children=True, type="joint") or []
                if all(qqgdshfal2121.getAttr(child + ".qqsgdsbzl2121") < qqsgdsbzl2121 for child in children):
                    qqsgdsdzl2121.append(qqsgdsczl2121[0])
        if qqsgdsdzl2121:
            qqgduajgzl2121(qqsgdsdzl2121, qqsgdsbzl2121)
            qqsgcsbzl2121 = qqsgdsdzl2121
        else:
            break
    qqsgdsezl2121 = []
    qqrtedsfgzl2121 = []
    qqsgdsfgzl2121 = []
    qrtedsfgzl2121 = []
    for qqgdlamkzl2121 in qqgdlannkzl2121:
        qqrtedasfgzl2121 = "head_lod0_mesh"
        qqrtebasfgzl2121 = qqgdshfal2121.xform(qqgdlamkzl2121, query=True, worldSpace=True, translation=True)
        qqrtebcsfgzl2121 = qqgdshfal2121.createNode("closestPointOnMesh")
        qqgdshfal2121.connectAttr(qqrtedasfgzl2121 + ".worldMesh", qqrtebcsfgzl2121 + ".inMesh")
        qqgdshfal2121.setAttr(qqrtebcsfgzl2121 + ".inPosition", qqrtebasfgzl2121[0], qqrtebasfgzl2121[1], qqrtebasfgzl2121[2])
        qqrtedcsfgzl2121 = qqgdshfal2121.getAttr(qqrtebcsfgzl2121 + ".closestVertexIndex")
        qqgdshfal2121.delete(qqrtebcsfgzl2121)
        vertex = qqrtedasfgzl2121 + ".vtx[{}]".format(qqrtedcsfgzl2121)
        qqgdshfal2121.select(vertex, replace=True)
        for i in range(1):
            qqrteecslklkzl2121 = qqgdshfal2121.ls(selection=True, flatten=True)
            qqrteecsfgzl2121 = []
            for vertex in qqrteecslklkzl2121:
                qqrteecsfgzl2121.extend(qqgdshfal2121.polyListComponentConversion(vertex, fromVertex=True, toEdge=True))
            qqgdshfal2121.select(qqrteecsfgzl2121)
            qqrteecsfgzl2121 = qqgdshfal2121.ls(selection=True, flatten=True)
            qqrteecslklkzl2121 = []
            for edge in qqrteecsfgzl2121:
                qqrteecslklkzl2121.extend(qqgdshfal2121.polyListComponentConversion(edge, fromEdge=True, toVertex=True))
            qqgdshfal2121.select(qqrteecslklkzl2121) 
            qqrteecslklkzl2121 = qqgdshfal2121.ls(selection=True, flatten=True)
        qqgdsmlfl2121_before = []
        for vertex in qqrteecslklkzl2121:
            position = qqgdshfal2121.pointPosition(vertex, world=True)
            qqgdsmlfl2121_before.append(position)
        qqgdshfal2121.setAttr("TargetBS.CustomShape", 1)
        qqgdsmlfl2121_after = []
        for vertex in qqrteecslklkzl2121:
            position = qqgdshfal2121.pointPosition(vertex, world=True)
            qqgdsmlfl2121_after.append(position)
        qqgdsnlfl2121_vertex = [] 
        for i in range(len(qqgdsmlfl2121_after)):
            sub_qqgdsnlfl2121 = []
            for j in range(3):
                sub_qqgdsnlfl2121.append(qqgdsmlfl2121_after[i][j] - qqgdsmlfl2121_before[i][j])
            qqgdsnlfl2121_vertex.append(sub_qqgdsnlfl2121)
        qqrtakzl2121 = [sum(x) / len(x) for x in zip(*qqgdsnlfl2121_vertex)]
        qqgdsnlfl2121_x = qqrtakzl2121[0]
        qqgdsnlfl2121_y = qqrtakzl2121[1]
        qqgdsnlfl2121_z = qqrtakzl2121[2]
        if not qqgdshfal2121.attributeQuery("qqgdsnlfl2121_x", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="qqgdsnlfl2121_x", at="double")
        if not qqgdshfal2121.attributeQuery("qqgdsnlfl2121_y", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="qqgdsnlfl2121_y", at="double")
        if not qqgdshfal2121.attributeQuery("qqgdsnlfl2121_z", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="qqgdsnlfl2121_z", at="double")
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_x", qqgdsnlfl2121_x)
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_y", qqgdsnlfl2121_y)
        qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_z", qqgdsnlfl2121_z)
        qqgdshfal2121.setAttr("TargetBS.CustomShape", 0)
        qqsgdsezl2121.append(qqgdlamkzl2121)
        qqrtedsfgzl2121.append(qqgdsnlfl2121_x)
        qqsgdsfgzl2121.append(qqgdsnlfl2121_y)
        qrtedsfgzl2121.append(qqgdsnlfl2121_z)
    for i in range(len(qqsgdsezl2121)):
        qqgdshfal2121.move(qqrtedsfgzl2121[i], qqsgdsfgzl2121[i], qrtedsfgzl2121[i], qqsgdsezl2121[i], relative=True) 
    qqrtckzl2121 = 1
    qqrtbkzl2121 = 0
    maxqqrtckzl2121 = 11
    while qqrtckzl2121 <= maxqqrtckzl2121:
        qqrtfeezl2121 = [joint for joint in qqgduajkzl2121 if qqgdshfal2121.getAttr(joint + ".qqsgdsbzl2121") == qqrtckzl2121]
        qqrtdezl2121 = [joint for joint in qqgduajkzl2121 if qqgdshfal2121.getAttr(joint + ".qqsgdsbzl2121") == qqrtbkzl2121]
        for qqgdlamkzl2121 in qqrtfeezl2121:
           qqrtfehzl2121 = qqgdshfal2121.xform(qqgdlamkzl2121, q=True, ws=True, translation=True)
           qqgdstslfl2121 = qqgdshfal2121.listRelatives(qqgdlamkzl2121, children=True, type="joint")
           qqrtjjjhzl2121 = []
           if qqgdstslfl2121:
               qqrtfegzl2121 = []
               for child_joint in qqgdstslfl2121:
                   if child_joint in qqrtdezl2121 and child_joint not in qqtrewzxjuzztru2121:
                       qqgdsnlfl2121_x = qqgdshfal2121.getAttr(child_joint + '.qqgdsnlfl2121_x')
                       qqgdsnlfl2121_y = qqgdshfal2121.getAttr(child_joint + '.qqgdsnlfl2121_y')
                       qqgdsnlfl2121_z = qqgdshfal2121.getAttr(child_joint + '.qqgdsnlfl2121_z')
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
                   if child_joint in qqgdlajkzl2121 and child_joint not in qqtrewzxjuzztru2121:
                       qqgdsnlfl2121_x = qqgdshfal2121.getAttr(child_joint + '.qqgdsnlfl2121_x')
                       qqgdsnlfl2121_y = qqgdshfal2121.getAttr(child_joint + '.qqgdsnlfl2121_y')
                       qqgdsnlfl2121_z = qqgdshfal2121.getAttr(child_joint + '.qqgdsnlfl2121_z')
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
                       qqrtfegzl2121.append([qqgdsnlfl2121_x, qqgdsnlfl2121_y, qqgdsnlfl2121_z])
               qqrtjjjhzl2121 = [sum(x) / len(x) for x in zip(*qqrtfegzl2121)]
               if not qqrtjjjhzl2121:
                   qqrtjjjhzl2121 = [0, 0, 0]
               avg_x = qqrtjjjhzl2121[0]
               avg_y = qqrtjjjhzl2121[1]
               avg_z = qqrtjjjhzl2121[2]
               qqgdshfal2121.move(avg_x, avg_y, avg_z, qqgdlamkzl2121, relative=True)
               for child_joint in qqgdstslfl2121:
                   qqgdshfal2121.move(-avg_x, -avg_y, -avg_z, child_joint, relative=True)
               end_place = qqgdshfal2121.xform(qqgdlamkzl2121, q=True, ws=True, translation=True)
               qqgdsnlfl2121_x = end_place[0] - qqrtfehzl2121[0]
               qqgdsnlfl2121_y = end_place[1] - qqrtfehzl2121[1]
               qqgdsnlfl2121_z = end_place[2] - qqrtfehzl2121[2]
               if not qqgdshfal2121.attributeQuery("qqgdsnlfl2121_x", node=qqgdlamkzl2121, exists=True):
                   qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="qqgdsnlfl2121_x", at="double")
               if not qqgdshfal2121.attributeQuery("qqgdsnlfl2121_y", node=qqgdlamkzl2121, exists=True):
                   qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="qqgdsnlfl2121_y", at="double")
               if not qqgdshfal2121.attributeQuery("qqgdsnlfl2121_z", node=qqgdlamkzl2121, exists=True):
                   qqgdshfal2121.addAttr(qqgdlamkzl2121, ln="qqgdsnlfl2121_z", at="double")
               qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_x", qqgdsnlfl2121_x)
               qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_y", qqgdsnlfl2121_y)
               qqgdshfal2121.setAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_z", qqgdsnlfl2121_z)           
        qqrtbkzl2121 += 1         
        qqrtckzl2121 += 1
    qqrtjwdfhzl2121 = 4
    for qqgdlamkzl2121 in qqgduajkzl2121:
        if qqgdshfal2121.attributeQuery("qqgdsnlfl2121_x", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.deleteAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_x")
        if qqgdshfal2121.attributeQuery("avg_y", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.deleteAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_y")
        if qqgdshfal2121.attributeQuery("qqgdsnlfl2121_z", node=qqgdlamkzl2121, exists=True):
            qqgdshfal2121.deleteAttr(qqgdlamkzl2121 + ".qqgdsnlfl2121_z")
    qqsgnnkzl2121 = []
    for joint in qqsgdlannkzl2121:
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqsgnnkzl2121.append(qqsgbbzl2121)
    qqrtjwfffhzl2121 = len(qqsgnnkzl2121)
    if qqrtjwfffhzl2121 > 0:
        qqsgjjkzl2121 = [sum(coord) / qqrtjwfffhzl2121 for coord in zip(*qqsgnnkzl2121)]
    else:
        qqsgjjkzl2121 = [0, 0, 0]
    for joint in qqsgdlannkzl2121:
        qqgdlamkzl2121=joint
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqgdshfal2121.move(-qqsgbbzl2121[0]/qqrtjwdfhzl2121, -qqsgbbzl2121[1]/qqrtjwdfhzl2121, -qqsgbbzl2121[2]/qqrtjwdfhzl2121, joint, relative=True)
        qqgdshfal2121.move(qqsgjjkzl2121[0]/qqrtjwdfhzl2121, qqsgjjkzl2121[1]/qqrtjwdfhzl2121, qqsgjjkzl2121[2]/qqrtjwdfhzl2121, joint, relative=True)
        qqgdshfal2121.move(qqgdshfal2121.getAttr(qqgdlamkzl2121 + ".dc_x")/qqrtjwdfhzl2121, qqgdshfal2121.getAttr(qqgdlamkzl2121 + ".dc_y")/qqrtjwdfhzl2121, qqgdshfal2121.getAttr(qqgdlamkzl2121 + ".dc_z")/qqrtjwdfhzl2121, joint, relative=True)
    qqsgnnkzl2121 = []
    for joint in qqsgdlannkzl2121_r:
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqsgnnkzl2121.append(qqsgbbzl2121)
    qqrtjwfffhzl2121 = len(qqsgnnkzl2121)
    if qqrtjwfffhzl2121 > 0:
        qqsgjjkzl2121 = [sum(coord) / qqrtjwfffhzl2121 for coord in zip(*qqsgnnkzl2121)]
    else:
        qqsgjjkzl2121 = [0, 0, 0]
    for joint in qqsgdlannkzl2121_r:
        qqgdlamkzl2121=joint
        qqsgbbzl2121 = qqgdshfal2121.xform(joint, query=True, worldSpace=True, translation=True)
        qqgdshfal2121.move(-qqsgbbzl2121[0]/qqrtjwdfhzl2121, -qqsgbbzl2121[1]/qqrtjwdfhzl2121, -qqsgbbzl2121[2]/qqrtjwdfhzl2121, joint, relative=True)
        qqgdshfal2121.move(qqsgjjkzl2121[0]/qqrtjwdfhzl2121, qqsgjjkzl2121[1]/qqrtjwdfhzl2121, qqsgjjkzl2121[2]/qqrtjwdfhzl2121, joint, relative=True)
        qqgdshfal2121.move(qqgdshfal2121.getAttr(qqgdlamkzl2121 + ".dc_x")/qqrtjwdfhzl2121, qqgdshfal2121.getAttr(qqgdlamkzl2121 + ".dc_y")/qqrtjwdfhzl2121, qqgdshfal2121.getAttr(qqgdlamkzl2121 + ".dc_z")/qqrtjwdfhzl2121, joint, relative=True)
    def qqgdshffl2121(qqgdshifl2121, target_joint):
        mov_pos = qqgdshfal2121.xform(qqgdshifl2121, query=True, worldSpace=True, rotatePivot=True)
        tar_pos = qqgdshfal2121.xform(target_joint, query=True, worldSpace=True, rotatePivot=True)
        qqgdstslfl2121 = qqgdshfal2121.listRelatives(qqgdshifl2121, c=True, type="joint")
        qqgdutslfl2121 = []
        for child_joint in qqgdstslfl2121:
            qqgdutslfl2121.append(qqgdshfal2121.xform(child_joint, q=True, ws=True, t=True))
        qqgdshfal2121.xform(qqgdshifl2121, translation=tar_pos, rotatePivot=mov_pos, worldSpace=True)
        for i, child_joint in enumerate(qqgdstslfl2121):
            qqgdshfal2121.xform(child_joint, ws=True, t=qqgdutslfl2121[i])

    qqgdzqqqwersstslfl2121 = qqgdshfal2121.pointPosition("head_lod0_mesh.vtx[22350]", world=True)
    qqgdzqqwersstslfl2121 = qqgdshfal2121.pointPosition("head_lod0_mesh.vtx[19337]", world=True)
    qqgdzqzqwersstslfl2121 = qqgdshfal2121.xform("FACIAL_C_Jaw", query=True, translation=True, worldSpace=True)
    qqgdzqaqwersstslfl2121 = qqgdshfal2121.listRelatives("FACIAL_C_Jaw", c=True, type="joint")
    qqgdzqbqwersstslfl2121 = []
    for child_joint in qqgdzqaqwersstslfl2121:
        qqgdzqbqwersstslfl2121.append(qqgdshfal2121.xform(child_joint, q=True, ws=True, t=True))
    # Set new joint position using vertex y-coordinate
    qqgdshfal2121.xform("FACIAL_C_Jaw", translation=(qqgdzqzqwersstslfl2121[0], (qqgdzqqqwersstslfl2121[1] + qqgdzqqwersstslfl2121[1]) / 2, (qqgdzqqqwersstslfl2121[2] + qqgdzqqwersstslfl2121[2]) / 2), worldSpace=True)
    
    for i, child_joint in enumerate(qqgdzqaqwersstslfl2121):
            qqgdshfal2121.xform(child_joint, ws=True, t=qqgdzqbqwersstslfl2121[i])
    qqgdshffl2121("FACIAL_C_LowerLipRotation", "FACIAL_C_Jaw")
    def qqtrepuu2121(moving, ref, distance_joints_x, distance_joints_y, distance_joints_z):
        qqrtjkslhzl2121 = qqgdshfal2121.xform(moving, query=True, worldSpace=True, rotatePivot=True)
        qqtrepu2121 = qqgdshfal2121.xform(ref, query=True, worldSpace=True, rotatePivot=True)
        qqgdshfal2121.xform(moving, translation=qqtrepu2121, worldSpace=True)
        qqgdshfal2121.move(distance_joints_x, distance_joints_y, distance_joints_z, moving, relative=True)
    qqtrepuu2121("FACIAL_C_TeethUpper", "FACIAL_C_LipUpper2", 0.02062227716338219, 1.3000883278700712, -3.352522450123213)
    qqtrepuu2121("FACIAL_C_TeethLower", "FACIAL_C_TeethUpper", 0, -1.7288506204431826, -0.16130734354544174)
    qqgdshffl2121("neck_01", "FACIAL_C_Neck1Root")
    qqgdshfal2121.move(-8.756818659788437e-07, -1.2664320775647866, -3.184565397183476, "spine_04", relative=True)
    qqgdshfal2121.move(8.756818659788437e-07, 1.2664320775647866, 3.184565397183476, "FACIAL_C_Neck1Root", relative=True)
    qqgdshfal2121.move(8.756818659788437e-07, 1.2664320775647866, 3.184565397183476, "neck_02", relative=True) 
    qqgdshfal2121.move(8.756818659788437e-07, 1.2664320775647866, 3.184565397183476, "clavicle_l", relative=True)
    qqgdshfal2121.move(8.756818659788437e-07, 1.2664320775647866, 3.184565397183476, "clavicle_r", relative=True)
    qqgdshffl2121("neck_02", "FACIAL_C_Neck2Root")
    qqgdshfal2121.move(-1.133513918706999e-06, 0.1523474504930391, -2.64695004846428, "neck_02", relative=True)
    qqgdshfal2121.move(1.133513918706999e-06, -0.1523474504930391, 2.64695004846428, "FACIAL_C_Neck2Root", relative=True)
    qqgdshfal2121.move(1.133513918706999e-06, -0.1523474504930391, 2.64695004846428, "head", relative=True)
    qqgdshffl2121("head", "neck_02")
    qqgdshfal2121.move(-2.4067497106321516e-07, 5.243699897720944, 1.1424691094592987, "head", relative=True)
    qqgdshfal2121.move(2.4067497106321516e-07, -5.243699897720944, -1.1424691094592987, "FACIAL_C_FacialRoot", relative=True)
    qqgdshffl2121("FACIAL_L_EyelidUpperA", "FACIAL_L_Eye")
    qqgdshffl2121("FACIAL_L_EyelidLowerB", "FACIAL_L_Eye")
    qqgdshffl2121("FACIAL_L_EyelidLowerA", "FACIAL_L_Eye")
    qqgdshffl2121("FACIAL_L_EyelidUpperB", "FACIAL_L_Eye")
    qqgdshffl2121("FACIAL_R_EyelidUpperA", "FACIAL_R_Eye")
    qqgdshffl2121("FACIAL_R_EyelidLowerB", "FACIAL_R_Eye")
    qqgdshffl2121("FACIAL_R_EyelidLowerA", "FACIAL_R_Eye")
    qqgdshffl2121("FACIAL_R_EyelidUpperB", "FACIAL_R_Eye")
    if qqgdshfal2121.objExists("body_mesh_CS"):
        qqgdshfbl2121(qqgduaggzl2121)
    qqtrewtru2121 = "head_lod0_mesh"
    qqtrewzztru2121 = qqgdshfal2121.duplicate(qqtrewtru2121)[0]
    qqgdshfal2121.setAttr(qqtrewzztru2121+'.translateX', lock=False)
    qqgdshfal2121.setAttr(qqtrewzztru2121+'.translateY', lock=False)
    qqgdshfal2121.setAttr(qqtrewzztru2121+'.translateZ', lock=False)
    qqgdshfal2121.move(75, 0, 0, qqtrewzztru2121, relative=True)
    blend_shape_node = "TargetBS"
    qqgdshfal2121.blendShape(blend_shape_node, edit=True, target=(qqtrewtru2121, 1, qqtrewzztru2121, 1.0))
    qqgdshfal2121.setAttr("TargetBS."+qqtrewzztru2121, -1)
    qqgdshfal2121.setAttr("TargetBS.CustomShape", 1)
    qqgdshfal2121.setAttr(qqtrewzztru2121 + ".visibility", 0)
    qqgdshfal2121.setAttr("CustomShape" + ".visibility", 0)
    qqgdsdfbt5hfal2121 = qqgdshfal2121.listRelatives("head_lod0_grp", children=True, type="transform")
    for qqgdsdfbt5hfal21 in qqgdsdfbt5hfal2121:
        if not qqgdsdfbt5hfal21 == "head_lod0_mesh":
            if qqgdshfal2121.objExists(qqgdsdfbt5hfal21 + "_CBS"):
                qqgdsdfbt5hfal21CS = qqgdsdfbt5hfal21 + "_CBS"
                qqgdshfal2121.hide(qqgdsdfbt5hfal21 + "_CS")
            else:
                qqgdsdfbt5hfal21CS = qqgdsdfbt5hfal21 + "_CS"          
            if qqgdshfal2121.objExists(qqgdsdfbt5hfal21CS):
                BS_CST = qqgdshfal2121.blendShape(qqgdsdfbt5hfal21, automatic=True)
                qqgdshfal2121.rename(BS_CST, qqgdsdfbt5hfal21 + "BS")
                dubqqgdsdfbt5hfal21 = qqgdshfal2121.duplicate(qqgdsdfbt5hfal21)[0]
                qqgdshfal2121.rename(dubqqgdsdfbt5hfal21, qqgdsdfbt5hfal21 + "dub")
                qqgdshfal2121.blendShape(qqgdsdfbt5hfal21 + "BS", edit=True, target=[(qqgdsdfbt5hfal21, 0, qqgdsdfbt5hfal21 + "dub", 1.0)])
                qqgdshfal2121.blendShape(qqgdsdfbt5hfal21 + "BS", edit=True, target=[(qqgdsdfbt5hfal21, 1, qqgdsdfbt5hfal21CS, 1.0)])
                qqgdshfal2121.setAttr(qqgdsdfbt5hfal21 + "BS." + qqgdsdfbt5hfal21 + "dub", -1)
                qqgdshfal2121.setAttr(qqgdsdfbt5hfal21 + "BS." + qqgdsdfbt5hfal21CS, 1)
                qqgdshfal2121.delete(qqgdsdfbt5hfal21 + "dub")
                qqgdshfal2121.hide(qqgdsdfbt5hfal21CS)
    qqgdshfal2121.hide("body_mesh_CS")
    if qqgdshfal2121.objExists("eyeLeft"):
        tuyt5 = qqgdshfal2121.polyEvaluate("eyeLeft", vertex=True)
        if tuyt5 == 770:
            qqgdwwddwal211221 = "eyeLeft_lod0_mesh"
            BS_CST = qqgdshfal2121.blendShape(qqgdwwddwal211221, automatic=True)
            qqgdshfal2121.rename(BS_CST, qqgdwwddwal211221 + "BS")
            dubOBJ = qqgdshfal2121.duplicate(qqgdwwddwal211221)[0]
            qqgdshfal2121.rename(dubOBJ, qqgdwwddwal211221 + "dub")
            qqgdshfal2121.blendShape(qqgdwwddwal211221 + "BS", edit=True, target=[(qqgdwwddwal211221, 0, qqgdwwddwal211221 + "dub", 1.0)])
            qqgdshfal2121.blendShape(qqgdwwddwal211221 + "BS", edit=True, target=[(qqgdwwddwal211221, 1, "eyeLeft", 1.0)])
            qqgdshfal2121.setAttr(qqgdwwddwal211221 + "BS." + qqgdwwddwal211221 + "dub", -1)
            qqgdshfal2121.setAttr(qqgdwwddwal211221 + "BS." + "eyeLeft", 1)
            qqgdshfal2121.delete(qqgdwwddwal211221 + "dub")
    if qqgdshfal2121.objExists("eyeRight"):
        tuyt5 = qqgdshfal2121.polyEvaluate("eyeRight", vertex=True)
        if tuyt5 == 770:
            qqgdwwddwal211221 = "eyeRight_lod0_mesh"
            BS_CST = qqgdshfal2121.blendShape(qqgdwwddwal211221, automatic=True)
            qqgdshfal2121.rename(BS_CST, qqgdwwddwal211221 + "BS")
            dubOBJ = qqgdshfal2121.duplicate(qqgdwwddwal211221)[0]
            qqgdshfal2121.rename(dubOBJ, qqgdwwddwal211221 + "dub")
            qqgdshfal2121.blendShape(qqgdwwddwal211221 + "BS", edit=True, target=[(qqgdwwddwal211221, 0, qqgdwwddwal211221 + "dub", 1.0)])
            qqgdshfal2121.blendShape(qqgdwwddwal211221 + "BS", edit=True, target=[(qqgdwwddwal211221, 1, "eyeRight", 1.0)])
            qqgdshfal2121.setAttr(qqgdwwddwal211221 + "BS." + qqgdwwddwal211221 + "dub", -1)
            qqgdshfal2121.setAttr(qqgdwwddwal211221 + "BS." + "eyeRight", 1)
            qqgdshfal2121.delete(qqgdwwddwal211221 + "dub")
    