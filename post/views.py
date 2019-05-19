from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page #缓存

from post.models import Post
from django.core.paginator import Paginator #分页器

from django.core.cache import caches

#获取缓存对象
cachesobj = caches["default"]



def cache_wrapper(func):
    def _wrapper(request, *args, **kwargs):
        #从缓存中获取对象
        data = cachesobj.get(request.path)

        #判断获取的数据是否为空
        if data:
            print("读取缓存中的数据！")
            return HttpResponse(data)

        #执行 views 函数，从数据库中获取数据
        print("从数据库中获取数据！")
        response = func(request, *args, **kwargs)

        #将数据缓存
        cachesobj.set(request.path, response.content)


        return response
    return _wrapper




def queryAll(request, current_num=1):
    current_num = int(current_num)
    #获取所有帖子信息
    post_list = Post.objects.all().order_by("-created")
    #创建分页器对象
    page = Paginator(post_list, 1)
    #拿取当前页数据
    data = page.page(current_num)


    begin = current_num - 5
    if begin < 1:
        begin = 1
    # begin = 1 if begin < 1 else begin

    end = begin + 9
    if end > page.num_pages:
        end = page.num_pages
    # end = page.num_pages if end > page.num_pages else end

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    page_list = range(begin, end + 1)



    return render(request, "index.html",
                  {"post_list": data, "page_list": page_list, "current_num": current_num})


def full_text(request, post_id):
    post_id = int(post_id)

    post = Post.objects.get(id=post_id)

    return render(request, "full_text.html", {"post": post})


def queryPostCategory(request, category_id):
    post_list = Post.objects.filter(category_id=category_id)

    return render(request, "category.html", {"post_list": post_list})


def queryPostByCreated(request, year, month):
    post_list = Post.objects.filter(created__year=year, created__month=month)

    return render(request, "category.html", {"post_list": post_list})
