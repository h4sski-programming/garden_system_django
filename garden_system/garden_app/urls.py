from django.urls import path

from . import views

app_name = 'garden_app'
urlpatterns = [
    path('', views.index, name='index')
]