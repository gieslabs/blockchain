import block_parent
import tree_chain
import inspect

def main():

    chain = tree_chain.Tree_Chain("producer_request_json")
    chain.root.add_child("supplier_json")
    found_node = chain.find_node("supplier_json")
    found_node.add_child("transport_json")
    #print(type(chain.root.child_list[0].child_list[0].data_block))

    print(inspect.getmembers(chain.find_node("transport_json").data_block)[2:3])

main()
