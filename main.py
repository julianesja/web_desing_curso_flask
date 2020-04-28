from flask import Flask, jsonify, request
from producto import productos

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get():
    return jsonify(productos)

@app.route('/<id>', methods = ['GET'])
def get_by_id(id):
    producto = [producto for producto in productos if producto['id'] == int(id)]
    if(len(producto) < 1):
        return jsonify({'mensaje': 'el producto no exite'})
    return jsonify(producto[0])

@app.route('/<id>', methods= ['DELETE'])
def delete(id):
    producto = [producto for producto in productos if producto['id'] == int(id)]
    if(len(producto) < 1):
        return jsonify({'mensaje': 'el producto no exite'})
    productos.remove(producto[0])
    return jsonify(productos)

@app.route('/<id>', methods= ['PUT'])
def put(id):
    producto = [producto for producto in productos if producto['id'] == int(id)]
    if(len(producto) < 1):
        return jsonify({'mensaje': 'el producto no exite'})
    producto[0]['nombre'] = request.json['nombre']
    return jsonify(productos)

@app.route('/', methods= ['POST'])
def post():
    producto = {'id':int(request.json['id']), 'nombre': request.json['nombre']}
    productos.append(producto)
    return jsonify(productos)


    
    



    



if __name__ == '__main__':
    app.run(debug=True)