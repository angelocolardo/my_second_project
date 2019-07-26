from django.urls import include, path
from apptwo import views


urlpatterns = [
    path('', views.index, name = 'index'),
]
