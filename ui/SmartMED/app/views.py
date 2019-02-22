from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Forms
from app.forms import homeForm

# Utils
# from app.utils import motorDriver
# Create your views here.
def home(request):
	if request.method == "POST":
		# function call to start the vehicle
		form = homeForm(request.POST)
		if form.is_valid():
			movement = form.cleaned_data['movements']
			if movement == "Forward":
				#motorDriver.moveForward()
				print('F')
			elif movement == "Left":
				#motorDriver.leftTurn()
				print('L')
			elif movement == "Right":
				#motorDriver.rightTurn()
				print('R')
			elif movement == "Backward":
				#motorDriver.moveBack()
				print('B')
			else:
				#motorDriver.stop()
				print('S')
			messages.success(request, "Vehicle is moving towards "+movement)
		else:
			messages.error(request, 'Failed to validate')
		return render(request, 'home.html', {'homeForm':homeForm})
	else:
		request.session['state'] = "START"
		return render(request, 'home.html', {'homeForm':homeForm})