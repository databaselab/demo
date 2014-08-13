#! /usr/bin/env python
def welcome_page_factory(global_config, **local_config):
	def welcome_page(environ, start_response):
		start_response('200 OK', [('Content-type', 'text/plain')])
		return ['Welcome!']
	return welcome_page

def about_page_factory(global_config, **local_config):
	def about_page(environ, start_response):
		start_response('200 OK', [('Content-type', 'text/plain')])
		return ['this is the wsgi demo page version 1.0']
	return about_page