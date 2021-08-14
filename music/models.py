import os
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def audio_validator(file):
    if file:
        print(file)
        if file.size > 12*1024*1024:
            raise ValidationError("Audio file too large ( > 12mb )")
        try:
            if not file.file.content_type in ['audio/mpeg','audio/mp4', 'audio/basic', 'audio/x-midi', 'audio/vorbis', 'audio/x-pn-realaudio', 'audio/vnd.rn-realaudio', 'audio/x-pn-realaudio', 'audio/vnd.rn-realaudio', 'audio/wav', 'audio/x-wav']:
                raise ValidationError("Sorry, we do not support that audio MIME type. Please try uploading an mp3 file, or other common audio type.")
        except:
            pass
        if not os.path.splitext(file.name)[1] in ['.mp3', '.au', '.midi', '.ogg', '.ra', '.ram', '.wav']:
            raise ValidationError("Sorry, your audio file doesn't have a proper extension.")
        return file
    else:
        raise ValidationError("Couldn't read uploaded file")

class songs(models.Model):
    user_linked = models.ForeignKey(User,on_delete=models.CASCADE)
    music = models.FileField(upload_to='music/',validators=[audio_validator])
    thubnail = models.ImageField(upload_to='photo',default='photo/default-music.png')
    serial_no = models.IntegerField()

    def __str__(self):
        return f'{self.user_linked} Music - {self.serial_no}'
    
    def get_absolute_url(self):
        return reverse('music_list')