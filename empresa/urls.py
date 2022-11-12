from django.urls import path
from empresa.views import nova_empresa, empresas, excluir_empresa, empresa

urlpatterns = [
    path("nova_empresa/", nova_empresa, name="nova_empresa"),
    path("empresas/", empresas, name="empresas"),
    path(
        "excluir_empresa/<int:id>",
        excluir_empresa,
        name="excluir_empresa",
    ),
    path("empresa/<int:id>", empresa, name="empresa_unica"),
]
