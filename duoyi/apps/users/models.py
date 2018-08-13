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

    # objects = UserProfileManager()

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        if str(self.name) != 'None':
            return str(self.name)
        else:
            return str(self.username)


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话号码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")

    # add_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="加入时间")

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.code)
