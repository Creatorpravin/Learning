from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ("tittle", ) #show the name as title on list

admin.site.register(models.Notes, NotesAdmin)
