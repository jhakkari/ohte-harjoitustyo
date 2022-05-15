from db_connection import get_database_connection
from entities.user import User

class UserRepository:
    """Vastaa käyttäjiin liittyvistä tietokantaoperaatioista"""

    def register(username, password):
        """Rekisteröi uuden käyttäjän."""
        try:
            connection = get_database_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))

            connection.commit()
        except:
            return False

        return login(username, password)

    def login(username, password):
        """Tarkastaa annetut tiedot, palauttaa User olion, mikäli pitävät paikkaansa."""
        connection = get_database_connection()
        cursor = connection.cursor()

        user = cursor.execute("SELECT id, username, password FROM users WHERE username=:username", {"username":username}).fetchone()
        if not user:
            return None
        else:
            if user[2] == password:
                return User(user[0], username, password)
            else:
                return None

    def check_existing_user(self, username):
        """Tarkastaa, löytyykö annetulla käyttäjänimellä osumaa tietokannasta"""
        connection = get_database_connection()
        cursor = connection.cursor()

        user = cursor.execute("SELECT * FROM users WHERE username=:username", {"username":username}).fetchone()
        if not user:
            return False
        else:
            return True

    def new_user(self, username, password):
        """Tallentaa uuden käyttäjän tietokantaan."""
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

        connection.commit()

    def check_user_credentials(self, username, password):
        """Tarkastaa, pitävätkö annetut tiedot paikkaansa."""
        connection = get_database_connection()
        cursor = connection.cursor()
        user = cursor.execute("SELECT id, username, password FROM users WHERE username=:username", {"username":username}).fetchone()
        if not user:
            return None
        else:
            if user[2] == password:
                return User(user[0], username, password)
            else:
                return None

user_repository = UserRepository()
