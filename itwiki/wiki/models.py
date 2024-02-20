from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField()
    date_published = models.DateTimeField()
    body = models.TextField(default='')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    statement = models.TextField()
    date_published = models.DateTimeField()

    def __str__(self):
        return self.statement[:50]

