from django.urls import path
from .views import update_subtopic_status
from . import views

app_name="wiki"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("articles/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("articles/all/", views.AllArticlesView.as_view(), name="all_articles"),
    path("topics/all/", views.AllTopicsView.as_view(), name="all_topics"),
    path('topic/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('subtopics/<int:subtopic_id>/update_status/', update_subtopic_status, name='update_subtopic_status'),]

