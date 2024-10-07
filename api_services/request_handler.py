from flask import Flask, request, jsonify
from helper_functions.llama_helper_functions import make_llama_call
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/make_post", methods=['POST'])
def make_post():
    print("POST MADE!")
    data = request.get_json()
    print("DATA: ", data)

    llama_response = make_llama_call(data)
    print("LLAMA RESPONSE: ", llama_response)

    return jsonify({ 'llama_response': llama_response })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)


