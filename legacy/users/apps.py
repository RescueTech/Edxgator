from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'edxgator.users'

    def ready(self):
        from . import signals