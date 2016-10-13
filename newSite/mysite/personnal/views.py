from django.shortcuts import render

def index(request):
	return render(request, 'personnal/home.html')

def contact(request):
	return render(request, 'personnal/contact.html')
