from service.client import Client

class Abstract(object):
	def __init__(self, client):
		self.client = client

	def get_client(self):
		return self.client
