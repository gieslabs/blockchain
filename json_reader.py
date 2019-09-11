import json

#This method just loads a json file from a given file.
def Load_Json(filename):
    #Replace this constant file path with whereever the json files will be stored on your computer.
    file_path = "C:\\Users\\Elliot'sLaptop\\Documents\\Blockchain research\\Python-Blockchain-library\\" + filename
    json_string = open(file_path).read()
    json_dict = json.loads(json_string)
    return json_dict
