from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponse


def index(request):
    times = settings.REPEAT_TIMES
    return HttpResponse('TIMES = %s' % times)
