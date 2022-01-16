from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/callback', methods=['POST'])
def agent_callback():
	open('/tmp/req', 'wb').write(bytes(request.data.encode('utf-8')))
	return jsonify({
		'data': {
			'agent': {
				'id': 1776,
				'name': 'Bill Tanthowi Jauhari',
				'sdk_email': 'Ny83g_bill@gmail.com',
				'email': 'bill@gmail.com',
				'sdk_key': '2xxxxxxxxxxxea743',
				'type': 2,
				'is_available': false,
				'avatar_uri': null,
				'is_verified': false,
				'force_offline': false,
				'count': 0
			}
		}
	})