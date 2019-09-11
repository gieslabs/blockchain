import block_parent
import inspect

"""
See "producer_request_block.py" for general explanation of fields and methods in block classes
"""

class Transport_Block(block_parent.Block):
    hash = ""
    """
    type_code is an internal code appended to every information
    json by the front end to tell which type of block the json is supposed to represent
    """
    type_code = ""
    previous_hash = ""
    #Identification code for the truck so shipments can be individually tracked
    truck_id = ""
    contents_of_shipment = ""
    number_of_item = 0
    quality_of_item = ""

    def __init__(self):
        self.hash = ""
        self.type_code = ""
        self.previous_hash = ""
        self.truck_id = ""
        self.number_of_item = 0
        self.contents_of_shipment = ""
        self.quality_of_item = ""

    def get_hash(self):
        return hash

    def get_previous_hash(self):
        return previous_hash

    def set_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.contents_of_shipment.encode('utf-8'))
        hasher.update(str(self.number_of_item).encode('utf-8'))
        hasher.update(self.truck_id.encode('utf-8'))
        hasher.update(self.quality_of_item.encode('utf-8'))
        self.hash = hasher.hexdigest()

    def calculate_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.contents_of_shipment.encode('utf-8'))
        hasher.update(str(self.number_of_item).encode('utf-8'))
        hasher.update(self.truck_id.encode('utf-8'))
        hasher.update(self.quality_of_item.encode('utf-8'))
        return hasher.hexdigest()

    def equals(self, other):
        if (type(other) != type(self)):
            return False
        return (self.type_code == other.type_code
                and self.contents_of_shipment == other.contents_of_shipment
                and self.number_of_item == other.number_of_item
                and self.truck_id == other.truck_id
                and self.quality_of_item == other.quality_of_item)
