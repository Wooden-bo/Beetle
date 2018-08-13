import xadmin

from .models import UserFav, UserComment


@xadmin.sites.register(UserFav)
class UserFavAdmin:
    pass


@xadmin.sites.register(UserComment)
class UserCommentAdmin:
    pass


