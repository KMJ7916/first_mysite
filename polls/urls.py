# polls 폴더에 urls.py가 없어서 새로 생성from django.urls import path

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="etc"),
    path("order", views.order_coffee, name="coffee"),
]