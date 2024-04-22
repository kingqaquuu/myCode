class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")


def main():
    restaurant = Restaurant("KFC", "Fast Food")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


if __name__ == "__main__":
    main()
