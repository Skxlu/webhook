from flask import Flask, request


app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
	data = request.json
	print("Empfangene Daten:", data)
	return {"Status": "OK"}, 200
