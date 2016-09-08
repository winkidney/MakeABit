from __future__ import unicode_literals

from random import randint

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
            "id": self.id,
            "author": self.author.username,
            "content": self.content,
            "tags": [tag.name for tag in self.tags.all()],
            "types": [type_.name for type_ in self.types.all()],
            "ctime": self.ctime.isoformat(),
            "mtime": self.ctime.isoformat(),
        }

    @classmethod
    def random(cls):
        # To be improved
        ids = tuple(id_tuple[0] for id_tuple in cls.objects.values_list("id"))
        random_index = randint(0, len(ids) - 1)
        return cls.objects.get(id=ids[random_index])
