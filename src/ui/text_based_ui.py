from repositories import user_repository

class TextBasedUi:
    
    def start(self):
        OpeningScreen().start()


class OpeningScreen:

    def __init__(self):
        self.commands = {
            "x": "quit application",
            "1": "login",
            "2": "register"
        }

    def start(self):
        print("Studying time & credits tracker")
        while True:
            print("")
            print("x : quit application\n1 : login\n2 : register")
            print("")
            command = input("> ")

            if not command in self.commands:
                print("command not found")
                print("")

            if command == "x":
                break
            elif command == "1":
                LoginScreen().start()
            elif command == "2":
                RegisterScreen().start()

class LoginScreen:

    def start(self):
        print()
        print("USER LOGIN")
        username = input("Username: ")
        password = input("Password: ")

        results = user_repository.login(username, password)
        if results == False:
            print("")
            print("Wrong username or password. Try again.")
            self.start()

        LandingScreen(username).start()



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

        if len(username) < 5:
            print("Chosen username is too short. Minimum of 5 characters.")
            self.start()

        if len(password) < 5:
            print("Use longer password. Minimum of 5 characters.")
            self.start()

        results = user_repository.register(username, password)
        if results == True:
            print("New account created")
            print("")
            LandingScreen(username).start()
        else:
            print("Creating new account failed. Try again.")
            self.start()


class LandingScreen:

    def __init__(self, user):
        self.user = user
        self.commands = {
            "x": "log out"
        }

    def start(self):
        print("You are logged in as", self.user)
        print("")
        while True:
            print("x : logout")
            command = input("> ")

            if command == "x":
                break
