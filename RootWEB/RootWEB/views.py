from django.shortcuts import render


def index(reqeust):
    pass('>>>>>>>>>>> root index')
    context = {'intro' : '혈맥강사와 함께하는 장고 프레임 웹 개발' }
    return render(request, 'index.html', context)