from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"article", views.ArticleViewSet)


urlpatterns = [
    path("login/", views.login),
    path("", include(router.urls)),
]

