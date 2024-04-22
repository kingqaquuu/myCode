def main():
    guests = ["Yuan Leyi", "Suolong","但偏偏意气用事"]
    print(f"Hello {guests[0]}, would you like to have dinner with me?")
    print(f"Hello {guests[1]}, would you like to have dinner with me?")
    print(f"Hello {guests[2]}, would you like to have dinner with me?")
    print(f"{guests[2]} can't come to dinner.")
    guests[2] = "浪迹天涯是理想"
    print(f"Hello {guests[0]}, would you like to have dinner with me?")
    print(f"Hello {guests[1]}, would you like to have dinner with me?")
    print(f"Hello {guests[2]}, would you like to have dinner with me?")
    print("I found a bigger table.")
    guests.insert(0, "酒酿小袁子")
    guests.insert(2,"TASHUOAI")
    guests.append("袁乐怡")
    print(f"Hello {guests[0]}, would you like to have dinner with me?")
    print(f"Hello {guests[1]}, would you like to have dinner with me?")
    print(f"Hello {guests[2]}, would you like to have dinner with me?")
    print(f"Hello {guests[3]}, would you like to have dinner with me?")
    print(f"Hello {guests[4]}, would you like to have dinner with me?")
    print(f"Hello {guests[5]}, would you like to have dinner with me?")
    print("I can only invite two people to dinner.")
    print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
    print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
    print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
    print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
    print(f"Hello {guests[0]}, would you like to have dinner with me?")
    print(f"Hello {guests[1]}, would you like to have dinner with me?")
    del guests[0]
    del guests[0]
    print(guests)


if __name__ == "__main__":
    main()

