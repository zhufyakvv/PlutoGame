from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


# Create your models here.
def user_directory_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/images/{1}'.format(instance.id, filename)


def user_directory_level_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/levels/{1}'.format(instance.by.id, filename)


class User(AbstractUser):
    image = models.ImageField(default='no_image.png', upload_to=user_directory_image_path)
    points = models.FloatField(default=10, blank=False)


class Mate(models.Model):
    a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a', blank=False)
    b = models.ForeignKey(User, on_delete=models.CASCADE, related_name='b', blank=False)

    a_confirmation = models.BooleanField(default=True, blank=False)
    b_confirmation = models.BooleanField(default=False, blank=False)

    date = models.DateTimeField(default=timezone.now, blank=False)


def mate_change(by, to):
    try:
        mate = Mate.objects.get(a=by, b=to)
        mate.a_confirmation = not mate.a_confirmation
    except ObjectDoesNotExist:
        try:
            mate = Mate.objects.get(a=to, b=by)
            mate.b_confirmation = not mate.b_confirmation
        except ObjectDoesNotExist:
            try:
                by = User.objects.get(id=by)
                to = User.objects.get(id=to)
                mate = Mate(a=by, b=to)
            except ObjectDoesNotExist:
                return
    mate.save()
    return mate


# TODO Levels, Comments,
class Level(models.Model):
    name = models.CharField(max_length=128, blank=False)
    date = models.DateTimeField(default=timezone.datetime.now, blank=False)

    by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    file = models.FileField(upload_to=user_directory_level_path)


class Article(models.Model):
    title = models.CharField(max_length=128, blank=True)
    value = models.TextField(max_length=512, blank=False)

    date = models.DateTimeField(default=timezone.now, blank=False)
    by = models.ForeignKey(User, on_delete=models.CASCADE)