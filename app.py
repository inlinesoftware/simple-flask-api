from flask import Flask
from flask import request, jsonify
import urllib2

app = Flask(__name__)
base_url = 'https://api.telegram.org/'

@app.route("/testSignal/<bot>/<chat_id>/<msg>", methods=['GET', 'POST'])
def broadcast(bot, chat_id, msg):
	if request.method == 'GET':
		contents = urllib2.urlopen(base_url+bot+"/sendMessage?chat_id="+chat_id+"&text="+msg).read()
		return contents
	if request.method == 'POST':
		bot = request.form.get('bot')
        	chat_id = request.form.get('chat_id')
        	msg = request.form.get('msg')
		contents = urllib2.urlopen(base_url+bot+"/sendMessage?chat_id="+chat_id+"&text="+msg).read()
		return jsonify(contents)

@app.route("/broadcast", methods=['POST'])
def broad():
	data = request.json
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True)