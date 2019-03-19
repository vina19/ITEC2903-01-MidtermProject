from django.shortcuts import render, get_object_or_404
from .models import SGMovies
from django.db.models import Q
from django.http import HttpResponse


# View inside the website
#def home request, and return a respond with home.html
def home(request):
	return HttpResponse("<h1>list</h1>")

def movie_create(request):
	# return render(request, 'SGFan/about.html', {'title' : 'About'})
	return HttpResponse("<h1>create</h1>")

def movie_detail(request, id=None):
	# return render(request, 'SGFan/about.html', {'title' : 'About'})
	instance = get_object_or_404(SGMovies, id=id)
	context = {
		"title" : instance.title,
		"instance" : instance
	}
	return render(request, 'SGFan/movie_detail.html', context)
	
def movie_list(request):
	# return render(request, 'SGFan/about.html', {'title' : 'About'})
	queryset = SGMovies.objects.all()
	context = {
		"object_list":queryset
	}
	return render(request, 'SGFan/home.html', context)

def movie_update(request):
	# return render(request, 'SGFan/about.html', {'title' : 'About'})
	return HttpResponse("<h1>update</h1>")

def movie_delete(request):
	# return render(request, 'SGFan/about.html', {'title' : 'About'})
	return HttpResponse("<h1>delete</h1>")
