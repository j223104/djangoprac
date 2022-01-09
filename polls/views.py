from django.shortcuts import HttpResponse
def index(request):
    return HttpResponse("hello you are at polls index")

