import xadmin
# Register your models here.
from blog.models import BlogModel,Category
from xadmin import views
from allauth.socialaccount.models import SocialAccount,SocialApp,SocialToken
from django.contrib.sites.models import Site
class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title="全栈笔记"
    site_footer="全栈笔记@认真写笔记，认真学习"
    #menu_style="accordion"

class BlogModelAdmin(object):
    search_fields=['title',]
    list_filter=['category',]
    list_display = ['title','category','url_slug','views','blogsequence']
    style_fields = {"body": "ueditor"}

class CategoryAdmin(object):
    list_display = ['name', 'parent','rank','views','is_finished','url_slug']
    search_fields=['name', ]
    list_filter=['name','create_time']


class SocialAccountAdmin(object):
    pass
class SocialAppAdmin(object):
    pass
class SocialLoginAdmin(object):
    pass
class SocialTokenAdmin(object):
    pass
class SiteAdmin(object):
    pass

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

xadmin.site.register(BlogModel,BlogModelAdmin)
xadmin.site.register(Category,CategoryAdmin)

xadmin.site.register(SocialAccount,SocialAccountAdmin)
xadmin.site.register(SocialApp,SocialAppAdmin)
xadmin.site.register(SocialToken,SocialTokenAdmin)


xadmin.site.register(Site,SiteAdmin)
