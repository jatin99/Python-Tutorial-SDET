import configparser 
import json
#pip install configparser 

class Utilities:
    config = configparser.ConfigParser()
        

    @staticmethod
    def get_data(fileName, section_name, variable):
        Utilities.config.read("./Day 5/"+fileName) 
        return Utilities.config.get(section_name, variable)

    @staticmethods
    def get_json_data(filename,keyname):
        with open("./Day 5/"+filename, "r") as file: 
            data = json.load(file)
        return data[keyname]


print(Utilities.get_data("config.ini","Database", "host"))
print(Utilities.get_data("config.ini","Settings", "username"))
print(Utilities.get_json_data("data.json","name"))