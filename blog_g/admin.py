from django.contrib import admin
from . models import BlogAuthor, BlogPost, BlogComment

# Register your models here.

class BlogPostInline(admin.TabularInline):
	"""
	Defines format of inline comment insertion (used in BlogAuthorAdmin)
	"""

	model = BlogPost

@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'bio')
	inlines      = [BlogPostInline]


class BlogCommentInline(admin.TabularInline):
	"""
	Defines format of inline comment insertion (used in BlogPostAdmin)
	"""

	model = BlogComment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'description', 'post_date')
	list_filter  = ('author', 'post_date')
	inlines      = [BlogCommentInline]

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/blog_g/static/blog/js/tinymce/jquery.tinymce.min.js',
        	'/blog_g/static/blog/js/tinymce/tinymce.min.js',
		]

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
	list_display = ('description', 'post_date', 'author', 'blog')
	list_filter  = ('post_date', 'author', 'blog')