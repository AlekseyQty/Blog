from datetime import datetime
from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=500)
    post_date = models.DateTimeField(default=datetime.now)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.post_title
