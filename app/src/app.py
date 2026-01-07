from flask import Flask, render_template, request, make_response
import os

app = Flask('TempName')

app.static_url_path = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@app.route('/health')
def healthcheck():
    return make_response({})

@app.route('/', methods = ['GET'])
def index():
    template_args = {}
    return render_template('index.html', **template_args)

@app.route('/', methods = ['POST'])
def index_data():
    data = request.form
    template_args = {
        'user_text': data['user_text']
    }
    return render_template('index.html', **template_args)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3001)