"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/<int:blog_id>',blog.views.detail,name="detail"),
    path('blog/new', blog.views.new , name ="new" ),
    path('blog/create', blog.views.create, name="create"),
    path('blog/edit/<int:blog_id>', blog.views.edit , name="edit"),
    path('blog/update/<int:blog_id>', blog.views.update, name = "update"),  
    path('blog/delete/<int:blog_id>', blog.views.delete, name = "delete"),
    path('portfolio/',portfolio.views.portfolio, name ="portfolio"),
    path('portfolio/upload', portfolio.views.upload, name="upload"),
    path('portfolio/create2', portfolio.views.create2, name="create2"),
    path('accounts/', include('accounts.urls')), # accounts 앱 안 urls 파일 참조
    path('comment/create/<int:blog_id>',blog.views.comment_create, name="comment_create"),
    path('blog/like/<int:blog_id>', blog.views.post_like, name="post_like"), # like를 위한 url
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
