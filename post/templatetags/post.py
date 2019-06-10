from django import template
register = template.Library()

'''
{% 태크 '' %}
{{value|필터}}
'''

from post.models import *
@register.simple_tag
def print_post_list():
    return Post.objects.all()
