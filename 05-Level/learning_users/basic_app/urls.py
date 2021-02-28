from django.urls import path,include
from basic_app import views
app_name = 'basic_app'


urlpatterns = [
    path('home',views.index,name="home"),
    path('register',views.register_users ,name="register"),    
]