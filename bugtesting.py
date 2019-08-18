import block_parent
import tree_chain

def main():
    tree_chain = tree_chain.Tree_Chain("producer_request_json")

    print(inspect.getmembers(tree_chain.root.data_block)[2:3])

main()
