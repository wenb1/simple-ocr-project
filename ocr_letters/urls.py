from django.urls import path
from . import views

app_name = 'ocr_letters'
urlpatterns = [
    path('add/', views.add, name='add'),
]
