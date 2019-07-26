from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'apptwo/index.html', context=date_dict)

   # my_dict = { 'insert_me': "Hello from views.py, oh no, sorry, i'm coming from apptwo/index.html"}
   # return render(request, 'apptwo/index.html', context=my_dict)