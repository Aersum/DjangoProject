# Generated by Django 2.1.5 on 2019-01-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20190116_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
