import xadmin
from .models import Goods, GoodsCategory, Brand, GoodsImage, IndexAd, Banner, HotSearchWords


@xadmin.sites.register(GoodsCategory)
class GoodsCategoryAdmin:
    list_display = ["name", "category_type", "parent_category", "create_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', 'desc']


@xadmin.sites.register(Brand)
class BrandAdmin:
    list_display = ["name", "image", "desc"]


@xadmin.sites.register(Goods)
class GoodsAdmin:
    list_display = ("name", 'category', "goods_sn", "market_price", "is_new", "is_hot")
    list_display_links = ("name",)
    list_editable = ("is_hot",)
    search_fields = ("name", "goods_brief", "goods_desc", "category", "goods_sn")
    list_filter = ("name",)
    list_quick_filter = [{"field": "name", "limit": 10}]
    refresh_times = [3, 5]

    class GoodsImagesInline:
        model = GoodsImage
        exclude = ["create_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


@xadmin.sites.register(IndexAd)
class IndexAdAdmin:
    list_display = ["category", "goods"]


@xadmin.sites.register(Banner)
class BannerAdmin:
    list_display = ["goods", "image", "index"]


@xadmin.sites.register(HotSearchWords)
class HotSearchWordsAdmin:
    list_display = ["keywords", "index"]
