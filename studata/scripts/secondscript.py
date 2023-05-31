from rest_framework import serializers
from rest_framework.parsers import JSONParser
import io
import json


"""import json
import io

# Assuming serialized_data is a JSON string
serialized_data = json.dumps({'key': 'value'})  # Replace with your serialized data

# Convert serialized_data to bytes
bytes_data = serialized_data.encode()

# Create a BytesIO object
bytes_io = io.BytesIO(bytes_data)

# Now you can use the bytes_io object as needed
# For example, you can read the contents using bytes_io.read()
"""
def run():
    d={"name":"Aniket"}
    serialized_data=json.dumps(d)
    bytes_data = serialized_data.encode()
    stream= io.BytesIO(bytes_data)
    parsedata= JSONParser.parse(stream)
    # print(data.read())
    print(parsedata)

