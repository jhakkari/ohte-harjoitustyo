class Course:

    """Tämä luokka kuvaa yksittäistä kurssia."""

    def __init__(self, id, user_id, name, credits, time_used, status):
        """Luokan konstruktori, luo uuden kurssin.

        Args:
            id: Kurssin yksilöivä id-numero.
            user_id: Kurssin luoneen käyttäjän yksilöivä id-numero.
            name: Kurssin nimi.
            credits: Kurssin laajuus (opintopisteet)
            time_used: Kurssin suorittamiseen käytetty aika.
            status: Kurssin tilanne: valmis/kesken/keskeytetty
        """
        
        self.id = id
        self.user_id = user_id
        self.name = name
        self.credits = credits
        self.time_used = time_used
        self.status = status

