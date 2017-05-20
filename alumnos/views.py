from django.shortcuts import (render, redirect)
from alumnos.forms import RegistrarPagoForm, RegistrarExamenForm
from alumnos.models import Pago, Inscripcion, Examen, EstadoInscripcion
from academias.models import Contenido, PlanPago, Asignatura
from django.http import Http404


def ver_pagos(request):
    """."""
    inscripcion_id = request.GET.get('inscripcion_id')
    alumno_nc = request.GET.get('alumno_nc')
    contenido = request.GET.get('contenido')
    pagos = Pago.objects.filter(inscripcion_id=inscripcion_id)
    mensaje = None
    if not pagos:
        mensaje = 'No hay pagos registrados'
    return render(
        request, 'alumnos/ver_pagos.html',
        {'pagos': pagos, 'mensaje': mensaje, 'alumno_nc': alumno_nc,
            'contenido': contenido, 'inscripcion_id': inscripcion_id})


def ver_examenes(request):
    """."""
    inscripcion_id = request.GET.get('inscripcion_id')
    alumno_nc = request.GET.get('alumno_nc')
    contenido = request.GET.get('contenido')
    examenes = Examen.objects.filter(inscripcion_id=inscripcion_id)
    mensaje = None
    if not examenes:
        mensaje = 'No hay exámenes registrados'
    return render(
        request, 'alumnos/ver_examenes.html',
        {'examenes': examenes, 'mensaje': mensaje, 'alumno_nc': alumno_nc,
            'contenido': contenido, 'inscripcion_id': inscripcion_id})


def registrar_examen(request):
    """."""
    if request.method == "GET":
        alumno_nc = request.GET.get('alumno_nc')
        inscripcion_id = request.GET.get('inscripcion_id')
        inscripcion = Inscripcion.objects.get(id=inscripcion_id)
        contenido = Contenido.objects.get(id=inscripcion.contenido.id)
        asignaturas = Asignatura.objects.filter(contenido=contenido)

    if request.method == "POST":
        form = RegistrarExamenForm(request.POST)
        if form.is_valid():
            # fecha = request.POST.get('fecha')
            fecha = request.POST.get('fecha_year') + '-' + '{:0>2}'.format(request.POST.get('fecha_month')) + '-' + '{:0>2}'.format(request.POST.get('fecha_day'))
            inscripcion_id = request.POST.get('inscripcion_id')
            nota = request.POST.get('nota')
            if request.POST.get('aprobado') == 'on':
                aprobado = True
            else:
                aprobado = False
            if request.POST.get('equivalencia') == 'on':
                equivalencia = True
            else:
                equivalencia = False
            asignatura_id = request.POST.get('asignatura_id')
            asignatura = Asignatura.objects.get(id=asignatura_id)
            new_examen = Examen.objects.create(
                fecha=fecha,
                nota=nota,
                inscripcion_id=inscripcion_id,
                aprobado=aprobado,
                equivalencia=equivalencia,
                asignatura=asignatura)
            new_examen.save()
            inscripcion = Inscripcion.objects.filter(id=inscripcion_id)
            if inscripcion:
                alumno_id = inscripcion[0].alumno.id
                return redirect('/admin/alumnos/alumno/{}/change/#inscripciones'.format(alumno_id))
            raise Http404
    else:
        form = RegistrarExamenForm()
    return render(
        request, 'alumnos/registrar_examen.html',
        {'form': form,
            'alumno_nc': alumno_nc,
            'contenido': contenido,
            'asignaturas': asignaturas,
            'inscripcion_id': inscripcion_id})


def historico_estados(request):
    """."""
    inscripcion_id = request.GET.get('inscripcion_id')
    alumno_nc = request.GET.get('alumno_nc')
    contenido = request.GET.get('contenido')
    historico_estados = EstadoInscripcion.objects.filter(
        inscripcion_id=inscripcion_id)
    mensaje = None
    if not historico_estados:
        mensaje = 'No hay histórico de estados'
    return render(
        request, 'alumnos/historico_estados.html',
        {'historico_estados': historico_estados, 'alumno_nc': alumno_nc,
            'contenido': contenido, 'inscripcion_id': inscripcion_id,
            'mensaje': mensaje})


def registrar_pago(request):
    """."""
    if request.method == "GET":
        alumno_nc = request.GET.get('alumno_nc')
        inscripcion_id = request.GET.get('inscripcion_id')
        inscripcion = Inscripcion.objects.get(id=inscripcion_id)
        contenido = Contenido.objects.get(id=inscripcion.contenido.id)
        plan_pago = PlanPago.objects.filter(contenido_id=contenido.id)

    if request.method == "POST":
        form = RegistrarPagoForm(request.POST)
        if form.is_valid():
            # fecha_pago = request.POST.get('fecha_pago')
            fecha_pago = request.POST.get('fecha_pago_year') + '-' + '{:0>2}'.format(request.POST.get('fecha_pago_month')) + '-' + '{:0>2}'.format(request.POST.get('fecha_pago_day'))
            inscripcion_id = request.POST.get('inscripcion_id')
            numero_comprobante = request.POST.get('numero_comprobante')
            importe = request.POST.get('importe')
            planpago_id = request.POST.get('planpago_id')
            planpago = PlanPago.objects.get(id=planpago_id)
            new_pago = Pago.objects.create(
                fecha_pago=fecha_pago,
                importe=importe,
                inscripcion_id=inscripcion_id,
                numero_comprobante=numero_comprobante,
                plan_pago=planpago)
            new_pago.save()
            inscripcion = Inscripcion.objects.filter(id=inscripcion_id)
            if inscripcion:
                alumno_id = inscripcion[0].alumno.id
                return redirect('/admin/alumnos/alumno/{}/change/#inscripciones'.format(alumno_id))
            raise Http404
    else:
        form = RegistrarPagoForm()
    return render(
        request, 'alumnos/registrar_pago.html',
        {'form': form,
            'alumno_nc': alumno_nc,
            'contenido': contenido,
            'inscripcion_id': inscripcion_id,
            'plan_pagos': plan_pago})
