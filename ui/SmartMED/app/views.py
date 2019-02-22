from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Forms
from app.forms import homeForm

# Create your views here.
def home(request):
	if request.method == "POST":
		# function call to start the vehicle
		form = homeForm(request.POST)
		if form.is_valid():
			movement = form.cleaned_data['movements']
			messages.success(request, "Vehicle is moving towards "+movement)
		else:
			messages.error(request, 'Failed to validate')
		return render(request, 'home.html', {'homeForm':homeForm})
	else:
		request.session['state'] = "START"
		return render(request, 'home.html', {'homeForm':homeForm})