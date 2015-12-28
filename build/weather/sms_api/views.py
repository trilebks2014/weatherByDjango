
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from weather.sms_api.models import smsApiPost
from weather.sms_api.serializers import SmsApiSerializer
from weather.authentication.models import Profile
from weather.service.models import ServiceSMS
import urllib2, urllib, json
from array import array
from django.db.models import Q

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def smsapi_list(request):
    print "Nothing here"

def smsapi_detail(request,service,city):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='"+city+"')"
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    # print "\n What does yql_url look like?\n"
    # print yql_url

    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)
    temp =round((int(data['query']['results']['channel']['item']['condition']['temp'])-32)/1.8)
    weather_condition =data['query']['results']['channel']['item']['condition']['text']
    # print temp
    # print weather_condition
    
    
    listPhone =[]
    sql = "SELECT * FROM authentication_profile INNER JOIN service_servicesms ON service_servicesms.id=authentication_profile.selectService_id INNER JOIN auth_user ON authentication_profile.user_id= auth_user.id WHERE authentication_profile.city='"+city+"' AND service_servicesms.service_id_api='"+service +"';"
    for p in Profile.objects.raw(sql):
        listPhone.append(p.__str__())
    PARAMS=[{"NUM":"1","CONTENT":temp},
            {"NUM":"2","CONTENT":weather_condition},
           ]
    print PARAMS
    print listPhone

    if request.method == 'GET':
        #  Take pk with service which is input by url
        pk=1
        date= 2
        sms_api=3
        for ser in ServiceSMS.objects.all():
            if(str(service)==str(ser.service_id_api)):
                pk=ser.id 
                date=ser.schedule
        for smsapi in smsApiPost.objects.all():
            if(smsapi.select_id==pk):
                sms_api=smsapi
        print sms_api
        datesend= "%02d/%02d/%02d %02d:%02d" % (date.day,date.month,date.year,date.hour,date.minute)
        JSON_API = {}
        JSON_API['PARAMS']=PARAMS
        JSON_API['MOBILELIST']=listPhone
        JSON_API['name']=sms_api.name
        JSON_API['REQID']=sms_api.REQID
        JSON_API['LABELID']=sms_api.LABELID
        JSON_API['CONTRACTID']=sms_api.CONTRACTID
        JSON_API['CONTRACTTYPEID']=sms_api.CONTRACTTYPEID
        JSON_API['TEMPLATEID']=sms_api.TEMPLATEID
        JSON_API['ISTELCOSUB']=sms_api.ISTELCOSUB
        JSON_API['AGENTID']=sms_api.AGENTID
        JSON_API['APIUSER']=sms_api.APIUSER
        JSON_API['APIPASS']=sms_api.APIPASS
        JSON_API['USERNAME']=sms_api.USERNAME
        JSON_API['SCHEDULETIME']=datesend
        JSON_API = JSONResponse(JSON_API)
        return JSON_API


        # smsApi = smsApiPost.objects.get(select_id=pk)
        # serializer = SmsApiSerializer(smsApi)
        # JSON= JSONResponse(serializer.data)
        # return JSON




