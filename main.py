from flask import Flask

app = Flask(__name__)

cats = [{'id': 0, 'name': "Daisy", 'race': "Siamese", 'age': 4},
        {'id': 1, 'name': "Bailey", 'race': "Siamese", 'age': 2},
        {'id': 2, 'name': "Babie", 'race': "British Shorthair", 'age': 3}]


@app.route('/cats')
def getAllCats():
    return cats


@app.route('/cats/<id>')
def getCatByID(id):
    id = int(id)
    global cats
    for cat in cats:
        if cat['id'] == id:
            return cat
    return "No cats were found"


@app.route('/cats', methods=['DELETE'])
def deletelist():
    global cats
    cats = []
    return "List deleted"


@app.route('/cats/<id>', methods=['DELETE'])
def deleteCatByID(id):
    id = int(id)
    global cats
    for cat in cats:
        if cat['id'] == id:
            cats.remove(cat)
            return "Cat was successfully removed"
    return "This cat ID either doesn't exist or was already deleted"


if __name__ == '__main__':
    app.run()
