# Generated by Django 3.2.9 on 2022-06-12 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0011_auto_20220612_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='name',
        ),
        migrations.RemoveField(
            model_name='association',
            name='willaya',
        ),
    ]