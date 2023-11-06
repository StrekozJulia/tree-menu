from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:menu_slug>/', views.index, name='menu'),
    path('<slug:menu_slug>/<slug:item_slug>/', views.index, name='item'),
]
