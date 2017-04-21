from django.contrib import admin
from app.models import *

# Register your models here.


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'city', 'website')
	list_editable = ('city',)
	list_display_links = ('website', 'name')
	search_fields = ('name',)
	list_filter = ('city',)
	ordering = ('-id',)
	# fields = ('name', 'city', 'address')  # exclude
	fieldsets = (
		(None, {
			'fields': ('name', 'city', 'address')
		}),
		('Preferences', {
			'classes': ('collapse',),
			'fields': ('website', 'state_province', 'country')
		})
	)

admin.site.register(Author)
# admin.site.register(Publisher)
# admin.site.register(Publisher, PublisherAdmin)
admin.site.register(AuthorDetail)
admin.site.register(Book)