
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')


class Teacher(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    

class Student(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    clas = models.ForeignKey('Clas', on_delete=models.CASCADE, related_name='students') 
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='students')

# schools = School.objects.all().select_related('director').prefetch_related('teachers')

class Director(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='director')


class Clas(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='clas')


class Lesson(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE, related_name='lessons')


class HeadTeacher(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE)