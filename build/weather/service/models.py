from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
# from weather.authentication.models import Profile
# Create your models here.
class ServiceSMS(models.Model):
    services = models.CharField(max_length=200,default="Day By Day",unique=True)
    service_id_api = models.CharField(max_length=200,default="daybyday",unique=True)
    schedule = models.DateTimeField('Send Schedule')
    def __str__(self):              # __unicode__ on Python 2
        return self.services

# class Content(models.Model):
# 	content = models.CharField(max_length=200,default="Fill paragraph here",unique =True)
# 	services = models.ForeignKey(ServiceSMS)
# 	def __str__(self):
# 		return str(self.content[0])
# class User(models.Model):
# customer = models.ForeignKey(RegisterSMS,on_delete=models.CASCADE)

# a = ServiceSMS(services= "2 days/ times")
# print (dir(a))
# print a.registersms_set

# a.save()


# class Reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     def __str__(self):              # __unicode__ on Python 2
#         return "%s %s" % (self.first_name, self.last_name)

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

#     def __str__(self):              # __unicode__ on Python 2
#         return self.headline

#     class Meta:
#         ordering = ('headline',)