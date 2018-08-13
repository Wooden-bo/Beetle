# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GoodsBanner(models.Model):
    image = models.CharField(max_length=100)
    index = models.IntegerField(unique=True)
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()
    goods = models.ForeignKey('GoodsGoods', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_banner'


class GoodsBrand(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.CharField(max_length=200)
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_brand'


class GoodsGoods(models.Model):
    goods_sn = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    click_num = models.IntegerField()
    sold_num = models.IntegerField()
    fav_num = models.IntegerField()
    goods_num = models.IntegerField()
    market_price = models.FloatField()
    shop_price = models.FloatField()
    goods_brief = models.TextField()
    goods_desc = models.TextField()
    ship_free = models.IntegerField()
    goods_front_image = models.CharField(max_length=100, blank=True, null=True)
    is_new = models.IntegerField()
    is_hot = models.IntegerField()
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()
    brand = models.ForeignKey(GoodsBrand, models.DO_NOTHING)
    category = models.ForeignKey('GoodsGoodscategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_goods'


class GoodsGoodscategory(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    desc = models.TextField()
    category_type = models.IntegerField()
    is_tab = models.IntegerField()
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_goodscategory'


class GoodsGoodsimage(models.Model):
    image = models.CharField(max_length=100)
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_goodsimage'


class GoodsHotsearchwords(models.Model):
    keywords = models.CharField(max_length=20)
    index = models.IntegerField(unique=True)
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_hotsearchwords'


class GoodsIndexad(models.Model):
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()
    category = models.ForeignKey(GoodsGoodscategory, models.DO_NOTHING)
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_indexad'
        unique_together = (('category', 'goods'),)


class ReversionRevision(models.Model):
    date_created = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reversion_revision'


class ReversionVersion(models.Model):
    object_id = models.CharField(max_length=191)
    format = models.CharField(max_length=255)
    serialized_data = models.TextField()
    object_repr = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    revision = models.ForeignKey(ReversionRevision, models.DO_NOTHING)
    db = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'reversion_version'
        unique_together = (('object_id', 'content_type', 'revision', 'db'),)


class TradeOrdergoods(models.Model):
    goods_num = models.IntegerField()
    create_time = models.DateTimeField()
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)
    order = models.ForeignKey('TradeOrderinfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trade_ordergoods'


class TradeOrderinfo(models.Model):
    order_sn = models.CharField(unique=True, max_length=30, blank=True, null=True)
    trade_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    pay_status = models.CharField(max_length=30)
    post_script = models.CharField(max_length=200)
    order_mount = models.FloatField()
    pay_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=100)
    signer_name = models.CharField(max_length=20)
    singer_mobile = models.CharField(max_length=11)
    create_time = models.DateTimeField()
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trade_orderinfo'


class TradeShoppingcart(models.Model):
    nums = models.IntegerField()
    create_time = models.DateTimeField()
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trade_shoppingcart'
        unique_together = (('goods', 'user'),)


class UserOperationUseraddress(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    signer_name = models.CharField(max_length=100)
    signer_mobile = models.CharField(max_length=11)
    create_time = models.DateTimeField()
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_operation_useraddress'


class UserOperationUserfav(models.Model):
    create_time = models.DateTimeField()
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_operation_userfav'
        unique_together = (('goods', 'user'),)


class UserOperationUserleavingmessage(models.Model):
    message_type = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_operation_userleavingmessage'


class UsersUserprofile(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6)
    mobile = models.CharField(unique=True, max_length=11, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    is_delete = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_userprofile'


class UsersUserprofileGroups(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_groups'
        unique_together = (('userprofile', 'group'),)


class UsersUserprofileUserPermissions(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_user_permissions'
        unique_together = (('userprofile', 'permission'),)


class UsersVerifycode(models.Model):
    code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_verifycode'


class XadminBookmark(models.Model):
    title = models.CharField(max_length=128)
    url_name = models.CharField(max_length=64)
    query = models.CharField(max_length=1000)
    is_share = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xadmin_bookmark'


class XadminLog(models.Model):
    action_time = models.DateTimeField()
    ip_addr = models.CharField(max_length=39, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.CharField(max_length=32)
    message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_log'


class XadminUsersettings(models.Model):
    key = models.CharField(max_length=256)
    value = models.TextField()
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_usersettings'


class XadminUserwidget(models.Model):
    page_id = models.CharField(max_length=256)
    widget_type = models.CharField(max_length=50)
    value = models.TextField()
    user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_userwidget'
