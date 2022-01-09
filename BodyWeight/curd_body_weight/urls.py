from django.urls import path
from .views import index, show, create_view, update, delete

app_name = 'bodyweight'
urlpatterns = [
    path('',index, name='index'),
    path('show/<int:id>', show, name='show'),
    path('create', create_view, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]