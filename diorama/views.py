from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# import datetime as dt

# Create your views here.
def welcome(request):
    images=Image.objects.all()
    return render(request, 'welcome.html',{'images':images})

def gallery(request):
    return render(request, 'pictures/gallery.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'pictures/search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'pictures/search.html', {"message":message})
  