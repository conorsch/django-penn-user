from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexPage(TemplateView):
    """
    The first page should show basic information about the process. It will be a static page.
    Django includes a flatpages app, but it's a lot faster to just use the templateview with
    the html in the template.
    """
    template_name = "django_penn_user/index.html"
