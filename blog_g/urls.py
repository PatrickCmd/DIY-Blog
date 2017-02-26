from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^blogs-all/$', views.BlogPostListView.as_view(), name='blogs'),
	url(r'^blogs-all/(?P<pk>\d+)$', views.BlogPostDetailView.as_view(), name='post-detail'),
	url(r'^add/$', views.BlogPostCreate.as_view(), name='post-add'),
	url(r'^blogs-all/(?P<pk>\d+)/update/$', views.BlogPostUpdateView.as_view(), name='post-update'),
	url(r'^blogs-all/(?P<pk>\d+)/comment/$', views.BlogCommentCreate.as_view(), name='post-comment'),
	url(r'^postedblogs/$', views.BlogPostsByAuthorListView.as_view(), name='my-blogposts'),
	url(r'^bloggers/$', views.BlogAuthorsListView.as_view(), name='authors'),
	url(r'^addauthor/$', views.BlogAuthorCreate.as_view(), name='add-author'),
	url(r'^bloggers/(?P<pk>\d+)$', views.BlogAuthorDetailView.as_view(), name='author-detail'),
]