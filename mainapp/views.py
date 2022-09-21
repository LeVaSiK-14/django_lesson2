from django.shortcuts import render
from mainapp.models import School, Teacher


def index(request):
    template_name = 'mainapp/index.html'
    schools = School.objects.all().select_related('director')
    school_amount = schools.count()
    context = {
        'schools': schools,
        'school_amount': school_amount,
    }
    
    return render(request, template_name, context=context)




def teachers(request):
    template_name = 'mainapp/teachers.html'
    teachers_list = Teacher.objects.all()
    context = {
        'teachers': teachers_list
    }
    return render(request, template_name, context=context)