
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')


class Teacher(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    

class Student(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    clas = models.OneToOneField('Clas', on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

    

class Director(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    school = models.OneToOneField(School, on_delete=models.CASCADE)


class Clas(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    
class Lesson(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)

class HeadTeacher(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя', default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE)