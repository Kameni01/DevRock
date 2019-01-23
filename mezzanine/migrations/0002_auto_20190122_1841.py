# Generated by Django 2.1.4 on 2019-01-22 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='files',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='files',
        ),
        migrations.AddField(
            model_name='files',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mezzanine.ProjectPage', verbose_name='Страница'),
        ),
        migrations.AddField(
            model_name='files',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mezzanine.Project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(null=True, upload_to='files/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='project',
            name='mainimg',
            field=models.ImageField(null=True, upload_to='mezzanine/MainImg'),
        ),
    ]
