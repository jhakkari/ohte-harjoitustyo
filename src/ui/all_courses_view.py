from tkinter import ttk, constants
from services.course_service import course_services

class AllCoursesView:

    def __init__(self, root, handle_show_dashboard_view):
        self._root = root
        self._handle_show_dashboard_view = handle_show_dashboard_view
        self._frame = None
        self._row_number = 1

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_show_course_info(self):
        courses = course_services.get_all_courses()

        if not courses:
            no_courses_label = ttk.Label(master=self._frame, text="Täällä on vielä tyhjää.")
            no_courses_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
            self._row_number += 1
        
        for course in courses:
            course_label = ttk.Label(master=self._frame, text=f"Nimi: {course[1]} laajuus: {course[2]} käytetty aika: {course[3]}h tila: {course[4]}")
            course_label.grid(row=self._row_number, columnspan=2, padx=5, pady=5)

            self._row_number += 1
    

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._frame, text="Omat kurssini")
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self._handle_show_course_info()

        dashboard_button = ttk.Button(master=self._frame, text="Takaisin", command=self._handle_show_dashboard_view)
        dashboard_button.grid(row=self._row_number, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)