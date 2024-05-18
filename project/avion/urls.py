from django.urls import path
from avion.views import index,avion_list,avion_create,aeropuertos_list,aeropuerto_create,aeropuerto_detail

app_name="avion"

urlpatterns=[
    path("",index,name="index"),
    path("avion/list",avion_list,name="avion_list"),
    path("avion/create",avion_create,name="avion_create"),
    path("avion/aeropuertos_list",aeropuertos_list,name="aeropuertos_list"),
    path("avion/aeropuerto_create",aeropuerto_create,name="aeropuerto_create"),
    path("avion/aeropuerto_detail/<int:pk>",aeropuerto_detail,name="aeropuerto_detail"),
]