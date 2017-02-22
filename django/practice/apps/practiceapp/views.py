from django.shortcuts import render, HttpResponse

def index(request):
    #return HttpResponse('hello there everyone')
    print ("*"*100)
    return render(request, "practiceapp/index.html")
# Create your views here.
def test(request):
    return HttpResponse('here is a number: 1')