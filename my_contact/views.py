from django.shortcuts import render
# from .forms import SubscriberForm
from my_contact.models import *

def my_contact(request):
	return render(request, 'my_contact/my_contact.html', locals())
