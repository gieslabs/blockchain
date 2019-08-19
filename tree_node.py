import block_parent
import tree_node_constructor

class Tree_Node(object):
    data_block = block_parent.Block()
    child_list = []

    def __init__(self, input_block):
        self.data_block = input_block
        self.child_list = []

    def add_child(self, filename):
        tree_node_constructor.construct_tree_node(self, filename)

    def equals(self, other):
        if type(self) is not type(other):
            return False
        if (self.data_block.equals(other.data_block)
            and self.child_list == other.child_list):
            return True
        return False
