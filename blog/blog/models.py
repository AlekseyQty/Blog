from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=500)
    post_date = models.DateTimeField(default=datetime.now)
    is_hidden = models.BooleanField(default=False)
    visit_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    class Meta:
        permissions = (('can_edit_content', 'Can edit content'),)

    def comment_sorted_set(self):
        return self.comment_set.order_by('creation_date')

    def __str__(self):
        return '{}'.format(self.post_title)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})


class Comment(models.Model):
    topic = models.ForeignKey(Post, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    reply_to = models.ForeignKey('blog.Comment',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {}'.format(self.author, self.body)
