from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET, require_POST

from TahrirBackend.models import EnToFaTranslation, FaToEnTranslation


def _build_translation_response(translations):
    return [
        {
            'word': t.destination,
            'rating': t.rating,
            'comments': [
                {
                    'comment': c.comment,
                    'submitter_name': c.submitter_name
                }
                for c in t.comments
            ]
        }
        for t in translations
    ]


@require_GET
def translate_en(request):
    term = request.GET['term']
    translations = EnToFaTranslation.objects.filter(source__word__contains=term, verified=True)
    if len(translations) == 0:
        return HttpResponseNotFound()

    response = _build_translation_response(translations)
    return JsonResponse(response)


@require_GET
def translate_fa(request):
    term = request.GET['term']
    translations = FaToEnTranslation.objects.filter(source__word__contains=term)
    if len(translations) == 0:
        return HttpResponseNotFound()

    response = _build_translation_response(translations)
    return JsonResponse(response, status=200)


@require_POST
def create_translation_fa(request):
    return None


@require_POST
def create_translation_en(request):
    return None


@require_POST
def create_comment(request):
    return None
