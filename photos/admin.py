from django.contrib import admin
from photos.models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'license', 'visibility',)
    list_filter = ('license', 'visibility',)
    search_fields = ('name', 'description',)

    def owner_name(self, photo):
        return "{0} {1}".format(photo.owner.first_name, photo.owner.last_name)
    owner_name.admin_order_field = 'owner'
    owner_name.short_description = 'Propietario'

admin.site.register(Photo, PhotoAdmin)
