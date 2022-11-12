from django.urls import path
from empresa.views import nova_empresa, empresas

urlpatterns = [
    path("nova_empresa/", nova_empresa, name="nova_empresa"),
    path("empresas/", empresas, name="empresas"),
]
