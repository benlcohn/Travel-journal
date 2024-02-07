from django.contrib import admin
from .models import Journal, Comment, Entry, Photo


# Register your models here.
admin.site.register(Journal)
admin.site.register(Comment)
admin.site.register(Entry)
admin.site.register(Photo)
