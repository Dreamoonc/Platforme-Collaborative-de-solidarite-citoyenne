# Generated by Django 4.0 on 2022-06-05 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_remove_localisation_wilaya_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benevole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('contenu', models.TextField(max_length=600)),
                ('nbr_max', models.IntegerField()),
                ('nbr_actuel', models.IntegerField(default=0)),
                ('adresse', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('SOLIDARITÉ ET INSERTION', 'SOLIDARITÉ ET INSERTION'), ('ÉDUCATION POUR TOUS', 'ÉDUCATION POUR TOUS'), ('PRÉVENTION ET PROTECTION', 'PRÉVENTION ET PROTECTION'), ('ART ET CULTURE POUR TOUS', 'ART ET CULTURE POUR TOUS'), ('PROTECTION DE LA NATURE', 'PROTECTION DE LA NATURE'), ('SPORT POUR TOUS', 'SPORT POUR TOUS'), ('SANTE POUR TOUS', 'SANTE POUR TOUS')], max_length=60)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.association')),
            ],
        ),
    ]
