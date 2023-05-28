from flask import Flask, request

app = Flask(__name__)

cats = [{'id': 0, 'name': "Daisy", 'race': "Siamese", 'age': 4},
        {'id': 1, 'name': "Bailey", 'race': "Siamese", 'age': 2},
        {'id': 2, 'name': "Babie", 'race': "British Shorthair", 'age': 3}]


@app.route('/cats')
def getAllCats():
    return cats


@app.route('/cats/<int:id>')
def getCatByID(id):
    for cat in cats:
        if cat['id'] == id:
            return cat
    return "No cats were found"


@app.route('/cats', methods=['POST'])
def AddCat():
    json_data = request.get_json()
    for cat in cats:
        if cat['id'] == json_data['id']:
            return "This cat is already added in the list"
    cats.append(json_data)

    return 'Cat added'


@app.route('/cats', methods=['DELETE'])
def deletelist():
    cats.clear()
    return "List deleted"


@app.route('/cats/<int:id>', methods=['DELETE'])
def deleteCatByID(id):
    for cat in cats:
        if cat['id'] == id:
            cats.remove(cat)
            return "Cat was successfully removed"
    return "This cat ID either doesn't exist or was already deleted"


@app.route('/cats/<int:id>', methods=['PUT'])
def updateCatByID(id):
    json_data = request.get_json()
    for cat in cats:
        if cat['id'] == id:
            for cat2 in cats:
                if cat2['id'] == json_data['id'] and cat2 != cat:
                    return "This cat's ID is conflicting with an already existing one"
            cats.remove(cat)
            cats.append(json_data)
            return "Cat updated"
    return "This cat ID either doesn't exist or was deleted"


if __name__ == '__main__':
    app.run()
