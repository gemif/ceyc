from django.shortcuts import render
from academias.models import Asignatura, PlanPago


def ver_asignaturas(request):
    """."""
    contenido_id = request.GET.get('contenido_id')
    contenido_nombre = request.GET.get('contenido_nombre')
    institucion_nombre = request.GET.get('institucion_nombre')
    asignaturas = Asignatura.objects.filter(contenido=contenido_id)
    mensaje = None
    if not asignaturas:
        mensaje = 'No hay asignaturas registradas'
    return render(
        request, 'academias/ver_asignaturas.html',
        {'asignaturas': asignaturas, 'mensaje': mensaje,
            'contenido_id': contenido_id, 'contenido_nombre': contenido_nombre,
            'institucion_nombre': institucion_nombre})


def ver_plan_pagos(request):
    """."""
    contenido_id = request.GET.get('contenido_id')
    contenido_nombre = request.GET.get('contenido_nombre')
    institucion_nombre = request.GET.get('institucion_nombre')
    plan_pagos = PlanPago.objects.filter(contenido=contenido_id)
    mensaje = None
    if not plan_pagos:
        mensaje = 'No hay un plan de pagos desarrollado'
    return render(
        request, 'academias/ver_plan_pagos.html',
        {'plan_pagos': plan_pagos, 'mensaje': mensaje,
            'contenido_id': contenido_id, 'contenido_nombre': contenido_nombre,
            'institucion_nombre': institucion_nombre})
