from django.db import models
from django.contrib.auth.hashers import make_password





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


class Usuario(models.Model):
    PACIENTE = 'paciente'
    SECRETARIA = 'secretaria'
    CAJERO = 'cajero'
    MEDICO = 'medico'

    ATRIBUTO_OP = [
        (PACIENTE, 'Paciente'),
        (SECRETARIA, 'Secretaria'),
        (CAJERO, 'Cajero'),
        (MEDICO, 'Medico'),
    ]

    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    rut = models.CharField(max_length=10, verbose_name='Rut')
    mail = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Mail')
    telefono = models.CharField(max_length=15, null=True, blank=True)
    contraseña = models.CharField(max_length=60)  
    atributo = models.CharField(max_length=10, choices=ATRIBUTO_OP,default='paciente')

    def save(self, *args, **kwargs):
        if self.contraseña:
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.rut