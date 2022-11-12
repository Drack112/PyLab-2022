from django.urls import path
from empresa.views import nova_empresa

urlpatterns = [path("nova_empresa/", nova_empresa, name="nova_empresa")]
