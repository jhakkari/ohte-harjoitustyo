from repositories import user_repository

class TextBasedUi:
    
    def start(self):
        OpeningScreen().start()


class OpeningScreen:

    def __init__(self):
        self.commands = {
            "X": "X quit application",
            "1": "1 register"}

    def start(self):
        while True:
            print(self.commands)
            command = input("> ")

            if not command in self.commands:
                print("command not found")

            if command == "X":
                break
            elif command == "1":
                RegisterScreen().start()



class RegisterScreen:

    def start(self):
        print()
        print("CREATE NEW ACCOUNT")
        username = input("Username: ")
        password = input(("Password: "))
        password_again = input("Re-enter password: ")

        if password != password_again:
            print("Passwords do not match. Try again.")
            self.start()

        if user_repository.register(username, password):
            print("New account created")
            LandingScreen().start()
        else:
            print("Creating new account failed. Try again.")
            self.start()


class LandingScreen:

    def start():
        print("You are logged in.")