import argparse
import os
import tempfile
import storageModel

parser = argparse.ArgumentParser()
parser.add_argument("-k","--key", help="The key is needed to access the value.")
parser.add_argument("-v","--value", help="The value you get when you enter the key.")
parser.add_argument("--clear", action="store_true", help="Clears storage.")

args = parser.parse_args()
key, value, clear = args.key, args.value, args.clear
storagePath = os.path.join(tempfile.gettempdir(), "storageData.data")

if clear:
    storageModel.Clear(storagePath)
    print("Storage cleared.")
elif key and value:
    storageModel.Add(storagePath, key, value)
elif key:
    outputValue = storageModel.GetValue(storagePath, key)
    
    if type(outputValue) is str or outputValue is None:
        print(outputValue)
    else:
        ", ".join(outputValue)