# Generated by Django 2.1.5 on 2019-01-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbie',
            name='author',
        ),
        migrations.AddField(
            model_name='hobbie',
            name='author',
            field=models.ManyToManyField(to='members.Profile'),
        ),
    ]
