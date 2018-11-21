from django.db import models
from DjangoUeditor.models import UEditorField
from uuslug import uuslug
import random

# Create your models here.
class BlogModel(models.Model):
    """文章"""
    def limit_blogFather_choices(self):
        blogFather=BlogModel.objects.filter(category=self.category)
        return {'blogFather':blogFather}

    title = models.CharField('标题', max_length=200, unique=True)
    desc = models.TextField(max_length=200, verbose_name=u"描述", blank=True, null=True)
    #body = models.TextField('正文')
    body=UEditorField(verbose_name=u"博文内容",width=600,height=300,imagePath="blog/ueditor/",filePath="blog/ueditor/",default="")
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    url_slug = models.SlugField(
        verbose_name=('Slug'),
        help_text=('Uri identifier.'),
        max_length=255,
        unique=True,


    )

    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE, blank=True, null=True
                                 , limit_choices_to={'rank': 1},)
    #blogFather=models.ForeignKey('self', default=None, on_delete=models.PROTECT,blank=True, null=True, verbose_name=u'父类章节',limit_choices_to=limit_blogFather_choices,)
    blogsequence = models.IntegerField(u"章节顺序", )
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by =  'created_time'

    def __unicode__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.url_slug.strip():
    #         # slug is null or empty
    #         self.url_slug = uuslug(self.title, instance=self, max_length=32, word_boundary=True)
    #     super(BlogModel, self).save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')

    parent = models.ForeignKey('self', default=None, on_delete=models.PROTECT,blank=True, null=True, verbose_name=u'上级分类')
    image = models.ImageField(upload_to="category/%Y/%m", verbose_name=u"封面图", max_length=100,blank=True,null=True)
    rank = models.IntegerField(default=0, verbose_name=u'展示排序')
    desc=models.TextField(max_length=200,verbose_name=u"描述",blank=True,null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    is_finished=models.BooleanField(default=False,verbose_name=u"是否完成")
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)
    url_slug = models.SlugField(
        verbose_name=('Slug'),
        help_text=('Uri identifier.'),
        max_length=255,
        unique=True,

    )
    def __unicode__(self):
        if self.parent:
            return '{}:{}'.format(self.parent, self.name)
        else:
            return '{}'.format(self.name)
            # return self.name
    def __str__(self):
        if self.parent:
            return '{}:{}'.format(self.parent, self.name)
        else:
            return '{}'.format(self.name)

    # def save(self, *args, **kwargs):
    #     if not self.url_slug.strip():
    #         # slug is null or empty
    #         self.url_slug = uuslug(self.name, instance=self, max_length=32, word_boundary=True)
    #     super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = verbose_name = u"分类"

