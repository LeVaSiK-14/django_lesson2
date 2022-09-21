# Generated by Django 3.2.7 on 2022-09-21 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20220921_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='student',
            name='clas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='mainapp.clas'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='mainapp.lesson'),
        ),
    ]
