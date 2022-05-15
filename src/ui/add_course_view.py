from tkinter import ttk, constants, IntVar, OptionMenu, StringVar
from services.course_service import course_services

class AddCourseView:
    def __init__(self, root, handle_show_dashboard_view):
        self._root = root
        self._handle_show_dashboard_view = handle_show_dashboard_view
        self._frame = None
        self._course_name_entry = None
        self._course_credits_entry = None
        self._course_time_used_entry = None
        self._course_status_entry = None
        self._error_variable = None
        self._error_label = None


        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, error_message):
        self._error_variable.set(error_message)
        self._error_label.grid()

    def _hide_error(self):
        self.error_label.grid_remove()

    def _handle_add_course(self):
        name = self._course_name_entry.get()
        status = self._course_status_entry.get()
        credits = self._course_credits_entry.get()
        time_used = self._course_time_used_entry.get()

        success = course_services.new_course(name, credits, time_used, status)

        if success:
            self._handle_show_dashboard_view()
        else:
            self._show_error("Tarkasta syöttämäsi tiedot.")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        credits_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        status_options = ["kesken", "valmis", "keskeytetty"]

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        header_label = ttk.Label(master=self._frame, text="Anna lisättävän kurssin tiedot")
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        name_label = ttk.Label(master=self._frame, text="Kurssin nimi")
        name_label.grid(row=1, column=0, padx=5, pady=5)

        self._course_name_entry = ttk.Entry(master=self._frame)
        self._course_name_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        credits_label = ttk.Label(master=self._frame, text="Kurssin laajuus (op)")
        credits_label.grid(row=2, column=0)
        self._course_credits_entry = IntVar()
        self._course_credits_entry.set(1)
        credits_menu = OptionMenu(self._frame, self._course_credits_entry, *credits_options)
        credits_menu.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)


        used_hours_label = ttk.Label(master=self._frame, text="Kurssiin käytetty aika (tunteina)")
        used_hours_label.grid(row=3, column=0)
        self._course_time_used_entry = ttk.Entry(master=self._frame)
        self._course_time_used_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)



        status_label = ttk.Label(master=self._frame, text="Kurssin tilanne")
        status_label.grid(row=4, column=0)
        self._course_status_entry = StringVar()
        self._course_status_entry.set("kesken")
        credits_menu = OptionMenu(self._frame, self._course_status_entry, *status_options)
        credits_menu.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        add_course_button = ttk.Button(master=self._frame, text="Lisää seurantaan", command=self._handle_add_course)
        add_course_button.grid(row=6, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        dashboard_button = ttk.Button(master=self._frame, text="Takaisin", command=self._handle_show_dashboard_view)
        dashboard_button.grid(row=7, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
