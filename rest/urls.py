from django.urls import path,include

from . import views
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'categorys', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]



