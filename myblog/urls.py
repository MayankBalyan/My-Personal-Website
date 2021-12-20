"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import ArticleSitemap
app_name = "main"

sitemaps = {
    'blog':ArticleSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('blog/<str:slug>', views.post),
    path('search', views.search, name="search"),
    path('latest', views.latestpost, name="latest"),
    path('trending', views.trending, name="trending"),
    path('postComment', views.postComment, name="postComment"),
    path('category/<slug:url>',views.category),
    path('categories',views.allcategory,name='categories'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('login-page',views.login_page,name='login_page'),
    path('register_page',views.register_page,name='register_page'),
    path('signup', views.handleSignUp, name="handleSignUp"),
     path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
