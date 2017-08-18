from django.shortcuts import render, redirect
from .models import Treasure
from .forms import TreasureForm
from django.http import HttpResponseRedirect
from pprint import pprint

def index(request):
	treasures = Treasure.objects.all()
	return render(request, 'index.html', {'treasures': treasures})

def detail(request, id):
	treasure = Treasure.objects.get(id=id)
	# import ipdb; ipdb.set_trace()
	return render(request, 'detail.html', {'treasure': treasure})


def post(request):
	if request.method == 'POST' and request.FILES['Image']:
		name1 = request.POST['name']
		value1 = request.POST['value']
		material1 = request.POST['material']
		location1 = request.POST['location']
		image1 = request.FILES['Image']
		treasure = Treasure.objects.create(name=name1, value=value1, material=material1, location=location1, image=image1)
		pprint(treasure)
		return redirect('index')
	else:	
		form = TreasureForm()
		return render(request, 'post_treasure.html', {'form': form})