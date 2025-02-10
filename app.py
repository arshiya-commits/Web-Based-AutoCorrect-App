from flask import Flask, render_template, request, jsonify
from autocorrect_model import correct_sentence
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    data = request.json
    corrected_text = correct_sentence(data['text'])
    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
     port = os.environ.get("PORT")
     if port is None or port == "":
        port = 5000  # Default to port 5000 if PORT is not set
     else:
        port = int(port)  # Convert PORT to an integer

     app.run(host="0.0.0.0", port=port, debug=True)