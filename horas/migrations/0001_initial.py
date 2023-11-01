# Generated by Django 4.2.6 on 2023-10-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HoraMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('rut_paciente', models.CharField(max_length=10)),
                ('nom_paciente', models.CharField(max_length=50)),
                ('mail_paciente', models.EmailField(blank=True, max_length=100, null=True)),
                ('rut_doctor', models.CharField(max_length=10)),
                ('nom_doctor', models.CharField(max_length=50)),
            ],
        ),
    ]