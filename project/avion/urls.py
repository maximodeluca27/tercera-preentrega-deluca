from django.urls import path
from avion.views import index,avion_list,avion_create

app_name="avion"

urlpatterns=[
    path("",index,name="index"),
    path("avion/list",avion_list,name="avion_list"),
    path("avion/create",avion_create,name="avion_create")
    
]