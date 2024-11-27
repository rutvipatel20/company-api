from django.db import models

class Color(models.Model):
    color_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name
    


class Person(models.Model):
    color=models.ForeignKey(Color,on_delete=models.CASCADE, related_name='color')
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    
