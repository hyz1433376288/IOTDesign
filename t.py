
import json

a = [i for i in range(0, 5)]
data = {
    'name':"sam",
    'length':a
}
filename = "data.json"
with open(filename, 'w') as file_obj:
    json.dump(data, file_obj)
with open(filename, 'r') as file_obj:
    jstr = json.load(file_obj)
    print(jstr)