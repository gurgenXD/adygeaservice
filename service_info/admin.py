from django.contrib import admin
from service_info.models import *


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Execution)
class ExecutionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'table_info',)
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )
