from django.conf import settings
from django.dispatch import receiver

from django.db.models.signals import post_save, post_migrate
from rest_framework.authtoken.models import Token

from .models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_migrate, sender=None)
def create_superuser(sender, **kwargs):
    """
    Creates a new superuser if doesn't exist after every migrate action
    User details are populated from settings (
        SUPERUSER_USERNAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD
    )
    """
    if getattr(settings, 'CREATE_SUPERUSER', False):

        email = settings.SUPERUSER_EMAIL
        password = settings.SUPERUSER_PASSWORD

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            print('Creating superuser ({0}:{1})'.format(email, password))
            User.objects.create_superuser(email=email, password=password)
