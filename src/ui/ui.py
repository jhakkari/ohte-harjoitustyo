from ui.register_view import RegisterView
from ui.login_view import LoginView
from ui.dashboard_view import DashboardView
from ui.add_course_view import AddCourseView
from ui.all_courses_view import AllCoursesView

class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""
    def __init__(self, root):
        """Luo uuden graafisesta käyttöliittymästä vastaavan luokan.

        Args:
            root: TKinter elementti, johon käyttöliitymä alustetaan.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän kirjautumisnäkymän."""
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self._show_login_view, self._show_dashboard_view)

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._show_register_view, self._show_dashboard_view)

        self._current_view.pack()

    def _show_dashboard_view(self):
        self._hide_current_view()
        self._current_view = DashboardView(self._root, self._show_login_view, self._add_course_view, self._all_courses_view)

        self._current_view.pack()
    
    def _add_course_view(self):
        self._hide_current_view()
        self._current_view = AddCourseView(self._root, self._show_dashboard_view)

        self._current_view.pack()

    def _all_courses_view(self):
        self._hide_current_view()
        self._current_view = AllCoursesView(self._root, self._show_dashboard_view)

        self._current_view.pack()