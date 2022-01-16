from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/callback', methods=['POST'])
def agent_callback():
	open('/tmp/req', 'wb').write(request.data)
	return 'Will be processed.'
