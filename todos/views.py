from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# from django.http import JsonResponse


# Create your views here.
def todo_list(request):
    # .order_by()排序
    todos = Todo.objects.all().order_by("-created", "-important")
    print(todos)

    return render(request, "todos/list.html", {"todos": todos})


def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()
    except:
        print("無此ID")

    return redirect("todo-list")


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    message = None

    if request.method == "GET":
        # instance將資料填入TodoForm
        form = TodoForm(instance=todo)
    elif request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            print("更新 Todo 完成！")
            message = "更新 Todo 完成！"

    return render(request, "todos/update.html", {"form": form, "message": message})


def todo_create(request):

    if request.method == "POST":
        print(request.POST)
        # 將使用者填入的資訊，傳給TodoForm()成為form物件
        form = TodoForm(request.POST)
        # form物件是否建立成功，成功就儲存
        if form.is_valid():
            form.save()
            print("新增 Todo 完成！")
            return redirect("todo-list")

    return render(request, "todos/create.html", {"form": TodoForm()})
