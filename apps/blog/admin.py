from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import *
# Register your models here.
admin.site.register(Tag)
# admin.site.register(Post)
# admin.site.register(Paragraph)
admin.site.register(Comment)
admin.site.register(Reply)
class ParagraphInLine(NestedStackedInline):
	model = Paragraph
	extra = 1
	fk_name = 'post'
class PostAdmin(NestedModelAdmin):
	model = Post
	filter_horizontal = ('tags',)
	list_display = ('title', 'get_tags')
	search_filter = ['title', 'tags']
	inlines = [ParagraphInLine]

admin.site.register(Post, PostAdmin)