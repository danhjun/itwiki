from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="itwiki/wiki/static/wiki/images", default="automation_programmability.png")
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField()
    date_published = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="itwiki/wiki/static/wiki/images", default="automation_programmability.png")
    link = models.URLField(max_length=200, default="https://www.cisco.com")

    def __str__(self):
        return self.title

class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    code = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    note_link = models.URLField(max_length=200, default="https://www.cisco.com")

    def __str__(self):
        return self.name