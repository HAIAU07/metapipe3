#All Rights Belongs to Uzay CALISKAN
#Artstation Marketplace Standart License 

import maya.cmds as qqdgffvdrevd2121
import sys
import os.path as ospathe
from os import environ
from sys import path as syspath
from sys import platform
import logging
import maya.OpenMaya as om
from maya import cmds  
from os import environ, makedirs
from os import path as ospath
threshold = 0
def update_threshold(text_field):
    global threshold
    thresholdstr = qqdgffvdrevd2121.textField(text_field, q=True, text=True)
    threshold = float(thresholdstr)
    print(f"New threshold: {threshold}")
    return threshold 
def target_mesh():
    selected_objects = qqdgffvdrevd2121.ls(selection=True)
    tar = selected_objects[1]
    print (tar)
    if len(selected_objects) != 2:
        print("Please select exactly two objects.")
        return
    qqdgffvdrevd2121.rename(selected_objects[0], "Custom")
    qqdgffvdrevd2121.blendShape(selected_objects[1], automatic=True)
    qqdgffvdrevd2121.rename("blendShape1", "TargetBS")
    qqdssxoklauh2121 = qqdgffvdrevd2121.listRelatives(tar, shapes=True, fullPath=True)
    print(qqdssxoklauh2121)
    qqdgffvdrevd2121.blendShape("TargetBS", edit=True, target=[(qqdssxoklauh2121[0], 0.0, "CustomShape", 1.0)])
def rename_eyes():
    selected_objects = qqdgffvdrevd2121.ls(selection=True)
    if len(selected_objects) != 2:
        print("Select 2 objects (Eyes)")
    else:
        qqdssxouh21210 = qqdgffvdrevd2121.getAttr(selected_objects[0] + ".visibility") == 0
        qqdssxouh21211 = qqdgffvdrevd2121.getAttr(selected_objects[1] + ".visibility") == 0
        if qqdssxouh21210 or qqdssxouh21211:
            qqdgffvdrevd2121.setAttr(selected_objects[0] + ".visibility", 1)
            qqdgffvdrevd2121.setAttr(selected_objects[1] + ".visibility", 1)
        qqdgffvdrevd2121.xform(selected_objects[0], centerPivots=True)
        qqdgffvdrevd2121.xform(selected_objects[1], centerPivots=True)
        pos1 = qqdgffvdrevd2121.xform(selected_objects[0], query=True, worldSpace=True, rotatePivot=True)
        pos2 = qqdgffvdrevd2121.xform(selected_objects[1], query=True, worldSpace=True, rotatePivot=True)
        if pos1[0] > 0 and pos2[0] > 0:
            print("Both eyes are on the positive X side of the origin")
        elif pos1[0] < 0 and pos2[0] < 0:
            print("Both eyes are on the negative X side of the origin")
        elif pos1[0] < 0 and pos2[0] > 0:
            if qqdgffvdrevd2121.objExists("eyeRight") or qqdgffvdrevd2121.objExists("eyeLeft"):
                print("Eye names already exist, Delete or rename them")
            else:
                qqdgffvdrevd2121.rename(selected_objects[0], "eyeRight")
                qqdgffvdrevd2121.rename(selected_objects[1], "eyeLeft")
        elif pos1[0] > 0 and pos2[0] < 0:
            if qqdgffvdrevd2121.objExists("eyeRight") or qqdgffvdrevd2121.objExists("eyeLeft"):
                print("Eye names already exist, Delete or rename them")
            else:
                qqdgffvdrevd2121.rename(selected_objects[0], "eyeLeft")
                qqdgffvdrevd2121.rename(selected_objects[1], "eyeRight")
        elif pos1[0] == 0 or pos2[0] == 0:
            print("Eye is in the middle")
        qqdgffvdrevd2121.setAttr("eyeRight" + ".visibility", 0)
        qqdgffvdrevd2121.setAttr("eyeLeft" + ".visibility", 0)
