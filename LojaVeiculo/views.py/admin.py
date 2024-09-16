from django.http import HttpResponse
def list_veiculos_view(request, id=None):

return HttpResponse('<h1>lista de veiculos de id %s!</h1>' % id)