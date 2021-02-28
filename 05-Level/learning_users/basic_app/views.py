from django.shortcuts import render
from basic_app.form import UserForm,UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register_users(request):
    
    registered = False
    if request.method == 'POST':
        user_form =  UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            if 'profile_pic' in request.FILES:
                profile_form.profile_pic = request.FILES['profile_pic']
            profile_form.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors) 
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request,'basic_app/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})   


