from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from core.views import index, CustomLoginView, contacto, register
from django.contrib.auth.views import LogoutView

app_name="core"

urlpatterns=[
    path("",index,name="index"),
    path("login/",CustomLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(template_name="core/logout.html"),name="logout"),
    path("contacto/",contacto,name="contacto" ),
    path("register/",register,name="register")
]

urlpatterns += staticfiles_urlpatterns()