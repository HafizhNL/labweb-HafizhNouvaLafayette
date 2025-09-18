from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_mahasiswa, name='daftar_mahasiswa'),
]