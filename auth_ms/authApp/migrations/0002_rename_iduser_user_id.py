# Generated by Django 3.2.8 on 2021-12-08 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='idUser',
            new_name='id',
        ),
    ]
