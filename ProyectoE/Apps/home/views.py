from django.shortcuts import render
from django.views.generic import TemplateView,CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from .forms import ClienteForm,MascotaForm,ProdcutoForm, RegistroForm, CitaForm
from django.urls import reverse_lazy
from Apps.home.models import  Mascota, Producto, Usuario, Cliente, Citas

# Create your views here.
class LoginView(TemplateView):
    template_name='login.html'

class LoginView(LoginView):
    template_name='login.html'
    
class HomeView(TemplateView):
    template_name='home.html'

class ServicioView(TemplateView):
    template_name='servicios.html'

class ClienteView(TemplateView):
    template_name='Datos de Cliente.html'

class ProductoView(TemplateView):
    template_name='productos.html'

class CitasView(TemplateView):
    template_name='citas.html'

class CrearClienteView(CreateView):
    template_name ='Datos de Cliente.html'
    form_class = ClienteForm
    success_url=reverse_lazy('home:mascotaapp')

class CrearCitasView(CreateView):
    template_name='Citas.html'
    form_class= CitaForm
    success_url= reverse_lazy('home:servapp')

class CrearMascotaView(CreateView):
    template_name ='mascota.html'
    form_class = MascotaForm
    success_url=reverse_lazy('home:servapp')

class CrearProductoView(CreateView):
    template_name ='productos.html'
    form_class = ProdcutoForm
    success_url=reverse_lazy('home:prodapp')

class ListarMascotaView(ListView):
    template_name = 'listarmascota.html'
    model = Mascota

    def get_queryset(self):
        vCliente = self.request.GET.get('raza')
        if(vCliente):
            return Mascota.objects.filter(raza__icontains=vCliente)
        else: 
            return Mascota.objects.all()

class ListarClientesView(ListView):
    template_name = 'listarcliente.html'
    model = Cliente

    def get_queryset(self):
        vNombre = self.request.GET.get('nombre')
        if(vNombre):
            return Cliente.objects.filter(nombre__icontains=vNombre)
        else: 
            return Cliente.objects.all()

class ListarProdView(ListView):
    template_name = 'listarprod.html'
    model = Producto

    def get_queryset(self):
        vNombre = self.request.GET.get('nombreP')
        if(vNombre):
            return Producto.objects.filter(nombre__icontains=vNombre)
        else: 
            return Producto.objects.all()

class ListarCitaView(ListView):
    template_name = 'listarcita.html'
    model = Citas

    def get_queryset(self):
        vNombre = self.request.GET.get('Fecha')
        if(vNombre):
            return Citas.objects.filter(Fecha__icontains=vNombre)
        else: 
            return Citas.objects.all()

class EditarMascotaView(UpdateView):
    template_name = 'editarmascota.html'
    model = Mascota
    form_class = MascotaForm
    success_url = reverse_lazy('home:listadomascota')

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url=reverse_lazy('home:homeapp')

class EditarClienteView(UpdateView):
    template_name = 'editarcliente.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('home:listadocliente')

class EditarProductosView(UpdateView):
    template_name = 'editarproducto.html'
    model = Producto
    form_class = ProdcutoForm
    success_url = reverse_lazy('home:listadoproductos')

class EditarCitasView(UpdateView):
    template_name = 'editarcitas.html'
    model = Citas
    form_class = CitaForm
    success_url = reverse_lazy('home:listadocita')

class ClienteDetalleView(DetailView):
    template_name = 'detallecliente.html'
    queryset= Cliente.objects.all()

class MascotaDetalleView(DetailView):
    template_name = 'detallemascota.html'
    queryset= Mascota.objects.all()

class ProductoDetalleView(DetailView):
    template_name = 'detalleprod.html'
    queryset= Producto.objects.all()

class CitaDetalleView(DetailView):
    template_name = 'detallecitas.html'
    queryset= Citas.objects.filter()