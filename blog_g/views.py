from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from .models import BlogPost, BlogAuthor, BlogComment

# Create your views here.

def index(request):
	"""
	view for the index page
	"""

	# Count of the main objects
	num_blogs   = BlogPost.objects.all().count()
	num_authors = BlogAuthor.objects.count()   # all() implied by default

	context = {
		'num_authors': num_authors,
		'num_blogs': num_blogs,
	}

	return render(request, 'blog_g/index.html', context)

class BlogPostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	"""
	Generic View for creating new Blog Post
	"""
	permission_required = 'can_create_edit_delete_posts'
	model               = BlogPost
	fields              = '__all__'


class BlogPostListView(generic.ListView):
	"""
	Generic-List View for Blog Post Lists
	"""

	model    = BlogPost   # generic view queries database for all Blog Post Model
	paginate_by = 5   # number of blog posts paginations per page

	context_object_name = 'blog_posts'
	template_name       = 'blog_g/blog_posts.html'

class BlogPostsByAuthorListView(LoginRequiredMixin, generic.ListView):
	"""
	Generic-List View for Blog Posts by particular Blog Author
	"""

	model     = BlogPost, BlogAuthor
	paginate_by  = 5

	context_object_name = 'blog_posts'
	template_name       = 'blog_g/posts_by_author.html'

	def get_queryset(self):
		# if self.request.user.is_authenticated:
		# 	user = self.request.user
		# 	if user in User.objects.filter(groups__name='Bloggers'):
		# 		return BlogPost.objects.filter(author=user).order_by('-post_date')
		user = BlogAuthor.objects.filter(name=self.request.user)
		return BlogPost.objects.filter(author=user).order_by('-post_date')


class BlogPostDetailView(generic.DetailView):
	"""
	View for particular blog detail
	"""

	model  = BlogPost

class BlogPostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	"""
	Generic View to update particular BlogPost
	"""

	permission_required = 'can_create_edit_delete_posts'
	model               = BlogPost
	fields              = ['title', 'description']

class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})

class BlogAuthorCreate(LoginRequiredMixin, CreateView):
	"""
	Generic View for creating new Authors
	"""

	model  = BlogAuthor
	fields = '__all__'

class BlogAuthorsListView(generic.ListView):
	"""
	View for a list of Blog Authors
	"""

	model = BlogAuthor
	context_object_name = 'blog_authors'
	template_name = 'blog_g/blog_authors.html'

class BlogAuthorDetailView(generic.DetailView):
	"""
	View for particular Author detail
	"""

	model  = BlogAuthor
