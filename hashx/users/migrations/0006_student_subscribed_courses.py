# Generated by Django 3.1 on 2021-03-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0010_auto_20200802_1508'),
        ('users', '0005_instructor_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subscribed_courses',
            field=models.ManyToManyField(to='acad.Course'),
        ),
    ]
