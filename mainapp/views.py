from re import template
from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import School, Teacher
from mainapp.forms import SchoolForm

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


def create_school(request):
    template_name = 'mainapp/create_school.html'
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SchoolForm()
    return render(request, template_name, {'form': form})


def retrieve_school(request, school_id):
    template_name = 'mainapp/get_school.html'
    school = get_object_or_404(School, id=school_id)
    return render(request, template_name, {'school': school})


def delete_school(request, school_id):
    school = get_object_or_404(School, id=school_id)
    school.delete()
    return redirect('/')


def update_school(request,school_id):
    template_name = 'mainapp/update_school.html'
    school = get_object_or_404(School, id=school_id)
    
    form = SchoolForm(request.POST or None, instance=school)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form': form, 'school': school})
