from django.shortcuts import render
#from AppTwo.models import Users
from AppTwo.forms  import NewUserForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):
    form = NewUserForm()
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid form submission")
    return render(request,'users.html',{'form':form})