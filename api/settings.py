# api/settings.py
INSTALLED_APPS = [
    # ...
    'encyclopedia',
]


# api/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']


WSGI_APPLICATION = 'api.wsgi.app'
