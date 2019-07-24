from import_export import resources
from .models import Application

class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application