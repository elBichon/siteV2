from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from links.models import Links

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Links.objects.all().order_by("-date")[:2],
 template_name="links/links.html")),
            ]
