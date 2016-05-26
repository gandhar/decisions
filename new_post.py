#!/usr/bin/python

import sys
from os.path import basename, isfile, splitext

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

wp = Client('http://localhost:8081/wordpress/xmlrpc.php', 'admin', 'password')

if len(sys.argv) == 1:
	print "pass text files with post content as arguments"
	exit()

for arg in sys.argv[1:]:
	if isfile(arg):
		content = open(arg)
		post = WordPressPost()
		post.title = splitext(basename(arg))[0]
		post.content = content.read()
		post.post_status = 'publish'
		wp.call(NewPost(post))
