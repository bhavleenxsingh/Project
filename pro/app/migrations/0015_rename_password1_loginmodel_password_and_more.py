# Generated by Django 5.0.6 on 2024-06-03 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_loginmodel_rename_signupf_signupmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginmodel',
            old_name='Password1',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='loginmodel',
            old_name='Username1',
            new_name='Username',
        ),
    ]
