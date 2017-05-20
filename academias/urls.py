from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^ver_asignaturas/$', views.ver_asignaturas, name='ver_asignaturas'),
    url(r'^ver_plan_pagos/$', views.ver_plan_pagos, name='ver_plan_pagos'),
]
