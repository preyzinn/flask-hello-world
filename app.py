from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello World!'
    })


# POST
@app.route('/api/hello', methods=['POST'])
def create_message():
    data = request.get_json()

    return jsonify({
        'received_data': data,
        'status': 'success'
    }), 201


# PUT
@app.route('/api/hello/<int:id>', methods=['PUT'])
def update_message(id):
    data = request.get_json()

    return jsonify({
        'id': id,
        'updated_data': data,
        'status': 'updated'
    })


# DELETE
@app.route('/api/hello/<int:id>', methods=['DELETE'])
def delete_message(id):
    return jsonify({
        'id': id,
        'status': 'deleted'
    })


if __name__ == '__main__':
    app.run(debug=True)