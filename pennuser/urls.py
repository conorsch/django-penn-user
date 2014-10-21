from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from pennuser.views import IndexPage

urlpatterns = patterns('',
    url(r'^$', IndexPage.as_view(), name='home'),
)
