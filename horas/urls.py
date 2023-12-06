from django.urls import path
from horas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('vsecretaria',views.ListadoHoras.as_view(), name='horamedica_list' ),
    path('new/',views.AgregarHoras.as_view(), name='horamedica_new' ),
    path('<int:pk>/edit/',views.EditarHoras.as_view(), name='horamedica_edit' ),
    path('<int:pk>/delete/',views.BorrarHoras.as_view(), name='horamedica_delete' ),

    path('usuarios/', views.ListarUsuarios.as_view(), name='usuario_list'),
    path('usuarios/new/', views.AgregarUsuario.as_view(), name='usuario_new'),
    path('usuarios/<int:pk>/edit/', views.EditarUsuario.as_view(), name='usuario_edit'),
    path('usuarios/<int:pk>/delete/', views.BorrarUsuario.as_view(), name='usuario_delete'),
]
