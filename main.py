from flask import (Flask, send_file, request, render_template)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['GET'])
def download():
    image_file = request.args.to_dict().get('image_file')
    return send_file(f'static/{image_file}.png', as_attachment=True)