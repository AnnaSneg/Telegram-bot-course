"""
Data on previously requested courses is recorded in the database. And at the next request, if the courses for the period
are already in the database, they are taken from the database, and not again from the web site.
"""

import sqlite3
import month

dbname = r'C:\Users\Admin\Documents\ExamBotGitHub\db\mycourse.db'
db = None
cursor = None


def table_exists(table_name):
    r = cursor.execute(f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    return cursor.fetchone()[0] == 1


def create_table():
    r = cursor.execute("""
    CREATE TABLE IF NOT EXISTS course
    (ccy TEXT NOT NULL,
    date TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    value REAL NOT NULL)  
    """)
    r = db.commit()


def date_to_text(d):
    return d.strftime("%Y-%m-%d")


def delete_for_period(ccy, date_begin, date_end):
    cursor.execute(f"""
    delete from course where
    ccy = '{ccy}'
    and date >= '{date_to_text(date_begin)}'
    and date <= '{date_to_text(date_end)}'
    """)
    db.commit()


def add_for_period(ccy, date_begin, date_end, courses):
    c2 = [(ccy, date_to_text(c[0]), c[1], c[2]) for c in courses]
    cursor.executemany("""
    INSERT INTO course
    VALUES (?, ?, ?, ?)""", [(c[0], c[1], c[2], c[3]) for c in c2])
    db.commit()


def get_for_period(ccy, date_begin, date_end):
    r = cursor.execute(f"""
    select * from course where
    ccy = '{ccy}'
    and date >= '{date_to_text(date_begin)}'
    and date <= '{date_to_text(date_end)}'
    """)
    r = cursor.fetchall()
    return r


def try_get_for_period(ccy, date_begin, date_end):
    r = get_for_period(ccy, date_begin, date_end)
    delta = date_end - date_begin
    return r if delta.days + 1 == len(r) else None


def get_courses(ccy, date_begin, date_end):
    global db
    global cursor
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        if not table_exists("course"):
            create_table()
        ccy = ccy.upper()
        r = try_get_for_period(ccy, date_begin, date_end)
        if r == None:
            delete_for_period(ccy, date_begin, date_end)
            add_for_period(ccy, date_begin, date_end, month.get_for_period(ccy, date_begin, date_end))
            r = get_for_period(ccy, date_begin, date_end)
        return r


# db.close()