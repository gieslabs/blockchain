import tree_node
import tree_node_constructor
import json_reader
import json_deserializer

class Tree_Chain(object):
    #Add instance variable for the root here
    root = tree_node.Tree_Node(None)

    def __init__(self, filename):
        self.root = tree_node_constructor.construct_tree_node(None, filename)

    def find_node(self, filename):
        json_dict = json_reader.Load_Json(filename)
        block_to_find = json_deserializer.Desz(json_dict)
        return internal_find_node(self.root, block_to_find)

def internal_find_node(node, to_find):
    if node.data_block.equals(to_find):
        return node

    #print("Should see this")
    for x in node.child_list:
        potential_find = internal_find_node(x, to_find)
        if potential_find is not None:
            return potential_find

    return None
