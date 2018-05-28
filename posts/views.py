# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


def index(request):
    posts = Posts.objects.all()
    context = {
        'title': "Latest Posts",
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def details(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    post = Posts.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/details.html', context)