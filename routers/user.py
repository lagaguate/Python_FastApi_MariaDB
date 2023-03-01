from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from typing import List
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)


user = APIRouter()


@user.get("/users", response_model=list, tags=["users"])
def get_user():
    return conn.execute(users.select()).fetchall()


@user.get("/users/{id}", response_model=User, tags=["users"])
def get_userxid(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/user/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User):
    result = conn.execute(users.update().values(nombre=user.nombre, email=user.email,
                          password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = {"nombre": user.nombre, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    # conn.commit()
    print(new_user)
    print(result)
    print(result.lastrowid)

    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
