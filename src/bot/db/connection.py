import sqlite3
from datetime import datetime, timedelta

from .initial_config import start_initial_db_config


class Connection(object):
    def __init__(self):
        start_initial_db_config()
        self.conn = sqlite3.connect('9gag.db')
        self.cursor = self.conn.cursor()

    def insert_img_name_in_db(self, src):
        self.cursor.execute("""
            INSERT INTO imgs_src (src)
            VALUES (?)
            """, (src,))
        self.conn.commit()

    def get_src(self, src):
        self.cursor.execute(
            "SELECT src FROM imgs_src WHERE src = ?", (src,))
        return self.cursor.fetchone()

    def img_name_already_exists_in_db(self, src):
        img_src = self.get_src(src)

        return True if img_src else False

    def save_img_name_if_dont_exists_in_db(self, src):
        if self.img_name_already_exists_in_db(src):
            return
        self.insert_img_name_in_db(src)

    def close_connection(self):
        self.conn.close()
