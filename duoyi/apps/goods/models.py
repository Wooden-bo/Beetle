from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True,
                                        verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat",
                                        on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否为导航", help_text="是否为导航")
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)


class Brand(models.Model):
    """
    品牌名
    """
    # category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="商品类目",
    #                              on_delete=models.DO_NOTHING)
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/", verbose_name="品牌LOGO", )
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)


class GoodsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目", on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, verbose_name="商品品牌", on_delete=models.PROTECT)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = RichTextUploadingField(verbose_name='商品描述')
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    objects = GoodsManager()

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="商品类目",
                                 on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE, verbose_name="商品")
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = '首页广告'
        verbose_name_plural = verbose_name
        unique_together = ('category', 'goods')

    def __str__(self):
        return str(self.goods.name)


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images", on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    image = models.ImageField(upload_to="goods/carousel/", verbose_name="图片")
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.goods.name)


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序", unique=True)
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.goods.name)


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序", unique=True)
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.keywords)
