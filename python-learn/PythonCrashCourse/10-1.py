filename = "learning_python.txt"
list1 = list()
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
with open(filename) as file_object:
    for c in file_object:
        list1.append(c)
print(list1)
