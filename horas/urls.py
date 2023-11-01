from django.urls import path
from horas import views

urlpatterns = [
    path('',views.ListadoHoras.as_view(), name='horamedica_list' ),
    path('new/',views.AgregarHoras.as_view(), name='horamedica_new' ),
    path('<int:pk>/edit/',views.EditarHoras.as_view(), name='horamedica_edit' ),
    path('<int:pk>/delete/',views.BorrarHoras.as_view(), name='horamedica_delete' )
]
