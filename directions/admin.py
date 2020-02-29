from django.contrib import admin
from directions.models import *


class CourseInline(admin.StackedInline):
    model = Course
    extra = 0
    classes = ('grp-collapse grp-closed',)

    fieldsets = (
        (None, {
            'fields': ('teachers', 'title', 'duration', 'course_reg', 'price', 'desc')
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


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'work_exp', 'teach_exp', 'text', 'is_active', 'image', 'image_tag')
        }),
    )

    readonly_fields = ('image_tag',)
    list_display = ('image_tag_mini', 'name', 'work_exp', 'teach_exp', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'text')


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'image', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'desc')
    inlines = (CourseInline,)
