from django.contrib import admin
from .models import Post,Category,BlogComment,Contact
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 
                    'published', 'date',]
    list_filter = ['published',]
    list_editable = ['published',]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post,ProductAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category,CategoryAdmin)

admin.site.register(BlogComment)
admin.site.register(Contact)