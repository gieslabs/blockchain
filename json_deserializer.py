import product_block
import inspect
import producer_request_block
import transport_block
import supplier_block

#Gets passed a dictionary
def Desz(json_dict):
    type_key = json_dict["type_code"]
    switcher = Switch()
    return switcher.choose_method(type_key, json_dict)

class Switch:
    def choose_method(self, type_key, json_dict):
        method_name = 'creator_for_' + type_key
        method = getattr(self,method_name,lambda :'Invalid')
        return method(json_dict)

    def creator_for_0P(self, json_dict):
        p1 = product_block.Product_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)

    def creator_for_PR(self, json_dict):
        p1 = producer_request_block.Producer_Request_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)

    def creator_for_0T(self, json_dict):
        p1 = transport_block.Transport_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)

    def creator_for_0S(self, json_dict):
        p1 = supplier_block.Supplier_Block()
        inspect_spam = inspect.getmembers(p1)
        fields_list = parse_inspect_spam(str(inspect_spam[2:3]))
        return initialize_block(p1, json_dict, fields_list)

def initialize_block(block, json_dict, fields_list):
    for i in json_dict.keys():
        if (i in fields_list):
            setattr(block,i,json_dict[i])

    #This might not actually be where I want to set the hash,
    #it might be done in a construction factory that wraps
    #what this file does
    block.set_hash();
    return block


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
