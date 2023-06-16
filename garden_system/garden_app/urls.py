from django.urls import path

from . import views

app_name = 'garden_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('zone/<int:id>', views.zone_settings, name='zone_settings'),
    path('change_state/<int:id>', views.change_zone_state, name='change_zone_state'),
]