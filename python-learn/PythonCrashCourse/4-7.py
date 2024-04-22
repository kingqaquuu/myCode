def main():
    list1 = []
    for i in range(3, 31):
        if i % 3 == 0:
            list1.append(i)
    for i in list1:
        print(i, end=" ")


if __name__ == "__main__":
    main()
