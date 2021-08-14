from django.urls.base import reverse_lazy
from music.forms import musicForm
from typing import List
from music.models import songs
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView,ListView


class createMusic(CreateView):
    form_class = musicForm
    template_name = 'create.html'
    success_url = reverse_lazy('music_list')
    

    def form_valid(self, form):
        form.instance.user_linked = self.request.user
        form.instance.serial_no = songs.objects.filter(user_linked=self.request.user).count()+1
        return super().form_valid(form)

def listMusic(request):
    song = songs.objects.filter(user_linked=request.user)
    musics = []
    pics = []
    for i in song:
        musics.append(i.music.url)
        pics.append(i.thubnail.url)
    context = {
        'songs':song,
        'music':musics,
        'pics':pics,
        'form' : musicForm()    
    }
    return render(request,'song_list.html',context=context)


