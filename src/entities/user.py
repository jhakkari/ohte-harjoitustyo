class User:
    """Tämä luokka kuvaa yksittäistä käyttäjää."""

    def __init__(self, id, username, password):
        """Luokan konstruktori. Luo uuden käyttäjän.

        Args:
            id: Käyttäjän yksilöivä id-numero.
            username: Käyttäjän käyttäjätunnus.
            password: Käyttäjän salasana.
        """

        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        """Palauttaa käyttäjän id-numeron"""
        return self.id
