import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line

from django.http import HttpResponse

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase.sqlite3',
        }
    },
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)


def index(request):
    return HttpResponse("Hello, World!")


urlpatterns = [url('^$', index), ]

execute_from_command_line(sys.argv)
