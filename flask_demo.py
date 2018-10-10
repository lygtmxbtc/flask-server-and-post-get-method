from flask import Flask, jsonify, request, abort

app = Flask(__name__)

result = [
    {
        'category': 'dog',
        'X': 107.7,
        'Y': 88.9
    }
]

@app.route('/api/v1.0/results', methods=['GET','POST'])
def get_result():
    if request.method == 'POST':
        # TODO: Deal with the input json
        if not request.json:
            abort(400)
        return jsonify({'result': 'successfully upload'})
    if request.method == 'GET':
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)