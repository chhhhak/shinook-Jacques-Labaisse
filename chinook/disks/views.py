from django.shortcuts import render , get_object_or_404, get_list_or_404
from .models import *

# Home page
def album_list(request):
    albums = get_list_or_404(Album)
    return render(request, 'disks/album_list.html', {'albums': albums})

# Detail page, specific to the album
def album_details(request, albumId):
    album = get_object_or_404(Album, pk=albumId)
    return render(request, 'disks/album_details.html', {'album': album})