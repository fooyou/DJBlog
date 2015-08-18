
"""djblog URL Configuration
    需要将此url(blog.urls)添加到主URL控制器上。
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # 对于index视图，此应用是唯一的，所以直接开始结束^$，即为根目录。
    url(r'^$', 'blog.views.index', name='index'),

    # 对于post，我们需要通过id访问，所以写了个正则表达式
    url(r'^(?P<pk>\d+)/$', 'blog.views.post', name='post'),
]
