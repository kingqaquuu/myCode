filename = "guest_book.txt"
with open(filename, "a") as file_object:
    while True:
        name = input("Please enter your name\n")
        print("Hello ", name)
        file_object.write(name + "\n")
