from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Category,BlogModel
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils.decorators import method_decorator
# Create your views here.



class IndexView(View):
    def get(self, request):
        index_lists = Category.objects.filter(rank=0)
        displayd_tutorial=Category.objects.filter(rank=1)[0:3]
        p_tutorial = ["",]


        params={"index_lists": index_lists,"displayd_tutorial":displayd_tutorial,'p_tutorial':p_tutorial}
        return render(request, "blog/index.html", params)

    def post(self, request):
        try:
            page = request.POST.get('page', 1)
        except PageNotAnInteger:
            page = 1
        try:
            cate_list = request.POST.get('cate', "newest")
        except PageNotAnInteger:
            cate_list = "newest"

        if cate_list == "newest":
            displayed_rawblog = BlogModel.objects.order_by('created_time')[0:10]
        elif cate_list == "most_view":
            displayed_rawblog = BlogModel.objects.order_by('-views')[0:10]

        Paginated_blog = Paginator(displayed_rawblog, request=request, per_page=5)
        displayed_blog = Paginated_blog.page(page)
        params = { "displayed_blog": displayed_blog,"cate_list":cate_list}
        return render(request, "blog/index_block.html", params)


class BlogFamilyView(View):
    def get(self, request, slug):
        index_lists = Category.objects.filter(rank=0)
        p_tutorial=Category.objects.filter(rank=0,url_slug=slug)
        s_tutorial = Category.objects.filter(rank=1,parent=p_tutorial[0].id)
        params = {"index_lists":index_lists,"s_tutorial": s_tutorial, "p_tutorial": p_tutorial}
        return render(request, "blog/blogfamily.html", params)

    def post(self, request):
        return render(request, "blog/blogfamily.html")


class BlogDetailView(View):
    def get(self, request, main_slug, son_slug):
        print("enter Detail.get")
        blog_slug=request.GET.get("blog","")
        index_lists = Category.objects.filter(rank=0)
        try:
            chapter=BlogModel.objects.filter(category__url_slug=son_slug).order_by("blogsequence")

        except Exception as e:
            #redirect here
            pass
        p_tutorial = Category.objects.get(rank=0, url_slug=main_slug)

        if  blog_slug:
            #blog = BlogModel.objects.filter(category__url_slug=son_slug, url_slug=blog_slug)[0]
            blog = BlogModel.objects.get(category__url_slug=son_slug, url_slug=blog_slug)
            blog.views = blog.views+1
            blog.save()


        else:
            blog=BlogModel.objects.filter(category__url_slug=son_slug).order_by("blogsequence")[0]
            blog.views = blog.views + 1
            blog.save()


        activated_cate=Category.objects.get(url_slug=main_slug)
        params={"index_lists": index_lists,"chapter":chapter,"blog":blog,"activated_cate":activated_cate,'p_tutorial':p_tutorial}

        return render(request, "blog/blogdetail.html", params)

    def post(self, request, main_slug, son_slug):
        blog_slug = request.POST.get("blog", "")
        if blog_slug:
            blog = BlogModel.objects.filter(category__url_slug=son_slug, url_slug=blog_slug)[0]

        else:
            blog = BlogModel.objects.filter(category__url_slug=son_slug).order_by("blogsequence")[0]

        # blog = BlogModel.objects.filter(category__name=blogFamily, id=blogid)[0]
        params = {"blog": blog}
        return render(request, "blog/post_blogdetail.html", params)



def blog_show_comment(request, id=''):
    blog = BlogModel.objects.get(id=id)

    return render(request, 'blog_comments_show.html', {"blog": blog})

def search(request):
    index_lists = Category.objects.filter(rank=0)
    p_tutorial = ["", ]
    q = request.GET.get('q')
    error_msg = ''
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'blog/search.html', {'error_msg': error_msg,"index_lists": index_lists,'p_tutorial':p_tutorial})

    displayed_rawblog = BlogModel.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))

    Paginated_blog = Paginator(displayed_rawblog, request=request, per_page=10)
    displayed_blog = Paginated_blog.page(page)


    return render(request, 'blog/search.html', {"index_lists": index_lists,'error_msg': error_msg,
                                               'displayed_blog': displayed_blog,'p_tutorial':p_tutorial})


def page_not_found(request):
    return render(request, '404.html')
def server_error(request):
    return render(request, '500.html')