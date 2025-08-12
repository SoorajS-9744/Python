import json

data = {'name': 'soo', 'age': 25, 'place': 'clt'}

# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

with open('data.json', 'r') as file:
    x = json.load(file)
print(x)
