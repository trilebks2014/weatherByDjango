from django.contrib import admin
from .models import ServiceSMS
# from .models import Content
from django.contrib.auth.models import User
# Register your models here.
# class RegisterAdmin(admin.ModelAdmin):
# 	# list_display = ('')
# 	filter_horizontal = ('customer',)
# class ContentInline(admin.TabularInline):
# 	model = Content
# 	extra = 1
# class ServiceSMSAdmin(admin.ModelAdmin):
# 	inlines = [ContentInline]

admin.site.register(ServiceSMS)