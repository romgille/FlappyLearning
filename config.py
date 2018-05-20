import json

cfg = []

with open('conf.json', 'r') as json_data_file:
    cfg = json.load(json_data_file)