def eye_transformation():
    eyejoint = qqdgffvdrevd2121.ls(selection=True)
    def perEye(eyejoint, target, eyemesh): 
        import math
        bounding_box = qqdgffvdrevd2121.exactWorldBoundingBox(eyemesh)
        center = [
            (bounding_box[0] + bounding_box[3]) / 2.0,
            (bounding_box[1] + bounding_box[4]) / 2.0,
            (bounding_box[2] + bounding_box[5]) / 2.0
        ]
        min_z = bounding_box[2]
        max_z = bounding_box[5]
        EyeMain = qqdgffvdrevd2121.xform(eyejoint, query=True, worldSpace=True, rotatePivot=True)
        EyeTarget = qqdgffvdrevd2121.xform(target, query=True, worldSpace=True, rotatePivot=True)
        joint_z = EyeMain[2]
        positionRatio = (joint_z - min_z)/(max_z - min_z)
        bounding_box = qqdgffvdrevd2121.exactWorldBoundingBox(target)
        center = [
            (bounding_box[0] + bounding_box[3]) / 2.0,
            (bounding_box[1] + bounding_box[4]) / 2.0,
            (bounding_box[2] + bounding_box[5]) / 2.0
        ]
        min_z = bounding_box[2]
        max_z = bounding_box[5]
        ratioMove_z = (max_z - min_z) * (positionRatio - 0.5)
        qqdgffvdrevd2121.xform(eyejoint, translation=EyeTarget, worldSpace=True)
        qqdgffvdrevd2121.move(0, 0, ratioMove_z, eyejoint, relative=True)
    perEye(eyejoint[1], "eyeRight", eyejoint[3])
    perEye(eyejoint[0], "eyeLeft", eyejoint[2])
def bind_skin(gender_mesh):
    def select_root_bones():
        # List all joints in the scene
        joints = qqdgffvdrevd2121.ls(type='joint')
        qqdsossdceoyth2121 = []
        for joint in joints:
            # Get the parent of the joints
            parent = qqdgffvdrevd2121.listRelatives(joint, parent=True)
            if not parent or qqdgffvdrevd2121.nodeType(parent[0]) != 'joint':
                qqdsossdceoyth2121.append(joint)
        qqdgffvdrevd2121.select(qqdsossdceoyth2121[0], replace=True) 
    select_root_bones()
    qqdsoghxeoyth2121 = qqdgffvdrevd2121.ls(selection=True, flatten=True)[0]
    qqdsxftuxh2121 = qqdgffvdrevd2121.ls(gender_mesh)[0]
    qqdsxftuxxh2121 = qqdgffvdrevd2121.duplicate(qqdsxftuxh2121)[0]
    qqdsstuxxh2121 = gender_mesh + "_duplicate"
    qqdgffvdrevd2121.rename(qqdsxftuxxh2121, qqdsstuxxh2121)
    qqdsstush2121 = qqdgffvdrevd2121.ls(qqdsstuxxh2121)[0]
    qqdgffvdrevd2121.select([qqdsstush2121, qqdsoghxeoyth2121])
    qqdsstcccch2121 = qqdgffvdrevd2121.skinCluster(qqdsoghxeoyth2121, qqdsstush2121)[0]
    qqdgffvdrevd2121.setAttr(qqdsstcccch2121 + ".skinningMethod", 1)
    qqdgffvdrevd2121.select([qqdsxftuxh2121, qqdsstush2121])
    qqdgffvdrevd2121.copySkinWeights(noMirror=True, surfaceAssociation="closestPoint", influenceAssociation=["name", "oneToOne"])
    qqdgffvdrevd2121.delete(qqdsxftuxh2121)
    qqdgffvdrevd2121.rename(qqdsstush2121, gender_mesh)
qqdgffqqdssedssu2121svd2121 = []     
def exclude():
    global qqdgffqqdssedssu2121svd2121
    qqdgffqqdssedssu2121svd2121 = [] 
    selected_objects = qqdgffvdrevd2121.ls(selection=True)
    qqdgffqqdssedssu2121svd2121 =  selected_objects
