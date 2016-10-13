
from django.shortcuts import render




from django.views.generic import ListView, DetailView

from .models import Links

links_list = ListView.as_view(
    queryset=LInks.objects.all(),
    template_name='links/links.html',
    paginate_by=2,
)



