import json
from functools import wraps

def to_json(function):
    @wraps(function)
    def wrapper():
        return json.dumps(function())
    
    return wrapper