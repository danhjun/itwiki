from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from ..models import Tag, Topic, Article, SubTopic

class ModelTestCase(TestCase):
    def setUp(self):
        # Create instances for use in multiple tests
        self.tag = Tag.objects.create(name='Education')
        self.topic = Topic.objects.create(name='Technology')
        self.article = Article.objects.create(
            title='New Advances in AI',
            blurb='A detailed look into artificial intelligence advancements.',
            date_published=timezone.now(),
            tag=self.tag,
            topic=self.topic,
            link='https://www.example.com'
        )
        self.subtopic = SubTopic.objects.create(
            topic=self.topic,
            name='Deep Learning',
            description='Exploring deep learning techniques.',
            code='DL101',
            status=True,
            note_link='https://www.example.com'
        )

    def test_tag_str(self):
        """Test the string representation of the Tag model."""
        self.assertEqual(str(self.tag), 'Education')

    def test_topic_str(self):
        """Test the string representation of the Topic model."""
        self.assertEqual(str(self.topic), 'Technology')

    def test_article_str(self):
        """Test the string representation of the Article model."""
        self.assertEqual(str(self.article), 'New Advances in AI')

    def test_subtopic_str(self):
        """Test the string representation of the SubTopic model."""
        self.assertEqual(str(self.subtopic), 'Deep Learning')

    def test_article_default_image(self):
        """Test that the default image is set for Article."""
        expected_image_path = 'automation_programmability.png'
        actual_image_path = self.article.image.name
        self.assertEqual(actual_image_path, expected_image_path)

    def test_subtopic_code_length(self):
        """Test that the SubTopic code adheres to the max_length constraint."""
        self.subtopic.code = 'LONGCODE1234'  # This should be too long based on the model definition
        with self.assertRaises(ValidationError):
            self.subtopic.full_clean()  # This will validate the model fields

