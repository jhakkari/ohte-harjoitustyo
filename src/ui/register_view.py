from tkinter import ttk, constants, StringVar
from services.user_service import user_service

class RegisterView:
    """Uuden käyttäjän rekisteröinnistä vastaava näkymä."""

    def __init__(self, root, handle_show_login_view, handle_show_dashboard_view):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.

        Args:
            root: TKinter elementti, johon näkymä alustetaan.
            handle_show_login_view: Kutsuttava arvo, kutsutaan kun halutaan takaisin kirjautumisnäkymään.
            handle_show_dashboard_view: Kutsuttava arvo, kutsutaan jos rekisteröinti onnistuu. Siirtää sovelluksen etusivulle,
        """

        self._root = root
        self.handle_show_login_view = handle_show_login_view
        self._handle_show_dashboard_view = handle_show_dashboard_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_again_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """TKinter toiminnallisuus"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """TKinter toiminnallisuus"""
        self._frame.destroy()

    def _show_error(self, error_message):
        self._error_variable.set(error_message)
        self._error_label.grid()

    def _hide_error(self):
        self.error_label.grid_remove()

    def _handle_register_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_again = self._password_again_entry.get()

        if len(username) < 8 or len(password) < 8:
            self._show_error("Käyttäjätunnus tai salasana on liian lyhyt")
        elif password != password_again:
            self._show_error("Salasanat eivät täsmää")
        else:
            if user_service.register(username, password, password_again):
                if user_service.login(username, password):
                    self._handle_show_dashboard_view()
                else:
                    self._show_error("Käyttäjätunnuksen luominen ei onnistunut. Yritä uudelleen.")




    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        header_label = ttk.Label(master=self._frame, text="Luo uusi käyttäjätunnus")
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        new_username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        new_username_label.grid(row=1, column=0, padx=5, pady=5)

        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        password_label.grid(row=2, column=0, padx=5, pady=5)

        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_again_label = ttk.Label(master=self._frame, text="Salasana uudelleen")
        password_again_label.grid(row=3, column=0, padx=5, pady=5)

        self._password_again_entry = ttk.Entry(master=self._frame)
        self._password_again_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        info_label = ttk.Label(master=self._frame, text="Käyttäjätunnuksen ja salasanan tulee olla vähintään 8 merkkiä pitkiä.")
        info_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self._error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        create_new_user_button = ttk.Button(master=self._frame, text="Rekisteröidy", command=self._handle_register_click)
        create_new_user_button.grid(columnspan=6, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        back_to_login_button = ttk.Button(master=self._frame, text="Takaisin", command=self.handle_show_login_view)
        back_to_login_button.grid(columnspan=7, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

