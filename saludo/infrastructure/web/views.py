import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from saludo.application.services.saludar_service import SaludarService
from saludo.domain.persona import Persona


@csrf_exempt
@require_POST
def saludar(request):
    try:
        datos = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "JSON inválido"},
            status=400,
            json_dumps_params={"ensure_ascii": False},
        )

    nombre = datos.get("nombre", "mundo")
    mensaje = SaludarService().saludar(Persona(nombre=nombre))
    return JsonResponse({"mensaje": mensaje}, json_dumps_params={"ensure_ascii": False})