from django.urls import path
from .views import index, contato
from django.contrib import admin

urlpatterns=[
path('admin/', admin.site.urls),
path('', index), 
path('contato', contato)

]