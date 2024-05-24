from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from avion.views import index,avion_list,avion_create,aeropuerto_create,aeropuerto_detail,aeropuerto_update,aeropuerto_delete
from avion.views import Aeropuertos_list

app_name="avion"

urlpatterns=[
    path("",index,name="index"),
    path("avion/list",avion_list,name="avion_list"),
    path("avion/create",avion_create,name="avion_create"),
    path("avion/aeropuertos_list",Aeropuertos_list.as_view(),name="aeropuertos_list"),
    path("avion/aeropuerto_create",aeropuerto_create,name="aeropuerto_create"),
    path("avion/aeropuerto_detail/<int:pk>",aeropuerto_detail,name="aeropuerto_detail"),
    path("avion/aeropuerto_update/<int:pk>",aeropuerto_update,name="aeropuerto_update"),
    path("avion/aeropuerto_delete/<int:pk>",aeropuerto_delete,name="aeropuerto_delete"),
]

urlpatterns += staticfiles_urlpatterns()