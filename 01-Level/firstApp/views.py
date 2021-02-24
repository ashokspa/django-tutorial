from django.shortcuts import render
from firstApp.models import AccessRecord

# Create your views here.

def index(request):
	access_records = AccessRecord.objects.all()
	profile = {"access_records":access_records}
	return render(request,'index.html',context=profile)