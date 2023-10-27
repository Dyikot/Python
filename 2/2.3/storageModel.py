
import json
import os

def Add(storagePath: str, key, value) -> None:
    def Serialize(jsonString) -> None:
        with open(storagePath, "w") as file:
            file.write(jsonString)
    
    def Deserialize() -> dict:
         with open(storagePath, "r") as file:
             return json.load(file)
         
    if not os.path.exists(storagePath):
        Serialize(json.dumps({key: value}))
    else:
        dictionary = Deserialize()
        existingValue = dictionary.get(key)

        if existingValue is not None:
            if type(existingValue) is list:
                existingValue.append(value)
                value = existingValue
            else:
                value = [existingValue, value]

        dictionary.update({key: value})
        Serialize(json.dumps(dictionary))
        
def Clear(storagePath: str) -> None:
    if os.path.exists(storagePath):
        os.remove(storagePath)

def GetValue(storagePath: str, key):
    if os.path.exists(storagePath):
        with open(storagePath, "r") as file:
            dictionary = json.load(file)
            if type(dictionary) is dict:
                return dictionary.get(key)
    
    return None