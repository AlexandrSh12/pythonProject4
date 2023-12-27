from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"FIO": "Шаповалов Александр Иванович"}

@app.get("/users")
def read_users():
    return {"Контактные данные": " 8-800-555-3535, улица Герцена 94"}

@app.get("/tools")
def read_tools():
    return {"Навыки разработчика": "Haskel, C#, C, SQL..."}

