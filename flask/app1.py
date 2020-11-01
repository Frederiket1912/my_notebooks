from flask import Flask, jsonify

app = Flask(__name__)

persons = [
    {
        'id': 1,
        'name': 'Holger'
    },
    {
        'id': 2,
        'name': 'Lars'
    },
    {
        'id': 3,
        'name': 'Brian'
    },
]


@app.route('/')
def say_hello():
    return 'Hello from my_notebooks!'


@app.route('/datagenerator/api/person/<int:no>', methods=['GET'])
def get_persons(no):
    if len(persons) == 0:
        abort(404)
    return jsonify(persons[no-1])
