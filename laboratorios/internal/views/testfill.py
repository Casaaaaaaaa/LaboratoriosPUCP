from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from internal.models import *
from . import forms


def index(request,
          service_id,
          essay_id,
          template='internal/testfill/index.html',
          extra_context=None):
    service = get_object_or_404(Service, pk=service_id)
    essay = get_object_or_404(service.essays, pk=essay_id)
    test_list = essay.testfill_set.all()

    context = {
        'service': service,
        'essay': essay,
        'test_list': test_list,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


def show(request,
         service_id,
         essay_id,
         test_id,
         template='internal/testfill/show.html',
         extra_context=None):
    service = get_object_or_404(Service, pk=service_id)
    essay = get_object_or_404(service.essays, pk=essay_id)
    test = get_object_or_404(essay.testfill_set, pk=test_id)
    parameter_forms = forms.ParameterFillFormset(
        queryset=test.parameterfill_set.all()
    )

    context = {
        'service': service,
        'essay': essay,
        'test': test,
        'parameter_forms': parameter_forms,
    }
    if extra_context is not None:
        context.update(extra_context)
    if request.is_ajax() or request.GET.get('type') == 'json':
        template = 'internal/testfill/show.table.html'
        rendered = render_to_string(template, context, request)
        return JsonResponse({
            'success': True,
            'render': rendered,
        }, json_dumps_params={'ensure_ascii': False})
    return render(request, template, context)


@require_http_methods(['POST'])
def update(request,
           service_id,
           essay_id,
           test_id):
    response = {
        'success': False,
    }
    parameter_forms = forms.ParameterFillFormset(request.POST)
    if parameter_forms.is_valid():
        parameter_forms.save()
        response['success'] = True
    else:
        response['error'] = str(parameter_forms.errors)

    if request.is_ajax():
        return JsonResponse(
            response,
            json_dumps_params={'ensure_ascii': False}
        )
    return redirect(
        'internal:testfill.show',
        service_id=service_id,
        essay_id=essay_id,
        test_id=test_id
    )