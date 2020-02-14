from django.contrib import admin
from .models import *


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0


class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GalleryCategory._meta.fields]

    class Meta:
        model = GalleryCategory

admin.site.register(GalleryCategory, GalleryCategoryAdmin)


class GalleryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Gallery._meta.fields]
    inlines = [GalleryImageInline]

    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)


class GalleryImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in GalleryImage._meta.fields]

    class Meta:
        model = GalleryImage

admin.site.register(GalleryImage, GalleryImageAdmin)