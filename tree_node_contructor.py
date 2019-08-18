import json_reader
import json_deserializer
import tree_node

def construct_tree_node(parent, filename):
    current_dict = json_reader.Load_Json(filename)
    current_block = json_deserializer.Desz(current_dict)

    if (parent is not None):
        current_block.previous_hash = parent.data_block.hash

    tree_node = Tree_Node(current_block)

    if (parent is not None):
        parent.child_list.append(tree_node)
        
    return tree_node
