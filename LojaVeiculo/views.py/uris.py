from django.urls import path
from lojaveiculo.views.LojaVeiculoView import list_veiculo_view
urlpatterns = [
path("", list_veiculo_view),
]
Conteúdo do __init__.py da pasta lojaveiculo/urls:
from .HomeUrls import *