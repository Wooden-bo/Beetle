from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE, help_text="商品id")
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username



class UserComment(models.Model):
    """
    商品评论
    """
    MESSAGE_CHOICES = (
        (1, "好评"),
        (2, "一般"),
        (3, "差评"),
    )
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.PROTECT)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.PROTECT)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="评论类型",
                                       help_text="留言类型: 1(好评),2(一般),3(差评)")
    subject = models.CharField(max_length=100, default="评论", verbose_name="主题")
    message = RichTextUploadingField(default="", verbose_name="评论内容", help_text="评论内容")

    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
