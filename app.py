from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Kams!'

@app.route('/movies')
def movies_fav():
    return 'Favorite movies include Fight Club, Usual Suspects, Rangitaranga'

if __name__ == '__main__':
    app.run()