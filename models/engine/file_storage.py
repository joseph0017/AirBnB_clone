"""Module for file_storage"""
import json

class FileStorage():
    """
    a class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """   
        json_data = FileStorage.__objects
        json_object = {obj: json_data[obj].to_dict() for obj in json_data.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_object, file, default=lambda o: o.__dict__, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised
        """
        dict_ = {}
        try:
            with open(self.__file_path, "r") as f:
                dict_ = json.loads(f.read())
                for key, value in dict_.items():
                    class_name = key.split(".")
                    self.__objects[key] = eval(class_name[0])(**value)
        except FileNotFoundError:
            pass
