#! /usr/bin/env python
import datetime
def default_wsgi_app(environ, start_response):
	print 'environment varibles:'
	for (k, v) in environ.items():
		print "%15s : %s" % (k, v)
	
	status  = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)
	
	return ['HaHa HeHe...generated@',str(datetime.datetime.now())]

def custom_app_factory(global_config, **local_config):
	# print the global variables defined in section [DEFAULT] section
	print 'Global Config:'
	for (k, v) in global_config.items():
		print "%15s : %s" % (k, v)
	# print the local variables defined in this non-DEFAULT section
	# where the custom_app_factory is refered as 
	# paste.app_factory = sample:custom_app_factory
	print 'Local Config:'
	for (k, v) in local_config.items():
		print "%15s : %s" % (k, v)
	
	return default_wsgi_app