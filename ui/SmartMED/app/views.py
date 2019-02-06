from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
	if request.method == "POST":
		if request.session['state'] == "START":
			request.session['state'] = "STOP"
			# function call to start the vehicle
			return render(request, 'home.html', {'state':request.session['state']})
		else:
			request.session['state'] = "START"
			# function call to stop the vehicle
			return render(request, 'home.html', {'state':request.session['state']})
	else:
		request.session['state'] = "START"
		return render(request, 'home.html', {'state':request.session['state']})