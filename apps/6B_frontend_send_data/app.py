from math import sqrt
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('junyi.html')


@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    a, b, c, d = user_data['a'], user_data['b'], user_data['c'], user_data['d']
    prediction = _return_prediction(a, b, c, d)
    return jsonify({'prediction': prediction})


def return_prediction(a, b, c):
    gbc = pickle.load(open(../../gbc.sav, 'rb'))
    X = np.array([[a,b,c,d]])
    return gbc.predict_proba(X)[0][1]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
