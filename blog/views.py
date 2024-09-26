from django.shortcuts import render

# Create your views here.

def blogs_view(request):
    context = {}

    return render(request, "blog.html", context)