from django.conf.urls import url

from words import views

urlpatterns = [
    url(
        r'^$',
        views.Home.as_view(template_name="words/home.html")
    ),
    url(
        r'^(?P<pk>[\d]+)/$',
        views.Detail.as_view(template_name="words/detail.html")
    ),
    url(
        r'^random/$',
        views.Random.as_view(template_name="words/detail.html")
    ),
]
