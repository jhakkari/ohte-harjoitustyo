from db_connection import get_database_connection

def register(username, password):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))

        connection.commit()
    except:
        return False

    return login(username, password)

def login(username, password):
    connection = get_database_connection()
    cursor = connection.cursor()

    user = cursor.execute("SELECT username, password FROM users WHERE username=:username", {"username":username}).fetchone()
    if not user:
        return False
    else:
        if user[1] == password:
            print("Olet kirjautunut sisään!")
            return True
        else:
            print("salasanat ei täsmää")
            return False