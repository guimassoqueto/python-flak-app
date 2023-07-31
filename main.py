from flask import (Flask, send_file, request, render_template)
from os import listdir
from app.settings import FLASK_PORT, FLASK_HOST


app = Flask(__name__)


@app.route('/')
def index():
    images = sorted([f for f in listdir('static')])
    return render_template('index.html', images=images)


@app.route('/download', methods=['GET'])
def download():
    image_file = request.args.to_dict().get('image_file')
    return send_file(f'static/{image_file}', as_attachment=True)


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
