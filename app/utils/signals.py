from axes.signals import user_locked_out
from django.dispatch import receiver
from rest_framework.exceptions import PermissionDenied


@receiver(user_locked_out)
def user_locked(*args, **kwargs):
    raise PermissionDenied("ご利用のアカウントは凍結されています。しばらく経ってからログインしてください")
