from django.contrib import admin
from .models import Application
from .resources import ApplicationResource
from import_export.admin import ImportExportModelAdmin

class ApplicationAdmin(ImportExportModelAdmin):
    resource_class = ApplicationResource

admin.site.register(Application, ApplicationAdmin)