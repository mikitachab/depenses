from django.http import HttpResponse


def hello(request):
    if request.method == "GET":
        return HttpResponse("Hello")
    return None
