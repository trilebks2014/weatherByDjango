from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from weather.service.models import ServiceSMS
from weather.authentication.models import Profile
from django.template.context_processors import csrf
from django.contrib.auth.models import User
# from weather.service.forms import RegisterForm
# Create your views here.

def home(request):
	if request.method == "POST":
		print "Do nothing"
		return render(request, 'core/cover.html')
	else:
		if request.user.is_authenticated():       
			services= ServiceSMS.objects.all()
			return render(request,'core/home.html',{'services':services,'user':request.user})
		else:
			return render(request, 'core/cover.html')
	# return render(request, 'core/cover.html')
def thanksregister(request,username):
	if request.method == 'POST':
		registerUser=1
		city = "da nang"
		service ="daybyday"
		print type(request.POST.get('selectservice'))
		select_choice = request.POST.get('selectservice')
		for ser in ServiceSMS.objects.all():
			if (str(ser.id) == select_choice):
				# registerUser=Profile()
				service = ser
		city = request.POST.get('enterCity')
		
		registerUser = Profile(user=User.objects.get(username=username),city=city,selectService=service)
		registerUser.save()

	return render(request,'core/thanks.html')