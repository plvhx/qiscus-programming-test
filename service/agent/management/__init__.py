import service.agent.channels as c
import service.agent.scope as s
import service.agent.sort_mode as smod
from service.abstract import Abstract

class Management(Abstract):
	def get_agent_by_ids(self, ids):
		norm    = map(lambda x: 'ids[]={}'.format(str(x)), ids)
		unified = '/api/v1/admin/agents/get_by_ids?' + '&'.join(norm if len(norm) != 0 else ['ids[]='])
		url     = self.get_base_url() + unified

		return self.get_client().get(url)

	def get_all_agents(self, page=None, limit=None, search=None, scope=None):
		url   = '/api/v2/admin/agents'
		query = []

		if isinstance(page, int):
			query.append('page={}'.format(str(page)))

		if isinstance(limit, int):
			query.append('limit={}'.format(str(limit)))

		if isinstance(search, str):
			query.append('search={}'.format(search))

		if isinstance(scope, str) and \
		   (scope == s.DIVISION or scope == s.NAME or scope == s.EMAIL):
			query.append('scope={}'.format(scope))

		url = url + '?' + '&'.join(query)

		return self.get_client().get(url)

	def get_agents_by_division(self, division_ids, page=None,
		                             limit=None, is_available=None, sort=None):
		url   = '/api/v2/admin/agents/by_division'
		query = []

		if isinstance(page, int):
			query.append('page={}'.format(str(page)))

		if isinstance(limit, int):
			query.append('limit={}'.format(str(limit)))

		if isinstance(is_available, bool):
			query.append('is_available={}'.format('true' if is_available == True else 'false'))

		if isinstance(sort, str) and \
		   (sort == smod.ASCENDING or sort == smod.DESCENDING):
			query.append('sort={}'.format(sort))

		query.append(map(lambda x: 'division_ids[]={}'.format(str(x)), division_ids))

		url = url + '?' + '&'.join(query)

		return self.get_client().get(url)

	def create_agent(self, payload):
		url = '/api/v2/admin/create_agent'
		return self.get_client().post(url, payload)

	def update_agent(self, agent_id, payload):
		url = '/api/v2/admin/agent/{}/update'.format(str(agent_id))
		return self.get_client().post(url, payload)

	def delete_agent(self, agent_id, payload):
		url = '/api/v1/admin/agent/{}/delete'.format(str(agent_id))
		return self.get_client().post(url, payload)

	def get_agent(self, user_id):
		url = '/api/v2/admin/agent/{}'.format(str(user_id))
		return self.get_client().get(url)

	def get_user_channel(self, user_id, channel=None):
		url   = '/api/v2/admin/agent/{}/channels'.format(str(user_id))
		query = []

		if isinstance(channel, str) and \
		   (channel == c.WHATSAPP or channel == c.FACEBOOK or \
		   	channel == c.LINE or channel == c.QISCUS or \
		   	channel == c.CUSTOM or channel == c.TELEGRAM):
			query.append('channel={}'.format(channel))

		url = url = '?' + '&'.join(query)

		return self.get_client().get(url)
