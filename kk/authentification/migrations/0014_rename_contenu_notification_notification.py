# Generated by Django 3.2.9 on 2022-06-16 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0013_auto_20220614_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='contenu',
            new_name='notification',
        ),
    ]