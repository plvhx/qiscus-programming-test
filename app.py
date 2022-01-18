import logging
import json
import service.config as conf

from flask import Flask
from flask import jsonify
from flask import request
from service.client import Client
from service.factory import ServiceFactory

app = Flask(__name__)
logger = logging.getLogger('gunicorn.error')

app.logger.handlers = logger.handlers
app.logger.level = logger.level

factory = ServiceFactory(Client(conf.BASE_URL))

def get_agent_auth_token(id):
	headers = {
		'Content-Type': 'application/json',
		'Qiscus-App-Id': conf.APP_ID,
		'Qiscus-Secret-Key': conf.APP_SECRET
	}
	response = factory \
		.get_agent_management() \
		.get_agent_by_ids([id], headers)

	if response == None:
		return False

	return response['data'][0]['authentication_token']

def assign_agent_to_room(agent_id, room_id):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Qiscus-App-Id': conf.APP_ID,
		'Qiscus-Secret-Key': conf.APP_SECRET
	}
	data = {
		'room_id': room_id,
		'agent_id': agent_id,
		'replace_latest_agent': False,
		'max_agent': 1
	}
	response = factory \
		.get_agent_service_admin() \
		.assign_agent(data, headers)

	return False if response == None else response

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/callback', methods=['POST'])
def agent_callback():
	data  = json.loads(request.data.decode())
	agent = data['candidate_agent']

	app.logger.info(json.dumps(data))
	app.logger.info(json.dumps(data['candidate_agent']));
	app.logger.info(agent['id'])
	app.logger.info(int(data['room_id']))

	response = assign_agent_to_room(agent['id'], int(data['room_id']))

	app.logger.info(response)

	if response == False:
		return jsonify({
			'message': 'There was an error when trying to assign agent to specified room.'
		}), 400

	return jsonify({
		'data': {
			'agent': {
				'id': agent['id'],
				'name': agent['name'],
				'sdk_email': agent['sdk_email'],
				'email': agent['email'],
				'sdk_key': agent['sdk_key'],
				'type': agent['type'],
				'is_available': agent['is_available'],
				'avatar_url': agent['avatar_url'],
				'is_verified': agent['is_verified'],
				'force_offline': agent['force_offline'],
				'count': 0
			}
		}
	})
