from django.contrib import admin

# Register your models here.
from .models import Article, Topic

admin.site.register(Article)
admin.site.register(Topic)