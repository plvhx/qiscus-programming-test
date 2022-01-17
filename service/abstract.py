from service.client import Client

class Abstract(object):
	def __init__(self, client):
		self.client = client
		self.base_url = ''

	def get_client(self):
		return self.client

	def get_base_url(self):
		return self.base_url
