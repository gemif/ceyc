from django.contrib import admin
from settings.models import Localidad, Concepto, Tipo, Estado, Modalidad, NombrePeriodo

# Register your models here.


class LocalidadAdmin(admin.ModelAdmin):
    """."""
    model = Localidad
    search_fields = ['localidad', 'codigo_postal']
    list_display = ['localidad', 'codigo_postal']


class ConceptoAdmin(admin.ModelAdmin):
    """."""
    model = Concepto


class TipoAdmin(admin.ModelAdmin):
    """."""
    model = Tipo
    search_fields = ['tipo']


class EstadoAdmin(admin.ModelAdmin):
    """."""
    model = Estado
    search_fields = ['estado']


class ModalidadAdmin(admin.ModelAdmin):
    """."""
    model = Modalidad
    search_fields = ['modalidad']


class NombrePeriodoAdmin(admin.ModelAdmin):
    """."""
    model = NombrePeriodo


admin.site.register(Tipo, TipoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Modalidad, ModalidadAdmin)
admin.site.register(Concepto, ConceptoAdmin)
admin.site.register(NombrePeriodo, NombrePeriodoAdmin)
