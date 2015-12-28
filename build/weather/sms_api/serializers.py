from weather.sms_api.models import smsApiPost
from rest_framework import serializers
from weather.authentication.models import Profile
from array import array
from weather.service.models import ServiceSMS

class SmsApiSerializer(serializers.ModelSerializer):
	class Meta:
		model = smsApiPost
		fields = ('name','REQID','LABELID','CONTRACTTYPEID','CONTRACTID','TEMPLATEID','ISTELCOSUB','AGENTID','APIUSER','APIPASS','USERNAME','select')
