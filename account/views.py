from django.shortcuts import render

from .models import OwnerInfo
# Create your views here.
def home(request):
    owner = OwnerInfo.objects.filter(is_visible=True)[0]
    context = {'owner': owner}
    return render(request, "index.html", context)


def about(request):
    context = {}

    return render(request, 'about.html', context)



def services_view(request):

    context = {}

    return render(request, "services.html", context)


def contact_view(request):

    context = {}

    return render(request, "contact.html", context)