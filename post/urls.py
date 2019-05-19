#coding = utf-8


from django.urls import path, re_path
from post import views


urlpatterns = [
    #主页
    path("", views.queryAll),
    #分页
    re_path(r"^page/(?P<current_num>\d+)/$", views.queryAll),
    #阅读全文
    re_path(r"^post/(?P<post_id>\d+)/$", views.full_text),
    #种类
    re_path(r"^category/(?P<category_id>\d+)/$", views.queryPostCategory),
    #归档分类
    re_path(r"^classify/(?P<year>\d{4})/(?P<month>\d{2})/$", views.queryPostByCreated)

]
