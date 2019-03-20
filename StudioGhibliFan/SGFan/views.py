from django.shortcuts import render, get_object_or_404
from .models import SGMovies
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SGMoviesForm

# View inside the website
#def home request, and return a respond with home.html
def movie_create(request):
	# return render(request, 'SGFan/about.html', {'title' : 'About'})
	form = SGMoviesForm(request.POST or None)

	# if all the form filled out with how it supposed to be then it will 
	# go to validation and it will save to the database.
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form" : form
	}
	return render(request, "SGFan/movie_form.html", context)

def movie_detail(request, id=None):
	instance = get_object_or_404(SGMovies, id=id)
	context = {
		"title" : instance.title,
		"instance" : instance
	}
	return render(request, 'SGFan/movie_detail.html', context)
	
def movie_list(request):
	queryset = SGMovies.objects.all()

	context = {
		"object_list":queryset
	}
	return render(request, 'SGFan/home.html', context)

def movie_update(request, id=None):
	instance = get_object_or_404(SGMovies, id=id)
	form = SGMoviesForm(request.POST or None, instance = instance)

	# if all the form filled out with how it supposed to be then it will 
	# go to validation and it will save to the database.
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title" : instance.title,
		"instance" : instance,
		"form" : form
	}
	return render(request, 'SGFan/movie_detail.html', context)


def movie_delete(request):
	return render(request, 'SGFan/about.html', {'title' : 'About'})

