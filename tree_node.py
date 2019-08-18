import block_parent

class Tree_Node(object):
    data_block = block_parent.Block()
    child_list = []

    def __init__(self, input_block):
        self.data_block = input_block
