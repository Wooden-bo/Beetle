"""duoyi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

import xadmin

urlpatterns = [
    # Django 后台管理
    path('admin/', admin.site.urls),
    # Xadmin 后台管理
    path('xadmin/', xadmin.site.urls),
    # DFR用户认证
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 富文本编辑器CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # DRF 自动文档
    path('docs/', include_docs_urls(title='xadmin')),

    path('goods/', include('goods.urls')),
    path('trade/', include('trade.urls')),
    path('users/', include('users.urls')),
    path('operation/', include('user_operation.urls'))

]
