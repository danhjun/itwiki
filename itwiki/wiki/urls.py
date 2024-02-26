from django.urls import path

from . import views

app_name="wiki"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("articles/all/", views.AllArticlesView.as_view(), name="all_articles"),
    path("topics/all/", views.AllTopicsView.as_view(), name="all_topics"),
]