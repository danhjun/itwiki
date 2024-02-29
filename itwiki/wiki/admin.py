from django.contrib import admin

# Register your models here.
from .models import Article, Topic, SubTopic

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(SubTopic)
