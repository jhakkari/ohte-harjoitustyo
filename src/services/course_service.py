from entities.course import Course
from repositories.course_repository import course_repository as default_course_repository
from services.user_service import user_service

class CourseService:
    """Vastaa kurssien hallinnoinnista"""

    def __init__(self):
        self._course_repository = default_course_repository
        self._user_service = user_service

    def new_course(self,name, credits, time_used, status):
        """Uuden kurssin tallentaminen. Palauttaa True, mikäli toiminto onnistui."""
        user_id = self._user_service.get_id()
        if self._course_repository.add_course(user_id, name, credits, time_used, status):
            return True
        else:
            return False

    def get_all_courses(self):
        """Palauttaa kaikki käyttäjän lisäämät kurssit."""
        user_id = self._user_service.get_id()
        results = self._course_repository.get_courses(user_id)
        return results

    def get_done_count(self):
        """Palauttaa käyttäjän tekemät kurssit."""
        user_id = self._user_service.get_id()
        results = self._course_repository.get_done_count(user_id)
        return results

    def get_ongoing_count(self):
        """Palauttaa käyttäjän meneillä olevat kurssit."""
        user_id = self._user_service.get_id()
        results = self._course_repository.get_ongoing_count(user_id)
        return results

    def get_dropped_count(self):
        """Palauttaa käyttäjän keskeyttämät kurssit"""
        user_id = self._user_service.get_id()
        results = self._course_repository.get_dropped_count(user_id)
        return results

    def get_done_credits_count(self):
        """Palauttaa käyttäjän tekemien kurssien opintopisteiden summan."""
        user_id = self._user_service.get_id()
        results = self._course_repository.get_done_credits_count(user_id)
        
        return results

    def get_ongoing_credits_count(self):
        """Palauttaa käyttäjän keskeneräisten kurssien opintopisteiden summan."""
        user_id = self._user_service.get_id()
        results = self._course_repository.get_ongoing_credits_count(user_id)
        return results

    def get_approx_hours(self):
        """Palauttaa kurssin viemän keskimääräisen ajan."""
        user_id = self._user_service.get_id()
        courses_hours = self._course_repository.get_done_hours(user_id)
        courses_count = self._course_repository.get_done_count(user_id)

        if courses_count[0] == 0:
            return 0
        
        return courses_hours[0] / courses_count[0]

    def get_done_hours(self):
        """Palauttaa suoritettujen kurssien viemän ajan lukumäärän."""
        user_id = self._user_service.get_id()
        hours = self._course_repository.get_done_hours(user_id)
        return hours


course_services = CourseService()