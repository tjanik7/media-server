from django.contrib import admin

from media.models import ImageHash


class ImageHashAdmin(admin.ModelAdmin):
    pass

admin.site.register(ImageHash, ImageHashAdmin)
