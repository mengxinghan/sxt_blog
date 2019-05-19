from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True, verbose_name="类别名")

    class Meta:
        db_table = "t-category"
        verbose_name_plural = "类别"

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True, verbose_name="标签名")

    class Meta:
        db_table = "t-tag"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="标题")
    desc = models.CharField(max_length=100, verbose_name="简介")
    content = RichTextUploadingField(verbose_name="内容")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类别")
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    class Meta:
        db_table = "t-post"
        verbose_name_plural = "帖子"

    def __str__(self):
        return self.title
