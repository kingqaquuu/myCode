class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0


def describe_user(self):
    print(f"First name: {self.first_name}")
    print(f"Last name: {self.last_name}")


def greet_user(self):
    print(f"Hello, {self.first_name} {self.last_name}!")


def increment_login_attempts(self):
    self.login_attempts += 1


def reset_login_attempts(self):
    self.login_attempts = 0


def main():
    user = User("Leyi", "Yuan")
    describe_user(user)
    greet_user(user)
    print(f"Login attempts: {user.login_attempts}")
    increment_login_attempts(user)
    increment_login_attempts(user)
    increment_login_attempts(user)
    print(f"Login attempts: {user.login_attempts}")
    reset_login_attempts(user)
    print(f"Login attempts: {user.login_attempts}")


if __name__ == "__main__":
    main()
