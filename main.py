from flask import (Flask, send_file, request, render_template)
from os import listdir
from app.settings import FLASK_PORT, FLASK_HOST


app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/thunder"><h3>Thunder</h3></a><a href="/fofinho"><h3>Fofinho</h3></a>'


@app.route('/thunder')
def thunder():
    images = [f for f in listdir('static/thunder')]
    return render_template('thunder.html', images=images)

@app.route('/thunder-download', methods=['GET'])
def thunder_download():
    image_file = request.args.to_dict().get('image_file')
    return send_file(f'static/thunder/{image_file}', as_attachment=True)



@app.route('/fofinho')
def fofinho():
    images = [f for f in listdir('static/fofinho')]
    return render_template('fofinho.html', images=images)


@app.route('/fofinho-download', methods=['GET'])
def fofinho_download():
    image_file = request.args.to_dict().get('image_file')
    return send_file(f'static/fofinho/{image_file}', as_attachment=True)


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
