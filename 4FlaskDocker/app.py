from flask import Flask, jsonify, request
from flask import render_template
import json
from datetime import datetime
import os

app = Flask(__name__)

def get_call_time():
    if True:
        mystring = "happy debug!"
        print(f"{mystring}")
        print("call time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    else:
        print("call time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

@app.route("/")
def index():
    get_call_time()
    with open('data/products.json') as f:
        data = json.load(f)

    return render_template('index.html', products=data)

@app.route('/api/get-json')
def hello():
    myvar = request.args.get("var1")
    return jsonify(hello=myvar)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)