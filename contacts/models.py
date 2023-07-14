from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500, blank=True, default="")
    email = models.EmailField(max_length=250, blank=True, default="")
    mobile = models.CharField(max_length=12, blank=True, default="")

    class Meta:
        ordering = ["name"]