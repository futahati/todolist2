from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


# 首頁
def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")


# 自我介紹
def profile(request):
    context = {
        "name": "irw",
        "age": 58,
        "height": 178,
        "weight": 78,
    }

    return JsonResponse(context)
