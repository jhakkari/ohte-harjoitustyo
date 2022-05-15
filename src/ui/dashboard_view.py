from tkinter import ttk, constants, StringVar
from services.user_service import user_service
from services.course_service import course_services

class DashboardView:
    """Sovelluksen päänäkymä. Vastaa tallennettujen kurssien tietojen esittämisestä."""

    def __init__(self, root, handle_show_login_view, handle_show_add_course_view, handle_show_all_courses_view):
        """Luokan konstruktori. Luo uuden päänäkymän.

        Args:
            root: TKinter-elementti.
            handle_show_login_view: Kutsuttava arvo, kun kirjaudutaan ulos. Näyttää kirjautumis ikkunan.
            handle_show_add_course_view: Kutsuttava arvo, jonka kautta voidaan lisätä kursseja seurantaan.
            handle_show_all_courses_view: Kutsuttava arvo, näyttää kaikki seurannassa olevat kurssit.
        """

        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_add_course_view = handle_show_add_course_view
        self._handle_show_all_courses_view = handle_show_all_courses_view
        self._frame = None

        self._initialize()

    def pack(self):
        """TKinter toiminnallisuus"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """TKinter toiminnallisuus"""
        self._frame.destroy()

    def _handle_logout(self):
        user_service.logout()
        self._handle_show_login_view()

    def _handle_view_statistics(self):
        done = course_services.get_done_count()
        ongoing = course_services.get_ongoing_count()
        dropped = course_services.get_ongoing_count()
        done_credits = course_services.get_done_credits_count()
        ongoing_credits = course_services.get_ongoing_credits_count()
        done_hours = course_services.get_done_hours()
        approx_hours = course_services.get_approx_hours()

        done_label = ttk.Label(master=self._frame, text=f"Suoritetut kurssit: {done[0]}kpl")
        done_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        done_credits_label = ttk.Label(master=self._frame, text=f"Suoritetut opintopisteet: {done_credits[0]}op")
        done_credits_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        hours_label = ttk.Label(master=self._frame, text=f"Opintoihin käytetty aika: {done_hours[0]}t")
        hours_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        empty_label = ttk.Label(master=self._frame, text="")
        empty_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        ongoing_label = ttk.Label(master=self._frame, text=f"Keskeneräiset kurssit: {ongoing[0]}kpl")
        ongoing_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        ongoing_credits_label = ttk.Label(master=self._frame, text=f"Keskeneräiset opintopisteet: {ongoing_credits[0]}op")
        ongoing_credits_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        approx_hours_label = ttk.Label(master=self._frame, text=f"Arvioitu aika kurssia kohden: {approx_hours}t")
        approx_hours_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        empt_label = ttk.Label(master=self._frame, text="")
        empt_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        dropped_label = ttk.Label(master=self._frame, text=f"Keskeytetyt kurssit: {dropped[0]}kpl")
        dropped_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._frame, text="Tiedot opinnoistasi")
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self._handle_view_statistics()

        add_course_button = ttk.Button(master=self._frame, text="Lisää kurssi", command=self._handle_show_add_course_view)
        add_course_button.grid(row=10, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        all_courses_button = ttk.Button(master=self._frame, text="Kaikki kurssini", command=self._handle_show_all_courses_view)
        all_courses_button.grid(row=11, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        logout_button = ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self._handle_logout)
        logout_button.grid(row=12, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)


        self._frame.grid_columnconfigure(1, weight=1, minsize=400)