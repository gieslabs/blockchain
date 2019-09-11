import product_block
import inspect
import producer_request_block
import transport_block
import supplier_block

"""
This is the method that will be called outside this file.
It takes a json and returns an initialized data block of the type and data specified in the json
"""
def Desz(json_dict):
    type_key = json_dict["type_code"]
    switcher = Switch()
    return switcher.choose_method(type_key, json_dict)

class Switch:
    """
    This method takes the type key and uses lambda expressions to make a method call
    out of the string for the appropriate creation method.
    This method essentially operates like a switch
    """
    def choose_method(self, type_key, json_dict):
        method_name = 'creator_for_' + type_key
        method = getattr(self,method_name,lambda :'Invalid')
        return method(json_dict)

    """
    If you want to add new block architypes in the future:
    1. Create a new creator method here
    2. Create the block class, inheriting from block_parent
    3. Thats it.
    """
    #Creates a Product Block
    def creator_for_0P(self, json_dict):
        p1 = product_block.Product_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)
    #Creates a Producer Request block
    def creator_for_PR(self, json_dict):
        p1 = producer_request_block.Producer_Request_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)
    #Creates a transport block
    def creator_for_0T(self, json_dict):
        p1 = transport_block.Transport_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)
    #Creates a supplier block
    def creator_for_0S(self, json_dict):
        p1 = supplier_block.Supplier_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)

"""
Using the list of fields this method sets all the fields of the given class
type according to the json.
"""
def initialize_block(block, json_dict, fields_list):
    for i in json_dict.keys():
        if (i in fields_list):
            setattr(block,i,json_dict[i])

    block.set_hash();
    return block

"""
The creation methods use a python tool called introspection to get a dictionary of
all fields and methods in a class

This method parses that output to find the instance variables and returns a list of them.
"""
def parse_inspect_spam(spam):
    fields_string = spam[15:len(spam)-3]
    fields = []

    fields_string = fields_string.replace("'", "")
    fields_string = fields_string.replace(" ", "")
    fields_string = fields_string.replace(",", "")
    fields_string = ''.join([i for i in fields_string if not i.isdigit()])

    fields_string = fields_string[:len(fields_string) - 1]
    fields = fields_string.split(':')
    return fields
