# Generated by Django 5.0.6 on 2024-05-31 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_signupf_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupf',
            old_name='ID',
            new_name='Username',
        ),
    ]
