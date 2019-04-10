from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from home.models import Supplier, Inventory


@login_required
def index(request):
	suppliers = Supplier.objects.all()
	context = {
		'suppliers':suppliers,
	}
	return render(request, 'home/index.html', context)

def inventory(request):
	inventory = Inventory.objects.all()
	context = {
		'inventory':inventory,
	}
	return render(request, 'home/index.html', context)