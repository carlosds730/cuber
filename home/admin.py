from django.contrib import admin
from .models import MainImage, MainText
from sorl.thumbnail.admin import AdminImageMixin


class MainImageAdmin(AdminImageMixin, admin.ModelAdmin):
    model = MainImage

class MainTextAdmin(AdminImageMixin, admin.ModelAdmin):
    model = MainText


admin.site.register(MainImage, MainImageAdmin)
admin.site.register(MainText, MainTextAdmin)
