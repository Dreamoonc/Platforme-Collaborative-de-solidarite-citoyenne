# Generated by Django 4.0 on 2022-05-21 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email adress')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='username')),
                ('phone', models.CharField(max_length=10, verbose_name='phone number ')),
                ('img', models.BinaryField(verbose_name='image')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentification.user')),
                ('name', models.CharField(max_length=255)),
                ('file', models.CharField(max_length=200)),
                ('willaya', models.CharField(choices=[(1, 'Adrar'), (2, 'Chlef'), (3, 'Laghouat'), (4, 'Oum-El-Bouaghi'), (5, 'Batna'), (6, 'Béjaïa'), (7, 'Biskra'), (8, 'Béchar'), (9, 'Blida'), (10, 'Bouira'), (11, 'Tamanrasset'), (12, 'Tébessa'), (13, 'Tlemcen'), (14, 'Tiaret'), (15, 'Tizi-Ouzou'), (16, 'Alger'), (17, 'Djelfa'), (18, 'Jijel'), (19, 'Sétif'), (20, 'Saïda'), (21, 'Skikda'), (22, 'Sidi Bel'), (23, 'Annaba'), (24, 'Guelma'), (25, 'Constantine'), (26, 'Médéa'), (27, 'Mostaganem'), (28, 'M’sila'), (29, 'Mascara'), (30, 'Ouargla'), (31, 'Oran'), (32, 'El Bayadh'), (33, 'Illizi'), (34, 'Bordj'), (35, 'Boumerdès'), (36, 'El-Tarf\t'), (37, 'Tindouf'), (38, 'Tissemsilt'), (39, 'El-Oued\t'), (40, 'Khenchela'), (41, 'Souk-Ahras'), (42, 'Tipaza\t'), (43, 'Mila'), (44, 'Aïn-Defla\t'), (45, 'Naâma'), (46, 'Aïn-Témouchent'), (47, 'Ghardaïa'), (48, 'Relizane'), (49, 'El M-Ghair\t'), (50, 'El Meniaa\t'), (51, 'Ouled Djellal'), (52, 'Bordj Badji '), (53, 'Béni Abbès'), (54, 'Timimoun'), (55, 'Touggourt'), (56, 'Djanet'), (57, 'In Salah'), (58, 'In Guezzam')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentification.user')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('willaya', models.CharField(choices=[(1, 'Adrar'), (2, 'Chlef'), (3, 'Laghouat'), (4, 'Oum-El-Bouaghi'), (5, 'Batna'), (6, 'Béjaïa'), (7, 'Biskra'), (8, 'Béchar'), (9, 'Blida'), (10, 'Bouira'), (11, 'Tamanrasset'), (12, 'Tébessa'), (13, 'Tlemcen'), (14, 'Tiaret'), (15, 'Tizi-Ouzou'), (16, 'Alger'), (17, 'Djelfa'), (18, 'Jijel'), (19, 'Sétif'), (20, 'Saïda'), (21, 'Skikda'), (22, 'Sidi Bel'), (23, 'Annaba'), (24, 'Guelma'), (25, 'Constantine'), (26, 'Médéa'), (27, 'Mostaganem'), (28, 'M’sila'), (29, 'Mascara'), (30, 'Ouargla'), (31, 'Oran'), (32, 'El Bayadh'), (33, 'Illizi'), (34, 'Bordj'), (35, 'Boumerdès'), (36, 'El-Tarf\t'), (37, 'Tindouf'), (38, 'Tissemsilt'), (39, 'El-Oued\t'), (40, 'Khenchela'), (41, 'Souk-Ahras'), (42, 'Tipaza\t'), (43, 'Mila'), (44, 'Aïn-Defla\t'), (45, 'Naâma'), (46, 'Aïn-Témouchent'), (47, 'Ghardaïa'), (48, 'Relizane'), (49, 'El M-Ghair\t'), (50, 'El Meniaa\t'), (51, 'Ouled Djellal'), (52, 'Bordj Badji '), (53, 'Béni Abbès'), (54, 'Timimoun'), (55, 'Touggourt'), (56, 'Djanet'), (57, 'In Salah'), (58, 'In Guezzam')], max_length=10)),
            ],
        ),
    ]
