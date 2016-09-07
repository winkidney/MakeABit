from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Type(models.Model):

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Word(models.Model):

    tags = models.ManyToManyField(Tag)
    types = models.ManyToManyField(Type)
    content = models.TextField()
    author = models.ForeignKey(User, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    def as_dict(self):
        return {
            "author": self.author.username,
            "content": self.content,
            "tags": [tag.name for tag in self.tags.all()],
            "types": [type_.name for type_ in self.types.all()],
            "ctime": self.ctime.isoformat(),
            "mtime": self.ctime.isoformat(),
        }