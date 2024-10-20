from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm



class RegistrarUsuariosForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields= ['nombre','apellido','edad', 'username','password1','password2', 'email','imagen']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    @transaction.atomic
    def save(self):
        user                =super().save(commit=False)
        user.is_superuser   =False
        user.is_staff       =False
        user.save()
        return user

