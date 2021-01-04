from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import LibraryList

@admin.register(LibraryList)
class LibraryListAdmin(ImportExportModelAdmin):
    pass
