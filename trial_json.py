from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/request', methods=['POST'])
def request():
    return jsonify({'result' : 'success'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 
