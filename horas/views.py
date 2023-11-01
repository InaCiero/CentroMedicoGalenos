from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from horas.models import HoraMedica


class ListadoHoras(generic.ListView):
    model = HoraMedica
    paginate_by = 5

    # Busqueda de horas agendadas por RUT
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        if q:
            return HoraMedica.objects.filter(rut_paciente__icontains=q)
        return super().get_queryset()

class AgregarHoras(generic.CreateView):
    model = HoraMedica
    fields = ('fecha', 'hora', 'rut_paciente', 'nom_paciente', 'mail_paciente', 'rut_doctor', 'nom_doctor',)
    success_url = reverse_lazy('horamedica_list')

class EditarHoras(generic.UpdateView):
    model = HoraMedica
    fields = ('fecha', 'hora', 'rut_paciente', 'nom_paciente', 'mail_paciente', 'rut_doctor', 'nom_doctor',)
    success_url = reverse_lazy('horamedica_list')

class BorrarHoras(generic.DeleteView):
    model = HoraMedica
    success_url = reverse_lazy('horamedica_list')