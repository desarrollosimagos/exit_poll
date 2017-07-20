from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def handler404(request):
    return render_to_response('404.html', RequestContext(request))


def handler500(request):
    return render_to_response('500.html', RequestContext(request))
