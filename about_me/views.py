from django.shortcuts import render
# from .forms import SubscriberForm
from about_me.models import *

def about_me(request):
	# gallery_images = GalleryImage.objects.filter(is_active = True, is_main=True)
	return render(request, 'about_me/about_me.html', locals())



