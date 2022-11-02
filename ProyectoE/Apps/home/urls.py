"""ProyectoE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import HomeView, ServicioView, LoginView, CrearClienteView, CrearMascotaView, CrearProductoView, CrearCitasView
from .views import ListarMascotaView, EditarMascotaView, RegistroView, ListarClientesView, ListarProdView, ListarCitaView
from .views import EditarClienteView, EditarProductosView, EditarCitasView, ClienteDetalleView, MascotaDetalleView, ProductoDetalleView
from .views import CitaDetalleView
app_name='home'
urlpatterns = [
     path('', HomeView.as_view(), name='homeapp'),
     path('servicios/', ServicioView.as_view(), name='servapp'),
     path('login/', LoginView.as_view(), name='loginapp'),
     path('Cliente/', CrearClienteView.as_view(), name='clienteapp'),
     path('Citas/', CrearCitasView.as_view(), name='citasapp'),
     path('Agregar mascota/', CrearMascotaView.as_view(), name='mascotaapp'),
     path('Productos/', CrearProductoView.as_view(), name='prodapp'),
     path('listado_mascota/', ListarMascotaView.as_view(), name='listadomascota'),
     path('listado_cliente/', ListarClientesView.as_view(), name='listadocliente'),
     path('listado_productos/', ListarProdView.as_view(), name='listadoproductos'),
     path('listado_cita/', ListarCitaView.as_view(), name='listadocita'),
     path('editar_mascota/<int:pk>', EditarMascotaView.as_view(), name='editarmascota'),
     path('registro/',RegistroView.as_view(), name='registroapp'),
     path('editar_cliente/<int:pk>', EditarClienteView.as_view(), name='editarcliente'),
     path('editar_producto/<int:pk>', EditarProductosView.as_view(), name='editarprod'),
     path('editar_cita/<int:pk>', EditarCitasView.as_view(), name='editarcita'),
     path('detalle_cliente/<int:pk>', ClienteDetalleView.as_view(), name='detallecliente'),
     path('detalle_mascota/<int:pk>', MascotaDetalleView.as_view(), name='detallemascota'),
     path('detalle_PRODUCTOS/<int:pk>', ProductoDetalleView.as_view(), name='detalleprod'),
     path('detalle_cita/<int:pk>', CitaDetalleView.as_view(), name='detallecita'),

]
