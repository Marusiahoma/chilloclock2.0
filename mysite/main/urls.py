from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="main"),
    path('shop', views.shop, name="shop"),
    path('create', views.create, name="create")
]