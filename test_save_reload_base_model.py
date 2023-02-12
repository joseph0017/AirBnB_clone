from models import storage
from models.base_model import BaseModel
import json

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

#testing out json.dump

# __file_path = 'filess.json'

# Dictionary ={
#     "name": "joseph",
#     "age": "26"
# }

# with open(__file_path, 'w', encoding='utf-8') as file:
#     json.dump(Dictionary, file)