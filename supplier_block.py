import block_parent
import inspect

class Supplier_Block(block_parent.Block):
    hash = ""
    type_code = ""
    previous_hash = ""
    supplier_id = ""
    number_of_item = 0
    item_supplied = ""

    def __init__(self):
        self.hash = ""
        self.type_code = ""
        self.previous_hash = ""
        self.supplier_id = ""
        self.number_of_item = 0
        self.item_supplied = ""

    def get_hash(self):
        return hash

    def get_previous_hash(self):
        return previous_hash

    def set_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.supplier_id.encode('utf-8'))
        hasher.update(str(self.number_of_item).encode('utf-8'))
        hasher.update(self.item_supplied.encode('utf-8'))
        self.hash = hasher.hexdigest()

    def calculate_hash(self):
        hasher = block_parent.hashlib.sha224()
        hasher.update(self.type_code.encode('utf-8'))
        hasher.update(self.previous_hash.encode('utf-8'))
        hasher.update(self.supplier_id.encode('utf-8'))
        hasher.update(str(self.number_of_item).encode('utf-8'))
        hasher.update(self.item_supplied.encode('utf-8'))
        return hasher.hexdigest()

    def equals(self, other):
        if (type(other) != type(self)):
            return False
        return (self.type_code == other.type_code
                and self.supplier_id == other.supplier_id
                and self.number_of_item == other.number_of_item
                and self.item_supplied == other.item_supplied)
