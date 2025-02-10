from flask import Flask, render_template, request, jsonify
from autocorrect_model import correct_sentence

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
    app.run(debug=True)
