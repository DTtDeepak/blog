from django.db.models import * 
from django.contrib.auth.models import User

# Create your models here.

class Tag(Model):
	name = CharField(max_length=100)
	def __unicode__(self):
		return self.name
class Post(Model):
	postedOn = DateTimeField(auto_now_add=True)
	title = CharField(max_length=100)
	gist = TextField()
	tags = ManyToManyField(Tag, blank=True, related_name='tag')
	image = TextField()
	backgroundImage = CharField(max_length=100, blank=True)
	gallery = CharField(max_length=100, blank=True)
	userUpVotes = ManyToManyField(User, blank=True, related_name="postLikes")
	url = CharField(max_length=100, unique=True)
	def __unicode__(self):
		return self.title
	def get_tags(self):
		return ", ".join([e.name for e in self.tags.all()])
	class Meta:
		ordering = ['-postedOn']

class Paragraph(Model):
	post = ForeignKey(Post)
	text = TextField(blank=True)
	image = CharField(max_length=100, blank=True)
	code = TextField(blank=True)
	def getCode(self):
		mylist = self.code.split('\n')
		return mylist
	def getText(self):
		mylist = self.text.split('\n')
		for l in mylist:
			print l
		return mylist
	# newCode = TextArea(blank=True) 
class Comment(Model):
	post = ForeignKey(Post)
	author = CharField(max_length=100, null=True)
	profilePicLink = TextField(blank=True, null=True)
	idLink = TextField(blank=True, null=True)
	comment = TextField(null=True)
	time = DateTimeField(auto_now_add=True, null=True)
	userUpVotes = ManyToManyField(User, blank=True, related_name='commentLikes')
	def __unicode__(self):
		return self.comment
	class Meta:
		ordering = ['time']
class Reply(Model):
	comment = ForeignKey(Comment)
	author = CharField(max_length=100, null=True)
	profilePicLink = TextField(blank=True)
	idLink = TextField(blank=True)
	reply = TextField()
	time = DateTimeField(auto_now_add=True, null=True)
	userUpVotes = ManyToManyField(User, blank=True, related_name='replyLikes')
	def __unicode__(self):
		return self.reply
	class Meta:
		ordering = ['time']
