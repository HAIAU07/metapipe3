#GNU General Public License
import pymel.core as pm
import maya.cmds as cmds
import sys

def calc():
    selected_meshes = cmds.ls(sl=True)
    targetblend = selected_meshes[0]
    # Assuming 'rl4Embedded_Archtype' is the name of the node
    node_name = 'head_lod0_mesh_blendShapes'

    # Get the PyNode for the specified node
    node = pm.PyNode(node_name)

    # Assuming 'bs_Output' is the name of the output attribute
    output_attr = node.weight

    # Get the connected plugs from the output attribute
    connected_plugs = output_attr.connections(plugs=True)
    blendIndex = []
    # Iterate over the connected plugs and print their values
    for index, plug in enumerate(connected_plugs, start=1):
        sub_node_value = plug.get()
        if sub_node_value == 1:
            print("Sub-node {} value: {}".format(index-1, sub_node_value))
            blendIndex = index-1
    print (blendIndex)
    blend_shape_node = 'head_lod0_mesh_blendShapes'
    rebuild_mesh = cmds.sculptTarget(blend_shape_node, e=True, regenerate=True, target=blendIndex)
    cmds.select(rebuild_mesh)
    blend_shape_node = "blendShape1"
    cmds.blendShape(rebuild_mesh[0], automatic=True)
    cmds.blendShape(blend_shape_node, edit=True, target=(rebuild_mesh[0], 2, targetblend+"_corrective", 1.0))
    cmds.setAttr(blend_shape_node+"."+targetblend+"_corrective", 1)
    #cmds.delete(rebuild_mesh[0])
    cmds.delete(targetblend+"_corrective")