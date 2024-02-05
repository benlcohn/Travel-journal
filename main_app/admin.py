from django.contrib import admin
from .models import Journal, Comment, Entry


# Register your models here.
admin.site.register(Journal)
admin.site.register(Comment)
admin.site.register(Entry)
