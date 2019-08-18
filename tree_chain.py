import tree_node
import tree_node_constructor

class Tree_Chain(object):
    #Add instance variable for the root here
    root = tree_node.Tree_Node()

    def __init__(self, filename):
        self.root =
            tree_node_constructor.construct_tree_node(None, filename)
