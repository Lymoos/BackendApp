# backendApp
>Использованная база данных: sqlite
### Документация:
```
http://localhost:8000/docs
```
### Установка всех необходимых библиотек:
```bash
pip install fastapi[all]
```
### Запуск:
1. Запускаем файл database.py
2. Вписываем в терминал:
   ```bash
   uvicorn main:app --reload
   ```
### Запросы
- /users/{id} [get]
  <br/>Получение данных пользователя по id
  <br/>
- /users [get]
  <br/>Получение данных всей таблицы users
- /user [post]
  <br/>Создание нового пользователя.
  <br/>Входные данные: username,password
- /user [delete]
  <br/>Удаление пользователя и его броней
  <br/>Входные данные: id
- /user} [put]
  <br/>Обновления данных пользователя
  <br/>Входные данные: id,username,password

- /booking [get]
  <br/> Получение всех данных из таблицы booking
- /booking [post]
  <br/>Создание брони по user_id
- /booking [delete]
  <br/>Удаление броней по user_id
