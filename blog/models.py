from django.db import models

# Create your models here.


class Blog(models.Model):
    tital = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):  # done so that we we get title name instead of of object(1,2,3...) in databases
        return self.tital

    def info(self):  # done so that we can get upto 100 word in blog page if it contains more
        return self.body[:100]
