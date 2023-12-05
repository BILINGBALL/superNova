from django.http import HttpResponse
from django.template.loader import get_template


def project_signature(request):
    return {'project': 'signature'}


def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)