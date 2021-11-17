import json

x1 =  '{ "name":"John", "age":30, "city":"New York"}'

y1 = json.loads(x1)

print(y1["age"])


x2 = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y2 = json.dumps(x2)

print(y2)