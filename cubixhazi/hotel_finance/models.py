from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)
    suite = models.BooleanField()
    price = models.FloatField()
    
    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    has_views = models.BooleanField()
    night_count = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} ({self.Type.name})'