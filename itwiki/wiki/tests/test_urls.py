from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import IndexView, AllArticlesView, AllTopicsView, TopicDetailView, update_subtopic_status

class TestWikiUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('wiki:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_all_articles_url_is_resolved(self):
        url = reverse('wiki:all_articles')
        self.assertEquals(resolve(url).func.view_class, AllArticlesView)

    def test_all_topics_url_is_resolved(self):
        url = reverse('wiki:all_topics')
        self.assertEquals(resolve(url).func.view_class, AllTopicsView)

    def test_topic_detail_url_is_resolved(self):
        url = reverse('wiki:topic_detail', args=[1])  # Assuming '1' is a valid topic ID
        self.assertEquals(resolve(url).func.view_class, TopicDetailView)

    def test_update_subtopic_status_url_is_resolved(self):
        url = reverse('wiki:update_subtopic_status', args=[1])  # Assuming '1' is a valid subtopic ID
        self.assertEquals(resolve(url).func, update_subtopic_status)

