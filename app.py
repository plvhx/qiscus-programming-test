from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/callback', methods=['POST'])
def agent_callback():
	open('/tmp/req', 'wb').write(bytes(request.data.encode('utf-8')))
	return 'Will be processed.'
