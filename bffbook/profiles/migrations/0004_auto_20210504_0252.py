# Generated by Django 3.1.7 on 2021-05-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210504_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], max_length=8),
        ),
    ]
