from django.urls import path

from vagas.views import nova_vaga

urlpatterns = [path("nova_vaga/", nova_vaga, name="nova_vaga")]
