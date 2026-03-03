from flask import Flask, jsonify
from flask_cors import CORS
from sniffer import generate_fake_packet

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "Packet Sniffer Backend Running"

@app.route("/packets")
def get_packets():
    return jsonify(generate_fake_packet())

if __name__ == "__main__":
    app.run()