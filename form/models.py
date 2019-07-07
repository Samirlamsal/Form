from django.db import models
from multiselectfield import MultiSelectField

class data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    expertise = MultiSelectField(choices=[('Python','Python'), ('JS','JS'), ('Java','Java'), ('Php','Php'),])




    def __str__(self):
        return self.name
