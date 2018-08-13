from rest_framework import serializers

from .models import Goods, GoodsCategory, Brand, Banner, HotSearchWords, IndexAd, GoodsImage


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        exclude = ('is_delete', 'create_time')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ('is_delete', 'create_time')


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Goods
        exclude = ('is_delete', 'create_time')


class GoodsImageSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = GoodsImage
        exclude = ('is_delete', 'create_time')


class IndexAdSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    goods = GoodsSerializer()

    class Meta:
        model = IndexAd
        exclude = ('is_delete', 'create_time')


class BannerSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = Banner
        exclude = ('is_delete', 'create_time')


class HotSearchWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        exclude = ('is_delete', 'create_time')
