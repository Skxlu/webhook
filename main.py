from flask import Flask, requests

app = Flask(__name__)


@app.route("/webhook", methods=["POST])
def webhook():
	data = requests.json
	print("Empfangene Daten:", data)
	return {"Status": "OK"}, 200
