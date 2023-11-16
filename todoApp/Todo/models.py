from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_valide = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    user = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title