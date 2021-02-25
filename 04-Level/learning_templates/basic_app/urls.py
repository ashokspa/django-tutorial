from django.urls import path,include
from basic_app import views

app_name = 'basic_app'

urlpatterns=[
    path('index',views.index,name='index'),
    path('other',views.other,name='other'),
    path('relative',views.relative_urls,name='relative')
]