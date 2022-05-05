from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# from django.http import HttpResponse

# Create your views here.

def home(request, caregory_slug=None):
	caregory_page = None
	products = None
	if caregory_slug != None:
		caregory_page = get_object_or_404(Category, slug=
			caregory_slug)
		products = Product.objects.filter(category=caregory_page,
			available=True)
	else:
		products = Product.objects.all().filter(available=True)
	return render(request, 'home.html', {'category':caregory_page,
		'products':products})


def product(request):
	return render(request, 'product.html')
