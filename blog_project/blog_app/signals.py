from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import *
import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info(f"[LOGIN] User '{user.username}' logged in from IP {get_client_ip(request)}.")

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(f"[LOGOUT] User '{user.username}' logged out from IP {get_client_ip(request)}.")

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    logger.warning(f"[FAILED LOGIN] Login attempt failed for username: {credentials.get('username')} from IP {get_client_ip(request)}.")

def get_client_ip(request):
    """Utility to get the IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


        
            
        
