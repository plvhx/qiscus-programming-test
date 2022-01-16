import logging

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
	app.logger.info(request.data)
	return jsonify({
		'data': {
			'agent': {
				'id': 1776,
				'name': 'Bill Tanthowi Jauhari',
				'sdk_email': 'Ny83g_bill@gmail.com',
				'email': 'bill@gmail.com',
				'sdk_key': '2xxxxxxxxxxxea743',
				'type': 2,
				'is_available': False,
				'avatar_uri': None,
				'is_verified': False,
				'force_offline': False,
				'count': 0
			}
		}
	})