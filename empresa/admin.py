from django.contrib import admin

from empresa.models import Tecnologias, Empresa, Vagas


# Register your models here.
admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)
