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
            username text primary key UNIQUE,
            password text
        );
    ''')

    connection.commit()

    cursor.execute('''
        create table courses (
            name text primary key UNIQUE,
            credits integer,
            time_used integer,
            status integer,
            creator text
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
    