from distutils.log import debug
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        try:
            x = int(request.form.get('temperature'))
            output = round(model.predict([[x]])[0], 2)
            return render_template('index.html', prediction_text=f'The Predicted Revenue is Rs. {output}/-')
        except:
            output = "Invalid Input !"
            return render_template('index.html', prediction_text=output)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
