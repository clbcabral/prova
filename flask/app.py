from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    nomes = ['fulano', 'ciclano', 'beltrano']
    return render_template('index.html', nomes=nomes)

@app.route('/params', methods=['GET'])
def params_get():
    print(request.args.get('q'))
    return "olar2"

@app.route('/post', methods=['POST'])
def params_post():
    print(request.form['foo'])
    return "olar3"

@app.route('/json', methods=['GET'])
def send_json():
    return jsonify({
        'a': 1
    })

@app.route('/get_json', methods=['POST'])
def get_json():
    print(request.json)
    return jsonify({
        'b': 2
    })

if __name__ == '__main__':
    app.run(debug=True)