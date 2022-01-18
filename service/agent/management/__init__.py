import service.agent.channels as c
import service.agent.scope as s
import service.agent.sort_mode as smod
from service.abstract import Abstract
from service.exception import IncompleteRequiredHeaderException

class Management(Abstract):
	def get_agent_by_ids(self, ids, headers=None):
		url  = '/api/v1/admin/agents/get_by_ids'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

		try:
			headers['Qiscus-Secret-Key']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-Secret-Key\' from headers list.'
			) from e

		norm = list(map(lambda x: 'ids[]=%d' % (x), ids))
		url  = url + '?' + '&'.join(norm if len(norm) != 0 else ['ids[]='])
		url  = self.get_client().get_base_url() + url

		return self.get_client().get(url)

	def get_all_agents(self, page=None, limit=None,
		                     search=None, scope=None, headers=None):
		url   = '/api/v2/admin/agents'
		query = []

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

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
		url = self.get_client().get_base_url() + url

		return self.get_client().get(url)

	def get_agents_by_division(self, division_ids, page=None,
		                             limit=None, is_available=None,
		                             sort=None, headers=None):
		url   = '/api/v2/admin/agents/by_division'
		query = []

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

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
		url = self.get_client().get_base_url() + url

		return self.get_client().get(url)

	def create_agent(self, payload, headers=None):
		url = '/api/v2/admin/create_agent'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

		url = self.get_client().get_base_url() + url

		return self.get_client().post(url, payload)

	def update_agent(self, agent_id, payload, headers=None):
		url = '/api/v2/admin/agent/{}/update'.format(str(agent_id))

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			)

		url = self.get_client().get_base_url() + url

		return self.get_client().post(url, payload)

	def delete_agent(self, agent_id, payload, headers=None):
		url = '/api/v1/admin/agent/{}/delete'.format(str(agent_id))

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

		url = self.get_client().get_base_url() + url

		return self.get_client().post(url, payload)

	def get_agent(self, user_id, headers=None):
		url = '/api/v2/admin/agent/{}'.format(str(user_id))

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

		url = self.get_client().get_base_url() + url

		return self.get_client().get(url)

	def get_user_channel(self, user_id, channel=None, headers=None):
		url   = '/api/v2/admin/agent/{}/channels'.format(str(user_id))
		query = []

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header name \'Qiscus-App-Id\' from headers list.'
			) from e

		if isinstance(channel, str) and \
		   (channel == c.WHATSAPP or channel == c.FACEBOOK or \
		   	channel == c.LINE or channel == c.QISCUS or \
		   	channel == c.CUSTOM or channel == c.TELEGRAM):
			query.append('channel={}'.format(channel))

		url = url = '?' + '&'.join(query)
		url = self.get_client().get_base_url() + url

		return self.get_client().get(url)
