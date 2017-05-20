# -*- coding: utf-8 -*-
"""."""
from django.contrib import admin
from alumnos.models import Pago, Examen, Alumno, Inscripcion, EstadoInscripcion
from django.utils.safestring import mark_safe


class InscripcionInline(admin.TabularInline):
    """."""
    model = Inscripcion
    suit_classes = 'suit-tab suit-tab-inscripciones'
    extra = 0
    readonly_fields = (
        'ultimo_estado', 'ver_pagos', 'registrar_pago', 'ver_examenes',
        'registrar_examen', 'historico_estado')
    list_display = [
        'contenido', 'legajo', 'ultimo_estado', 'registrar_pago', 'ver_pagos',
        'ver_examenes', 'registrar_examen', 'historico_estado']

    def registrar_pago(self, object):
        """."""
        alumno_nc = object.alumno.nombre_completo
        inscripcion_id = object.id
        contenido = object.contenido
        return mark_safe(
            """<a href="/alumnos/registrar_pago?alumno_nc={0}&inscripcion_id={1}&contenido={2}">Registrar Pago</a>""".format(alumno_nc, inscripcion_id, contenido))

    def ver_pagos(self, object):
        """."""
        inscripcion_id = object.id
        alumno_nc = object.alumno.nombre_completo
        contenido = object.contenido
        return mark_safe(
            """<a href="/alumnos/ver_pagos?alumno_nc={0}&inscripcion_id={1}&contenido={2}">Ver Pagos</a>""".format(alumno_nc, inscripcion_id, contenido))

    def ver_examenes(self, object):
        """."""
        inscripcion_id = object.id
        alumno_nc = object.alumno.nombre_completo
        contenido = object.contenido
        return mark_safe(
            """<a href="/alumnos/ver_examenes?alumno_nc={0}&inscripcion_id={1}&contenido={2}">Ver Examenes</a>""".format(alumno_nc, inscripcion_id, contenido))

    def registrar_examen(self, object):
        """."""
        alumno_nc = object.alumno.nombre_completo
        inscripcion_id = object.id
        contenido = object.contenido
        return mark_safe(
            """<a href="/alumnos/registrar_examen?alumno_nc={0}&inscripcion_id={1}&contenido={2}">Registrar Examen</a>""".format(alumno_nc, inscripcion_id, contenido))

    def historico_estado(self, object):
        """."""
        inscripcion_id = object.id
        alumno_nc = object.alumno.nombre_completo
        contenido = object.contenido
        return mark_safe(
            """<a href="/alumnos/historico_estados?alumno_nc={0}&inscripcion_id={1}&contenido={2}">Historico Estados</a>""".format(alumno_nc, inscripcion_id, contenido))


class AlumnoAdmin(admin.ModelAdmin):
    """."""
    inlines = (InscripcionInline,)
    list_display = ['nombre_completo', 'tipo_documento',
                    'numero_documento', 'telefono', 'email']
    search_fields = ['apellido', 'nombre', 'numero_documento']
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'nombre', 'apellido', 'tipo_documento', 'numero_documento']
        }),
        ('Domicilio', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['domicilio', 'localidad']}),
        ('Contacto', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['telefono', 'celular', 'email']}),
    ]

    suit_form_tabs = (('general', 'General'),
                      ('inscripciones', 'Inscripciones'))


class PagoAdmin(admin.ModelAdmin):
    """."""
    model = Pago
    list_display = ['fecha_pago'.format('%Y-%M-%d'),
                    'numero_comprobante', 'importe']
    search_fields = ['fecha_pago']


class ExamenAdmin(admin.ModelAdmin):
    """."""
    model = Examen


class EstadoInscripcionAdmin(admin.ModelAdmin):
    """."""
    model = EstadoInscripcion


class InscripcionAdmin(admin.ModelAdmin):
    """."""
    model = Inscripcion


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(EstadoInscripcion, EstadoInscripcionAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
