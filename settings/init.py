from environ import Env

from .base import *


env = Env()

APP_ENV = env('APP_ENV', default='local')

if APP_ENV == 'staging':
    from .staging import *
elif APP_ENV == 'production':
    from .production import *
elif APP_ENV == 'local':
    from .local import *

if not DEBUG:
    REST_FRAMEWORK.update(
        {
            'DEFAULT_RENDERER_CLASSES': [
                'rest_framework.renderers.JSONRenderer',
            ]
        }
    )
