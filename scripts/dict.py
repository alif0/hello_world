# dictionary has key and values (items)

d1 = {"name": "ali", "class": "python"}
print(d1)

for key,value in d1.items():
  print(key, value)
  print("--------")

d2 = dict({"name": "syed", "class": "devops"})
print(d2)

print("--------------------------------------------------")
d3 = {"name": ["ali"], "class": ["python", "devops", "aws"], "name": ["syed"], "class" : ["datascience", "programming", "gcp"]}
for key,value in d3.items():
  print(key, value)
  print("--------")

print("--------------------------------------------------")
for key,value in d3.items():
  print(key)
  for v in (value):
    print("---", v)
  print("--------")

print("--------------------------------------------------")
for key,value in d3.items():
  print(key)
  for v in (value):
    print("--" + v)
  print("--------")

