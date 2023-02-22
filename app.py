from flask import Flask, render_template, redirect
from views import kiosk
from flask_cors import CORS,cross_origin


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key="dti_kiosk2021_hashbrown_0_0_1"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.register_blueprint(kiosk.app)


app.run(host="0.0.0.0",debug=True)