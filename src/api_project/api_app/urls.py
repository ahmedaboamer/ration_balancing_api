from django.conf.urls import url
from django.conf.urls import include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Hello-ViewSet', views.HelloViewSet,base_name='Hello-ViewSet')
router.register('profile', views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns =[
url(r'^hello-api/',views.HelloAPIView.as_view()),
url(r'',include(router.urls))
]
