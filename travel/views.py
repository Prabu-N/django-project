from django.shortcuts import render, redirect
from .models import prabu,feed
from django.contrib.auth.models import User,auth
from .form import feed_back

def index(request):

	ps=prabu.objects.all()

	return render(request,'index.html',{'ps':ps})

def news(request):
	return render(request,'news.html')

def destinations(request):
	ps=prabu.objects.all()
	return render(request,'destinations.html',{'ps':ps})

def contact(request):
	return render(request,'contact.html')

def element(request):
	return render(request,'elements.html')

def feedback(request):
	form=feed_back(request.POST or None)
	if form.is_valid():
		form.save()
		form=feed_back()

	context={
	    'form':form
	        }
	return render(request,'feed.html',context)







