from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    description = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'