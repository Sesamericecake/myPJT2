from django.http        import JsonResponse
from django.shortcuts import render
from .models        import *

# Create your views here.

def index(request):
    print('>>>>> bbs index')
    #model - orm: modelNmae.objects.all()
    boards = WebBbs.objects.order_by('-id')
    print('bbs result type - ', type(boards))
    print('bbs result value - ', boards)
    context = {
        'boards' : boards
    }
    return render(request, 'bbs/index.html')

def createForm(request):
    print(">>>> bbs form")
    return render (request, 'bbs/createForm.html')

def create(request):
    print(">>>> bbs create")
    title = request.POST['title']
    writer = request.POST['writer']
    content = request.POST['content']
    print('debug-  ', title, writer, content)

    #orm - insert - save()
    bbs = WebBbs(title= title, writer = writer, content = content)
    bbs.save()

    return redirect('bbs_index')


def read(request):
    print('>>>> bbs read')
    id = request.get['id']
    print('debug - ', id)
    #조횟수 올리기
    #select
    board = WebBbs.objects.get(id=id)
    # update - commit - save()
    board.viewcnt = board.viewcnt + 1
    board.save()

    context = {
        'board' : board
    }

    return render(request, 'bbs/read.html', context)
    #select - orm- get| filter

def remove(request):
    print(">>>>>> bbs remove")
    id = request.GET['id']
    print(">>>>>debug - ", id)
    #orm - delete
    board = WebBbs.objects.get(id=id)
    board.delete()

    return redirect('bbs_index')

def update(request) :
    print('>>>> bss update')
    title = request.GET['title']
    id = request.GET['id']
    content = request.GET['content']
    print('debug-  ', title, id, content)
    #orm - update
    board = WebBbs.objects.get(id=id)
    board.title = title
    board.content = content
    board.save() #commit

    return redirect('bbs_index')


def search(request):
    print('>>>>> bbs search')
    type = request.POST['type']
    keyword = request.POST['keyword']
    print('debug -', type, keyword)

    # orm

    jsonObj = {'id' : 'jslim', 'title': '공지'}
    return JsonResponse(jsonObj, safe = False)


    if type == 'title':
        boards = WebBbs.objects.filter(title__icontains = keyword)
    if type == 'writer' :
        boards = WebBbs.objects.filter(writer__startswith = keyword)
    print('result - ', type(boards))
    print('data - ', boards )
    jsonAry= []
    for bbs in boards :
        jsonAry.append({
            'id' : bbs.id, 'title' : bbs.title, 'writer': bbs.writer,
            'regdate' : bbs.regdate, 'viewcnt' :bbs.viewcnt
        })
    return JsonResponse(jsonAry, safe = False)