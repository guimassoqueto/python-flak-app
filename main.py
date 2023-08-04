from flask import (Flask, send_file, request, render_template)
from os import listdir
from app.settings import FLASK_PORT, FLASK_HOST


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><a href="/thunder">Thunder</a></h1><h1><a href="/kadec">Kadec</a></h1>'


@app.route('/thunder')
def thunder():
    images = [f for f in listdir('static/thunder')]
    return render_template('thunder.html', images=images)

@app.route('/thunder-download', methods=['GET'])
def thunder_download():
    image_file = request.args.to_dict().get('image_file')
    return send_file(f'static/thunder/{image_file}', as_attachment=True)



@app.route('/kadec')
def kadec():
    images = [f for f in listdir('static/kadec')]
    return render_template('kadec.html', images=images)


@app.route('/kadec-download', methods=['GET'])
def kadec_download():
    image_file = request.args.to_dict().get('image_file')
    return send_file(f'static/kadec/{image_file}', as_attachment=True)


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
