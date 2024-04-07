from django.urls import path

from . import views

urlpatterns = [
    path('', views.colors_page, name='colors_page'),
    path('pdf', views.pdf_page, name='pdf_page'),
]
