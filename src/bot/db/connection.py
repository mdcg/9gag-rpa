import sqlite3
from datetime import datetime, timedelta


class Connection(object):
    def __init__(self):
        self.conn = sqlite3.connect('9gag.db')
        self.cursor = self.conn.cursor()

    def insert_img_src(self, src):
        self.cursor.execute("""
            INSERT INTO imgs_src (src)
            VALUES (?)
            """, (src,))
        self.conn.commit()

    def get_src(self, src):
        self.cursor.execute(
            "SELECT src FROM imgs_src WHERE src = ?", (src,))
        return self.cursor.fetchone()

    def check_if_src_already_exists(self, src):
        img_src = self.get_src(src)

        return True if img_src else False

    def close_connection(self):
        self.conn.close()
