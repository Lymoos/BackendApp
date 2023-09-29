import sqlite3
import timeRed
import json
from typing import Optional

def dict_factory(cursor, row):#перевод в json
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def db_usersRead(user_id):#чтение всей таблицы users из базы данных
    db = sqlite3.connect('backend.db',check_same_thread=False)
    conn = db.cursor()
    conn.row_factory = dict_factory
    a = conn.execute("SELECT * FROM users WHERE id = ?",(user_id,)).fetchall()
    db.close()
    return json.dumps(a)
def db_usersReadAll():
    db = sqlite3.connect('backend.db',check_same_thread=False)
    conn = db.cursor()
    conn.row_factory = dict_factory
    a = conn.execute("SELECT * FROM users").fetchall()
    db.close()
    return json.dumps(a)
def db_usersCreate(username,password):#создание нового пользователя
    db = sqlite3.connect('backend.db')
    conn = db.cursor()
    timeCreate = timeRed.timenow()
    timeUpdate = timeRed.timenow()
    conn.execute("INSERT INTO users (username,password,created_at,updated_at) VALUES(?,?,?,?);",(username,password,timeCreate,timeUpdate))
    db.commit()
    db.close()
def db_usersDelete(user_id):#удаление пользователя
    db = sqlite3.connect('backend.db')
    conn = db.cursor()
    conn.execute("DELETE FROM users WHERE id = ?",(user_id,))
    conn.execute("DELETE FROM bookings WHERE user_id = ?",(user_id,))
    db.commit()
    db.close()
def db_usersUpdate(user_id,username,password):#обновление данных о пользователе
    db = sqlite3.connect('backend.db')
    conn = db.cursor()
    timeUpdate = timeRed.timenow()
    conn.execute("UPDATE users  SET username = ?,password = ?,updated_at = ? WHERE id = ?",(username,password,timeUpdate,user_id))
    db.commit()
    db.close()
def db_bookingCreate(user_id,comment: Optional[str]):#создание нового бронирования
    db = sqlite3.connect('backend.db')
    conn = db.cursor()
    timeCreate = timeRed.timenow()
    timeAfter = timeRed.timeAfter()
    conn.execute("INSERT INTO bookings (user_id,start_time,end_time,comment) VALUES(?,?,?,?);",(user_id,timeCreate,timeAfter,comment))
    db.commit()
    db.close()
def db_bookingRead():#чтение всей таблицы booking из базы данных
    db = sqlite3.connect('backend.db',check_same_thread=False)
    conn = db.cursor()
    conn.row_factory = dict_factory
    a = conn.execute("SELECT * FROM bookings").fetchall()
    db.close()
    return json.dumps(a)
def db_bookingDelete(id):#удаление брони
    db = sqlite3.connect('backend.db')
    conn = db.cursor()
    conn.execute("DELETE FROM bookings WHERE id = ?",(id,))
    db.commit()
    db.close()
