# -*- coding: utf-8 -*-
"""."""
from django.db import models
from django.utils import timezone
from settings.models import Estado


class Alumno(models.Model):
    """."""
    TIPOS_DOC = (
        ('D', 'DNI'),
        ('C', 'CEDULA'),
    )
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    tipo_documento = models.CharField(
        max_length=1,
        choices=TIPOS_DOC,
        default='D')
    numero_documento = models.PositiveIntegerField(unique=True)
    domicilio = models.CharField(max_length=100, blank=True)
    localidad = models.ForeignKey(
        'settings.Localidad', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=25, blank=True)
    celular = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    @property
    def nombre_completo(self):
        """."""
        return '{} {}'.format(self.apellido, self.nombre)

    class Meta:
        """."""
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        """."""
        return self.nombre_completo


class Examen(models.Model):
    """."""
    fecha = models.DateField(default=timezone.now())
    nota = models.PositiveSmallIntegerField(default=0)
    equivalencia = models.BooleanField(default=False)
    aprobado = models.BooleanField(default=False)
    asignatura = models.ForeignKey(
        'academias.Asignatura', on_delete=models.CASCADE)
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE)

    class Meta:
        """."""
        verbose_name_plural = 'Examenes'

    def __str_(self):
        """."""
        return '{} {} {}'.format(self.asignatura.asignatura, self.nota,
                                 self.fecha)


class Inscripcion(models.Model):
    """."""
    contenido = models.ForeignKey(
        'academias.Contenido', on_delete=models.CASCADE)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    legajo = models.CharField(max_length=15, blank=True)

    @property
    def ultimo_estado(self):
        """."""
        ultimo_estado = EstadoInscripcion.objects.filter(
            inscripcion_id=self.id).latest('fecha')
        return ultimo_estado.estado

    class Meta:
        """."""
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        """."""
        return '{} - {}'.format(self.contenido.contenido,
                                self.contenido.institucion.abreviatura)

    def save(self, *args, **kwargs):
        """."""
        self.save_base()
        inscripcion_id = self.id
        estado = Estado.objects.get(estado='Inscripto')
        EstadoInscripcion.objects.create(
            inscripcion_id=inscripcion_id, fecha=timezone.now(), estado=estado)
        super(Inscripcion, self).save(*args, **kwargs)


class Pago(models.Model):
    """."""
    fecha_pago = models.DateField(default=timezone.now())
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE)
    numero_comprobante = models.CharField(max_length=15)
    importe = models.DecimalField(max_digits=6, decimal_places=2)
    plan_pago = models.ForeignKey(
        'academias.PlanPago', on_delete=models.CASCADE)

    class Meta:
        """."""
        verbose_name_plural = 'Pagos'

    def __str__(self):
        """."""
        return '{} {} {} {}'.format(
            self.fecha_pago, self.numero_comprobante,
            self.plan_pago.concepto.concepto, self.importe)


class EstadoInscripcion(models.Model):
    """."""
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now())
    estado = models.ForeignKey('settings.Estado', on_delete=models.CASCADE)

    def __str__(self):
        """."""
        return '{} {}'.format(self.fecha, self.estado)
