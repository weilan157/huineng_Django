from django.shortcuts import render


# 跳转到主页


def index(request):
    return render(request, 'chat.html')

