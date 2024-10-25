from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('note_info/<int:note_id>', views.note_info, name='note_info'),  # modified to capture an integer ID
]
