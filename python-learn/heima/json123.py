import json
data=[{'name':'kingqaquuu','age':21},{'name':'suolong','age':20}]
data=json.dumps(data)
print(data)
data=json.loads(data)
print(data)