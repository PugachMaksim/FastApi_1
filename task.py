"""
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Создайте маршрут для обновления информации о пользователе (метод PUT)
Создайте маршрут для удаления информации о пользователе (метод DELETE).
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []


@app.post("/user/")
async def add_user(user: User):
    users.append(user)
    return user


@app.get("/users/")
async def get_user():
    return users


@app.put("/update/{user_id}")
async def update(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
        return user


@app.delete("/users/{user_id}")
async def del_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return {"user_id": users.pop(i)}
        return HTTPException(status_code=404, detail='Movie not found')
