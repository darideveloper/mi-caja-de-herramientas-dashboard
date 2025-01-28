from django.contrib import admin
from blog import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)
    

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)
    

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'url')
    search_fields = ('name', 'url')


@admin.register(models.Duration)
class DurationAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('value',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'category', 'created_at', 'image')
    search_fields = ('title', 'text')
    search_help_text = 'Buscar por título o texto'
    list_filter = ('group', 'category', 'duration', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (
            "General", {
                'fields': (
                    'title',
                    'group',
                    'category',
                    'duration',
                    'links',
                    'text',
                    'created_at',
                    'updated_at',
                )
            }
        ),
        (
            'Multimedia', {
                'fields': (
                    'image', 'video', 'audio'
                )
            }
        ),
    )