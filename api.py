from flask import Flask, jsonify, request

app = Flask(__name__)

items=[
    {"id": 1, "name":"item 1","description":"this is item 1"},
    {"id": 2, "name":"item 2","description":"this is item 2"}
]

@app.route("/")
def index():
    return "this a sample to do list"

@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_items():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'item not found'})
    new_item={
        'id':items[-1]["id"] +1 if items else 1,
        'name': request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    itm = next((item for item in items if item['id']==item_id),None)
    if itm is None:
        return jsonify({"error":"item not found"})
    itm['name'] = request.json.get('name',itm['name'])
    itm['description'] = request.json.get('description',itm['description'])
    return jsonify(itm)

@app.route('/item/<int:item_id>', methods=['DELETE'])
def del_item(item_id):
    global items
    items = [item for item in items if item['id']!= item_id]
    return jsonify({"result":"item deleted"})
    



@app.route('/item/<int:item_id>', methods=['GET'])
def item(item_id):
    itm=next((item for item in items if item['id']== item_id),None)
    if itm is None:
        return jsonify({'error':'item not found'})
    return jsonify(itm)


if __name__ == '__main__':
    app.run(debug=True)