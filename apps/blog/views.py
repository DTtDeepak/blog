from django.shortcuts import render, get_object_or_404
from apps.blog.models import *
# Create your views here.

def home(request):
	args = {}
	posts = Post.objects.all()
	tags = Tag.objects.all()
	args['posts'] = posts
	args['tags'] = tags
	return render(request, 'blog/index.html', args)
def post(request, url):
	args = {}
	post = get_object_or_404(Post, url=url)
	args["post"] = post
	return render(request, 'blog/post.html', args)
