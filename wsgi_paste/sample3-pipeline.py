#! /usr/bin/env python

def heading_filter_factory(global_conf, **local_conf):
	def filter(app):
			return HeadingFilteredApp(app, global_conf.get('heading_level', '1'))
	return filter
	
def html_filter_factory(global_conf, **local_conf):
	def filter(app):
			return HtmlFitleredApp(app)
	return filter

def content_factory(global_conf, **local_conf):
	def response_content(environ, start_response):
		return [local_conf.get('page_content', 'Nothing')]
	return response_content
	
class HeadingFilteredApp(object):
	def __init__(self, app, level):
		self.app, self.level = app, (int)(level)

	def __call__(self, environ, start_response):
		res = self.app(environ, start_response)
		res = "<h%d>%s</h%d>" % (self.level, res[0], self.level)
		return [res]
		
class HtmlFitleredApp(object):
	def __init__(self, app):
		self.app = app
	
	def __call__(self, environ, start_response):
		res = self.app(environ, start_response)
		style="margin-left:auto; margin-right:auto; background-color:#27a; width:80%; padding:20px;color:white"
		res = "<html><title>HTML DEMO</title><body width=100%%><div style='%s'> %s <div></body></html>" % (style, res[0])
		start_response('200 OK', [('Content-type', 'text/html')])
		return [res]
