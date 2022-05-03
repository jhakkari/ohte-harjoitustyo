from db_connection import get_database_connection

def add_course(name, credits, time_used, status, creator):
    connection = get_database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO courses VALUES (?, ?, ?, ?, ?)", (name, credits, time_used, status, creator))
        connection.commit()
        return True
    except:
        return False

def get_courses(creator):
    connection = get_database_connection()
    cursor = connection.cursor()

    courses = cursor.execute("SELECT name, credits, time_used, status FROM courses WHERE creator=:creator", {"creator":creator}).fetchall()
    return courses

def get_statistics(creator):
    connection = get_database_connection()
    cursor = connection.cursor()

    result = cursor.execute("SELECT COUNT(name), SUM(time_used), SUM(credits) FROM courses WHERE creator=:creator", {"creator":creator}).fetchone()
    return result

def remove_course(name):
    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM courses WHERE name=:name", {"name":name})
        connection.commit()
        return True
    except:
        return False