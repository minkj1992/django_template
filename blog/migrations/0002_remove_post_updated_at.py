# Generated by Django 2.2 on 2019-04-07 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]
