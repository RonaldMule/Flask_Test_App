from flask import Flask, jsonify, request
app = Flask(__name__)


products_dic = {
    'sugar': 10,
    'salt':2,
    'posho':8,
    'water': 5
}

@app.route("/", methods=['GET'])
def hello():
    return "Welcome to my shop!", 200


@app.route("/products", methods=['GET'])
def products():
    products_list = list(products_dic.keys())
    return jsonify(products_list), 200


@app.route("/inventory", methods=['GET'])
def inventory():
    return jsonify(products_dic), 200


@app.route("/add-prodcuct", methods=['POST'])
def add_product():
    new_product = request.json
    products_dic = products_dic.update(new_product)
    return jsonify(products_dic), 200


# if __name__ == '__main__':
#     app.run(debug=True)