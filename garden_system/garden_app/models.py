from django.db import models

# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=False)
    state = models.BooleanField(default=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.name}, {self.state}'