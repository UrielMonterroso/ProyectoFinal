from django import forms
from .models import Cliente,Mascota,Producto, Citas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota
        fields='__all__'

class ProdcutoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model=Citas
        fields='__all__'

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
