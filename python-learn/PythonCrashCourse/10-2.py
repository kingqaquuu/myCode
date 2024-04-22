filename = "learning_python.txt"
with open(filename) as file_object:
    contents = file_object.read()
contents1 = contents.replace("Python", "C")
print(contents1)
