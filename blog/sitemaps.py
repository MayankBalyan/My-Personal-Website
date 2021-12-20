from django.contrib.sitemaps import Sitemap
from .models import Post
 
 
class ArticleSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date
        
    def location(self,obj):
        return '/blog/%s' % (obj.slug)