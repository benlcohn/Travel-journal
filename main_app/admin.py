from django.contrib import admin
from .models import Journal, Comment


# Register your models here.
admin.site.register(Journal)
admin.site.register(Comment)
