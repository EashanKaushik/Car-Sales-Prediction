from flask import Flask, url_for
from app import views

app = Flask(__name__)

app.add_url_rule('/predict', 'predict', views.predict, methods=['GET','POST'])

app.add_url_rule('/home', 'home', views.home)

if __name__ == '__main__':
    app.run(debug=True)