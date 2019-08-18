import json

def Load_Json(filename):
    file_path = "C:\\Users\\Elliot'sLaptop\\Documents\\Blockchain research\\Python-Blockchain-library\\" + filename
    json_string = open(file_path).read()
    json_dict = json.loads(json_string)
    return json_dict
