
from django.contrib import admin
from django.urls import path,include
from api.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name = 'home'),
    path('api/',include('api.urls')),  # using urls.py in api folder 
]
