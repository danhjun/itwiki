from django.views import generic
from django.views.generic import ListView
from .models import Topic, Article, SubTopic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

class AllArticlesView(generic.ListView):
    model = Article
    template_name = 'wiki/all_articles.html'  # You'll need to create this template
    context_object_name = 'all_articles_list'

    def get_queryset(self):
        """Return all articles ordered by publication date."""
        return Article.objects.order_by("-date_published")[:12]
    
class AllTopicsView(ListView):
    model = Topic
    template_name = "wiki/all_topics.html"  # Specify your template here
    context_object_name = "all_topic_list"   # This is the context variable to be used in the template

class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = "wiki/detail_topic.html"  # You'll create this template in the next step

@csrf_exempt
def update_subtopic_status(request, subtopic_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status')

            # Explicitly convert status to boolean if it's not already
            if isinstance(status, bool):
                new_status = status
            elif status in ['true', 'True', True]:
                new_status = True
            elif status in ['false', 'False', False]:
                new_status = False
            else:
                return JsonResponse({"error": "Invalid 'status' value"}, status=400)

            subtopic = SubTopic.objects.get(id=subtopic_id)
            subtopic.status = new_status
            subtopic.save()
            return JsonResponse({"success": True, "status": subtopic.status})
        except SubTopic.DoesNotExist:
            return JsonResponse({"error": "SubTopic not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing 'status' field"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)

