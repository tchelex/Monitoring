from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Monitoring
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    # получить последнюю запись
    reg_user = User.objects.latest('id')
    if Monitoring.objects.filter(day=reg_user.date_joined).exists():
        monitor = Monitoring.objects.filter(day=reg_user.date_joined)
        monitor.update(count=F('count') + 1)
        monitor.list_users()
    else:
        monitor = Monitoring(day=reg_user.date_joined, count=1)
        monitor.save()
