# Generated by Django 5.0.6 on 2024-06-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_feedmodel_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedmodel',
            name='Message',
            field=models.TextField(default=' ', max_length=300),
        ),
    ]
