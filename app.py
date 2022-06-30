from flask_bcrypt import Bcrypt
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
import subprocess
from predict import result
from keras.models import load_model
model = load_model("model_closeprice.h5")

app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.post('/predict')
def predict():
    import subprocess
    subprocess.call("predict.py", shell=True)

    while True:
        text=request.get_json().get("message")
        Open = text["O"];
        Low = text["L"];
        Volume = text["V"];
        r= model.predict(87,78,7886)
        print(r)
        message ={"answer": "v"}
        return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)