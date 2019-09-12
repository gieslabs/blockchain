Welcome to the blockchain logistics library:

To utilize the library:
1. Json files are used as the input for all block creation.
2. In order to run anything you will need to update the file path in json_reader.
3. After doing that you will be able to call the Tree_Chain constructor to create the root of your tree.
4. At this point simply call add_child on any tree_node which you want to add a child to with an appropriate filename leading to a json.

To add new block types:
1. You must write the class file for the new block(it must inherit from block_parent and implement all of the methods).
2. You must come up with a type_code for your new block that is unique to that block type.
3. Last you must implement the creator method in the json_deserializer file named according to your type_code.
  a. For how to implement this method, base it off of the other creator methods.
  b. The only parts that have to be changed are the type of block you construct in the first line and the name of the method.
4. You can now construct your new block type with an appropriate json.

Extra tips:
1. If you pass in a json that does not contain all the fields for a block type, it will only set the fields that were given data. This is because I believe this part should be handled on the front-end(i.e. not allowing the user to submit incomplete information).
2. You can view the sample_main to see how I implemented a simple tree and demonstrated the find_node function.
