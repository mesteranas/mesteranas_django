from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.post)
admin.site.register(models.Comments)
admin.site.register(models.requestProject)

