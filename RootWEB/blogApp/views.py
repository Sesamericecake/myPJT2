from django.shortcuts import render

# Create your views here.
def index(request):
    print(">>>>>>> blog index")
    return render(request, 'blog/index.html')
