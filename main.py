from fastapi import FastAPI
import database
app = FastAPI(
    title="bookingApp"
)

#Выполнение запросов к сущности User
@app.get("/users/{id}") # получение данных о пользователе по его id
def userRead(id:int):
    return database.db_usersRead(id)
@app.get("/users")
def userReadAll():
    return database.db_usersReadAll()
@app.post("/users") #создание нового пользователя
def usersCreate(username:str,password:str):
    database.db_usersCreate(username,password)
    return {"created"} 
@app.put("/users") #обновление данных пользователя по его id
def usersUpdate(user_id:int,username:str,password:str):
    database.db_usersUpdate(user_id,username,password)
    return {"Updated"}
@app.delete("/users") #удаление пользователя по id
def usersDelete(user_id:int):
    database.db_usersDelete(user_id)
    return {"deleted"}

#Выполнение запросов к сущности Booking
@app.get("/booking") #получение таблицы бронирований
def bookingRead():
    return database.db_bookingRead()
@app.post("/booking") #создание брони по id пользователя
def bookingCreate(user_id:int,comment:str | None = None):
    database.db_bookingCreate(user_id,comment)
    return {"created"}
@app.delete("/booking") #удаление брони по id брони
def bookingDelete(id:int):
    database.db_bookingDelete(id)
    return {"deleted"}
    
    

