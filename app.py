from flask import Flask, request, jsonify
from chatbot import get_response  # from chatbot.py

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    reply = get_response(message)
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
