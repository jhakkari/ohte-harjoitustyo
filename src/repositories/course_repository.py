from db_connection import get_database_connection
from entities.course import Course

class CourseRepository:

    def add_course(self, user_id, name, credits, time_used, status):
        connection = get_database_connection()
        cursor = connection.cursor()
        try:
            sql = ("INSERT INTO courses (user_id, name, credits, time_used, status) VALUES (:user_id, :name, :credits, :time_used, :status)")
            connection.execute(sql, {"user_id":user_id, "name":name, "credits":credits, "time_used":time_used, "status":status})
            connection.commit()
            return True
        except:
            return False

    def get_courses(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        courses = cursor.execute("SELECT id, name, credits, time_used, status FROM courses WHERE user_id=:user_id", {"user_id":user_id}).fetchall()
        return courses

    def get_done_count(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        results = cursor.execute("SELECT COUNT(*) FROM courses WHERE status='valmis' and user_id=:user_id", {"user_id":user_id}).fetchone()
        return results

    def get_ongoing_count(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        results = cursor.execute("SELECT COUNT(*) FROM courses WHERE status='kesken' and user_id=:user_id", {"user_id":user_id}).fetchone()
        return results

    def get_dropped_count(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        results = cursor.execute("SELECT COUNT(*) FROM courses WHERE status='keskeytetty' and user_id=:user_id", {"user_id":user_id}).fetchone()
        return results

    def get_done_credits_count(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        results = cursor.execute("SELECT SUM(credits) FROM courses WHERE status='valmis' and user_id=:user_id", {"user_id":user_id}).fetchone()
        return results

    def get_ongoing_credits_count(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        results = cursor.execute("SELECT SUM(credits) FROM courses WHERE status='kesken' and user_id=:user_id", {"user_id":user_id}).fetchone()
        return results

    def get_statistics(user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        result = cursor.execute("SELECT COUNT(name), SUM(time_used), SUM(credits) FROM courses WHERE user_id=:user_id", {"user_id":user_id}).fetchone()
        return result

    def get_done_hours(self, user_id):
        connection = get_database_connection()
        cursor = connection.cursor()

        results = cursor.execute("SELECT SUM(time_used) FROM courses WHERE status='valmis' and user_id=:user_id", {"user_id":user_id}).fetchone()
        return results

course_repository = CourseRepository()