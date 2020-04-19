from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({"hola": "webdesing"})


if __name__ == '__main__':
    app.run()