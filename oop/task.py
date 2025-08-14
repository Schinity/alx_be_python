import json

data = {
    "name": "nmaju terence",
    "age": 30,
    "location": "buea",
    "occupation": "web developer",
    "website": "www.bigtee.io"
}
# Convert the dictionary to a JSON string with indentation
json_data = json.dumps(data, indent=4)
# Print the JSON string
print(json_data)
# Save the JSON string to a file
with open("data.json", "w") as json_file:
    json_file.write(json_data)

# Deserialize the JSON string back into a Python dictionary
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

# Print the loaded data
print(loaded_data)