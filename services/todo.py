from grpc import aio

from protos import todo_pb2
from protos import todo_pb2_grpc
from models.todo_model import Todo


class TodoService(todo_pb2_grpc.TodoServiceServicer):
    async def create_todo_item(self, request, context):
        todo = await Todo.insert(
            Todo(name=request.name, completed=request.completed, day=request.day)
        )
        return todo_pb2.CreateTodoResponse(todo=todo[0])

    async def list_todo_items(self, request, context):
        todos = await Todo.select()
        return todo_pb2.ListTodosResponse(todos=todos)

    async def get_todo_item(self, request, context):
        todo = await Todo.select().where(Todo.id == request.id).first()
        return todo_pb2.GetTodoResponse(todo=todo)

    async def delete_todo_item(self, request, context):
        await Todo.delete().where(Todo.id == request.id)
        return todo_pb2.DeleteTodoResponse(success=True)

    async def update_todo_item(self, request, context):
        await Todo.update(
            {
                Todo.name: request.name,
                Todo.completed: request.completed,
                Todo.day: request.day,
            }
        ).where(Todo.id == request.id)
        todo = await Todo.select().where(Todo.id == request.id).first()
        return todo_pb2.UpdateTodoResponse(todo=todo)


async def run_todo_service(address):
    await Todo.create_table(if_not_exists=True)
    server = aio.server()
    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoService(),
        server
    )
    server.add_insecure_port(address)
    print(f"Running todo service on {address}")
    await server.start()
    await server.wait_for_termination()
