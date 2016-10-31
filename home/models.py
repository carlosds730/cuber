from base.models import PrimaryModel, BaseImage
from django.db import models
from tinymce import models as tinymce_models


def _get_next_order(cls):
    last_object = cls.objects.first()
    if last_object:
        return last_object.sort_order + 1
    else:
        return 1


def get_next_image_order():
    return _get_next_order(MainImage)


def get_next_text_order():
    return _get_next_order(MainText)


class MainImage(BaseImage):
    class Meta:
        ordering = ['-sort_order']

    sort_order = models.PositiveSmallIntegerField(verbose_name='Sort order', default=get_next_image_order)
    headline = models.CharField(max_length=250)


class MainText(models.Model):
    class Meta:
        ordering = ['-sort_order']

    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    sort_order = models.PositiveSmallIntegerField(default=get_next_text_order)

    def __str__(self):
        return self.title