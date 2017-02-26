from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db import models
from datetime import date

# Create your models here.

class BlogAuthor(models.Model):
	"""
	Model representing Blog Author object
	"""

	name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	bio  = models.TextField(max_length=2000, null=True, blank=True, help_text="Bio Data of Author")

	class Meta:
		permissions = (('can_create_edit_delete_authors', 'create edit delete author'),)

	def get_absolute_url(self):
		"""
		Returns url to a particular author details
		"""

		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""
		String representation of Blog Author object in admin site
		"""
		# print(self.name)
		str_rep = str(self.name)
		# print(type(str_rep))

		return '%s' % (str_rep)


class BlogPost(models.Model):
	"""
	Model representing Post object
	"""

	title        = models.CharField(max_length=200)
	author       = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True, help_text="Select Author for this Blog Post")
	description  = models.TextField(max_length=10000, help_text="Description content of blog post")
	post_date    = models.DateField(null=True, blank=True)

	class Meta:
		permissions = (('can_create_edit_delete_posts', 'create edit delete post'),)
		ordering    = ["-post_date"]

	# def display_author(self):
	# 	"""
	# 	Creates string for Author    # this is required for display in admin
	# 	"""
	# 	return ', '.join([user.username for user in self.author.all()[:3] ])
	# display_author.short_description = 'Author'

	def get_absolute_url(self):
		"""
		Returns url to particular post detail
		"""

		return reverse('post-detail', args=[str(self.id)])

	def __str__(self):
		"""
		string representation of blog post in admin site
		"""

		return self.title


class BlogComment(models.Model):
	"""
	Model representing Blog Comment object
	"""

	description  = models.TextField(max_length=10000, help_text="Description content of blog comment")
	post_date    = models.DateTimeField(default=timezone.now)
	author       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="Select Author for this Blog Comment")
	blog         = models.ForeignKey(BlogPost, on_delete=models.CASCADE, help_text="Blog Post related to this comment")

	class Meta:
		ordering = ['post_date']

	def get_absolute_url(self):
		"""
		Returns url representation of comment instance
		"""

		return reverse('comment-detail', args=[str(self.id)])

	def __str__(self):
		"""
		String representation of comment
		"""

		return '%s-%s' % (str(self.id), str(self.post_date))
