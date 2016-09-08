import json

from django.core import serializers
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView

from words.models import Word


class Home(ListView):
    model = Word

    def get(self, request, *args, **kwargs):
        if request.GET.get('json') == 'true':
            return HttpResponse(serializers.serialize('json', self.get_queryset()))
        return super(Home, self).get(request, *args, **kwargs)


class Detail(DetailView):
    model = Word

    def get(self, request, *args, **kwargs):
        if request.GET.get('json') == 'true':
            obj = self.get_object()
            return HttpResponse(json.dumps(obj.as_dict()))
        return super(Detail, self).get(request, *args, **kwargs)


class Random(DetailView):
    model = Word

    def get_object(self, queryset=None):
        return self.model.random()

    def get(self, request, *args, **kwargs):
        if request.GET.get('json') == 'true':
            obj = self.get_object()
            return HttpResponse(json.dumps(obj.as_dict()))
        return super(Random, self).get(request, *args, **kwargs)