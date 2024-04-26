from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from ..models import Topic, Article, SubTopic, Tag

class ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Tag instance
        cls.tag = Tag.objects.create(name='Science')

        # Create a Topic instance with a default image, change the path as per your requirements
        cls.topic = Topic.objects.create(
            name='Test Topic',
            image='itwiki/wiki/static/wiki/images/automation_programmability.jpg'  # Use a valid path or a default set in your model
        )

        # Create an Article instance with all required fields including a timezone-aware datetime
        cls.article = Article.objects.create(
            title='Test Article',
            blurb='Short description of the article.',
            date_published=timezone.now(),
            tag=cls.tag,
            topic=cls.topic,
            image='itwiki/wiki/static/wiki/images/automation_programmability.jpg',  # Adjust according to actual usage or use the default
            link='https://www.example.com'
        )

        # Create a SubTopic instance
        cls.subtopic = SubTopic.objects.create(
            topic=cls.topic,
            name='Test SubTopic',
            description='Detailed description of the subtopic.',
            code='CODE123',
            status=False,
            note_link='https://www.example.com'
        )

    def test_index_view(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wiki/index.html')
        self.assertEqual(len(response.context['latest_article_list']), 1)  # expecting 1 article based on setUpTestData

    def test_all_articles_view(self):
        response = self.client.get(reverse('wiki:all_articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wiki/all_articles.html')
        self.assertTrue('all_articles_list' in response.context)

    def test_all_topics_view(self):
        response = self.client.get(reverse('wiki:all_topics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wiki/all_topics.html')
        self.assertTrue('all_topic_list' in response.context)

    def test_update_subtopic_status_post(self):
        subtopic_id = SubTopic.objects.first().id
        response = self.client.post(reverse('wiki:update_subtopic_status', args=[subtopic_id]),
                                    {'status': 'true'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"success": True, "status": True})

    def test_update_subtopic_status_invalid_method(self):
        subtopic_id = SubTopic.objects.first().id
        response = self.client.get(reverse('wiki:update_subtopic_status', args=[subtopic_id]))
        self.assertEqual(response.status_code, 400)
