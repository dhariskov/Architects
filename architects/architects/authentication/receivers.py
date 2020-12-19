from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from architects.authentication.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(user=instance, display_name=instance.username, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
        profile.save()
