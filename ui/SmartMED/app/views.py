from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Forms
from app.forms import homeForm
from app.forms import topologyForm

# All the function calls from utils have been commented, uncomment when running on Raspberry Pi
# from app.utils import motor as motorDriver

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
			messages.success(request, "Bot is moving towards "+movement)
		else:
			messages.error(request, 'Failed to validate')
		return render(request, 'home.html', {'homeForm':homeForm})
	else:
		#request.session['state'] = "START"
		return render(request, 'home.html', {'homeForm':homeForm})

def topology(request):
	# functional calll that tells the bot to which bed the medicies should be delivered
	if request.method == "POST":
		form = topologyForm(request.POST)
		if form.is_valid():
			beds = form.cleaned_data['beds']
			try:
				bedNums = list(map(int, beds.split(' ')))
				print(bedNums)
				messages.success(request, "Bot will deliver medicines to beds"+ beds)
				#motorDriver.runMotor(bedNums)
			except Exception as e:
				messages.error(request, "Please enter bed numbers e.g 1 2 3")
		else:
			messages.error(request, 'Failed to validate')
		return render(request, 'topology.html', {'topologyForm':topologyForm})
	else:
		return render(request, 'topology.html', {'topologyForm':topologyForm})

