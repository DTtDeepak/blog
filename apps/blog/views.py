from django.shortcuts import render, get_object_or_404, redirect
from apps.blog.models import *
from itertools import chain
from stop_words import get_stop_words
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponseRedirect,HttpResponse


def home(request):
	args = {}
	posts = Post.objects.order_by('-postedOn')[:5]
	tags = Tag.objects.all()
	args['posts'] = posts
	args['tags'] = tags
	return render(request, 'blog/index.html', args)
def posts(request):
	args ={}
	posts = Post.objects.all()
	tags = Tag.objects.all()
	args['posts'] = posts
	args['tags'] = tags
	return render(request, 'blog/posts.html', args)
def post(request, url):
	args = {}
	post = get_object_or_404(Post, url=url)
	args["post"] = post
	return render(request, 'blog/post.html', args)
def tags(request):
	args = {}
	posts = Post.objects.all()
	tags = Tag.objects.all()
	args['posts'] = posts
	args['tags'] = tags
	return render(request, 'blog/index.html', args)
def tag(request, name):
	args = {}
	tag = get_object_or_404(Tag, name=name)
	args['tag'] = tag
	posts = Post.objects.all()
	args['posts'] = posts
	return render(request, 'blog/tag.html', args)
def comment(request):
	postid = request.POST.get('postid')
	post = get_object_or_404(Post, pk=postid)
	authorname = request.POST.get('author')
	profilePicLink = request.POST.get('profilePicLink')
	idLink = request.POST.get('idLink')
	text = request.POST.get('text')
	com = post.comment_set.create(author=authorname,profilePicLink=profilePicLink,idLink=idLink, comment=text)
	com.save()
	return redirect(request.GET['next'])
def reply(request):
	print "Hello"
	print request.POST.get('commentid')	
	print "did I get commentid?"
	commentid = request.POST.get('commentid')
	comment = get_object_or_404(Comment, pk=commentid)
	authorname = request.POST.get('author')
	profilePicLink = request.POST.get('profilePicLink')
	idLink = request.POST.get('idLink')
	text = request.POST.get('text')
	rep = comment.reply_set.create(author=authorname,profilePicLink=profilePicLink,idLink=idLink, comment=text)
	rep.save()
	return redirect(request.GET['next'])

def reply(request):
	return
def search(request):
    if 'q' in request.GET and request.GET['q']:
    	stopwords = get_stop_words('english')
    	# print stopwords
        args = {}
        q = request.GET['q']
        posts1 = Post.objects.filter(gist__icontains=q )
        tags = Tag.objects.filter(name__icontains=q)
        posts2 = Post.objects.filter(title__icontains=q )
        posts = list(chain(posts1, posts2))
        q = q.split(" ")
        for i in range(len(q)):
        	if q[i] not in stopwords:
		        posts1 = Post.objects.filter(gist__icontains=q[i])
		        posts = list(chain(posts, posts1))
		        tags1 = Tag.objects.filter(name__icontains=q[i])
		        tags = list(chain(tags, tags1))

        args['posts'] = posts
        args['tags'] = tags
        # print len(args['posts'])  
        if(len(args['posts']) == 0 and len(args['tags']) == 0):
        	args['flag']=0
    	else:
    		args['flag']=1
		args['posts'] = list(set(args['posts']))
		args['tags'] = list(set(args['tags']))
		# print args['posts']
		# print type(args['posts'])
		# print args['tags']
        return render(request, 'blog/search.html',args)
    else:
        args = {}
        q = request.GET['q']
        posts = Post.objects.all()
        tags = Tag.objects.all()
        args['posts'] = posts
        args['tags'] = tags
        return render(request, 'blog/search.html',args)
