from django.db import models

# Create your models here.


class job(models.Model):
    image = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)

    def __str__(self):  # done so that we we get title name instead of of object(1,2,3...) in databases
        return self.summery
