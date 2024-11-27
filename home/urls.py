from django.urls import path
from home.views import index,people,PersonAPI,RegisterAPI,LoginAPI

urlpatterns = [
    path("index/",index),
    path("people/",people),
    path("person/",PersonAPI.as_view()),
    path("register/",RegisterAPI.as_view()),
    path("login/",LoginAPI.as_view())
]
