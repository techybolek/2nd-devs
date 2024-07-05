from flask import Flask, request, jsonify
import c4_l5m

app = Flask(__name__)

def do_work(question):
    answer = c4_l5m.oai_answer_api(question)
    print("Answer:", answer)
    return jsonify({"reply": answer})
    

@app.route('/api/get', methods=['GET'])
def get_data():
    question = request.args.get('question')
    resp = do_work(question)
    return resp, 200

@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    print("Request received:", data)
    question = data['question']
    resp = do_work(question)
    return resp, 201

if __name__ == '__main__':
    app.run(debug=True)

