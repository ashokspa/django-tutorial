from django.shortcuts import render
from AppTwo.models import Users

# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):
    user_list = Users.objects.all()
    user_list_data = {"user_list":user_list}
    print(user_list_data)
    return render(request,'users.html',context=user_list_data)