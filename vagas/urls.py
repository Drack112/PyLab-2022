from django.urls import path

from vagas.views import (
    nova_vaga,
    vaga,
    nova_tarefa,
    realizar_tarefa,
    envia_email,
)

urlpatterns = [
    path("nova_vaga/", nova_vaga, name="nova_vaga"),
    path("vaga/<int:id>", vaga, name="vaga"),
    path("nova_tarefa/<int:id_vaga>", nova_tarefa, name="nova_tarefa"),
    path(
        "realizar_tarefa/<int:id>",
        realizar_tarefa,
        name="realizar_tarefa",
    ),
    path("envia_email/<int:id_vaga>", envia_email, name="envia_email"),
]
