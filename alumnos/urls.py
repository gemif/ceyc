from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^ver_pagos/$', views.ver_pagos, name='ver_pagos'),
    url(r'^registrar_pago/$', views.registrar_pago, name='registrar_pago'),
    url(r'^ver_examenes/$', views.ver_examenes, name='ver_examenes'),
    url(r'^registrar_examen/$', views.registrar_examen,
        name='registrar_examen'),
    url(r'^historico_estados/$', views.historico_estados,
        name='historico_estados'),
]
