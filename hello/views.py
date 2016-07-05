from __future__ import unicode_literals

import os

from django.http import HttpResponse


def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('TIMES = %s' % times)
