from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers



urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    path('sistemas/', include('sistemas.urls')),
    path('catalogos/', include('catalogos.urls')),
    path('basededatos/', include('bases_de_datos.urls')),

]
