import sqlite3
from sqlite3 import Error



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file) # creates dbfile in memory. Can also use db_file inside ()
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_entry(conn, survey):
    """
    Create a new survey entry
    :param conn:
    :param survey:
    """
    sql = ''' INSERT INTO surveys (RespondentID, SeenSWFilms, FanOfSWFilms, ShotFirst, SeenExUniverse, FanOfExUniverse, FanOfStarTrek)
                VALUES (?,?,?,?,?,?,?); '''
    cur = conn.cursor()
    cur.execute(sql, survey)
    conn.commit()

def select_all(conn):
    """
    Query all rows in the task table
    :param conn: The connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM surveys WHERE RespondentID = 123420")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"Starwars.db"


    conn = create_connection(database)
    with conn:
        # create a new entry
        project = (123420, 'Yes', 'Yes', 'Greedo', 'Yes', 'Yes', 'Yes')
        project_id = create_entry(conn, project)

        print("2. Query all tasks")
        select_all(conn)

if __name__ == '__main__':
    main()
