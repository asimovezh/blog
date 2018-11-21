from django.contrib import admin

# Register your models here.
from blog.models import BlogModel,Category

class BlogModelAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogModel,BlogModelAdmin)
admin.site.register(Category,CategoryAdmin)