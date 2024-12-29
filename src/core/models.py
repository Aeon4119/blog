from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics')
    
    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})