import block_parent
import inspect

class Producer_Request_Block(block_parent.Block):
    hash = ""
    type_code = ""
    previous_hash = ""
    item_requested = ""
    request_name = ""
    number_of_item_requested = 0

    def __init__(self):
        self.hash = ""
        self.type_code = ""
        self.previous_hash = ""
        self.item_requested = ""
        self.number_of_item_requested = 0
        self.request_name = ""

    def get_hash(self):
        return hash

    def get_previous_hash(self):
        return previous_hash

    def set_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.item_requested.encode('utf-8'))
        hasher.update(str(self.number_of_item_requested).encode('utf-8'))
        hasher.update(self.request_name.encode('utf-8'))
        self.hash = hasher.hexdigest()

    def calculate_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.item_requested.encode('utf-8'))
        hasher.update(str(self.number_of_item_requested).encode('utf-8'))
        hasher.update(self.request_name.encode('utf-8'))
        return hasher.hexdigest()

    def equals(self, other):
        if (type(other) != type(self)):
            return False
        return (self.type_code == other.type_code
                and self.item_requested == other.item_requested
                and self.number_of_item_requested == other.number_of_item_requested
                and self.request_name == other.request_name)
