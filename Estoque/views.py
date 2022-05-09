from django.shortcuts import render

def notfound404(request, exception):
    return render(request, '404.html', status=404)
