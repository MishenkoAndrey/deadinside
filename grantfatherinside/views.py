from django.db.models import Q
from django.shortcuts import render
from .models import Post
from .models import Tag
# Create your views here.


def get_filter(q):
    filter_ = Q()
    if q is not None:
        filter_ = Q(tags__in=Tag.objects.filter(name__in=q.split(',')))
    return filter_


def index(request):
    q = request.GET.get('q')
    posts = Post.objects.filter(get_filter(q)).distinct()
    return render(request, 'index.html', {"posts": posts})
