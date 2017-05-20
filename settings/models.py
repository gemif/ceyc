from django.db import models


class Modalidad(models.Model):
    """."""
    modalidad = models.CharField(max_length=30)

    class Meta:
        """."""
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        """."""
        return self.modalidad


class Concepto(models.Model):
    """."""
    concepto = models.CharField(max_length=20)

    class Meta:
        """."""
        verbose_name_plural = 'Conceptos'

    def __str__(self):
        """."""
        return self.concepto


class Estado(models.Model):
    """."""
    estado = models.CharField(max_length=15)

    class Meta:
        """."""
        verbose_name_plural = 'Estados'

    def __str__(self):
        """."""
        return self.estado


class Localidad(models.Model):
    """."""
    localidad = models.CharField(max_length=30)
    codigo_postal = models.CharField(max_length=10, default='')

    class Meta:
        """."""
        verbose_name_plural = 'Localidades'

    def __str__(self):
        """."""
        return '({}){}'.format(self.codigo_postal, self.localidad)


class Tipo(models.Model):
    """."""
    tipo = models.CharField(max_length=20)

    class Meta:
        """."""
        verbose_name_plural = 'Tipos'

    def __str__(self):
        """."""
        return self.tipo


class NombrePeriodo(models.Model):
    """."""
    nombre_periodo = models.CharField(max_length=15)

    def __str__(self):
        """."""
        return self.nombre_periodo
