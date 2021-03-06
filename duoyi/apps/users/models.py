from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
GENDER = (("male", "男"),
          ("female", "女"))


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=GENDER, default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话", unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱", unique=True)
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="加入时间")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        if str(self.name) != 'None':
            return str(self.name)
        else:
            return str(self.username)


#  使用redis保存验证码
# class VerifyCode(models.Model):
#     """
#     短信验证码
#     """
#     code = models.CharField(max_length=10, verbose_name='验证码')
#     mobile = models.CharField(max_length=11, verbose_name='电话号码')
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")
#
#     class Meta:
#         verbose_name = '短信验证码'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.code)


from django.contrib.auth import get_user_model

User = get_user_model()


class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

