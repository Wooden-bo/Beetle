from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GoodsListViewSet

router = DefaultRouter()
router.register('goods', GoodsListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
