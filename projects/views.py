from django.shortcuts import render

# Create your views here.

def projects_view(request):

    context = {}
    return render(request, "portfolio.html", context)

