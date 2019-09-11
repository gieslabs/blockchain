import tree_node
import tree_node_constructor
import json_reader
import json_deserializer

"""
This class stores the overarching structure of the entire library
The tree contains tree nodes that all contant actual blockchain blocks are their data
Security is upheld because the blocks in the tree are still in an encryption chain,
however the organization structure allows the user to treat it like a tree, which is more suited to logistics
"""
class Tree_Chain(object):
    #The root is the start of the tree, initially empty
    root = tree_node.Tree_Node(None)

    #initialized with a filename that sets the data in the root to the json from the filename
    def __init__(self, filename):
        self.root = tree_node_constructor.construct_tree_node(None, filename)

    #Given the data for a block from the file, this method finds the node that contains this data in the tree.
    def find_node(self, filename):
        json_dict = json_reader.Load_Json(filename)
        block_to_find = json_deserializer.Desz(json_dict)
        return internal_find_node(self.root, block_to_find)

#An internal helper method for find_node
def internal_find_node(node, to_find):
    if node.data_block.equals(to_find):
        return node

    #print("Should see this")
    for x in node.child_list:
        potential_find = internal_find_node(x, to_find)
        if potential_find is not None:
            return potential_find


    return None
