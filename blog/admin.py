from django.contrib import admin
from blog.models import *

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	class Media:
		js = (
			'/static/js/kindeditor-4.1.10/kindeditor-min.js',
			'/static/js/kindeditor-4.1.10/lang/zh_CN.js',
			'/static/js/kindeditor-4.1.10/config.js',
		)


admin.site.register(User)
admin.site.register(Tag)
# admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

