from django.shortcuts import render

def index(reqeust):
    pass('>>>>>>>>>>> blog index')
    return render(request, 'blog/index.html')