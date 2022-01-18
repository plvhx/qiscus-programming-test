from service.client import Client
from service.agent.management import Management
from service.agent.management.division import Division
from service.agent.service.admin import Admin
from service.agent.service.agent import Agent

class ServiceFactory(object):
	def __init__(self, client):
		self.client = client

	def get_client(self):
		return self.client

	def get_agent_management(self):
		return Management(self.get_client())

	def get_agent_management_division(self):
		return Division(self.get_client())

	def get_agent_service_admin(self):
		return Admin(self.get_client())

	def get_agent_service_agent(self):
		return Agent(self.get_client())
