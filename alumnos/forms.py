from django import forms
from alumnos.models import Pago, Examen
from django.forms.extras.widgets import SelectDateWidget


class RegistrarPagoForm(forms.ModelForm):
    """."""
    class Meta:
        """."""
        model = Pago
        fields = ('fecha_pago', 'numero_comprobante', 'importe')
        widgets = {'fecha_pago': SelectDateWidget}


class RegistrarExamenForm(forms.ModelForm):
    """."""
    class Meta:
        """."""
        model = Examen
        fields = ('fecha', 'nota', 'equivalencia', 'aprobado')
        widgets = {'fecha': SelectDateWidget}
