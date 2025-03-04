from django.contrib import admin
from .models import Textbook

class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edition', 'condition')


admin.site.register(Textbook, TextbookAdmin)
