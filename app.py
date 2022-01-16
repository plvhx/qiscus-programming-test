import logging
import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
logger = logging.getLogger('gunicorn.error')

app.logger.handlers = logger.handlers
app.logger.level = logger.level

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/callback', methods=['POST'])
def agent_callback():
	data  = json.loads(request.data.decode())
	agent = data['candidate_agent']

	app.logger.info(json.dumps(data['candidate_agent']));

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
