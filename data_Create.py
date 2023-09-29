import sqlite3
#ЗАПУСТИТЬ ЭТОТ ФАЙЛ ДО ЗАПУСКА main.py
def db_setup():#создание таблиц в базу данных
    db = sqlite3.connect('backend.db')
    conn = db.cursor()
    conn.execute("""CREATE TABLE IF NOT EXISTS users(
                 id INTEGER PRIMARY KEY,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL,
                 created_at STRING NOT NULL,
                 updated_at STRING NOT NULL);""")
    conn.execute("""CREATE TABLE IF NOT EXISTS bookings (
                 id INTEGER PRIMARY KEY,
                 user_id INTEGER NOT NULL,
                 start_time STRING NOT NULL,
                 end_time STRING NOT NULL,
                 comment TEXT
                 )""")
    db.commit()
    db.close()

db_setup()