from base.models import PrimaryModel, BaseImage
from django.db import models


def get_next_image_order():
    last_object = MainImage.objects.order_by('-sort_order').last()
    if last_object:
        return last_object.sort_order + 1
    else:
        return 1


class MainImage(BaseImage):
    sort_order = models.PositiveSmallIntegerField(verbose_name='Sort order', default=get_next_image_order)
