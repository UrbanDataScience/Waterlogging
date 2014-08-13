from django.db import models

# Create your models here.
class person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name