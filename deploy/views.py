from flask import render_template, request, Flask, url_for
from deploy.utils import make_prediction

GENDER = {'male': 1, 'female': 0}

def home():
    return render_template('home.html', pagename='Home')

def predict():
    prediction_made = False

    if request.method == 'POST':
        prediction_made = True

        age = request.form['age']
        gender = request.form['gender']
        annual = request.form['annual']
        net = request.form['net']
        credit =  request.form['credit']

        gender = gender.lower()
        gender = GENDER[gender]

        predict_data = [gender, age, annual, credit, net]

        result = make_prediction(predict_data)

        return render_template('prediction.html', pagename='Car Purchase Prediction', prediction_made=prediction_made, result=result)
    
    return render_template('prediction.html', pagename='Make Car Purchase Prediction', prediction_made=prediction_made)

