import pandas as pd
import sqlite3

conn = sqlite3.connect("demo.db")
cur = conn.cursor()
# table 1: songs
cur.execute(
    """
    CREATE TABLE songs (
        song_id INTEGER PRIMARY KEY,
        year INTEGER CHECK (year > 0),
        artist TEXT,
        track TEXT,
        time TEXT,
        genre TEXT,
        date_entered TEXT,
        date_peaked TEXT
    )
    """
)
cur.execute("PRAGMA table_info(songs)")
cur.fetchall()

# table 2: ranks
cur.execute(
    """
    CREATE TABLE ranks (
        rank_id INTEGER PRIMARY KEY,
        song_id INTEGER,
        week INTEGER CHECK (week > 0),
        rank INTEGER CHECK (rank > 0),
        FOREIGN KEY (song_id) REFERENCES songs(song_id)
    )
    """
)
cur.execute("PRAGMA table_info(ranks)")
cur.fetchall()


# select song year that peaked in 2000
cur.execute("SELECT * FROM songs WHERE date_peaked LIKE '%2000%'")
cur.fetchall()


def filter_table(cur, table_name, col_name, criteria):
    # select song year that peaked in 2000
    cur.execute("SELECT * FROM %s WHERE %s LIKE %s" % (table_name, col_name, criteria))
    cur.fetchall()


def remove_table(cur, table_name):
    cur.execute("DROP TABLE %s" % table_name)
