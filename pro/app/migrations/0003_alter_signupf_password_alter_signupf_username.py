# Generated by Django 5.0.6 on 2024-05-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_signup_signupf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupf',
            name='Password',
            field=models.CharField(max_length=10, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='signupf',
            name='Username',
            field=models.CharField(max_length=15, verbose_name='Username'),
        ),
    ]