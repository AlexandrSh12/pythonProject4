from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "ФИО: Шаповалов Александр Иванович"}

@app.get("/users")
def read_users():
    return {"data": "Контактные данные: 8-800-555-3535, улица Герцена 94"}

@app.get("/tools")
def read_tools():
    return {"data": "Навыки разработчика: Haskel, C#, C, SQL..."}

