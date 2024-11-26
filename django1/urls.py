
from django.contrib import admin
from django.urls import path,include
from secretaria.urls import index,contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contato',contato )
]
