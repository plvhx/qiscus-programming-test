from service.abstract import Abstract
from service.exception import IncompleteRequiredHeaderException
from service.exception import HeaderValueViolationException
from service.exception import TypeErrorException

class Agent(Abstract):
	def hand_over(self, data, headers=None):
		url = '/api/v1/agent/service/assign_agent'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		try:
			headers['Qiscus-Secret-Key']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-Secret-Key\' from headers list.'
			) from e

		try:
			headers['Qiscus-User-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-Header-Id\' from headers list.'
			) from e

		if headers['Content-Type'] != 'application/x-www-form-urlencoded':
			raise HeaderValueViolationException(
				'Content-Type value must be \'application/x-www-form-urlencoded\'.'
			)

		return self.get_client().post(url, data)

	def mark_as_resolved(self, data, headers=None):
		url = '/api/v1/agent/service/mark_as_resolved'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Content-Type']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Content-Type\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		return self.get_client().post(url, data)

	def takeover_status(self, headers=None):
		url = '/api/v1/app/config/agent_takeover'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		return self.get_client().get(url)

	def available_agents(self, room_id, limit=None,
		                       cursor_after=None, cursor_before=None,
		                       is_available_in_room=False, headers=None):
		url   = '/api/v2/agent/service/available_agents'
		query = []

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		if not isinstance(room_id, int):
			raise TypeErrorException('\'room_id\' must be an integer.')

		query.append('room_id=%d' % (room_id))

		if isinstance(limit, int):
			query.append('limit=%d' % (limit))

		if isinstance(cursor_after, int):
			query.append('cursor_after=%d' % (cursor_after))

		if isinstance(cursor_before, int):
			query.append('cursor_before=%d' % (cursor_before))

		if isinstance(is_available_in_room, bool):
			query.append('is_available_in_room=%s' % ('true' if is_available_in_room == True else 'false'))

		url = url + '?' + '&'.join(query)

		return self.get_client().get(url)

	def get_total_unserved(self, headers=None):
		url = '/api/v2/agent/service/total_unserved'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		return self.get_client().get(url)

	def takeover_unserved(self, headers=None):
		url = '/api/v2/agent/service/takeover_unserved'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		return self.get_client().post(url)

	def add_agent(self, data, headers=None):
		url = '/api/v2/agent/service/add_agent'

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		return self.get_client().post(url)

	def get_other_agents(self, cursor_after=None, cursor_before=None,
		                       room_id=None, limit=None, headers=None):
		url   = '/api/v2/agent/service/other_agents'
		query = []

		if isinstance(headers, dict):
			self.get_client().set_headers(headers)

		headers = self.get_client().get_headers()

		try:
			headers['Authorization']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Authorization\' from headers list.'
			) from e

		try:
			headers['Qiscus-App-Id']
		except KeyError as e:
			raise IncompleteRequiredHeaderException(
				'Missing header \'Qiscus-App-Id\' from headers list.'
			) from e

		if isinstance(cursor_after, int):
			query.append('cursor_after=%d' % (cursor_after))

		if isinstance(cursor_before, int):
			query.append('cursor_before=%d' % (cursor_before))

		if isinstance(room_id, int):
			query.append('room_id=%d' % (room_id))

		if isinstance(limit, int):
			query.append('limit=%d' % (limit))

		url = url + '?' + '&'.join(query)

		return self.get_client().get(url)
