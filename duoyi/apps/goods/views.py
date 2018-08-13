from django.shortcuts import render

# Create your views here.

from rest_framework import mixins, viewsets

from .models import Goods
from .serializers import GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """
    List all goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
