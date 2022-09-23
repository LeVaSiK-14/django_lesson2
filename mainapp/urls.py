from django.urls import path
from mainapp.views import index, teachers, create_school, retrieve_school, delete_school, update_school

urlpatterns = [
    path('', index, name='index'),
    path('teachers/', teachers, name='teacher'),
    path('create_school/', create_school, name='create_school'),
    path('get_school/<int:school_id>/', retrieve_school, name='retrieve_school'),
    path('delete_school/<int:school_id>/', delete_school, name='delete_school'),
    path('update_school/<int:school_id>', update_school, name='update_school'),
]
