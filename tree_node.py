import block_parent
import tree_node_constructor


#Class for the nodes in the tree
class Tree_Node(object):
    data_block = block_parent.Block()
    #Each node stores a list of its children for search crazy
    child_list = []


    def __init__(self, input_block):
        self.data_block = input_block
        self.child_list = []

    def add_child(self, filename):
        tree_node_constructor.construct_tree_node(self, filename)

        #Equals checks if the node contains the same data as another and if their lists of children are equal
    def equals(self, other):
        if type(self) is not type(other):
            return False
        if (self.data_block.equals(other.data_block)
            and self.child_list == other.child_list):
            return True
        return False
