from flask import Flask

app = Flask(__name__)

cats = [{'name': "Daisy", 'race': "Siamese", 'age': 4},
        {'name': "Bailey", 'race': "Siamese", 'age': 2},
        {'name': "Babie", 'race': "British Shorthair", 'age': 3}]


@app.route('/kats')
def getAllCats():
    return cats


if __name__ == '__main__':
    app.run()
