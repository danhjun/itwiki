from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Tag, Topic, Article, Comment


class IndexView(generic.ListView):
    template_name = "wiki/index.html"
    
    context_object_name = "latest_article_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by("-date_published")[:4]
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the topics
        context['topic_list'] = Topic.objects.all()
        return context

class DetailView(generic.DetailView):
    model = Article
    template_name = "wiki/detail.html"



