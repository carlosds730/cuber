from django.contrib import admin
from .models import Driver, Car, Image
from sorl.thumbnail.admin import AdminImageMixin


class DriverImageAdmin(AdminImageMixin, admin.StackedInline):
    model = Image
    exclude = ['car']
    extra = 0

class CarImageAdmin(AdminImageMixin, admin.StackedInline):
    model = Image
    exclude = ['driver']
    extra = 0

class DriverAdmin(AdminImageMixin, admin.ModelAdmin):
    model = Driver
    inlines = [DriverImageAdmin]

class CarAdmin(AdminImageMixin, admin.ModelAdmin):
    model = Car
    inlines = [CarImageAdmin]


admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
