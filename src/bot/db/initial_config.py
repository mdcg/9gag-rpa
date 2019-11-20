import sqlite3


def start_initial_db_config():
    conn = sqlite3.connect('9gag.db')
    cursor = conn.cursor()

    # get the count of tables with the name
    cursor.execute(
        """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='imgs_src'""")

    # if the count is 1, then table exists
    if not cursor.fetchone()[0] == 1:
        cursor.execute(
            """CREATE TABLE imgs_src (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, src TEXT NOT NULL)""")
        print('Successfully created table.')
        conn.close()
        return 

    conn.commit()
    conn.close()
