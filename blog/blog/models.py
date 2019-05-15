from datetime import datetime
from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=500)
    post_date = models.DateTimeField(default=datetime.now)
    is_hidden = models.BooleanField(default=False)
    visit_count = models.PositiveIntegerField(default=0)

    def comment_sorted_set(self):
        return self.comment_set.order_by('creation_date')

    def __str__(self):
        return '{} -> {}'.format(self.pk, self.post_title)


class Comment(models.Model):
    topic = models.ForeignKey(Post, on_delete=models.PROTECT)
    author = models.CharField(max_length=50)
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    reply_to = models.ForeignKey('blog.Comment',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {}'.format(self.author, self.body)