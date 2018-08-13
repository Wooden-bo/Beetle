import xadmin
from xadmin import views
from .models import UserAddress


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSettings:
    site_title = "朵颐"
    site_footer = "DuoYi"


@xadmin.sites.register(UserAddress)
class UserAddressAdmin:
    pass

# @xadmin.sites.register(VerifyCode)
# class VerifyCodeAdmin:
#     list_display = ['code', 'mobile', "create_time"]
