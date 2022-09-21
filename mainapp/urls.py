from django.urls import path
from mainapp.views import index, teachers

urlpatterns = [
    path('', index, name='index'),
    path('teachers/', teachers, name='teacher'),
]
