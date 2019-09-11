import block_parent
import inspect

"""
See "producer_request_block.py" for general explanation of fields and methods in block classes
"""

class Product_Block(block_parent.Block):
    hash = ""
    """
    type_code is an internal code appended to every information
    json by the front end to tell which type of block the json is supposed to represent
    """
    type_code = ""
    previous_hash = ""
    item_name = ""
    number_of_item = 0

    def __init__(self):
        self.hash = ""
        self.type_code = ""
        self.previous_hash = ""
        self.item_name = ""
        self.number_of_item = 0

    def get_hash(self):
        return hash

    def get_previous_hash(self):
        return previous_hash

    def set_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.item_name.encode('utf-8'))
        hasher.update(str(self.number_of_item).encode('utf-8'))
        self.hash = hasher.hexdigest()

    def calculate_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.item_name.encode('utf-8'))
        hasher.update(str(self.number_of_item).encode('utf-8'))
        return hasher.hexdigest()

    def equals(self, other):
        if (type(other) != type(self)):
            return False
        return (self.type_code == other.type_code
                and self.item_name == other.item_name
                and self.number_of_item == other.number_of_item)
