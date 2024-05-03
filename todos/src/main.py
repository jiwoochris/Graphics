from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping": "pong"}

todo_data = {
    1: {
        "id": 1,
        "contents": "Hello FastAPI 1!",
        "is_done": True,
    },
    2: {
        "id": 2,
        "contents": "Hello FastAPI 2!",
        "is_done": False,
    },
    3: {
        "id": 3,
        "contents": "Hello FastAPI 3!",
        "is_done": False,
    },
}

@app.get("/todos")
def get_todos_handler(order: str | None = None):
    ret = list(todo_data.values())
    if order and order == "DESC":
        return ret[::-1]
    return ret

@app.get("/todos/{todo_id}")
def get_todos_handler(todo_id: int):
    return todo_data.get(todo_id, {})

class CreateToDoRequest(BaseModel):
    id: int
    contents: str
    is_done: bool

@app.post("/todos")
def create_todos_handler(request: CreateToDoRequest):

    todo_data[request.id] = request
    return todo_data[request.id]