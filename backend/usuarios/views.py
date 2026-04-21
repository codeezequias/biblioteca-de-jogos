from django.http import JsonResponse
from tarefas.models import EventoAcademico
from django.shortcuts import get_object_or_404


def listar_usuarios(request):
    eventos = EventoAcademico.objects.all()
    return JsonResponse(list(eventos.values()), safe=False)


def buscar_usuario_por_id(request, id):
    evento = get_object_or_404(EventoAcademico, id=id)
    return JsonResponse({
        "id": evento.id,
        "nome": evento.nome,
        "descricao": evento.local,
    })