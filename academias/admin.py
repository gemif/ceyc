from django.contrib import admin
from django.utils.safestring import mark_safe
from academias.models import (
    PlanPago, DerechoExamen, Asignatura, Contenido, Institucion)
# Register your models here.


class ContenidoInline(admin.StackedInline):
    """."""
    model = Contenido
    suit_classes = 'suit-tab suit-tab-contenidos'
    extra = 0
    list_display = ['asignatura']
    readonly_fields = (
        'asignatura', 'ver_asignaturas', 'plan_pago', 'ver_plan_pagos', 'derecho_examen')
    ordering = ('contenido',)

    def asignatura(self, object):
        """."""
        return mark_safe(
            """<a href="/admin/academias/asignatura/">Asignaturas</a>""")

    def ver_asignaturas(self, object):
        """."""
        contenido_id = object.id
        contenido_nombre = object.contenido
        institucion_nombre = object.institucion
        return mark_safe(
            """<a href="/academias/ver_asignaturas?contenido_id={0}&contenido_nombre={1}&institucion_nombre={2}">Ver Asignaturas</a>""".format(contenido_id, contenido_nombre, institucion_nombre))

    def plan_pago(self, object):
        """."""
        return mark_safe(
            """<a href="/admin/academias/planpago/">Plan de Pagos</a>""")

    def ver_plan_pagos(self, object):
        """."""
        contenido_id = object.id
        contenido_nombre = object.contenido
        institucion_nombre = object.institucion
        return mark_safe(
            """<a href="/academias/ver_plan_pagos?contenido_id={0}&contenido_nombre={1}&institucion_nombre={2}">Ver Plan Pagos</a>""".format(contenido_id, contenido_nombre, institucion_nombre))

    def derecho_examen(self, object):
        """."""
        return mark_safe(
            """<a href="/admin/academias/derechoexamen/">Derecho a Examen\
            </a>""")


class InstitucionAdmin(admin.ModelAdmin):
    """."""
    inlines = (ContenidoInline, )
    list_display = ['institucion', 'abreviatura', 'telefono', 'web']
    search_fields = ['institucion', 'abreviatura']

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['institucion', 'descripcion', 'direccion']
        }),
        ('Contacto', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['contacto', 'telefono', 'celular', 'email']}),
        ('Otros', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['infoadicional', 'abreviatura']}),
    ]

    suit_form_tabs = (('general', 'General'), ('contenidos', 'Contenidos'))


class PlanPagoAdmin(admin.ModelAdmin):
    """."""
    model = PlanPago
    # search_fields = ['concepto'] # no esta funcionando el search
    list_display = ['contenido', 'concepto', 'cuota']
    ordering = ('contenido', 'orden', 'concepto')


class DerechoExamenAdmin(admin.ModelAdmin):
    """."""
    model = DerechoExamen


class AsignaturaAdmin(admin.ModelAdmin):
    """."""
    model = Asignatura
    list_display = ['contenido', 'asignatura', 'anio',
                    'numero_periodo', 'nombre_periodo']
    search_fields = ['asignatura']
    ordering = ('contenido', 'anio', 'numero_periodo', 'asignatura')


class ContenidoAdmin(admin.ModelAdmin):
    """."""
    model = Contenido


admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(DerechoExamen, DerechoExamenAdmin)
admin.site.register(PlanPago, PlanPagoAdmin)
