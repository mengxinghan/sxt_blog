#coding = utf-8
"""全局上下文"""
from django.db.models import Count

from post.models import Post




def getRightInfo(request):
    #1.获取分类信息
    right_post_category = Post.objects.values("category__category_name", "category_id")\
        .annotate(c=Count("*")).order_by("-c")

    #获取近期文章
    right_post_newest = Post.objects.all().order_by("-created")[:3]

    #查询归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(
        'select created,count("*") c from `t-post` group by Date_format(created,"%Y-%m") order by created desc,c desc'
    )
    right_post_classify = cursor.fetchall()

    return {
        "right_post_category": right_post_category,
        "right_post_newest": right_post_newest,
        "right_post_classify": right_post_classify,
    }
