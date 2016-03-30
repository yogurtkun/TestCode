import json

a = [(1,2),(2,3),3,4,6]

a_json = json.dumps(a)

print(a_json)

b = json.loads(a_json)

print(b)