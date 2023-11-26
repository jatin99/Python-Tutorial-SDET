import json

# Your JSON string
json_string = '{"key": "value", "number": 42}'

# Load the JSON data from the string
# Load the JSON data from the file
with open('./day 5/data.json', 'r') as file:
    data = json.load(file)

# Now 'data' contains the content of the JSON string as a Python data structure
print(data['address']['street'])
print(data['name'])


