from to_json import to_json

@to_json
def get_data():
    return {"answer": 42}

print(f"Function value:\t{ get_data() }\nFunction name:\t{ get_data.__name__ }")