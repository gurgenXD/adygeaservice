from django.contrib import admin
from gallery.models import Album, ImageInAlbum


class ImageInAlbumInline(admin.TabularInline):
    model = ImageInAlbum
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'is_active', 'image', 'image_tag')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_display = ('image_tag_mini', 'title', 'created_date', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'desc')
    inlines = (ImageInAlbumInline,)
