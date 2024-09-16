from django.urls import path
from lojaveiculo.views.veiculoView import list_veiculo_view
urlpatterns = [

path("", list_veiculo_view),
path("<int:id>", list_veiculo_view),

]