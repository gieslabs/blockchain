import json_reader
import json_deserializer
import tree_node

"""
This method constructs a tree node with a data_block represented by the file
It also checks the parents to get the previous hash for the data block
"""
def construct_tree_node(parent, filename):
    current_dict = json_reader.Load_Json(filename)
    current_block = json_deserializer.Desz(current_dict)

    if (parent is not None):
        current_block.previous_hash = parent.data_block.hash

    node = tree_node.Tree_Node(current_block)

    if (parent is not None):
        parent.child_list.append(node)

    return node
