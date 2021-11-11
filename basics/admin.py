from django.contrib import admin

from .models import Article, Category
# from home.models import CreationDate

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'summary',
        'date_added',
    )
    

    ordering = ('pk',)

    class Media(admin.ModelAdmin):
        css = {
            'all': ('css/base.css',)
        }

        js = ('js/tinymce.js',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)