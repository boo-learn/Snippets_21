from django.db import models
from django.contrib.auth.models import User


class Lang(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.ForeignKey(to=Lang, null=True, on_delete=models.PROTECT)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return f"Snippet {self.name} | {self.user}"


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name="comments")
