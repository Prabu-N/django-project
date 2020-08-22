from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from  django.contrib import messages




def signin(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']
		if password1==password2:
			if User.objects.filter(username=username).exists():

				messages.info(request,'username taken')
				return redirect('signin')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'password taken')
				return redirect('signin')
			else:
			    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
			    user.save()
		return redirect('login')

	else:	
		return render(request,'signin.html')
def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'invalid password or username')
			return redirect('login')
	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')

