from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Post

def index(request):
    ''' blog列表 '''

    # 对Post进行all查询
    posts = Post.objects.all()
    return render_to_response('index.html',    # 模板
        {"posts": posts},   # 传递给模板的数据
        context_instance=RequestContext(request)    # 使用context_instance传递request变量给模板
    )

def post(request, pk):
    ''' 单篇文章 '''

    # 对Post 根据 pk 进行查询
    post = get_object_or_404(Post, pk=pk)

    return render_to_response("post.html",
        {"post": post},
        context_instance=RequestContext(request)
    )
