from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_GET, require_POST

from TahrirBackend.models import EnToFaTranslation, FaToEnTranslation, Comment


def _build_translation_response(translations):
    return [
        {
            'translation': t.translation,
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
def get_translation(request):
    word, lang = request.GET.get('word'), request.GET.get('lang')
    if not word or not lang:
        return HttpResponseBadRequest()

    if lang == 'en':
        translations = EnToFaTranslation.objects.filter(word__word=word, verified=True)
    elif lang == 'fa':
        translations = FaToEnTranslation.objects.filter(word__word=word, verified=True)
    else:
        return HttpResponseBadRequest()

    if len(translations) == 0:
        return HttpResponseNotFound()

    response = _build_translation_response(translations)
    return JsonResponse(response, status=200)


@require_POST
def create_translation(request):
    word, translation, lang = request.POST.get('word'), request.POST.get('translation'), request.POST.get('lang')
    if not word or not translation or not lang:
        return HttpResponseBadRequest()

    submitter_name = request.POST.get('name')
    if lang == 'en':
        EnToFaTranslation.objects.create(word=word, translation=translation, submitter_name=submitter_name)
    elif lang == 'fa':
        FaToEnTranslation.objects.create(word=word, translation=translation, submitter_name=submitter_name)
    else:
        return HttpResponseBadRequest()

    return HttpResponse('Comment successfully created')


@require_POST
def create_comment(request):
    word, translation, lang = request.POST.get('word'), request.POST.get('translation'), request.POST.get('lang')
    if not word or not translation or not lang:
        return HttpResponseBadRequest()

    try:
        if lang == 'en':
            translation = EnToFaTranslation.objects.get(word=word, translation=translation)
        elif lang == 'fa':
            translation = FaToEnTranslation.objects.get(word=word, translation=translation)
        else:
            return HttpResponseBadRequest()
    except (EnToFaTranslation.DoesNotExist, FaToEnTranslation.DoesNotExist):
        return HttpResponseBadRequest()

    name, comment, rating = request.POST.get('name'), request.POST.get('comment'), require_POST.get('rating')
    if not name or not comment or not rating:
        return HttpResponseBadRequest()

    Comment.objects.create(translation=translation, submitter_name=name, comment=comment, rating=rating)

    return HttpResponse('Comment successfully created')
