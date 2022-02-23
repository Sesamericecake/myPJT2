from django.shortcuts import render , redirect
from .models            import *
# Create your views here.
def index(request) :
    print(">>>>> user index")
    return render(request, 'user/index.html')

# select * from WebUser where user_id = x and user_pwd = x
#  orm : modelName.objects.get()
# select * from WebUser
# orm : model
def login(request) :
    print('>>>>> user login')
    if request.method == 'POST':
        print('>>>> request post')
        id = request.POST['id']
        pwd = request.POST['pwd']
        # model = DB(Select)
        # 정보를 담는 작업을 필요로 한다.
        user = WebUser.objects.get(user_id = id, user_pwd = pwd) #where 절
        print('model value -', user.user_name)
        context = {'loginUser': user}
        return render(request, 'user/ok.html', context)
    else :
        print('>>>> request get')
        # request.GET['id']

def list(request) :
    print('>>>>user list')
    division = request.GET['category']
    print('param -' , division)
    #model - select * from table where cat = sport
    users = WebUser.object.all()
    for u in user:
        print('>>>>>>' , u.user_name)
    context = {'users': users}
    return render(request, 'user/list.html',context)


def detail(request):
    print('>>>>> user detail')
    id = request.GET['id']
    print('>>>>> param id-', id)
    user = WebUser.objects.get(user_id = id)
    if user is not None :
        context = {'user': user}
   else :
        context = {'error' : '사용자 정보가 존재하지 않습니다!!'}

    return render (request, 'user/detail.html', context)


def registerForm(request):
    print('>>>>> user registerForm -')
    return render (request, 'user/join.html')

def join(request):
    print('>>>>> user join -')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    print('>>>> param values-', id, pwd, name)
    #insert into table(id, pwd, name) values('', '', '')
    #orm : modelName(attr - value).save()
    WebUser(user_id = id, user_pwd = pwd, user_name = name).save()
    #return render(request, 'user/index.html')
    return redirect('index')