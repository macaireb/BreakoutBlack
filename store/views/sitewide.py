from django.db.models.signals import post_save
from django.conf import settings
from store.models.customer import UserProfile


# @receiver(post_save, sender=UserProfile, dispatch_uid="update_users", weak=False)
def update_users(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
        userprofile.save()
        # also try old boilerplate way but keep the save in there


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
        print("conencted user with custom model")
        userprofile.save()


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)