def rig_transformation():
    qqdgffadrevd2121 = qqdgffvdrevd2121.ls(selection=True) 
    global qqdgffacsvd2121
    qqdgffacsvd2121 = qqdgffadrevd2121[0]
    def qqdgffbbsvd2121(joints):
        for joint in joints:
            if not qqdgffvdrevd2121.attributeQuery('qqdghfggfvd2121', node=joint, exists=True):
                qqdgffvdrevd2121.addAttr(joint, longName='qqdghfggfvd2121', attributeType='long', defaultValue=0)
                qqdgffvdrevd2121.setAttr(joint + '.qqdghfggfvd2121', keyable=True)
    def qqdgffcbsvd2121(joints, value):
        for joint in joints:
            qqdgffvdrevd2121.setAttr(joint + '.qqdghfggfvd2121', value)
    global qqdgffqqdssedssu2121svd2121
    qqdgffcesvd2121 = qqdgffvdrevd2121.ls(type="joint")
    qqdgffcesvd2121oints = list(set(qqdgffcesvd2121) - set(qqdgffqqdssedssu2121svd2121))
    qqdgffbbsvd2121(qqdgffcesvd2121)
    qqdgffdesvd2121 = [joint for joint in qqdgffcesvd2121oints if not qqdgffvdrevd2121.listRelatives(joint, children=True, type='joint')]
    qqdgffcbsvd2121(qqdgffcesvd2121, 100)
    qqdgffcbsvd2121(qqdgffdesvd2121, 0)
    qqdgffeesvd2121 = []
    for qqdgffeffvd2121 in qqdgffdesvd2121:
        qqdgffggfvd2121 = qqdgffvdrevd2121.listRelatives(qqdgffeffvd2121, parent=True, type="joint")
        if qqdgffggfvd2121:
            children = qqdgffvdrevd2121.listRelatives(qqdgffggfvd2121, children=True, type="joint") or []
            if all(qqdgffvdrevd2121.getAttr(child + ".qqdghfggfvd2121") == 0 for child in children):
               
               qqdgffeesvd2121.append(qqdgffggfvd2121[0])  
    qqdgffcbsvd2121(qqdgffeesvd2121, 1)
    qqdghfggfvd2121 = 1
    while qqdgffeesvd2121:
        qqdghfggfvd2121 += 1
        qqdghfgifvd2121 = []
        for qqdgffeffvd2121 in qqdgffeesvd2121:
            qqdgffggfvd2121 = qqdgffvdrevd2121.listRelatives(qqdgffeffvd2121, parent=True, type="joint")
            if qqdgffggfvd2121:
                children = qqdgffvdrevd2121.listRelatives(qqdgffggfvd2121, children=True, type="joint") or []
                if all(qqdgffvdrevd2121.getAttr(child + ".qqdghfggfvd2121") < qqdghfggfvd2121 for child in children):
                    qqdghfgifvd2121.append(qqdgffggfvd2121[0])
        if qqdghfgifvd2121:
            qqdgffcbsvd2121(qqdghfgifvd2121, qqdghfggfvd2121)
            qqdgffeesvd2121 = qqdghfgifvd2121
        else:
            break
    qqdgcsgifvd2121 = []
    qqdgcsbtrud2121x = []
    qqdgcsbtrud2121y = []
    qqdgcsbtrud2121z = []
    # DELTA X CALCULATE
    for qqdgffeffvd2121 in qqdgffdesvd2121:
        qqdgcsbtrod2121 = qqdgffacsvd2121
        qqdgcotrod2121 = qqdgffvdrevd2121.xform(qqdgffeffvd2121, query=True, worldSpace=True, translation=True)
        qqdocotrod2121 = qqdgffvdrevd2121.createNode("closestPointOnMesh")
        qqdgffvdrevd2121.connectAttr(qqdgcsbtrod2121 + ".worldMesh", qqdocotrod2121 + ".inMesh")
        qqdgffvdrevd2121.setAttr(qqdocotrod2121 + ".inPosition", qqdgcotrod2121[0], qqdgcotrod2121[1], qqdgcotrod2121[2])
        qqdocuutrod2121 = qqdgffvdrevd2121.getAttr(qqdocotrod2121 + ".closestVertexIndex")
        qqdgffvdrevd2121.delete(qqdocotrod2121)
        vertex = qqdgcsbtrod2121 + ".vtx[{}]".format(qqdocuutrod2121)
        qqdgffvdrevd2121.select(vertex, replace=True)
        for i in range(1):
            qqdocbtrtrod2121 = qqdgffvdrevd2121.ls(selection=True, flatten=True)
            edges = []
            for vertex in qqdocbtrtrod2121:
                edges.extend(qqdgffvdrevd2121.polyListComponentConversion(vertex, fromVertex=True, toEdge=True))
            qqdgffvdrevd2121.select(edges)
            edges = qqdgffvdrevd2121.ls(selection=True, flatten=True)
            qqdocbtrtrod2121 = []
            for edge in edges:
                qqdocbtrtrod2121.extend(qqdgffvdrevd2121.polyListComponentConversion(edge, fromEdge=True, toVertex=True))
            qqdgffvdrevd2121.select(qqdocbtrtrod2121)
            qqdocbtrtrod2121 = qqdgffvdrevd2121.ls(selection=True, flatten=True)
        qqdocbtraod2121 = []
        for vertex in qqdocbtrtrod2121:
            position = qqdgffvdrevd2121.pointPosition(vertex, world=True)
            qqdocbtraod2121.append(position)
        qqdgffvdrevd2121.setAttr("TargetBS.CustomShape", 1)
        qqdocbtrbod2121 = []
        for vertex in qqdocbtrtrod2121:
            position = qqdgffvdrevd2121.pointPosition(vertex, world=True)
            qqdocbtrbod2121.append(position)
        qqdssedoou2121vertex = [] 
        for i in range(len(qqdocbtrbod2121)):
            qqdodbtrbod2121 = []
            for j in range(3):
                qqdodbtrbod2121.append(qqdocbtrbod2121[i][j] - qqdocbtraod2121[i][j])
            qqdssedoou2121vertex.append(qqdodbtrbod2121)
        qqdodbtrbgd2121 = [sum(x) / len(x) for x in zip(*qqdssedoou2121vertex)]
        qqdssedoou2121x = qqdodbtrbgd2121[0]
        qqdssedoou2121y = qqdodbtrbgd2121[1]
        qqdssedoou2121z = qqdodbtrbgd2121[2]
        if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121x", node=qqdgffeffvd2121, exists=True):
            qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121x", at="double")
        if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121y", node=qqdgffeffvd2121, exists=True):
            qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121y", at="double")
        if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121z", node=qqdgffeffvd2121, exists=True):
            qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121z", at="double")
        qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121x", qqdssedoou2121x)
        qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121y", qqdssedoou2121y)
        qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121z", qqdssedoou2121z)
        qqdgffvdrevd2121.setAttr("TargetBS.CustomShape", 0)
        qqdgcsgifvd2121.append(qqdgffeffvd2121)
        qqdgcsbtrud2121x.append(qqdssedoou2121x)
        qqdgcsbtrud2121y.append(qqdssedoou2121y)
        qqdgcsbtrud2121z.append(qqdssedoou2121z)
    for i in range(len(qqdgcsgifvd2121)):
        qqdgffvdrevd2121.move(qqdgcsbtrud2121x[i], qqdgcsbtrud2121y[i], qqdgcsbtrud2121z[i], qqdgcsgifvd2121[i], relative=True) 
    for qqdgffeffvd2121 in qqdgffcesvd2121oints:
        qqdgcsbtrod2121 = qqdgffacsvd2121
        qqdgcotrod2121 = qqdgffvdrevd2121.xform(qqdgffeffvd2121, query=True, worldSpace=True, translation=True)
        qqdocotrod2121 = qqdgffvdrevd2121.createNode("closestPointOnMesh")
        qqdgffvdrevd2121.connectAttr(qqdgcsbtrod2121 + ".worldMesh", qqdocotrod2121 + ".inMesh")
        qqdgffvdrevd2121.setAttr(qqdocotrod2121 + ".inPosition", qqdgcotrod2121[0], qqdgcotrod2121[1], qqdgcotrod2121[2])
        qqdocuutrod2121 = qqdgffvdrevd2121.getAttr(qqdocotrod2121 + ".closestVertexIndex")
        qqdgffvdrevd2121.delete(qqdocotrod2121)
        vertex = qqdgcsbtrod2121 + ".vtx[{}]".format(qqdocuutrod2121)
        qqdgffvdrevd2121.select(vertex, replace=True)
        for i in range(1):
            qqdocbtrtrod2121 = qqdgffvdrevd2121.ls(selection=True, flatten=True)
            edges = []
            for vertex in qqdocbtrtrod2121:
                edges.extend(qqdgffvdrevd2121.polyListComponentConversion(vertex, fromVertex=True, toEdge=True))
            qqdgffvdrevd2121.select(edges)
            edges = qqdgffvdrevd2121.ls(selection=True, flatten=True)
            qqdocbtrtrod2121 = []
            for edge in edges:
                qqdocbtrtrod2121.extend(qqdgffvdrevd2121.polyListComponentConversion(edge, fromEdge=True, toVertex=True))
            qqdgffvdrevd2121.select(qqdocbtrtrod2121)
            qqdocbtrtrod2121 = qqdgffvdrevd2121.ls(selection=True, flatten=True)
        qqdocbtraod2121 = []
        for vertex in qqdocbtrtrod2121:
            position = qqdgffvdrevd2121.pointPosition(vertex, world=True)
            qqdocbtraod2121.append(position)
        qqdgffvdrevd2121.setAttr("TargetBS.CustomShape", 1)
        qqdocbtrbod2121 = []
        for vertex in qqdocbtrtrod2121:
            position = qqdgffvdrevd2121.pointPosition(vertex, world=True)
            qqdocbtrbod2121.append(position)
        qqdssedoou2121vertex = [] 
        for i in range(len(qqdocbtrbod2121)):
            qqdodbtrbod2121 = []
            for j in range(3):
                qqdodbtrbod2121.append(qqdocbtrbod2121[i][j] - qqdocbtraod2121[i][j])
            qqdssedoou2121vertex.append(qqdodbtrbod2121)
        qqdodbtrbgd2121 = [sum(x) / len(x) for x in zip(*qqdssedoou2121vertex)]
        qqdssedoou2121vrtx = qqdodbtrbgd2121[0]
        qqdssedoou2121vrty = qqdodbtrbgd2121[1]
        qqdssedoou2121vrtz = qqdodbtrbgd2121[2]
        if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121vrtx", node=qqdgffeffvd2121, exists=True):
            qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121vrtx", at="double")
        if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121vrty", node=qqdgffeffvd2121, exists=True):
            qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121vrty", at="double")
        if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121vrtz", node=qqdgffeffvd2121, exists=True):
            qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121vrtz", at="double")
        qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121vrtx", qqdssedoou2121vrtx)
        qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121vrty", qqdssedoou2121vrty)
        qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121vrtz", qqdssedoou2121vrtz)
        qqdgffvdrevd2121.setAttr("TargetBS.CustomShape", 0)
        if (-threshold < qqdgcotrod2121[0] < threshold):
            qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121vrtx", 0)
    qqdssedssu2121 = 1
    qqdssedu2121 = 0
    def select_root_bones():
        joints = qqdgffvdrevd2121.ls(type='joint')
        qqdsossdceoyth2121 = []
        for joint in joints:
            # Get the parent of the joints
            parent = qqdgffvdrevd2121.listRelatives(joint, parent=True)
            if not parent or qqdgffvdrevd2121.nodeType(parent[0]) != 'joint':
                qqdsossdceoyth2121.append(joint)
        qqdgffvdrevd2121.select(qqdsossdceoyth2121[0], replace=True)
    select_root_bones()
    selected_joint = qqdgffvdrevd2121.ls(selection=True, flatten=True)[0]
    rootqqdssedssu2121 = qqdgffvdrevd2121.getAttr(selected_joint + ".qqdghfggfvd2121")
    maxqqdssedssu2121 = rootqqdssedssu2121-1
    while qqdssedssu2121 <= maxqqdssedssu2121:
        joint_qqdssedssu2121 = [joint for joint in qqdgffcesvd2121oints if qqdgffvdrevd2121.getAttr(joint + ".qqdghfggfvd2121") == qqdssedssu2121]
        qqdscscedssu2121 = [joint for joint in qqdgffcesvd2121oints if qqdgffvdrevd2121.getAttr(joint + ".qqdghfggfvd2121") == qqdssedu2121]
        for qqdgffeffvd2121 in joint_qqdssedssu2121:
           first_place = qqdgffvdrevd2121.xform(qqdgffeffvd2121, q=True, ws=True, translation=True)
           child_joints = qqdgffvdrevd2121.listRelatives(qqdgffeffvd2121, children=True, type="joint")
           qqdscscsedscbtu2121 = []
           if child_joints:
               qqdscscedscbtu2121 = []
               for child_joint in child_joints:
                   if child_joint in qqdscscedssu2121:
                       qqdssedoou2121x = qqdgffvdrevd2121.getAttr(child_joint + '.qqdssedoou2121x')
                       qqdssedoou2121y = qqdgffvdrevd2121.getAttr(child_joint + '.qqdssedoou2121y')
                       qqdssedoou2121z = qqdgffvdrevd2121.getAttr(child_joint + '.qqdssedoou2121z')
                       qqdscscedscbtu2121.append([qqdssedoou2121x, qqdssedoou2121y, qqdssedoou2121z])
               qqdscscedscbtu2121.append([qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrtx'), qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrty'), qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrtz')])
               qqdscscedscbtu2121.append([qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrtx'), qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrty'), qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrtz')])
               qqdscscedscbtu2121.append([qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrtx'), qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrty'), qqdgffvdrevd2121.getAttr(qqdgffeffvd2121 + '.qqdssedoou2121vrtz')])
               qqdscscsedscbtu2121 = [sum(x) / len(x) for x in zip(*qqdscscedscbtu2121)]
               if not qqdscscsedscbtu2121:
                   qqdscscsedscbtu2121 = [0, 0, 0]
               qqdsouoyth2121x = qqdscscsedscbtu2121[0]
               qqdsouoyth2121y = qqdscscsedscbtu2121[1]
               qqdsouoyth2121z = qqdscscsedscbtu2121[2]
               qqdgffvdrevd2121.move(qqdsouoyth2121x, qqdsouoyth2121y, qqdsouoyth2121z, qqdgffeffvd2121, relative=True)
               for child_joint in child_joints:
                   qqdgffvdrevd2121.move(-qqdsouoyth2121x, -qqdsouoyth2121y, -qqdsouoyth2121z, child_joint, relative=True)
               end_place = qqdgffvdrevd2121.xform(qqdgffeffvd2121, q=True, ws=True, translation=True)
               qqdssedoou2121x = end_place[0] - first_place[0]
               qqdssedoou2121y = end_place[1] - first_place[1]
               qqdssedoou2121z = end_place[2] - first_place[2]
               if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121x", node=qqdgffeffvd2121, exists=True):
                   qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121x", at="double")
               if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121y", node=qqdgffeffvd2121, exists=True):
                   qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121y", at="double")
               if not qqdgffvdrevd2121.attributeQuery("qqdssedoou2121z", node=qqdgffeffvd2121, exists=True):
                   qqdgffvdrevd2121.addAttr(qqdgffeffvd2121, ln="qqdssedoou2121z", at="double")
               qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121x", qqdssedoou2121x)
               qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121y", qqdssedoou2121y)
               qqdgffvdrevd2121.setAttr(qqdgffeffvd2121 + ".qqdssedoou2121z", qqdssedoou2121z)           
        qqdssedu2121 += 1         
        qqdssedssu2121 += 1
def complete():
    new_mesh = qqdgffvdrevd2121.duplicate(qqdgffacsvd2121)[0]
    qqdgffvdrevd2121.setAttr(new_mesh+'.translateX', lock=False)
    qqdgffvdrevd2121.setAttr(new_mesh+'.translateY', lock=False)
    qqdgffvdrevd2121.setAttr(new_mesh+'.translateZ', lock=False)
    qqdgffvdrevd2121.move(75, 0, 0, new_mesh, relative=True)
    qqdsosuoyth2121 = "TargetBS"
    qqdgffvdrevd2121.blendShape(qqdsosuoyth2121, edit=True, target=(qqdgffacsvd2121, 1, new_mesh, 1.0))
    qqdgffvdrevd2121.setAttr("TargetBS."+new_mesh, -1)
    qqdgffvdrevd2121.setAttr("TargetBS.CustomShape", 1)
    qqdgffvdrevd2121.setAttr(new_mesh + ".visibility", 0)
    qqdgffvdrevd2121.setAttr("CustomShape" + ".visibility", 0)
    gender_mesh = qqdgffacsvd2121
    bind_skin(gender_mesh)
def move2target_joint():
    qqdgffadrevd2121 = qqdgffvdrevd2121.ls(selection=True)
    moving_joint = qqdgffadrevd2121[0]
    target_joint = qqdgffadrevd2121[1]
    mov_pos = qqdgffvdrevd2121.xform(moving_joint, query=True, worldSpace=True, rotatePivot=True)
    tar_pos = qqdgffvdrevd2121.xform(target_joint, query=True, worldSpace=True, rotatePivot=True)
    child_joints = qqdgffvdrevd2121.listRelatives(moving_joint, c=True, type="joint")
    child_positions = []
    for child_joint in child_joints:
        child_positions.append(qqdgffvdrevd2121.xform(child_joint, q=True, ws=True, t=True))
    qqdgffvdrevd2121.xform(moving_joint, translation=tar_pos, rotatePivot=mov_pos, worldSpace=True)
    for i, child_joint in enumerate(child_joints):
        qqdgffvdrevd2121.xform(child_joint, ws=True, t=child_positions[i])  
def refMove():
    qqdgffadrevd2121 = qqdgffvdrevd2121.ls(selection=True)
    moving = qqdgffadrevd2121[0]
    ref = qqdgffadrevd2121[1]
    xMoving = qqdgffvdrevd2121.xform(moving, query=True, worldSpace=True, rotatePivot=True)
    xRef = qqdgffvdrevd2121.xform(ref, query=True, worldSpace=True, rotatePivot=True)
    qqdgffvdrevd2121.xform(moving, translation=xRef, worldSpace=True)
def export_fbx():
    path = outPath
    filename = "Rigged_Character.fbx"
    filepath = path + "/" + filename
    # Export the selected objects as FBX
    qqdgffvdrevd2121.file(filepath, force=True, options="groups=0;ptgroups=0;materials=0;smoothing=1;normals=1", type='FBX export', exportSelected=True)
qqdgffacsvd2121="ok"
def show_dna_edit_window(outPath):
    window_name = "JOINT TRANSFORMATION TOOL"
    if qqdgffvdrevd2121.window(window_name, exists=True):
        qqdgffvdrevd2121.deleteUI(window_name)
    qqdgffvdrevd2121.window(window_name, title=window_name, width=360, height=500, sizeable=False, resizeToFitChildren=True)
    color = (0.164, 0.384, 0) # RGB values for #0077c2
    colorbuttons = (.2, 0.2, 0.2) # RGB values for #0077c2
    layout = qqdgffvdrevd2121.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 120)], columnSpacing=[(1,120)], backgroundColor=(0.1, 0.1, 0.1))
    qqdgffvdrevd2121.text(label="", height=10)    
    qqdgffvdrevd2121.text(label="JOINT TRNS", height=60, font="boldLabelFont")
    qqdgffvdrevd2121.text(label="", height=5)
    qqdgffvdrevd2121.button(label="Set Target Mesh", command=lambda x: target_mesh(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=5)
    qqdgffvdrevd2121.button(label="Set Eyes", command=lambda x: rename_eyes(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=5)
    qqdgffvdrevd2121.button(label="Eye Trns", command=lambda x: eye_transformation(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=25)
    text_field = qqdgffvdrevd2121.textField(text="0")
    qqdgffvdrevd2121.button(label="Threshold", command=lambda x: update_threshold(text_field), backgroundColor=color, height=20)
    qqdgffvdrevd2121.button(label="Exclude", command=lambda x: exclude(), backgroundColor=colorbuttons, height=20)
    qqdgffvdrevd2121.button(label="Joint Trns", command=lambda x: rig_transformation(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=5) 
    qqdgffvdrevd2121.button(label="Complete", command=lambda x: complete(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=25)   
    qqdgffvdrevd2121.button(label="Move Independent", command=lambda x: move2target_joint(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=5)  
    qqdgffvdrevd2121.button(label="Reference Move", command=lambda x: refMove(), backgroundColor=colorbuttons, height=40)
    qqdgffvdrevd2121.text(label="", height=5) 
    qqdgffvdrevd2121.button(label="Export", command=lambda x: export_fbx(outPath), backgroundColor=color, height=40)
    qqdgffvdrevd2121.text(label="", height=5)
    qqdgffvdrevd2121.text(label="ARTS AND SPELLS©2023",height=40, font="boldLabelFont")
    qqdgffvdrevd2121.showWindow()
outPath = "C:\Arts and Spells"
