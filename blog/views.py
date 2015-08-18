from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import Http404
from django.views.generic import ListView, DetailView

from blog.models import Post, Category

# class PostList(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'index.html'

# index = PostList.as_view()

# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'post'
#     template_name = 'post.html'

# post = PostDetailView.as_view()


def index(request):
   ''' blog列表 '''

   # 对Post进行all查询
   posts = Post.objects.all()
   categories = Category.objects.all()
   return render_to_response('index.html',    # 模板
           {"posts": posts, "categories": categories},   # 传递给模板的数据
           context_instance=RequestContext(request)    # 使用context_instance传递request变量给模板
   )

def post(request, pk):
   ''' 单篇文章 '''

   # 对Post 根据 pk 进行查询
   post = get_object_or_404(Post, pk=pk)
   categories = Category.objects.all()

   return render_to_response("post.html",
           {"post": post, "categories": categories},
           context_instance=RequestContext(request)
   )

def category(request, pk):
    ''' 相应分类下的文章检索 '''

    # 读取分类如果不存在就404
    try:
        cate = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404

    # 获取分类下的所有文章。
    posts = cate.post_set.all()
    return render_to_response('index.html',
            {'posts': posts,
                'is_category': True,
                'cate_name': cate.name,
                'categories': Category.objects.all()},
            context_instance=RequestContext(request)
    )
