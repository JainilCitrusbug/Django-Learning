from django.db import models

# Create your models here.

class student(models.Model):
    std_id = models.IntegerField( null=True, blank=True)
    std_name = models.CharField(max_length=70, null=True, blank=True)
    std_email = models.EmailField(max_length=70, null=True, blank=True)
    std_number = models.CharField(max_length=10,  null=True, blank=True)

    def __str__(self):
        return self.std_name

