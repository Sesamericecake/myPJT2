from django.shortcuts import render

def index(request):
    print('>>>>>> static index')
    return render(request, 'nodynamic/index.html' )

def line(request):
    print('>>>>>> static line')
    return render(request, 'nondynamic/line.html')