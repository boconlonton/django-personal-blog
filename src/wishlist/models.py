from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False)
    note = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_selected = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name[:20]}'

    def summary(self):
        return f'{self.description[:50]}'
