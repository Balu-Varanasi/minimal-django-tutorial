import sys

from django.conf import settings
from django.core.management import execute_from_command_line

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

urlpatterns = []

execute_from_command_line(sys.argv)
