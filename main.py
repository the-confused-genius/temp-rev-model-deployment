from distutils.log import debug
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('templates\index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        prediction = model.predict([[int(request.form.get('temperature'))]])
        output = round(prediction[0], 2)
        return render_template('templates\index.html', prediction_text=f'The Predicted Revenue is Rs. {output}/-')


if __name__ == '__main__':
    app.run(debug=True)
