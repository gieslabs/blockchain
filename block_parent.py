import hashlib
"""
    The block class acts as a parent to every other block implemented.
    All of its methods must be implemented in all of the child blocks.
"""
class Block(object):
    #This method returns the hash of the current block.
    def get_hash(self):
        pass
    #This method returns the hash of the block before it in the chain.
    #This info is stored in every block.
    def get_previous_hash(self):
        pass
    #This method calculates the hash of the block and sets the hash field to the calculated value.
    def set_hash(self):
        pass
    #This method calculates the hash of the block used to call it and returns that hash
    def calculate_hash(self):
        pass
    #The equals method checks if the block used to call and the passes block are equal in all ways
    def equals(self, other):
        pass
    #Constructor for the block, different for each block
    def init(self):
        pass
