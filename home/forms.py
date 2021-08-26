from django.forms import ModelForm
from .models import producto

class agregar_producto_form(ModelForm):
	class Meta:
		model = producto
		fields = '__all__'
