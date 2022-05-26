from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


''' when the user is save and send this signal(post_save) which will
be received by the create_profile() and this create_profile()
received all the argument send by create_profile which are instance of user,
created 
'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(users=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(save_profile, sender=User)