from django.conf.urls import url
from . import views

urlpatterns =[
url(r'^hello-api/',views.HelloAPIView.as_view()),
]
