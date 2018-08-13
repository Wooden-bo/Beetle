import xadmin

from .models import ShoppingCart, OrderInfo


@xadmin.sites.register(ShoppingCart)
class ShoppingCartAdmin:
    list_display = ('user', 'goods')


@xadmin.sites.register(OrderInfo)
class OrderInfoAdmin:
    pass
