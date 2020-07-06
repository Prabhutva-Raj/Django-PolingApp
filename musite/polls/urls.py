from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<ques_id>[0-9]+)/$', views.details , name="detail"),
    url(r'^(?P<ques_id>[0-9]+)/results$', views.results , name="results"),
    url(r'^(?P<ques_id>[0-9]+)/votess$', views.vote , name="votess"),
]