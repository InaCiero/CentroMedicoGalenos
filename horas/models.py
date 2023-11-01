from django.db import models


# Modelos~.

class HoraMedica(models.Model):
    fecha = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    rut_paciente  = models.CharField(max_length=10, verbose_name='Rut del Paciente')
    nom_paciente = models.CharField(max_length=50, verbose_name='Nombre del Paciente')
    mail_paciente = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Mail del Paciente')
    rut_doctor = models.CharField(max_length=10, verbose_name='Rut del Doctor')
    nom_doctor = models.CharField(max_length=50, verbose_name='Nombre del Doctor')

    def __str__(self) -> str:
        return self.nom_paciente
