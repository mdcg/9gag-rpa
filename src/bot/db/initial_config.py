import sqlite3


def start_initial_db_config():
    conn = sqlite3.connect('9gag.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE imgs_src (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            src TEXT NOT NULL,
    );
    """)
    print('Tabela criada com sucesso.')
    conn.close()
