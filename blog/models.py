from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField('文章分类', max_length=64)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('标题', max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField('内容')
    pub_data = models.DateTimeField(auto_now_add=True)
    po_type = models.ForeignKey(Category, verbose_name='文章分类', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    ''' 使用models.permalink或者使用url来reverse，参见template '''
    # @models.permalink
    # def get_absolute_url(self):
    #     return ('post', (), {'pk': self.pk})
    #     # return reverse('post', args=[str(self.pk),])

