import block_parent
import inspect


class Producer_Request_Block(block_parent.Block):
    hash = ""
    """
    type_code is an internal code appended to every information
    json by the front end to tell which type of block the json is supposed to represent
    """
    type_code = ""
    previous_hash = ""
    #Data inputed through the json
    item_requested = ""
    #Represets what a producer would label their request, inputed through json
    request_name = ""
    #inputed through json
    number_of_item_requested = 0

    """
    This is required so that the variables will exist when we search for the
    fields with introspection.
    """
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

    """
    hasher stores an object that uses the elements added to make an encryped hash
    the .hexdigest() returns the actual hash
    """
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

    """
    Verifies that both objects are the same type then compares every field other than hash
    and previous_hash since those are unique to every block.
    """
    def equals(self, other):
        if (type(other) != type(self)):
            return False
        return (self.type_code == other.type_code
                and self.item_requested == other.item_requested
                and self.number_of_item_requested == other.number_of_item_requested
                and self.request_name == other.request_name)
