from db_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()

    cursor.execute('''
        drop table if exists courses;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            id integer primary key,
            username text UNIQUE,
            password text
        );
    ''')

    connection.commit()

    cursor.execute('''
        create table courses (
            id integer primary key,
            user_id integer,
            name text,
            credits integer,
            time_used integer,
            status string
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
    