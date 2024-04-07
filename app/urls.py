from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('colors', views.colors_page, name='colors_page'),
    path('pdf', views.pdf_page, name='pdf_page'),
]
