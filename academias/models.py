from django.db import models
from django.core.validators import URLValidator
from settings.models import *


class Institucion(models.Model):
    """."""
    institucion = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=80, blank=True)
    direccion = models.CharField(max_length=80, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=20, blank=True)
    web = models.TextField(validators=[URLValidator()], blank=True)
    email = models.EmailField(blank=True)
    contacto = models.CharField(max_length=50, blank=True)
    infoadicional = models.CharField(max_length=150, blank=True)
    abreviatura = models.CharField(max_length=8)

    class Meta:
        """."""
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        """."""
        return self.institucion


class Contenido(models.Model):
    """."""
    UNIDADES_DURACION = (
        ('A', 'Año/s'),
        ('D', 'Día/s'),
        ('M', 'Mes/es'),
    )
    contenido = models.CharField(max_length=50)
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, default='')
    tipo = models.ForeignKey('settings.Tipo', on_delete=models.CASCADE)
    modalidad = models.ForeignKey(
        'settings.Modalidad', on_delete=models.CASCADE)
    duracion = models.SmallIntegerField(default=0)
    unidad_duracion = models.CharField(
        max_length=1,
        default='A',
        choices=UNIDADES_DURACION)
    acepta_licencias = models.BooleanField(default=False)
    cantidad_minima_pagos = models.PositiveSmallIntegerField(default=0)
    cantidad_max_examenes_por_inscripcion = models.PositiveSmallIntegerField(
        default=0)
    abreviatura = models.CharField(max_length=8, blank=True)
    vigente = models.BooleanField(default=True)
    infoadicional = models.CharField(max_length=150, blank=True)

    class Meta:
        """."""
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        """."""
        return '{} - {}'.format(self.contenido, self.institucion.abreviatura)


class Asignatura(models.Model):
    """."""
    asignatura = models.CharField(max_length=40)
    contenido = models.ForeignKey('Contenido', on_delete=models.CASCADE)
    anio = models.PositiveSmallIntegerField(default=0, verbose_name="año")
    numero_periodo = models.PositiveSmallIntegerField(default=0)
    nombre_periodo = models.ForeignKey(
        'settings.NombrePeriodo', on_delete=models.CASCADE)
    infoadicional = models.CharField(max_length=150, blank=True)

    class Meta:
        """."""
        verbose_name_plural = 'Asignaturas'

    def __str__(self):
        """."""
        return self.asignatura


class PlanPago(models.Model):
    """."""
    contenido = models.ForeignKey('Contenido', on_delete=models.CASCADE)
    concepto = models.ForeignKey('settings.Concepto', on_delete=models.CASCADE)
    cuota = models.PositiveSmallIntegerField(default=0)
    orden = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        """."""
        return '{} {}'.format(self.concepto, self.cuota)


class DerechoExamen(models.Model):
    """."""
    contenido = models.ForeignKey('Contenido', on_delete=models.CASCADE)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)
    planpago = models.ForeignKey('PlanPago', on_delete=models.CASCADE)

    class Meta:
        """."""
        verbose_name = 'Derecho A Examen'
        verbose_name_plural = 'Derecho a Examenes'

    def __str__(self):
        """."""
        return 'Asignatura: {} Concepto: {} Cuota: {}'.format(
            self.asignatura.asignatura, self.planpago.concepto,
            self.planpago.cuota)
