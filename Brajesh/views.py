from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to home<h1/>")