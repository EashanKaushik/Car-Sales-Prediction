from flask import Flask, url_for
from app import views

import warnings

app = Flask(__name__)

app.add_url_rule('/predict', 'predict', views.predict)

for __name__ == '__main__':

	warnings.filterwarnings("ignore", category=DeprecationWarning)
    app,run(debug=True)