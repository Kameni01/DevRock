# Generated by Django 2.1.4 on 2019-02-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'To do'), (1, 'In progress'), (2, 'On review'), (3, 'Done')], default=0),
        ),
    ]
