from piccolo.columns import Boolean, Varchar, Integer
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table

# DB = SQLiteEngine("bd.sqlite")
DB = SQLiteEngine("todo_service/bd.sqlite")


class Todo(Table, db=DB):
    name = Varchar()
    completed = Boolean(default=False)
    day = Integer(default=0)
