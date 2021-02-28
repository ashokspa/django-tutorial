from django.shortcuts import render
from basic_app.forms import UserProfileForm
# Create your views here.

def index(request):
    form = UserProfileForm()
    if request.method=='POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("Invalid form")
            
    return render(request,'index.html',{'form':form})

