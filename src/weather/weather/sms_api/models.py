from django.db import models
from weather.authentication.models import Profile
from weather.service.models import ServiceSMS
from django.contrib.auth.models import User
# Create your models here.
class smsApiPost(models.Model):
	# idsms = models.IntegerField(default=0,unique=True)
	name = models.CharField(max_length=200)
	REQID = models.CharField(max_length=200)
	LABELID = models.CharField(max_length=200,default='12911')
	CONTRACTTYPEID = models.CharField(max_length=200,default='1')
	CONTRACTID = models.CharField(max_length=200,default='19741')
	TEMPLATEID = models.CharField(max_length=200,default='78382')
	ISTELCOSUB = models.CharField(max_length=2,default='0')		
	AGENTID = models.CharField(max_length=200,default='191')
	APIUSER = models.CharField(max_length=200,default='kdvnptqnm')
	APIPASS = models.CharField(max_length=200,default='kdvnptqnm')
	USERNAME = models.CharField(max_length=200,default='kdvnptqnm')
	select = models.OneToOneField(ServiceSMS,primary_key=True, on_delete=models.CASCADE,default=0)
	
	def __str__(self):
		return str(self.name)












	# class Meta:
	# 	ordering = ('idsms',)



# from __future__ import unicode_literals

# from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# # Create your models here.

# EXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in EXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

#     def __str__(self):
#         return str(self.title)