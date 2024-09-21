
from jinja2 import Environment, FileSystemLoader
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja_env(**options):
    env = Environment(**options)
    env.globals.update({
        'static':staticfiles_storage.url,
        'url':reverse,
    })
    return env