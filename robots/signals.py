from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Robot
from orders.models import Order
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Robot)
def handler(instance, **kwargs):

    query = Order.objects.filter(robot_serial=instance.serial)

    if query.exists():
        message_text = (f'Добрый день!\n'
                        f'Недавно вы интересовались нашим роботом '
                        f'модели {instance.serial[:2]}, версии {instance.serial[3:5]}.\n'
                        f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами')

        emails = list(
            query.select_related('customer__email').
            values_list('customer__email', flat=True)
        )

        send_mail('Робот в наличии!', message_text, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=emails, fail_silently=False)
