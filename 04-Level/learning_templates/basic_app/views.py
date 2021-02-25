from django.shortcuts import render

# Create your views here.
def index(request):
    context_data = {"message":"Hello world","number":90}
    return render(request,'basic_app/index.html',context_data)
    
def other(request):
    return render(request,'basic_app/other.html')
    
def relative_urls(request):
    return render(request,'basic_app/relative_urls.html')