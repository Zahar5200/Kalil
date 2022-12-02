from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def adminData(request):
    return render(request, 'main/adminData.html')
