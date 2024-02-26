from django.contrib import admin
from . import models

admin.site.register(models.Quiz)
admin.site.register(models.Respondent)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Result)
admin.site.register(models.Option)