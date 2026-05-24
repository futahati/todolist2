from django.shortcuts import render
from .models import Todo

# from django.http import JsonResponse


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)

    return render(request, "todos/list.html", {"todos": todos})
