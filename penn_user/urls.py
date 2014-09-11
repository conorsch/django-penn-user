from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django_penn_user.views import IndexPage

urlpatterns = patterns('',
    url(r'^$', IndexPage.as_view(), name='home'),
)
