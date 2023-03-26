from flask import Flask, jsonify, request

app = Flask(__name__)

# Define endpoints
@app.route('/talents', methods=['GET'])
def get_talents():
    # TODO: Retrieve list of talents from database
    talents = []

    return jsonify({'talents': talents})

@app.route('/talents', methods=['POST'])
def create_talent():
    talent = request.json
    # TODO: Save talent to database and return saved talent object with ID

    return jsonify({'talent': talent}), 201

@app.route('/destinations', methods=['GET'])
def get_destinations():
    # TODO: Retrieve list of destinations from database
    destinations = []

    return jsonify({'destinations': destinations})

@app.route('/destinations', methods=['POST'])
def create_destination():
    destination = request.json
    # TODO: Save destination to database and return saved destination object with ID

    return jsonify({'destination': destination}), 201

if __name__ == '__main__':
    app.run()
