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
	if request.method == 'POST':
		form = TreasureForm(request.POST, request.FILES)
		# import ipdb; ipdb.set_trace()
		if form.is_valid():
			treasure = form.save(commit=False)
			form.save()
		return redirect('index')
	form = TreasureForm()
	return render(request, 'post_treasure.html', {'form': form})