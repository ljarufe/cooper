# -*- coding: utf-8 -*-

from django import template
from django.db.models import Max
# models
from blog.models import Post

register = template.Library()

@register.inclusion_tag('common/templatetags/blog_url.html')
def blog_next_url(post_id):
    """
    Renderiza la url del siguiente post, en forma circular
    """
    try:
        post = Post.objects.get(id=post_id+1)
        next_id = post_id + 1
    except Post.DoesNotExist:
        next_id = 1
    return {'id': next_id}
    
    
@register.inclusion_tag('common/templatetags/blog_url.html')
def blog_previous_url(post_id):
    """
    Renderiza la url del anterior post, en forma circular
    """
    try:
        post = Post.objects.get(id=post_id-1)
        next_id = post_id - 1
    except Post.DoesNotExist:
        next_id = Post.objects.aggregate(Max('id'))['id__max']
    return {'id': next_id}
