from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView
from .models import Topic, Article
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
    
class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "wiki/detail_article.html"

class AllArticlesView(generic.ListView):
    template_name = 'wiki/all_articles.html'  # You'll need to create this template
    context_object_name = 'all_articles_list'
    paginate_by = 10  # Optional: if you want to paginate the articles

    def get_queryset(self):
        """Return all articles ordered by publication date."""
        return Article.objects.order_by("-date_published")
    
class AllTopicsView(ListView):
    model = Topic
    template_name = "wiki/all_topics.html"  # Specify your template here
    context_object_name = "all_topic_list"   # This is the context variable to be used in the template

class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = "wiki/detail_topic.html"  # You'll create this template in the next step
