from django.shortcuts import render
# from .forms import SubscriberForm
from gallery.models import *

def gallery(request):
	gallery_images = GalleryImage.objects.filter(is_active = True, is_main=True)
	return render(request, 'galleries/gallery.html', locals())




def galleries(request, gallery_id):
    gallery_images = GalleryImage.objects.filter(is_active=True, is_main=True)
    gallery = Gallery.objects.get(id=gallery_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'galleries/photossession.html', locals())
